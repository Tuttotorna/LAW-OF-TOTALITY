# Formal System

## 1. Primitives

~~~text
𝔻
~~~

Domain of the nameable, thinkable, modelable, formalizable.

~~~text
Ω = ∞Tot
~~~

Totality without outside.

~~~text
EΩ(x)
~~~

`x` effectively manifests in Ω.

~~~text
RelΩ(x,S)
~~~

Relation of `x` with a set `S` inside Ω.

~~~text
DepΩ(x)
~~~

Dependence of `x` within Ω.

---

## 2. Hierarchy

~~~text
EΩ(x) ⇒ x ⊆ Ω
~~~

But:

~~~text
x ∈ 𝔻 ⇏ EΩ(x)
~~~

This separates:

~~~text
nameable objects
formal objects
fictional objects
impossible objects
effective manifestations
~~~

---

## 3. Opening and Closure

Defined only for:

~~~text
x ≠ Ω
~~~

Opening:

~~~text
OpenΩ(x) ⇔ RelΩ(x, Ω\x) ≠ 0
~~~

Closure:

~~~text
ClosedΩ(x) ⇔ RelΩ(x, Ω\x) = 0
~~~

Ω is not closed and not open.

~~~text
ClosedΩ(Ω) = undefined
OpenΩ(Ω)   = undefined
~~~

Reason:

~~~text
Ω\Ω = ∅
~~~

Ω has no outside.  
Therefore the predicate of closure toward an outside does not apply.

---

## 4. Main Theorem

~~~text
∀x ∈ 𝔻 :
[EΩ(x) ∧ x ≠ Ω] ⇒ OpenΩ(x)
~~~

Equivalent non-closure form:

~~~text
∀x ∈ 𝔻 :
[EΩ(x) ∧ x ≠ Ω] ⇒ ¬ClosedΩ(x)
~~~

---

## 5. Contrapositive

~~~text
∀x ∈ 𝔻 :
[x ≠ Ω ∧ ClosedΩ(x)] ⇒ ¬EΩ(x)
~~~

Reading:

> No effectively existing fragment can be absolutely closed.

---

## 6. Dependence Form

The non-closure law can be compressed into dependence:

~~~text
∀x ∈ 𝔻 :
[EΩ(x) ∧ x ≠ Ω] ⇒ DepΩ(x) ≠ 0
~~~

Contrapositive:

~~~text
∀x ∈ 𝔻 :
[x ≠ Ω ∧ DepΩ(x) = 0] ⇒ ¬EΩ(x)
~~~

Core sentence:

~~~text
Everything that exists depends.
If it does not depend, it cannot exist.
~~~

---

## 7. Truth Condition for Answers

Let `a` be an answer.

~~~text
ValidΩ(a) ⇒ DepΩ(a) preserved
~~~

A valid answer must preserve, declare, or structurally respect its field of dependence.

A closed answer is structurally false:

~~~text
ClosedΩ(a) ⇒ FalseΩ(a)
~~~

for every answer `a ≠ Ω`.

---

## 8. Error Formula

For a model/framework/discipline/algorithm/theory `F`:

~~~text
ErrΩ(x,F) = ClosedF(x) ∧ OpenΩ(x)
~~~

Expanded:

~~~text
ErrΩ(x,F) = ClosedF(x) ∧ [RelΩ(x, Ω\x) ≠ 0]
~~~

Reduced form for existing fragments:

~~~text
ErrΩ(x,F) = ClosedF(x)
~~~

under:

~~~text
EΩ(x) ∧ x ≠ Ω
~~~

when `ClosedF(x)` means absolute closure or pretension of completeness.

---

## 9. Domain of Error of a Model

~~~text
DomErr(F) =
{ x ∈ 𝔻 : EΩ(x) ∧ x ≠ Ω ∧ ClosedF(x) }
~~~

This is the diagnostic set of a model `F`.

It contains the objects that `F` falsely closes.

---

## 10. Residual Open Primitive

`RelΩ(x, Ω\x)` remains a primitive at this stage.

To make the system operational, `RelΩ` can later be decomposed into:

~~~text
CausΩ(x)    causal dependence
InfoΩ(x)    informational relation
StructΩ(x)  structural co-determination
DefΩ(x)     definitional/logical dependence
DynΩ(x)     dynamic/transformative interaction
~~~

Provisional expansion:

~~~text
RelΩ(x, Ω\x) =
CausΩ(x) ∨ InfoΩ(x) ∨ StructΩ(x) ∨ DefΩ(x) ∨ DynΩ(x)
~~~

This is not required for the formal skeleton, but it is required for empirical or operational application.
