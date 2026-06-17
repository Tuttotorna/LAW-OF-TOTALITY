# Formal Theorems and Counterexamples Core

## Status

This document turns the Law of Totality / Structural Error Formula into a reviewable formal core.

It does not claim external validation.

It provides definitions, theorem schemas, proof sketches, conditions of application, and counterexample classes.

The purpose is to make the framework easier to attack, refine, reject, or strengthen.

## 1. Purpose

The central distinction is:

Every theory closes locally. Reality remains open.

The formal question is:

When does a finite framework become structurally invalid for an actual use?

The proposed answer is:

Structural error occurs when a locally closed framework is used beyond its valid scope while excluding at least one dependency critical for that use.

## 2. Primitive Terms

Omega, written Ω:

The total field. It has no external field relative to the framework.

x:

The object being treated. It may be a situation, decision, claim, model, game, proof, metric, person, institution, system, policy, AI answer, or mathematical object.

F:

A finite framework. Examples include a theory, model, map, language, rule, metric, proof environment, game, decision protocol, algorithm, or AI response.

U:

The actual use being made of F with respect to x. Examples include prediction, decision, classification, explanation, deployment, policy, certification, judgement, or action.

d:

A dependency relevant to x for U.

## 3. Predicates

Finite(F):

F is finite or operationally bounded.

Treats(F,x):

F treats, models, describes, decides, classifies, proves, predicts, explains, or acts upon x.

Manifest_Ω(x):

x is manifested in Ω.

Proper_Ω(x):

x is a proper object in Ω, meaning x is not Ω itself.

LocalClosure_F(x):

F makes x tractable by closing it locally.

Open_Ω(x):

x remains open in Ω with respect to the total field of possible dependencies.

ValidScope(F,x):

The valid scope within which F may be used on x without structural overextension.

ActualUse_U(F,x):

F is actually being used for U with respect to x.

CriticalDep_Ω(d,x,U):

d is a dependency of x that is critical for the validity of U.

Preserved_F(d):

F preserves d adequately for U.

Excluded_F(d):

F excludes, ignores, abstracts away, suppresses, or fails to preserve d.

UseExceedsScope(F,x,U):

U exceeds ValidScope(F,x).

ValidUse_Ω(F,x,U):

F is structurally valid for U with respect to x.

Err_Ω(x,F,U):

A structural error occurs in the use of F on x for U.

## 4. Axioms

Axiom A1: Finite treatment requires local closure.

If F is finite and F treats x, then F produces a local closure of x.

Formal schema:

    Finite(F) and Treats(F,x) implies LocalClosure_F(x)

Axiom A2: Proper manifested objects remain open in Ω.

If x is manifested in Ω and x is not Ω, then x remains open in Ω.

Formal schema:

    Manifest_Ω(x) and Proper_Ω(x) implies Open_Ω(x)

Axiom A3: Local closure is not total closure.

A local closure of x by F does not imply total closure of x in Ω.

Formal schema:

    LocalClosure_F(x) does not imply Closed_Ω(x)

Axiom A4: Valid use depends on use-relevant dependencies.

If d is critical for U, and F excludes d, then F cannot be sufficient for U without restriction, supplementation, or external control.

Formal schema:

    CriticalDep_Ω(d,x,U) and Excluded_F(d) implies NotSufficient_Ω(F,x,U)

Axiom A5: Incompleteness is not automatically error.

F may exclude many dependencies without error if those dependencies are not critical for U.

Formal schema:

    Excluded_F(d) and not CriticalDep_Ω(d,x,U) does not imply Err_Ω(x,F,U)

## 5. Definition of Structural Error

Structural error is defined as:

    Err_Ω(x,F,U) iff
    LocalClosure_F(x)
    and ActualUse_U(F,x)
    and UseExceedsScope(F,x,U)
    and there exists d such that CriticalDep_Ω(d,x,U) and Excluded_F(d)

Plain form:

    Structural error =
    local closure
    + actual use beyond valid scope
    + excluded critical dependency

This is the operational core.

## 6. Definition of Valid Use

A framework F is valid for use U on x only if U remains within the valid scope of F and every dependency critical for U is preserved, controlled, or the use is restricted accordingly.

Formal schema:

    ValidUse_Ω(F,x,U) iff
    ActualUse_U(F,x)
    and not UseExceedsScope(F,x,U)
    and for every d:
        if CriticalDep_Ω(d,x,U),
        then Preserved_F(d) or ControlledOutside_F(d) or RestrictedUse_U(F,x,d)

This does not require omniscience.

It requires scope discipline.

## 7. Theorem 1: Theory-Reality Asymmetry

Theorem:

Every finite framework closes locally, while every proper manifested object remains open in Ω.

Assumptions:

    Finite(F)
    Treats(F,x)
    Manifest_Ω(x)
    Proper_Ω(x)

By A1:

    LocalClosure_F(x)

By A2:

    Open_Ω(x)

Therefore:

    LocalClosure_F(x) and Open_Ω(x)

Interpretation:

F can close x in theory.

x remains open in reality.

So:

    Closed in theory. Open in reality.

Proof status:

This is a theorem schema relative to the primitive definitions and axioms.

## 8. Theorem 2: Local Correctness Does Not Imply Valid Use

Theorem:

A result may be locally correct inside F and still not valid for U.

Assumptions:

    LocalCorrect_F(x)
    ActualUse_U(F,x)
    UseExceedsScope(F,x,U)
    exists d such that CriticalDep_Ω(d,x,U) and Excluded_F(d)

Then by the Structural Error definition:

    Err_Ω(x,F,U)

Therefore:

    LocalCorrect_F(x) does not imply ValidUse_Ω(F,x,U)

Interpretation:

A proof, model, metric, rule, game equilibrium, or AI answer can be correct inside its own framework and still fail for the actual use.

