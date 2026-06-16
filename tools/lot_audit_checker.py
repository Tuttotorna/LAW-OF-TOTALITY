#!/usr/bin/env python3
import json
from pathlib import Path

def structural_error(case):
    local = bool(case.get("local_closure"))
    within = bool(case.get("use_within_scope"))
    critical = set(case.get("critical_dependencies", []))
    excluded = set(case.get("excluded_dependencies", []))
    missing_critical = bool(critical.intersection(excluded))
    return local and (not within) and missing_critical

def main():
    path = Path("examples/lot_audit_cases.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    for case in data["cases"]:
        got = structural_error(case)
        expected = bool(case["expected_structural_error"])
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} {case['id']}: got={got}, expected={expected}")
        if got != expected:
            failures.append(case["id"])
    if failures:
        raise SystemExit(f"failed cases: {failures}")
    print("All structural audit examples passed.")

if __name__ == "__main__":
    main()
