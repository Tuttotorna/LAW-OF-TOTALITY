# The RelΩ Operator — v0.3.0

## 1. Status

`RelΩ` remains useful, but v0.3.0 places determinability before generic relation.

Earlier form:

~~~text
OpenΩ(x) ⇔ RelΩ(x, ResΩ(x)) ≠ 0
~~~

Hardened form:

~~~text
ManifestΩ(x) ∧ x ≠ Ω
⇒
∃d [DetCondΩ(d,x)]
~~~

Relation is now subordinate to determinability.

---

## 2. Determinability Condition

~~~text
DetCondΩ(d,x)
~~~

means:

~~~text
d is a non-zero condition without which x is not determinable as x.
~~~

This may include relations, but is not reduced to relation.

---

## 3. DepΩ

~~~text
DepΩ(x) = { d : DetCondΩ(d,x) }
~~~

So:

~~~text
DepΩ(x) ≠ ∅
~~~

means:

~~~text
x has at least one condition that makes it determinable as x.
~~~

---

## 4. Candidate Condition Types

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

---

## 5. Minimal and Critical Conditions

Minimal condition:

~~~text
MinimalDepΩ(x)
~~~

A condition required for x to manifest as x.

Critical condition:

~~~text
CriticalDepΩ(d,x,U)
~~~

A condition required for use U to remain valid.

The operational audit uses critical conditions.

---

## 6. Practical Diagnostic

For any `x`, ask:

~~~text
What makes x determinable as x?
What distinguishes x from non-x?
What condition would make x collapse, change, or lose identity?
What condition is required by the actual use U?
What condition is excluded by the model F?
~~~

---

## 7. Warning

Do not reduce determinability to causality.

Do not reduce dependence to any relation.

The hard nucleus is:

~~~text
No manifestation as x without a condition of determinability.
~~~
