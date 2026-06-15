# Applied Case #001 — Monty Hall

## Why this case matters

The Monty Hall problem is a clean public demonstration of the Law of Totality.

It is famous, simple, and fully enumerable.

The point is not that the switching result is new.

The point is that the common wrong answer reveals a deeper structural error:

> the final visible fragment is mistaken for the whole probability structure.

---

## The problem

There are three doors.

Behind one door there is a car.

Behind two doors there are goats.

The player chooses one door.

The host knows where the car is, opens another door, and always reveals a goat.

The player can now stay with the first choice or switch to the remaining closed door.

---

## The common wrong answer

Many people say:

> There are now two closed doors, so the probability is 50/50.

This reasoning is wrong because it treats the final visible state as the whole structure.

The final visible state is:

> two closed doors.

But the total generating structure includes more than that.

It includes:

- the first choice;
- the original 1/3 probability;
- the host's knowledge;
- the host's rule;
- the opened goat door;
- the information transferred by the host's action.

---

## Full enumeration

Assume the player first chooses Door 1.

| Case | Car position | Host action | Stay | Switch |
|---|---|---|---|---|
| 1 | Door 1 | Opens a goat door | Wins | Loses |
| 2 | Door 2 | Opens Door 3 | Loses | Wins |
| 3 | Door 3 | Opens Door 2 | Loses | Wins |

Therefore:

- staying wins in 1 case out of 3;
- switching wins in 2 cases out of 3.

So:

$$
P(\text{Stay wins}) = \frac{1}{3}
$$

$$
P(\text{Switch wins}) = \frac{2}{3}
$$

The correct choice is:

> Switch.

---

## Law of Totality reading

The error is not arithmetic.

The error is structural.

The visible local fragment says:

> two closed doors.

The total generating structure says:

> the host's action is not neutral; it carries information because it is constrained by knowledge and rule.

The final state looks symmetrical.

The generating structure is not symmetrical.

This is the key point:

> A local fragment can look symmetrical while the total generating structure is asymmetrical.

---

## Structural diagnosis

The mistaken 50/50 answer appears when this fragment:

> two closed doors remain

is treated as if it were equivalent to the whole structure:

> initial choice + host knowledge + host rule + constrained reveal + transferred information.

That substitution produces the error.

The correction is not to compute harder.

The correction is to restore the total structure before computing.

---

## General form

Monty Hall is a practical case of fragment-totality divergence:

$$
E_{\Omega}(x)=\lim_{A\to\Omega}\Delta(F_A(x),\Omega_A(x))
$$

Here:

- \(F_A(x)\) is the visible final fragment: two closed doors;
- \(\Omega_A(x)\) is the accessible total probability structure;
- \(\Delta\) is the structural difference between the apparent 50/50 symmetry and the real 1/3 vs 2/3 asymmetry.

---

## Conclusion

The Monty Hall problem shows that a correct answer does not emerge from the visible fragment alone.

It emerges only when the total generating structure is restored.

This is the practical force of the Law of Totality:

> do not solve the fragment as if it were the whole.

