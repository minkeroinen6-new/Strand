#!/usr/bin/env python3
"""Validates policy/rules.yaml and writes a compliance matrix (SEC-008, SEC-009).

Fails if: the file is missing or empty, a rule lacks id, rule, owner or enforced_by,
an id repeats, or an owner is not defined. Prints how many rules it checked.
"""
import argparse
import os
import sys

import yaml

REQUIRED = ("id", "rule", "owner", "enforced_by")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", default="policy/rules.yaml")
    parser.add_argument("--matrix", help="write compliance matrix markdown to this path")
    args = parser.parse_args()

    with open(args.rules, encoding="utf-8") as f:
        doc = yaml.safe_load(f) or {}
    rules = doc.get("rules") or []
    owners = doc.get("owners") or {}

    errors, seen = [], set()
    for i, rule in enumerate(rules):
        for key in REQUIRED:
            if not rule.get(key):
                errors.append(f"rule #{i + 1} ({rule.get('id', '?')}): missing {key}")
        rid = rule.get("id")
        if rid in seen:
            errors.append(f"{rid}: duplicate id")
        seen.add(rid)
        if rule.get("owner") and rule["owner"] not in owners:
            errors.append(f"{rid}: owner '{rule['owner']}' not defined under owners")

    print(f"policy_check: checked {len(rules)} rules")
    if not rules:
        errors.append("no rules checked (SEC-009)")
    for e in errors:
        print(f"ERROR {e}")

    if args.matrix:
        os.makedirs(os.path.dirname(args.matrix) or ".", exist_ok=True)
        sha = os.environ.get("GITHUB_SHA", "local")
        with open(args.matrix, "w", encoding="utf-8") as out:
            out.write(f"# Vaatimusmatriisi\n\nCommit: `{sha}`\n\n")
            out.write("| Sääntö | Kuvaus | Omistaja | Valvonta | Todiste |\n| --- | --- | --- | --- | --- |\n")
            for r in rules:
                owner = owners.get(r.get("owner"), r.get("owner"))
                enforced = ", ".join(r.get("enforced_by") or [])
                out.write(f"| {r.get('id')} | {r.get('rule')} | {owner} | {enforced} | {r.get('evidence', '')} |\n")
        print(f"policy_check: wrote {args.matrix}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
