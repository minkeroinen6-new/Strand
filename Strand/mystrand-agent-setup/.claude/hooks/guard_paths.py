#!/usr/bin/env python3
"""PreToolUse hook: blocks edits to guardrail, no-fly and secret paths listed in policy/no-fly.yaml.

Claude Code sends the tool call as JSON on stdin. Exit code 2 blocks the call and
shows stderr to the agent as the reason. Rules: SEC-001, SEC-005, SEC-006, SEC-007.
"""
import fnmatch
import json
import os
import sys

PROJECT = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
NO_FLY = os.path.join(PROJECT, "policy", "no-fly.yaml")


def load_patterns(path):
    """Minimal parser for the list sections of no-fly.yaml (no PyYAML dependency)."""
    sections, current = {}, None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].rstrip()
            if not line:
                continue
            if not line.startswith(" ") and line.endswith(":"):
                current = line[:-1]
                sections[current] = []
            elif line.lstrip().startswith("- ") and current:
                sections[current].append(line.lstrip()[2:].strip().strip('"'))
    return sections


def matches(rel, pattern):
    if pattern.endswith("/**"):
        return rel == pattern[:-3] or rel.startswith(pattern[:-2])
    if pattern.startswith("**/"):
        return fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(os.path.basename(rel), pattern[3:])
    return fnmatch.fnmatch(rel, pattern)


def main():
    event = json.load(sys.stdin)
    tool_input = event.get("tool_input", {})
    target = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not target:
        return 0

    rel = os.path.relpath(os.path.abspath(os.path.join(PROJECT, target)), PROJECT).replace(os.sep, "/")
    if rel.startswith(".."):
        print(f"Estetty: {target} on projektin ulkopuolella.", file=sys.stderr)
        return 2

    try:
        sections = load_patterns(NO_FLY)
    except OSError:
        print("Estetty: policy/no-fly.yaml puuttuu, joten muokkauksia ei sallita (SEC-009).", file=sys.stderr)
        return 2

    reasons = {
        "guardrails": "suojakaide, jota agentti ei muuta (SEC-007)",
        "no_fly": "no-fly-alue, jonka muutokset tekee ihminen (SEC-006)",
        "secrets": "salaisuustiedosto (SEC-001)",
    }
    for section, reason in reasons.items():
        for pattern in sections.get(section, []):
            if matches(rel, pattern):
                print(
                    f"Estetty: {rel} on {reason}. Älä yritä kiertää estoa. "
                    "Kirjaa tarvittava muutos Linear-tikettiin ihmisen tehtäväksi.",
                    file=sys.stderr,
                )
                return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
