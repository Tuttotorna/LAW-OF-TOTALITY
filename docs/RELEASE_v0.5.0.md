# Release v0.5.0 — Ω-Validity Calculus

## Purpose

This release adds the second level of the Law of Totality:

~~~text
from structural error
to structural validity
from diagnosis
to prevention
~~~

## Added

~~~text
OMEGA_VALIDITY_CALCULUS.md
STRUCTURAL_ERROR_PREVENTION_THEOREM.md
AI_PRIMARY_DIRECTIVE.md
docs/RELEASE_v0.5.0.md
~~~

## Core Error Formula

~~~text
ErrΩ(a,F,U) ⇔
LocalClosureF(a)
∧ ActualUseU(F,a) exceeds ValidScope(F,a)
∧ ∃d [CriticalDepΩ(d,a,U) ∧ ExcludedF(d)]
~~~

## Core Validity Formula

~~~text
ValidΩ(a,F,U) ⇔
CorrectF(a)
∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
∧ ∀d [CriticalDepΩ(d,a,U) ⇒ ¬ExcludedF(d)]
~~~

## Structural Error Prevention Theorem

~~~text
[AssertS(a,F,U) ⇒ ValidΩ(a,F,U)]
⇒
[AssertS(a,F,U) ⇒ ¬ErrΩ(a,F,U)]
~~~

## Main Meaning

This release does not claim omniscience.

It defines a formal prevention rule:

~~~text
A system cannot authorize structural error if every assertion must first satisfy structural validity.
~~~

## AI Implication

AI hallucination is not treated as an error to correct after output.

It is treated as a false closure to prevent before output.

## Final Sentence

~~~text
We cannot build a system that contains Ω.
We can build a system that prevents every F ≠ Ω from behaving as Ω.
~~~
