# Formal System — v0.5.0 Review-Resistant Core

## 1. Purpose

This file defines the formal skeleton of the Law of Totality.

The system is intentionally minimal. It does not attempt to formalize all of reality. It defines the conditions under which a local framework becomes structurally invalid when used beyond its valid scope.

## 2. Primitive Field

    𝔻

Domain of the nameable, thinkable, modelable, decidable, formalizable, or operationally treatable.

    Ω = ∞Tot

Total field without outside.

    Outside(Ω) = ∅

Ω is not a proper object inside itself. Ω has a different logical type from every proper manifestation.

## 3. Manifestation Predicates

    ManifestΩ(x)

`x` manifests within Ω.

    ProperΩ(x) ⇔ ManifestΩ(x) ∧ x ≠ Ω

`x` is a proper manifestation, not totality itself.

## 4. Determinability

    DetCondΩ(d,x)

`d` is a non-zero condition without which `x` is not determinable as `x`.

    DepΩ(x) = { d : DetCondΩ(d,x) }

The dependence set of `x`.

Core axiom-schema:

    ∀x∈𝔻:
    ProperΩ(x) ⇒ ∃d DetCondΩ(d,x)

Expanded:

    ∀x∈𝔻:
    [ManifestΩ(x) ∧ x≠Ω] ⇒ ∃d DetCondΩ(d,x)

Equivalent dependence form:

    ∀x∈𝔻:
    ProperΩ(x) ⇒ DepΩ(x) ≠ ∅

Contrapositive:

    ∀x∈𝔻:
    [x≠Ω ∧ DepΩ(x)=∅] ⇒ ¬ManifestΩ(x)

Reading:

> If something has no condition by which it is determinable as itself, it cannot manifest as something.

## 5. Ω Type Clause

For Ω:

    ProperΩ(Ω) = false
    DepΩ(Ω) = non-applicable / type-error
    OpenΩ(Ω) = undefined
    ClosedΩ(Ω) = undefined

Reason:

    Ω = totality without outside

Dependence applies to proper manifestations, not to Ω as totality.

## 6. Local Closure

    LocalClosureF(x)

A framework `F` closes `x` locally for a defined operation, context, representation, abstraction, model, or decision.

Local closure is not error.

It is necessary for:

    mathematics
    proof
    software
    engineering
    medicine
    law
    maps
    science
    diagnosis
    decision-making
    AI answers

## 7. Valid Scope

    ValidScope(F,x)

The set of uses for which framework `F` can treat `x` without excluding conditions critical to those uses.

    ActualUseU(F,x)

The concrete use, deployment, interpretation, decision, or inference made with `F` about `x`.

Scope violation:

    ScopeViolationΩ(F,x,U) ⇔
    ActualUseU(F,x) exceeds ValidScope(F,x)

Operational form:

    ScopeViolationΩ(F,x,U) ⇔
    ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

## 8. Critical Dependency

    CriticalDepΩ(d,x,U)

`d` is a dependency of `x` that is required for the concrete use `U`.

Important distinction:

    DetCondΩ(d,x) does not imply CriticalDepΩ(d,x,U) for every U.

A dependency may exist without being critical for a specific use.

## 9. Exclusion

    ExcludedF(d)

Framework `F` omits, suppresses, cannot represent, ignores, abstracts away, or treats as irrelevant dependency `d`.

Exclusion is not automatically error.

Exclusion becomes error only if `d` is critical for `U`.

## 10. Structural Error Formula

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

Short form:

    Structural error =
    local closure used beyond valid scope while excluding a critical dependency.

## 11. Validity Formula

    ValidΩ(a,F,U) ⇔
    CorrectF(a)
    ∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
    ∧ CriticalDepΩ(a,U) preserved

Therefore:

    CorrectF(a) ≠ ValidΩ(a,F,U)

A statement can be locally correct and structurally invalid.

## 12. Prevention Formula

A structural error is prevented when at least one of the following occurs:

    ¬LocalClosureF(x)

or:

    ActualUseU(F,x) ⊆ ValidScope(F,x)

or:

    ∀d [CriticalDepΩ(d,x,U) ⇒ PreservedF(d)]

Operationally:

    PreventErrΩ(x,F,U) ⇔
    DeclareScope(F,x)
    ∧ IdentifyUse(U)
    ∧ PreserveCriticalDeps(x,U)
    ∧ BlockUseBeyondScope(F,x,U)

## 13. Non-Claims

The formal system does not claim:

    all mistakes are structural errors
    all dependencies are critical
    all closures are false
    all frameworks are invalid
    Ω can be fully represented by a finite system

## 14. Core Result

    Local correctness does not guarantee structural validity.

That is the operational theorem of the repository.

## Corollary: Theory-Reality Asymmetry

For every proper manifested object:

```text
Manifest_Ω(x) ∧ x ≠ Ω ⇒ Open_Ω(x)
```

Any finite theory, model, map, rule, game, metric, proof environment, or framework `F` that treats `x` must perform some local closure:

```text
Theory_F(x) ⇒ LocalClosure_F(x)
```

Therefore:

```text
LocalClosure_F(x) ∧ Open_Ω(x)
```

This is the Theory-Reality Asymmetry:

> Every theory closes locally. Reality remains open.

The corollary does not claim that local closure is false.

Local closure is necessary for finite understanding, calculation, decision, and action.

The structural error appears only when the local closure is used as sufficient for an actual use `U` that requires dependencies excluded by `F`.

## Formal Theorem Companion

The formal theorem and counterexample layer is specified in:

[`FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md`](FORMAL_THEOREMS_AND_COUNTEREXAMPLES.md)

It introduces a compact review structure:

    primitive terms
    predicates
    axioms
    theorem schemas
    conditions of application
    negative controls
    counterexample classes

Central theorem schema:

    Finite(F) and Treats(F,x) implies LocalClosure_F(x)

    Manifest_Ω(x) and Proper_Ω(x) implies Open_Ω(x)

Therefore:

    LocalClosure_F(x) and Open_Ω(x)

This is the formal form of:

    Closed in theory. Open in reality.
