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
