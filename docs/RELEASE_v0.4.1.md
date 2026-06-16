# Release v0.4.1 — Notation, Citation, and Operational Case Correction

## Purpose

This release is not a theoretical expansion.

It is a stabilization release.

## Corrections

~~~text
∀x ∈ D :
~~~

has been corrected to:

~~~text
∀x ∈ D :
~~~

The missing domain symbol made the formal notation visually broken.

## Metadata

~~~text
CITATION.cff → version 0.4.1
.zenodo.json → publication / technicalnote
~~~

## Operational Cases Added

~~~text
examples/CASE_001_AI_HALLUCINATION.md
examples/CASE_002_ECONOMIC_MODEL_SCOPE.md
examples/CASE_003_PROJECT_SAFETY.md
~~~

## Core Formula Preserved

~~~text
∀x ∈ D :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

## Error Formula Preserved

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

## Status

This release improves formal readability, metadata coherence, and operational inspectability.

It does not claim external validation.
