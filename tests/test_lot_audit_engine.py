import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lot_audit_engine import (
    AuditCase,
    audit,
    STRUCTURAL_ERROR,
    LEGITIMATE_LOCAL_CLOSURE,
    INSUFFICIENT_INFORMATION,
)


class TestLotAuditEngine(unittest.TestCase):

    def test_structural_error(self):
        case = AuditCase(
            object_x="AI legal answer",
            framework_F="general language model",
            actual_use_U="final legal advice",
            local_closure=True,
            scope_overrun=True,
            critical_dependencies=["jurisdiction", "current law"],
            excluded_dependencies=["jurisdiction"],
        )
        self.assertEqual(audit(case)["verdict"], STRUCTURAL_ERROR)

    def test_legitimate_local_closure(self):
        case = AuditCase(
            object_x="2 + 2 = 4",
            framework_F="ordinary integer arithmetic",
            actual_use_U="ordinary integer arithmetic",
            local_closure=True,
            scope_overrun=False,
            critical_dependencies=["definitions"],
            excluded_dependencies=[],
        )
        self.assertEqual(audit(case)["verdict"], LEGITIMATE_LOCAL_CLOSURE)

    def test_insufficient_information(self):
        case = AuditCase(
            object_x="unknown claim",
            framework_F="unknown",
            actual_use_U="unknown",
            local_closure=None,
            scope_overrun=None,
        )
        self.assertEqual(audit(case)["verdict"], INSUFFICIENT_INFORMATION)

    def test_excluded_dependency_must_be_critical(self):
        case = AuditCase(
            object_x="minor statement",
            framework_F="limited framework",
            actual_use_U="slightly broader use",
            local_closure=True,
            scope_overrun=True,
            critical_dependencies=["A"],
            excluded_dependencies=["B"],
        )
        self.assertNotEqual(audit(case)["verdict"], STRUCTURAL_ERROR)


if __name__ == "__main__":
    unittest.main()
