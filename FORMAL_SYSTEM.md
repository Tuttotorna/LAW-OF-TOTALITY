# Formal System — Hardened Core

## 1. Primitives

~~~text
𝔻
~~~

Domain of the nameable, thinkable, modelable, formalizable.

~~~text
Ω = ∞Tot
~~~

Total field without outside.

~~~text
EΩ(x)
~~~

`x` effectively manifests in Ω.

~~~text
ResΩ(x)
~~~

Residual field of Ω relative to x.

This replaces the fragile set-theoretic notation `Ω minus x`.

Ω is not treated as an ordinary set.

~~~text
RelΩ(x, ResΩ(x))
~~~

Relation of `x` with the residual field of Ω relative to x.

~~~text
DepΩ(x)
~~~

Dependence of `x` within Ω.

---

## 2. Hierarchy

~~~text
EΩ(x) ⇒ x manifests within Ω
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

## 3. Proper Manifestation

The law applies only to proper manifestations.

~~~text
ProperΩ(x) ⇔ EΩ(x) ∧ x ≠ Ω
~~~

The clause `x ≠ Ω` is essential.

Without it, Ω itself becomes a false counterexample.

---

## 4. Opening and Absolute Closure

Defined only for:

~~~text
x ≠ Ω
~~~

Opening:

~~~text
OpenΩ(x) ⇔ RelΩ(x, ResΩ(x)) ≠ 0
~~~

Absolute closure:

~~~text
AbsolutelyClosedΩ(x) ⇔ RelΩ(x, ResΩ(x)) = 0
~~~

Ω is not closed and not open.

~~~text
ClosedΩ(Ω) = undefined
OpenΩ(Ω)   = undefined
~~~

Reason:

~~~text
Ω has no outside.
Therefore the predicate of closure toward an outside does not apply to Ω.
~~~

---

## 5. Main Theorem / Main Axiom

At this stage the law should be treated as a meta-structural axiom or theorem-schema, depending on the chosen primitive basis.

~~~text
∀x ∈ 𝔻 :
ProperΩ(x) ⇒ OpenΩ(x)
~~~

Expanded:

~~~text
∀x ∈ 𝔻 :
[EΩ(x) ∧ x ≠ Ω] ⇒ RelΩ(x, ResΩ(x)) ≠ 0
~~~

Dependence form:

~~~text
∀x ∈ 𝔻 :
[EΩ(x) ∧ x ≠ Ω] ⇒ DepΩ(x) ≠ 0
~~~

---

## 6. Contrapositive

~~~text
∀x ∈ 𝔻 :
[x ≠ Ω ∧ DepΩ(x) = 0] ⇒ ¬EΩ(x)
~~~

Reading:

> No absolutely independent proper fragment can effectively manifest.

---

## 7. Proof Direction From Determinability

A stronger derivation can be attempted from determinability.

~~~text
EΩ(x) as x
⇒ x is determinable as x
⇒ x is distinguishable from non-x
⇒ distinction requires relation/difference/condition
⇒ DepΩ(x) ≠ 0
~~~

Thus:

~~~text
Manifestation as x requires determinability.
Determinability requires non-zero relation.
Therefore manifestation as x requires dependence.
~~~

This is the strongest current proof direction.

---

## 8. Local Closure Versus Absolute Closure

Local closure can be legitimate.

~~~text
LocalClosureF(x)
~~~

means that a framework `F` closes `x` for a defined purpose, scope, axiom system, model, calculation, or decision.

Absolute closure is different.

~~~text
AbsolutelyClosedΩ(x)
~~~

means that `x` has no dependence, relation, condition, distinction, or determinability beyond itself.

The law rejects absolute closure of proper manifestations.

It does not reject useful local closure.

---

## 9. Hardened Error Formula

Initial version:

~~~text
ErrΩ(x,F) = ClosedF(x) ∧ OpenΩ(x)
~~~

Correction:

~~~text
ErrΩ(x,F) =
LocalClosureF(x) ∧ ScopeViolationΩ(F,x)
~~~

Equivalent operational version:

~~~text
ErrΩ(x,F) =
ClosedF(x) ∧ ClaimsTotalityF(x)
~~~

Where:

~~~text
ScopeViolationΩ(F,x) =
F uses its local closure beyond its field of validity.
~~~

And:

~~~text
ClaimsTotalityF(x) =
F(x) is treated as Ω(x).
~~~

---

## 10. Validity Formula

~~~text
ValidΩ(a,F) =
CorrectF(a) ∧ ScopeDeclared(F) ∧ DepΩ(a) preserved
~~~

Therefore:

~~~text
CorrectF(a) ≠ ValidΩ(a)
~~~

A locally correct answer is structurally valid only when it preserves scope and dependence.

---

## 11. Domain of Structural Error

~~~text
DomErr(F) =
{ x ∈ 𝔻 :
  EΩ(x) ∧ x ≠ Ω ∧ LocalClosureF(x) ∧ ScopeViolationΩ(F,x)
}
~~~

This is the diagnostic set of a model `F`.

It contains the objects that `F` does not merely close locally, but falsely totalizes.

---

## 12. Summary

~~~text
Proper manifestation implies dependence.
Dependence implies non-absolute-closure.
Local closure is allowed.
False totalization is error.
~~~
