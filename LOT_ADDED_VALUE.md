# LOT Added Value — v0.7.0

## One Sentence

The Law of Totality adds a portable structural-error predicate for detecting when local correctness becomes invalid use.

## What It Does Not Add

It does not add the idea that:

    models have limits;
    context matters;
    systems have dependencies;
    maps are not territories;
    formal systems have limits;
    decisions need validation;
    AI systems require governance.

These are already known.

## What It Adds

It adds a compact, reusable relation:

    x = object being treated
    F = framework treating it
    U = actual use of that treatment
    ValidScope(F,x) = conditions where the treatment remains valid
    CriticalDepΩ(d,x,U) = dependency required by the actual use
    ExcludedF(d) = dependency excluded by the framework

Error appears when:

    F is treated as sufficient for U
    while U requires d
    and F excludes d.

## Why This Matters

Many failures are not caused by local falsehood.

They are caused by local truth used as global sufficiency.

Examples:

    a correct metric used as total value;
    a correct model used outside distribution;
    a correct legal rule used as justice;
    a correct grade used as identity;
    a correct AI answer used as professional advice;
    a correct map used for the wrong terrain;
    a correct formal proof used as whole-system safety.

## The Key Correction

The law changes the question from:

    Is F correct?

to:

    Is F valid for U, given the dependencies required by U?

This is the decisive shift.

## Strategic Position

LOT should be introduced as:

    a structural validity audit layer

not as:

    a replacement for existing disciplines.

## Operational Use

For any finite treatment:

    identify x;
    identify F;
    identify U;
    declare ValidScope(F,x);
    list dependencies required by U;
    identify dependencies excluded by F;
    decide whether any excluded dependency is critical for U.

## Output

The output is not total truth.

The output is a structural validity judgment:

    valid inside scope;
    invalid for actual use;
    under-specified;
    requires domain review;
    negative control: no structural error.

## Core Boundary

LOT does not know all dependencies automatically.

It forces the dependency question into the open.

This is not weakness.

This is the anti-hallucination property of the framework.
