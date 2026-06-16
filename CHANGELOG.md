# Changelog


## v0.5.0 — Ω-Validity Calculus

This release adds the second formal level of the Law of Totality.

### Added

~~~text
OMEGA_VALIDITY_CALCULUS.md
STRUCTURAL_ERROR_PREVENTION_THEOREM.md
AI_PRIMARY_DIRECTIVE.md
docs/RELEASE_v0.5.0.md
~~~

### Core transition

~~~text
from structural error
to structural validity
from diagnosis
to prevention
~~~

### Structural Error Formula

~~~text
ErrΩ(a,F,U) ⇔
LocalClosureF(a)
∧ ActualUseU(F,a) exceeds ValidScope(F,a)
∧ ∃d [CriticalDepΩ(d,a,U) ∧ ExcludedF(d)]
~~~

### Structural Validity Formula

~~~text
ValidΩ(a,F,U) ⇔
CorrectF(a)
∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
∧ ∀d [CriticalDepΩ(d,a,U) ⇒ ¬ExcludedF(d)]
~~~

### Theorem

~~~text
[AssertS(a,F,U) ⇒ ValidΩ(a,F,U)]
⇒
[AssertS(a,F,U) ⇒ ¬ErrΩ(a,F,U)]
~~~

### Meaning

A theory of structural error permits a theory of structural validity.

A theory of structural validity permits prevention of that class of error.

---


## v0.4.1 — Notation, Citation, and Operational Case Correction

This release corrects repository-level formal consistency.

### Corrected

~~~text
∀x ∈ D :
~~~

has been replaced by:

~~~text
∀x ∈ D :
~~~

This removes the broken domain notation that appeared in the previous Markdown rendering.

### Metadata updated

~~~text
CITATION.cff: version 0.4.1
date-released: 2026-06-16
.zenodo.json: upload_type publication
publication_type technicalnote
~~~

### Added

~~~text
examples/CASE_001_AI_HALLUCINATION.md
examples/CASE_002_ECONOMIC_MODEL_SCOPE.md
examples/CASE_003_PROJECT_SAFETY.md
docs/RELEASE_v0.4.1.md
~~~

### Core preserved

~~~text
∀x ∈ D :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

The release does not expand the theory.

It stabilizes notation, citation, metadata, and minimal operational inspection cases.

---

## v0.4.0 — Infinity / No-Outside Clarification

This release clarifies the status of Ω.

### Core clarification

~~~text
Ω = ∞Tot
Ω = totality
Ω = infinity
Outside(Ω) = ∅
~~~

### Main correction

The law does not say that Ω depends.

The law applies only to proper manifestations:

~~~text
∀x ∈ D :
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

### Core sentence

~~~text
Ω does not depend because Ω is the infinite totality without outside.
Every x ≠ Ω depends because every x ≠ Ω is a proper manifestation with determinability conditions.
~~~

### New file

~~~text
INFINITY_NO_OUTSIDE.md
~~~

---

## v0.3.0 — Determinability Core and Operational Audit

Core upgrade:

~~~text
generic dependence ⇒ conditions of determinability
~~~

New central formula:

~~~text
∀x ∈ D :
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
ClaimsTotality ⇒ ActualUse exceeds ValidScope
~~~

---

## v0.2.0 — Hardened Non-Closure

Corrected local closure.

Core distinction:

~~~text
Local closure is not error.
False totalization of local closure is error.
~~~

---

## v0.1.0 — Formal Core

Initial formal repository release.

Core sentence:

~~~text
Everything that exists depends.
If it does not depend, it cannot exist.
~~~
