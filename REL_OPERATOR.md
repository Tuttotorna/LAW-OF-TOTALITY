# The RelΩ Operator — Hardened Version

## 1. Current Status

`RelΩ` remains a primitive.

~~~text
RelΩ(x, ResΩ(x)) = relation of x with the residual field of Ω relative to x
~~~

This version avoids treating Ω as an ordinary set.

Instead of writing:

~~~text
Ω minus x
~~~

we write:

~~~text
ResΩ(x)
~~~

where `ResΩ(x)` means the residual field relative to x.

---

## 2. Basic Use

For any `x ≠ Ω`:

~~~text
OpenΩ(x) ⇔ RelΩ(x, ResΩ(x)) ≠ 0
~~~

Absolute closure:

~~~text
AbsolutelyClosedΩ(x) ⇔ RelΩ(x, ResΩ(x)) = 0
~~~

The law states that no proper manifestation is absolutely closed.

~~~text
EΩ(x) ∧ x ≠ Ω ⇒ RelΩ(x, ResΩ(x)) ≠ 0
~~~

---

## 3. Possible Decomposition

A preliminary decomposition:

~~~text
RelΩ(x, ResΩ(x)) =
CausΩ(x)
∨ InfoΩ(x)
∨ StructΩ(x)
∨ DefΩ(x)
∨ DynΩ(x)
∨ TempΩ(x)
∨ ObsΩ(x)
∨ ConseqΩ(x)
∨ DiffΩ(x)
~~~

Where:

~~~text
CausΩ(x)    causal dependence
InfoΩ(x)    informational relation
StructΩ(x)  structural co-determination
DefΩ(x)     definitional/logical dependence
DynΩ(x)     dynamic or transformative interaction
TempΩ(x)    temporal dependence
ObsΩ(x)     observational / measurement dependence
ConseqΩ(x)  consequential dependence
DiffΩ(x)    differential/distinction dependence
~~~

---

## 4. Minimal Operational Rule

To show that `x` is not absolutely closed, it is enough to identify one non-zero relation type.

~~~text
∃r ∈ RelTypes :
rΩ(x) ≠ 0
~~~

Then:

~~~text
OpenΩ(x)
~~~

---

## 5. Practical Diagnostic

For any object `x`, ask:

~~~text
What causes x?
What defines x?
What distinguishes x?
What conditions x?
What changes x?
What observes x?
What does x affect?
What does x require?
What does x exclude?
What does x imply?
What field makes x determinable as x?
~~~

If any answer is non-empty, then:

~~~text
AbsolutelyClosedΩ(x) = false
~~~

---

## 6. Warning

`RelΩ` must not be reduced prematurely to a single relation type.

If `RelΩ` is reduced only to causality, then logical, informational, structural, symbolic, mathematical, and observational dependence may be missed.

The operator must remain broad enough to preserve the law:

~~~text
Every proper manifestation depends.
~~~
