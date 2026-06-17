# Law of Totality

## The Law of Absolute Non-Closure

This repository formalizes a meta-structural rule for diagnosing structural error:

> A proper manifestation cannot be treated as absolutely closed when its determinability depends on conditions outside the local framework used to describe, decide, model, or answer it.

Operational core:

    Structural error =
    local closure
    + use beyond valid scope
    + excluded critical dependency

Formalized:

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

Where:

    Ω = ∞Tot, total field without outside
    x = proper manifestation under treatment
    F = framework, model, theory, discipline, algorithm, answer, map, procedure
    U = concrete use of F
    d = critical determinability-condition required by U

## Correct Claim

This repository does **not** claim that every possible mistake, typo, random failure, accident, or false statement has the same cause.

The precise claim is narrower and stronger:

> Every structural error caused by false framework sufficiency can be diagnosed as a local closure used beyond its valid scope while excluding at least one critical dependency required by the concrete use.

This is the review-resistant form of the law.

## Local Closure Clause

Local closure is not error.

Local closure is necessary for mathematics, engineering, law, science, medicine, software, cartography, diagnosis, AI answers, and decision-making.

The structural error begins only when a local closure is used beyond its valid scope while excluding a dependency critical to the concrete use.

## Core Distinction

    Correct inside F ≠ Valid for U

A statement, model, answer, or procedure can be correct inside a framework and still invalid for a concrete use.

Validity requires:

    ValidΩ(a,F,U) ⇔
    CorrectF(a)
    ∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
    ∧ CriticalDepΩ(a,U) preserved

## Ω Clause

Ω is not an object among objects.

    Ω = ∞Tot
    Ω = total field without outside
    Outside(Ω) = ∅

Therefore:

    DepΩ(Ω) = non-applicable / type-error
    OpenΩ(Ω) = undefined
    ClosedΩ(Ω) = undefined

The law applies only to proper manifestations:

    ProperΩ(x) ⇔ ManifestΩ(x) ∧ x ≠ Ω

Core law:

    ∀x∈𝔻:
    [ManifestΩ(x) ∧ x≠Ω] ⇒ ∃d DetCondΩ(d,x)

## v0.6.0 Error Atlas Layer

The repository now includes `ERROR_ATLAS.md`, a cross-domain case layer showing how the structural error formula maps across AI, law, medicine, model risk, engineering, politics, education, institutions, language, memory, economics, systems, and negative controls.

The atlas does not claim that the Law of Totality explains every thing as total content.

It shows that every finite treatment submitted to the law can be explained in its structural validity or invalidity:

    object
    framework
    actual use
    valid scope
    excluded critical dependencies

This is the bridge from formal statement to real-world visibility.

## Repository Map

| File | Function |
|---|---|
| `FORMAL_SYSTEM.md` | Formal primitives, typing, axiom schema, validity and error formulas |
| `ERROR_FORMULA.md` | Hardened operational formula of structural error |
| `CLAIMS_AND_SCOPE.md` | What the repository claims and does not claim |
| `OPERATIONAL_AUDIT.md` | Step-by-step audit protocol |
| `VALIDATION_CASES.md` | Test cases and falsification conditions |
| `RELATED_WORK.md` | Comparison with existing fields |
| `AI_PRIMARY_DIRECTIVE.md` | How the law constrains AI answers |
| `DECISION_VALIDITY.md` | Decision-level version of the framework |
| `CASEBOOK.md` | Concrete examples |
| `GLOSSARY.md` | Controlled vocabulary |
| `tools/lot_audit_checker.py` | Minimal structural audit checker |
| `examples/lot_audit_cases.json` | Machine-readable examples |

## Status

Current status:

    v0.5.0 = operational framework, not externally validated theory

The repository is suitable for:

- structural audit of decisions;
- model-use validation;
- AI answer validation;
- post-hoc failure analysis;
- framework-scope diagnosis;
- prevention of overconfident local closure.

It is not yet:

- a peer-reviewed scientific theory;
- a complete mathematical foundation;
- a substitute for domain expertise;
- proof that every error in every domain has one identical cause.

## One-Sentence Version

> A framework becomes structurally false when it is used beyond the field that makes it valid.

## Minimal Audit Question

    What critical dependency required by this use has been excluded by the framework?

If the answer is non-empty and the framework is still used as sufficient, the structural error is present.
