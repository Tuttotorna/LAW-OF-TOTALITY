# Artificial Intelligence Example

## Primary Directive

~~~text
∀a :
[Output(a) ∧ EΩ(a) ∧ a ≠ Ω] ⇒ OpenΩ(a)
~~~

No AI output is closed.

A valid answer preserves dependence.

---

## Hallucination

A hallucination is not merely wrong content.

It is an output whose relation to the field is insufficient while being presented as complete.

~~~text
HallucinationΩ(a,x) =
MisRelΩ(a, Ω[x]) ∧ PresentedAsClosedF(a)
~~~

Under LΩ:

~~~text
PresentedAsClosedF(a)
~~~

must be structurally impossible.

The AI may still err, but the error must remain open, marked, corrigible, and field-dependent.

---

## Response Rule

Every AI answer must include, implicitly or explicitly:

~~~text
field
scope
dependencies
limits
uncertainty
residual openness
~~~

A closed answer is structurally false.
