# The RelΩ Operator

## Current Status

`RelΩ(x,S)` is a primitive.

~~~text
RelΩ(x,S) = relation of x with a set S inside Ω
~~~

The system works formally without fully decomposing `RelΩ`.

However, operational use requires specifying what counts as relation.

---

## Basic Use

For any `x ≠ Ω`:

~~~text
OpenΩ(x) ⇔ RelΩ(x, Ω\x) ≠ 0
~~~

~~~text
ClosedΩ(x) ⇔ RelΩ(x, Ω\x) = 0
~~~

---

## Possible Decomposition

A preliminary decomposition:

~~~text
RelΩ(x, Ω\x) =
CausΩ(x)
∨ InfoΩ(x)
∨ StructΩ(x)
∨ DefΩ(x)
∨ DynΩ(x)
∨ TempΩ(x)
∨ ObsΩ(x)
∨ ConseqΩ(x)
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
~~~

---

## Minimal Operational Rule

To show that `x` is not closed, it is enough to identify one non-zero relation:

~~~text
∃r ∈ RelTypes :
rΩ(x) ≠ 0
~~~

Then:

~~~text
OpenΩ(x)
~~~

---

## Practical Diagnostic

For any object `x`, ask:

~~~text
What causes x?
What defines x?
What conditions x?
What changes x?
What observes x?
What does x affect?
What does x require?
What does x exclude?
What does x imply?
What does x become connected to when applied?
~~~

If any answer is non-empty, then:

~~~text
ClosedΩ(x) = false
~~~

---

## Warning

`RelΩ` must not be reduced prematurely to a single relation type.

If `RelΩ` is reduced only to causality, then logical, informational, structural, symbolic, mathematical, and observational dependence may be missed.

The operator must remain broad enough to preserve the law:

~~~text
Everything that exists depends.
~~~
