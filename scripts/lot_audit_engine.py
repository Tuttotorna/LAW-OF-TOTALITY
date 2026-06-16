#!/usr/bin/env python3
"""
Law of Totality — Structural Error Audit Engine

This module implements the operational audit rule:

    ErrΩ(x,F,U) ⇔
        LocalClosureF(x)
        ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
        ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

It is deliberately simple.
It does not prove the Law of Totality.
It makes the audit repeatable.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import json
import pathlib


STRUCTURAL_ERROR = "structural_error"
LEGITIMATE_LOCAL_CLOSURE = "legitimate_local_closure"
INSUFFICIENT_INFORMATION = "insufficient_information"
TYPE_BOUNDARY = "type_boundary"
NO_ERROR_DETECTED = "no_error_detected"


@dataclass
class AuditCase:
    object_x: str
    framework_F: str
    actual_use_U: str
    local_closure: Optional[bool]
    scope_overrun: Optional[bool]
    critical_dependencies: List[str] = field(default_factory=list)
    excluded_dependencies: List[str] = field(default_factory=list)
    type_boundary: bool = False
    notes: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AuditCase":
        return cls(
            object_x=data.get("object_x", ""),
            framework_F=data.get("framework_F", ""),
            actual_use_U=data.get("actual_use_U", ""),
            local_closure=data.get("local_closure", None),
            scope_overrun=data.get("scope_overrun", None),
            critical_dependencies=data.get("critical_dependencies", []) or [],
            excluded_dependencies=data.get("excluded_dependencies", []) or [],
            type_boundary=bool(data.get("type_boundary", False)),
            notes=data.get("notes", ""),
        )


def normalize(values: List[str]) -> set:
    return {str(v).strip().lower() for v in values if str(v).strip()}


def excluded_critical_dependencies(case: AuditCase) -> set:
    critical = normalize(case.critical_dependencies)
    excluded = normalize(case.excluded_dependencies)
    return critical.intersection(excluded)


def audit(case: AuditCase) -> Dict[str, Any]:
    if case.type_boundary:
        verdict = TYPE_BOUNDARY
        reason = "The case is a type-boundary case, not a normal proper manifestation audit."

    elif case.local_closure is None or case.scope_overrun is None:
        verdict = INSUFFICIENT_INFORMATION
        reason = "The audit lacks enough information about local closure or scope overrun."

    elif case.local_closure and case.scope_overrun and excluded_critical_dependencies(case):
        verdict = STRUCTURAL_ERROR
        reason = (
            "Local closure is present, actual use exceeds valid scope, "
            "and at least one critical dependency is excluded."
        )

    elif case.local_closure and not case.scope_overrun:
        verdict = LEGITIMATE_LOCAL_CLOSURE
        reason = "Local closure is present but remains inside its valid scope."

    else:
        verdict = NO_ERROR_DETECTED
        reason = "The conjunction required for structural error is not satisfied."

    return {
        "object_x": case.object_x,
        "framework_F": case.framework_F,
        "actual_use_U": case.actual_use_U,
        "verdict": verdict,
        "reason": reason,
        "excluded_critical_dependencies": sorted(excluded_critical_dependencies(case)),
        "formula_checked": (
            "LocalClosureF(x) ∧ ActualUseU(F,x) exceeds ValidScope(F,x) "
            "∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]"
        ),
    }


def audit_many(cases: List[AuditCase]) -> List[Dict[str, Any]]:
    return [audit(case) for case in cases]


def load_cases(path: str) -> List[AuditCase]:
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    return [AuditCase.from_dict(item) for item in data]


def main():
    root = pathlib.Path(__file__).resolve().parents[1]
    cases_path = root / "examples" / "audit_cases.json"
    cases = load_cases(str(cases_path))
    results = audit_many(cases)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