Public form:

    local correctness does not imply valid use

## 9. Theorem 3: Incompleteness Alone Is Not Structural Error

Theorem:

A framework is not structurally invalid merely because it excludes something.

Assumptions:

    LocalClosure_F(x)
    Excluded_F(d)
    not CriticalDep_Ω(d,x,U)

Then the excluded dependency d does not satisfy the critical dependency condition in the Structural Error definition.

Therefore, exclusion of d alone does not imply:

    Err_Ω(x,F,U)

Interpretation:

The Law of Totality does not say every finite framework is wrong.

It says finite frameworks become structurally invalid when used beyond the dependencies they preserve.

## 10. Theorem 4: Wrong Framework Condition

Theorem:

If a framework excludes a dependency required by the actual use, and the use treats the framework as sufficient, then the framework is structurally invalid for that use.

Assumptions:

    LocalClosure_F(x)
    ActualUse_U(F,x)
    UseAsSufficient_U(F,x)
    CriticalDep_Ω(d,x,U)
    Excluded_F(d)

If UseAsSufficient_U(F,x) occurs while d is excluded, then U exceeds the valid scope of F.

Therefore:

    Err_Ω(x,F,U)

Interpretation:

The error is not merely inside the framework.

The error is in the relation between framework, use, and excluded dependency.

## 11. Theorem 5: Wrong Game Condition

Let G be a game-theoretic framework.

A game G may define players, strategies, payoffs, information, rules, and equilibrium conditions.

Theorem:

An equilibrium inside G does not imply valid strategic use in reality.

Assumptions:

    Equilibrium_G(x)
    ActualUse_U(G,x)
    CriticalDep_Ω(d,x,U)
    Excluded_G(d)

If d is critical for U but excluded by G, then G is not sufficient for U.

Therefore:

    Equilibrium_G(x) does not imply ValidUse_Ω(G,x,U)

Interpretation:

Game theory calculates inside the game.

The Law of Totality audits whether the game is valid for the use.

Nash-compatible distinction:

    Nash: given a game, what equilibrium follows?
    Law of Totality: given a real use, does this game have the right to represent it?

## 12. Conditions of Application

The framework should not be applied vaguely.

To claim a structural error, the analyst must identify:

1. x: the object treated;
2. F: the framework used;
3. U: the actual use;
4. ValidScope(F,x): the valid scope of F;
5. at least one d: a dependency critical for U;
6. Excluded_F(d): evidence that F excludes or fails to preserve d;
7. why U exceeds the valid scope of F.

If these cannot be identified, the correct output is not structural error.

The correct output is one of:

    insufficiently specified
    possible scope risk
    suspected dependency gap
    requires domain audit

This prevents the formula from becoming rhetoric.

## 13. Counterexample Classes

A reviewer can challenge the framework by producing one of the following.

Counterexample Class A:

All conditions of the Structural Error Formula are present, but no structural error exists.

Required structure:

    LocalClosure_F(x)
    ActualUse_U(F,x)
    UseExceedsScope(F,x,U)
    exists d such that CriticalDep_Ω(d,x,U) and Excluded_F(d)
    but not Err_Ω(x,F,U)

Counterexample Class B:

A real structural error exists, but there is no excluded critical dependency.

Required structure:

    Err_Ω(x,F,U)
    but no d exists such that CriticalDep_Ω(d,x,U) and Excluded_F(d)

Counterexample Class C:

A finite framework treats a proper real object without producing local closure.

Required structure:

    Finite(F)
    Treats(F,x)
    Manifest_Ω(x)
    Proper_Ω(x)
    but not LocalClosure_F(x)

Counterexample Class D:

A proper manifested object is fully closed in Ω.

Required structure:

    Manifest_Ω(x)
    Proper_Ω(x)
    Closed_Ω(x)

Counterexample Class E:

An existing framework captures the same structure with equal or greater operational clarity.

Required structure:

    another framework defines:
    x
    F
    U
    valid scope
    excluded critical dependencies
    use beyond scope
    negative controls
    counterexample conditions

and does so with equal or greater compactness and transferability.

## 14. Negative Controls

The following should not be classified as structural errors by default.

Arithmetic slip:

A wrong calculation due only to local arithmetic mistake.

Missing condition:

No actual use U is identified.

Harmless abstraction:

F excludes d, but d is not critical for U.

Scoped model:

F is used explicitly within its declared scope.

Draft use:

An AI answer is used as a draft rather than as final authority.

Toy game:

A game is used only for abstract analysis, not for real-world decision.

These negative controls are essential.

Without them, the framework would overclassify.

## 15. Nash-Style Review Test

A mathematically hostile reviewer may ask:

What is the object?

Answer:

    x, F, U, d, Ω

What is the definition?

Answer:

    Err_Ω(x,F,U) iff local closure, use beyond scope, and excluded critical dependency are jointly present.

What is the theorem?

Answer:

    finite treatment gives local closure; proper manifested objects remain open; therefore theory-reality asymmetry follows.

What is not an error?

Answer:

    incompleteness alone is not error; exclusion matters only when critical for U.

How can it be broken?

Answer:

    produce a counterexample from Class A, B, C, D, or E.

## 16. Non-Claims

This document does not claim:

The framework is externally validated.

The framework replaces domain expertise.

The framework automatically discovers all dependencies.

The framework proves empirical facts without evidence.

The framework eliminates the need for case-by-case analysis.

The precise claim is narrower:

A finite framework becomes structurally invalid for an actual use when that use exceeds the framework's valid scope while requiring at least one dependency that the framework excludes.

## 17. Compact Summary

Closed in theory.

Open in reality.

Valid only by use.

Error only by excluded critical dependency.

Counterexample-ready by design.
