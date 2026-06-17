# Audits

This directory contains compiled example audits applying the Law of Totality.

The goal is not to repeat the theory.

The goal is to show how the audit template works on concrete objects.

Each audit should identify:

1. object;
2. framework;
3. actual use;
4. valid scope;
5. local closure;
6. D0-D5 dependency classification;
7. excluded D4/D5 dependency;
8. false sufficiency;
9. falsification condition;
10. final verdict.

A valid audit may reach one of three verdicts:

- structural error;
- no structural error;
- insufficient evidence.

The main example file is:

- [`EXAMPLE_AUDITS.md`](EXAMPLE_AUDITS.md)
