#!/usr/bin/env python3
"""Checks that every stored field is classified in policy/data-map.yaml (GDPR-001, SEC-009).

Input: a text file with one `table.column` per line, produced by a stack-specific step
(e.g. listing the ORM schema). Fails if any field is unclassified, a class is unknown,
or no fields were checked at all.
"""
import sys

import yaml

CLASSES = {"public", "internal", "pii", "sensitive", "kyc"}


def main():
    if len(sys.argv) != 2:
        print("usage: check_data_map.py <schema-fields.txt>")
        return 2
    try:
        with open(sys.argv[1], encoding="utf-8") as f:
            fields = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except OSError:
        fields = []

    with open("policy/data-map.yaml", encoding="utf-8") as f:
        mapped = (yaml.safe_load(f) or {}).get("fields") or {}

    errors = []
    for name, spec in mapped.items():
        if (spec or {}).get("class") not in CLASSES:
            errors.append(f"{name}: unknown or missing class")
    for field in fields:
        if field not in mapped:
            errors.append(f"{field}: not classified in policy/data-map.yaml")

    print(f"check_data_map: checked {len(fields)} schema fields against {len(mapped)} classified fields")
    if not fields:
        errors.append("no schema fields checked (SEC-009): is build/schema-fields.txt generated?")
    for e in errors:
        print(f"ERROR {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
