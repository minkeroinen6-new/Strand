#!/usr/bin/env python3
"""Detects drift in GitHub protection settings for MyStrand (SEC-012, SEC-013, SEC-009).

Compares the live organization ruleset with settings/ruleset-mystrand-main.json and checks
secret scanning push protection on the MyStrand repo. Posts a Slack alert on any deviation.

Env: GITHUB_TOKEN (GitHub App token with organization Administration: read and repository
Administration: read), ORG, REPO, optional SLACK_WEBHOOK_URL.
"""
import json
import os
import sys
import urllib.request

API = "https://api.github.com"


def gh(path):
    req = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def slack(text):
    url = os.environ.get("SLACK_WEBHOOK_URL")
    if not url:
        return
    data = json.dumps({"text": text}).encode()
    urllib.request.urlopen(urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}))


def compare_rules(desired, actual, problems):
    actual_by_type = {r["type"]: r for r in actual.get("rules", [])}
    checked = 0
    for rule in desired["rules"]:
        checked += 1
        live = actual_by_type.get(rule["type"])
        if not live:
            problems.append(f"rule '{rule['type']}' missing")
            continue
        for key, want in (rule.get("parameters") or {}).items():
            got = (live.get("parameters") or {}).get(key)
            if key == "workflows":
                want_paths = sorted(w["path"] for w in want)
                got_paths = sorted(w.get("path") for w in (got or []))
                if want_paths != got_paths:
                    problems.append(f"required workflows differ: want {want_paths}, got {got_paths}")
            elif got != want:
                problems.append(f"{rule['type']}.{key}: want {want!r}, got {got!r}")
    return checked


def main():
    org, repo = os.environ["ORG"], os.environ["REPO"]
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "..", "settings", "ruleset-mystrand-main.json"), encoding="utf-8") as f:
        desired = json.load(f)

    problems, checked = [], 0

    summaries = gh(f"/orgs/{org}/rulesets")
    match = [r for r in summaries if r.get("name") == desired["name"]]
    if not match:
        problems.append(f"organization ruleset '{desired['name']}' not found")
    else:
        actual = gh(f"/orgs/{org}/rulesets/{match[0]['id']}")
        checked += 1
        if actual.get("enforcement") != "active":
            problems.append(f"enforcement is '{actual.get('enforcement')}', want 'active'")
        if actual.get("bypass_actors"):
            problems.append(f"bypass actors present: {actual['bypass_actors']}")
        include = (actual.get("conditions") or {}).get("repository_name", {}).get("include", [])
        if repo not in include:
            problems.append(f"repository '{repo}' not in ruleset conditions: {include}")
        checked += compare_rules(desired, actual, problems)

    repo_info = gh(f"/repos/{org}/{repo}")
    checked += 1
    push_protection = ((repo_info.get("security_and_analysis") or {}).get("secret_scanning_push_protection") or {}).get("status")
    if push_protection != "enabled":
        problems.append(f"secret scanning push protection is '{push_protection}', want 'enabled'")

    print(f"check_drift: checked {checked} settings")
    if checked == 0:
        problems.append("no settings checked (SEC-009)")
    for p in problems:
        print(f"DRIFT {p}")
    if problems:
        slack(f":rotating_light: MyStrandin GitHub-suojauksissa poikkeama ({len(problems)}):\n" + "\n".join(f"• {p}" for p in problems))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
