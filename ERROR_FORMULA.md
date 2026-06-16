# Formula of Error — v0.3.0 Operational Version

## 1. Previous Hardened Formula

Version 0.2.0:

~~~text
ErrΩ(x,F) =
LocalClosureF(x) ∧ ScopeViolationΩ(F,x)
~~~

This was stronger than the original formula because it protected legitimate local closure.

---

## 2. Remaining Weakness

The term:

~~~text
ScopeViolationΩ(F,x)
~~~

was still too abstract.

The term:

~~~text
ClaimsTotalityF(x)
~~~

could sound psychological or explicit.

But many errors are not explicit claims.

They happen in actual use.

A model may not say "I am total", yet it may be used as if it were sufficient.

---

## 3. v0.3.0 Operational Error Formula

~~~text
ErrΩ(x,F,U) ⇔
LocalClosureF(x)
∧ ActualUseU(F,x) exceeds ValidScope(F,x)
∧ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

Where:

~~~text
x = manifestation under treatment
F = framework, model, theory, discipline, answer, algorithm
U = concrete use or deployment of F
d = critical determinability-condition or dependency
~~~

---

## 4. Short Form

~~~text
Error = local closure used beyond valid scope while excluding a critical condition.
~~~

---

## 5. Why Local Closure Is Not Error

Local closure is necessary for:

~~~text
mathematical proof
engineering calculation
medical diagnosis
maps
software
law
science
decision-making
ordinary answers
~~~

The problem is not closure inside a declared field.

The problem is closure used beyond the field that makes it valid.

---

## 6. Scope Violation

~~~text
ScopeViolationΩ(F,x,U) ⇔
ActualUseU(F,x) exceeds ValidScope(F,x)
~~~

Operational test:

~~~text
ScopeViolationΩ(F,x,U) ⇔
∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

Meaning:

> The use U requires a critical condition d, but F excludes d.

---

## 7. Correctness Versus Validity

~~~text
CorrectF(a) ≠ ValidΩ(a,F,U)
~~~

Correctness inside a framework does not imply validity in a concrete use.

Hardened validity:

~~~text
ValidΩ(a,F,U) ⇔
CorrectF(a)
∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
∧ CriticalDepΩ(a,U) preserved
~~~

---

## 8. Example: Arithmetic

~~~text
2 + 2 = 4
~~~

This is locally correct in ordinary arithmetic.

It is not false because it is locally closed.

It would become structurally false only if used as a total description of Ω or beyond its valid field.

---

## 9. Example: Algorithm

An algorithm can be correct in specification.

~~~text
CorrectSpec(A)
~~~

But deployment can fail.

~~~text
CorrectSpec(A) ≠ ValidDeploymentΩ(A,U)
~~~

Error:

~~~text
ErrΩ(A,F,U) ⇔
LocalClosureF(A)
∧ ActualUseU(F,A) exceeds ValidScope(F,A)
∧ ∃d [CriticalDepΩ(d,A,U) ∧ ExcludedF(d)]
~~~

---

## 10. Diagnostic Questions

For any `F`, `x`, and `U`, ask:

~~~text
What does F close locally?
What is the valid scope of F?
How is F actually used?
Does actual use exceed valid scope?
Which determinability-conditions are critical for U?
Which of them are excluded by F?
What failure or fragility follows from the exclusion?
~~~

---

## 11. Core Sentence

~~~text
Do not ask only whether a model is correct.
Ask whether its use preserves the conditions that make the object determinable in that use.
~~~
