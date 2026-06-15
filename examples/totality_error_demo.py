from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Case:
    name: str
    declared_fragment: Dict[str, int]
    accessible_total_field: Dict[str, int]


def structural_distance(fragment: Dict[str, int], total_field: Dict[str, int]) -> float:
    keys = sorted(set(fragment) | set(total_field))
    if not keys:
        return 0.0
    distance = 0.0
    for key in keys:
        distance += abs(fragment.get(key, 0) - total_field.get(key, 0))
    return distance / len(keys)


def classify(distance: float) -> str:
    if distance == 0:
        return "COMPATIBLE"
    if distance <= 1:
        return "LOW_DISTANCE"
    if distance <= 3:
        return "STRUCTURAL_INCONGRUENCE"
    return "HIGH_STRUCTURAL_ERROR"


cases: List[Case] = [
    Case(
        name="local_correct_total_compatible",
        declared_fragment={"benefit": 5, "damage": 0, "dependency": 0},
        accessible_total_field={"benefit": 5, "damage": 0, "dependency": 0},
    ),
    Case(
        name="local_profit_global_damage",
        declared_fragment={"benefit": 8, "damage": 0, "dependency": 0},
        accessible_total_field={"benefit": 8, "damage": 6, "dependency": 4},
    ),
    Case(
        name="plausible_answer_missing_constraints",
        declared_fragment={"facts": 7, "constraints": 1, "consequences": 1},
        accessible_total_field={"facts": 7, "constraints": 6, "consequences": 5},
    ),
]


def main() -> None:
    print("Law of Totality — minimal structural error demo")
    print("=" * 72)
    print("Error is modeled as distance between local fragment and accessible total field.")
    print()

    for case in cases:
        distance = structural_distance(case.declared_fragment, case.accessible_total_field)
        print(f"{case.name}:")
        print(f"  fragment: {case.declared_fragment}")
        print(f"  accessible_total_field: {case.accessible_total_field}")
        print(f"  E_Ω approximation: {distance:.3f}")
        print(f"  classification: {classify(distance)}")
        print()


if __name__ == "__main__":
    main()
