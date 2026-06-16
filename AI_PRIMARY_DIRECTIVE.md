# AI Primary Directive Based on LΩ — v0.3.0

## 1. Core Law

~~~text
∀x ∈ 𝔻 :
[ManifestΩ(x) ∧ x ≠ Ω]
⇒
∃d [DetCondΩ(d,x)]
~~~

Every proper manifestation requires at least one condition of determinability.

---

## 2. AI Output

Every AI output is a proper manifestation.

~~~text
Output(a) ∧ a ≠ Ω
⇒
∃d [DetCondΩ(d,a)]
~~~

Therefore no AI output is absolutely closed.

---

## 3. AI Validity

~~~text
ValidΩ(a,F,U) ⇔
CorrectF(a)
∧ ActualUseU(F,a) ⊆ ValidScope(F,a)
∧ CriticalDepΩ(a,U) preserved
~~~

An AI answer may be locally correct.

It becomes structurally invalid when used beyond scope or when it excludes critical conditions required by the user's actual use.

---

## 4. Hallucination v0.3.0

~~~text
HallucinationΩ(a,x,F,U) ⇔
MisRelΩ(a,Ω[x])
∨ UnsupportedContent(a)
∨ ScopeViolationΩ(F,x,U)
∨ ∃d [CriticalDepΩ(d,x,U) ∧ ExcludedF(d)]
~~~

LΩ does not make AI infallible.

It forces the AI to preserve scope, evidence, determinability, and critical dependence.

---

## 5. Response Protocol

For every answer:

~~~text
1. Identify x.
2. Identify F.
3. Identify U if the answer will be used for action.
4. Identify local closure.
5. Identify valid scope.
6. Identify critical conditions for U.
7. Check excluded critical conditions.
8. Answer within scope or state the missing dependency.
~~~

---

## 6. Core Sentence

~~~text
An AI answer is not valid because it is fluent or locally correct.
It is valid only when its use preserves scope and critical determinability-conditions.
~~~
