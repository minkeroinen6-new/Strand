#!/usr/bin/env python3
"""PreToolUse hook for Bash: blocks commands that could reach production, leak secrets
or bypass the guardrails. Complements the deny rules in .claude/settings.json, which
match command prefixes only. Rules: SEC-001, SEC-005, SEC-007.
"""
import json
import re
import sys

BLOCKED = [
    (r"(^|\s)(cat|less|more|head|tail|grep|cp|scp)\s+[^|;&]*\.env\b", "salaisuustiedoston lukeminen (SEC-001)"),
    (r"\b(printenv|env)\b\s*$", "ympäristömuuttujien tulostaminen (SEC-001)"),
    (r"\bgit\s+push\b.*(--force|-f\b)", "force push (SEC-007)"),
    (r"\bgit\s+push\b.*\b(main|master)\b", "suora push päähaaraan (SEC-007)"),
    (r"--no-verify\b", "tarkistusten ohittaminen (SEC-007)"),
    (r"\b(kubectl|helm|terraform\s+apply|pulumi\s+up)\b", "infrastruktuurin muuttaminen (SEC-005)"),
    (r"\b(psql|mysql|mongosh|redis-cli)\b", "suora tietokantayhteys (SEC-005)"),
    (r"\bprod(uction)?\b.*\b(db|database|api)\b", "viittaus tuotantoympäristöön (SEC-005)"),
    (r"\b(chmod|chown)\b.*\.claude", "suojakaiteiden oikeuksien muuttaminen (SEC-007)"),
    (r"(>|tee\s+)\s*\S*(policy/(rules|no-fly)\.yaml|\.claude/|\.github/)", "suojakaiteiden muokkaus komentorivillä (SEC-007)"),
]


def main():
    event = json.load(sys.stdin)
    command = event.get("tool_input", {}).get("command", "")
    for pattern, reason in BLOCKED:
        if re.search(pattern, command):
            print(f"Estetty: {reason}. Jos tehtävä vaatii tätä, kirjaa se Linear-tikettiin ihmisen tehtäväksi.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
