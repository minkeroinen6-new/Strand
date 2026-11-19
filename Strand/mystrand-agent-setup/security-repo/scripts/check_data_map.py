#!/usr/bin/env python3
"""Checks that every stored field is classified in policy/data-map.yaml (GDPR-001, SEC-009).

Input: a text file with one `table.column` per line, produced by a stack-specific step
(e.g. listing the ORM schema). Fails if any field is unclassified, a class is unknown,
or no fields were checked at all.
"""
import argparse
import sys

import yaml

CLASSES = {"public", "internal", "pii", "sensitive", "kyc"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fields_file", help="schema fields, one table.column per line")
    parser.add_argument("--data-map", default="policy/data-map.yaml")
    args = parser.parse_args()
    try:
        with open(args.fields_file, encoding="utf-8") as f:
            fields = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except OSError:
        fields = []

    with open(args.data_map, encoding="utf-8") as f:
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
