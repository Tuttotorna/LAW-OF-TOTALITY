# Glossary — v0.5.0

## Ω

Total field without outside.

    Ω = ∞Tot
    Outside(Ω) = ∅

Ω is not a proper manifestation.

## 𝔻

Domain of the nameable, thinkable, modelable, decidable, or formalizable.

## ManifestΩ(x)

`x` manifests within Ω.

## ProperΩ(x)

`x` is a proper manifestation.

    ProperΩ(x) ⇔ ManifestΩ(x) ∧ x ≠ Ω

## DetCondΩ(d,x)

`d` is a non-zero condition without which `x` is not determinable as `x`.

## DepΩ(x)

Set of determinability conditions of `x`.

    DepΩ(x) = { d : DetCondΩ(d,x) }

## LocalClosureF(x)

Framework `F` closes `x` locally for a defined operation.

Local closure is not error.

## ValidScope(F,x)

The set of uses for which framework `F` can validly treat `x`.

## ActualUseU(F,x)

The concrete use of `F` regarding `x`.

## CriticalDepΩ(d,x,U)

Dependency `d` is required for use `U` of `x`.

## ExcludedF(d)

Framework `F` excludes, ignores, abstracts away, cannot represent, or suppresses `d`.

## ErrΩ(x,F,U)

Structural error.

    ErrΩ(x,F,U) ⇔
    LocalClosureF(x)
    ∧ ActualUseU(F,x) exceeds ValidScope(F,x)
    ∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]

## ValidΩ(a,F,U)

Structural validity of answer/output `a`.

    ValidΩ(a,F,U) ⇔
    CorrectF(a)
    ∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
    ∧ CriticalDepΩ(a,U) preserved

## Structural Error

A local closure used beyond valid scope while excluding a critical dependency.

## False Sufficiency

The treatment of a framework as sufficient for a use that requires conditions the framework does not preserve.
