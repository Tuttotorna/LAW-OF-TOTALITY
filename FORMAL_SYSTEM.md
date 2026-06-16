# Formal System — v0.3.0 Determinability Core

## 1. Primitives

~~~text
𝔻
~~~

Domain of the nameable, thinkable, modelable, formalizable.

~~~text
Ω = ∞Tot
~~~

Total field without outside.

Ω is not an ordinary object inside 𝔻.

Ω has a different logical type from every proper manifestation.

~~~text
ManifestΩ(x)
~~~

`x` manifests within Ω.

~~~text
ProperΩ(x)
~~~

`x` is a proper manifestation.

Definition:

~~~text
ProperΩ(x) ⇔ ManifestΩ(x) ∧ x ≠ Ω
~~~

~~~text
DetCondΩ(d,x)
~~~

`d` is a non-zero condition without which `x` is not determinable as `x`.

~~~text
DepΩ(x)
~~~

Set of determinability-conditions of `x`.

Definition:

~~~text
DepΩ(x) = { d : DetCondΩ(d,x) }
~~~

~~~text
ResΩ(x)
~~~

Residual field of Ω relative to x.

This avoids naive set-theoretic treatment of Ω.

---

## 2. Core Axiom / Theorem-Schema

~~~text
∀x ∈ 𝔻 :
ProperΩ(x) ⇒ ∃d [DetCondΩ(d,x)]
~~~

Expanded:

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

Equivalent dependence form:

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
DepΩ(x) ≠ ∅
~~~

---

## 3. Contrapositive

~~~text
∀x ∈ 𝔻 :
[x ≠ Ω ∧ DepΩ(x) = ∅]
⇒
¬ManifestΩ(x)
~~~

Reading:

> If a supposed proper manifestation has no condition of determinability, it cannot manifest as something.

---

## 4. Determinability Argument

The strongest derivation path is:

~~~text
ManifestΩ(x) as x
⇒ x is determinable as x
⇒ x is distinguishable as x
⇒ at least one condition makes x distinguishable/determinable
⇒ ∃d [DetCondΩ(d,x)]
⇒ DepΩ(x) ≠ ∅
~~~

Therefore:

~~~text
No determinability condition
⇒ no distinguishability
⇒ no manifestation as x
~~~

---

## 5. Relation, Dependence, Determinability

Version 0.3.0 separates three levels:

~~~text
RelΩ(x)       = x stands in relation
DepΩ(x)       = x has dependence
DetCondΩ(d,x) = d is necessary for x to be determinable as x
~~~

Not every relation is automatically a critical dependence.

Not every dependence is equally relevant to every use.

For existence as a proper manifestation, minimal determinability is required.

For error diagnosis, critical excluded determinability-conditions are required.

---

## 6. Types of Determinability Conditions

A determinability-condition may be:

~~~text
logical
definitional
structural
semantic
differential
axiomatic
causal
temporal
material
informational
observational
dynamic
consequential
contextual
~~~

The law is not limited to physical causality.

---

## 7. Local Closure and Absolute Closure

~~~text
LocalClosureF(x)
~~~

A framework `F` closes `x` locally for a defined scope.

This can be valid.

~~~text
AbsolutelyClosedΩ(x)
~~~

`x` has no non-zero determinability-condition, dependence, relation, distinction, or field-reference.

For proper manifestations, absolute closure is impossible.

~~~text
ProperΩ(x) ⇒ ¬AbsolutelyClosedΩ(x)
~~~

---

## 8. Operational Error Formula

Let:

~~~text
F = framework/model/theory/algorithm/discipline/answer
U = concrete use of F
x = manifestation under treatment
d = critical determinability-condition
~~~

Then:

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

This replaces the weaker phrase:

~~~text
ClaimsTotalityF(x)
~~~

with actual operational use.

---

## 9. Scope Violation

~~~text
ScopeViolationΩ(F,x,U) ⇔
ActualUseU(F,x) exceeds ValidScope(F,x)
~~~

Equivalent diagnostic form:

~~~text
ScopeViolationΩ(F,x,U) ⇔
∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

A model fails structurally when its use requires a condition that the model excludes.

---

## 10. Validity Formula

~~~text
ValidΩ(a,F,U) ⇔
CorrectF(a)
∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
∧ CriticalDepΩ(a,U) preserved
~~~

Therefore:

~~~text
CorrectF(a) ≠ ValidΩ(a,F,U)
~~~

Correctness inside F is not structural validity in use U.

---

## 11. Summary

~~~text
Proper manifestation requires determinability.
Determinability requires at least one non-zero condition.
Local closure is legitimate inside scope.
Structural error is scope violation plus excluded critical condition.
~~~

<!-- BEGIN V0.4_TYPE_STATUS_OF_OMEGA -->
# v0.4.0 — Type Status of Ω

## 1. Ω Is Not a Proper Manifestation

Ω must not be treated as one more object inside the field.

~~~text
Ω = ∞Tot
Ω = total field without outside
Outside(Ω) = ∅
~~~

Therefore:

~~~text
ProperΩ(Ω) = false
~~~

The predicate `ProperΩ(x)` applies only to manifestations distinct from Ω:

~~~text
ProperΩ(x) ⇔ ManifestΩ(x) ∧ x ≠ Ω
~~~

## 2. Dependence Applies Only to Proper Manifestations

The law is:

~~~text
∀x ∈ 𝔻 :
ProperΩ(x) ⇒ ∃d [DetCondΩ(d,x)]
~~~

Expanded:

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

For Ω:

~~~text
DepΩ(Ω) = type-error / non-applicable
DetCondΩ(d,Ω) = not required in the same sense
OpenΩ(Ω) = undefined
ClosedΩ(Ω) = undefined
~~~

## 3. Why Ω Does Not Depend

Dependence requires a condition, field, outside, distinction, or residual reference relative to a proper manifestation.

But:

~~~text
Outside(Ω) = ∅
ResΩ(Ω) = not applicable
~~~

Ω does not depend because Ω is not a fragment.

Ω coincides with the infinite total field of conditions.

## 4. Correct Chain

~~~text
Ω = totality
Ω = infinity
infinity = without outside
without outside = not dependent on another field
~~~

For every `x ≠ Ω`:

~~~text
x is not the infinite totality
x has residual field
x has determinability conditions
x depends
~~~

## 5. Final Type-Correct Form

~~~text
Ω = ∞Tot ∧ Outside(Ω)=∅
∀x∈𝔻 :
[ManifestΩ(x) ∧ x≠Ω] ⇒ ∃d DetCondΩ(d,x)
DepΩ(Ω) = non-applicable
~~~
<!-- END V0.4_TYPE_STATUS_OF_OMEGA -->
