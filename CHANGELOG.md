<!-- BEGIN V0.4_CHANGELOG -->
# v0.4.0 — Infinity / No-Outside Clarification

This release clarifies the status of Ω.

## Core clarification

~~~text
Ω = ∞Tot
Ω = totality
Ω = infinity
Outside(Ω) = ∅
~~~

## Main correction

The law does not say that Ω depends.

The law applies only to proper manifestations:

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

For Ω:

~~~text
DepΩ(Ω) = non-applicable / type-error
OpenΩ(Ω) = undefined
ClosedΩ(Ω) = undefined
~~~

## Core sentence

~~~text
Ω does not depend because Ω is the infinite totality without outside.
Every x ≠ Ω depends because every x ≠ Ω is a proper manifestation with determinability conditions.
~~~

## New file

~~~text
INFINITY_NO_OUTSIDE.md
~~~
<!-- END V0.4_CHANGELOG -->

# Changelog

## v0.3.0 — Determinability Core and Operational Audit

Core upgrade:

~~~text
generic dependence
⇒
conditions of determinability
~~~

New central formula:

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

Operational error formula:

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

Added files:

~~~text
DETERMINABILITY_PRINCIPLE.md
OPERATIONAL_AUDIT.md
OPERATIONAL_TEST_TEMPLATE.md
~~~

Major correction:

~~~text
ClaimsTotality
⇒
ActualUse exceeds ValidScope
~~~

## v0.2.0 — Hardened Non-Closure

Corrected local closure.

Core distinction:

~~~text
Local closure is not error.
False totalization of local closure is error.
~~~

## v0.1.0 — Formal Core

Initial formal repository release.

Core sentence:

~~~text
Everything that exists depends.
If it does not depend, it cannot exist.
~~~
