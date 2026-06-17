# Example Audits

## Purpose

This file shows how the Law of Totality can be applied through the reusable audit template.

The examples are intentionally generic.

They are not presented as historical claims.

They are structural audit demonstrations.

Each example tests whether the following four conditions are present:

1. local closure;
2. use beyond valid scope;
3. excluded D4/D5 dependency;
4. false sufficiency.

If all four are present, the verdict is:

> structural error.

If one is absent, the verdict is:

> no structural error.

If the required information cannot be established, the verdict is:

> insufficient evidence.

---

# Audit 1 — AI answer used as final authority

## Object audited

| Field | Answer |
|---|---|
| Name of object | AI answer used as final authority |
| Type of object | AI answer |
| Domain | legal / medical / financial / technical decision support |
| Auditor | example audit |
| Date | not applicable |
| Version or source | generic case |

---

## 1. Object definition

| Question | Answer |
|---|---|
| What is the object? | A fluent AI-generated answer to a domain-specific question. |
| What claim, output, decision or action does it produce? | It gives a confident response that appears complete and usable. |
| What does it appear to close, decide, explain, predict or authorize? | It appears to close the user's uncertainty and provide a final answer. |

---

## 2. Framework identification

| Question | Answer |
|---|---|
| What framework is being used? | A language model response based on available prompt context, training data and possible limited retrieval. |
| What assumptions does it rely on? | That the available context is sufficient to answer. |
| What does it include? | Linguistic coherence, general knowledge, pattern completion, possibly retrieved context. |
| What does it exclude? | Missing documents, current law, full user-specific context, jurisdiction, source verification, real-time facts. |
| Is the framework formal, empirical, procedural, statistical, linguistic, institutional or mixed? | Mixed: linguistic, statistical and evidential if retrieval is present. |

---

## 3. Actual use

| Question | Answer |
|---|---|
| What is the actual use? | The user relies on the answer for a real decision. |
| Who or what relies on the output? | A user, organization or operator. |
| Is the use theoretical, practical, operational, legal, financial, medical, safety-critical or public? | Potentially legal, financial, medical, technical or operational. |
| What happens if the output is wrong or insufficient? | The user may act on unsupported, outdated or contextually invalid information. |

---

## 4. Valid scope

| Question | Answer |
|---|---|
| What is the declared valid scope? | Draft, explanation, preliminary reasoning or bounded answer from available evidence. |
| What are the boundary conditions? | The answer is valid only relative to available context and declared uncertainty. |
| What assumptions must remain true? | The relevant facts must be included; the answer must not be treated as final authority without verification. |
| What cases are outside scope? | Legal, medical, financial or safety-critical final decisions without source verification and domain review. |
| Is the actual use inside or outside this scope? | outside |

---

## 5. Local closure check

| Question | Answer |
|---|---|
| Does the framework present a closed output? | yes |
| Is the output presented as complete, sufficient, final or decision-ready? | yes, in the problematic version |
| Is uncertainty declared? | no |
| Are missing dependencies declared? | no |
| Closure verdict | local closure |

---

## 6. Dependency identification

| Candidate dependency | Type | Why it may matter |
|---|---|---|
| Current facts | temporal / evidential | The answer may be outdated. |
| Full source document | evidential | The answer may miss decisive text. |
| Jurisdiction | contextual / authority | Legal validity can change by jurisdiction. |
| User-specific constraints | contextual | The same answer may be invalid for a specific case. |
| Domain expert review | authority / evidential | High-stakes use may require professional validation. |

---

## 7. Dependency severity classification

| Dependency | Level | Reason for level | What would lower this level? |
|---|---|---|---|
| Current facts | D4 | If the answer concerns current law, price, medical guidance or technical status, outdated information can invalidate use. | The question is historical or explicitly non-current. |
| Full source document | D4 | If the answer interprets a document, missing document context can invalidate the answer. | The answer is only generic and not document-specific. |
| Jurisdiction | D4 | Legal validity may depend on jurisdiction. | The answer is not legal or jurisdiction is irrelevant. |
| User-specific constraints | D4 | Medical, financial or operational advice may change by user context. | The answer is purely educational. |
| Professional authorization | D5 in regulated/high-stakes cases | Some actions must not proceed without qualified authority. | The use is not regulated, not high-stakes or clearly provisional. |

---

## 8. Excluded D4/D5 dependency check

| Question | Answer |
|---|---|
| Is there a D4 critical dependency? | yes |
| Is there a D5 blocking dependency? | possible in regulated or safety-critical use |
| Which D4/D5 dependency is excluded? | Current facts, full context, jurisdiction or user-specific conditions. |
| Is it included by the framework? | no |
| Is it preserved by the framework? | no |
| Is it declared as missing? | no |
| Is it controlled by another mechanism? | no |

---

## 9. Use-beyond-scope check

| Question | Answer |
|---|---|
| Is the actual use beyond the valid scope? | yes |
| Which scope boundary is exceeded? | The answer is used as final authority rather than provisional support. |
| Is the scope violation declared? | no |
| Is the output still being used as sufficient? | yes |

---

## 10. False sufficiency check

| Question | Answer |
|---|---|
| Is the framework treated as sufficient? | yes |
| Is the missing dependency D4 or D5? | yes |
| Is the missing dependency required by the actual use? | yes |
| Is the missing dependency undeclared or uncontrolled? | yes |
| False sufficiency present? | yes |

---

## 11. Structural error verdict

| Required condition | Present? | Evidence |
|---|---|---|
| Local closure | yes | The answer is presented as complete. |
| Use beyond valid scope | yes | It is used as final authority. |
| Excluded D4/D5 dependency | yes | Critical context/source/currentness is missing. |
| False sufficiency | yes | The answer is treated as enough. |

| Verdict | Answer |
|---|---|
| Final verdict | structural error |
| Reason | A locally coherent AI answer is used as sufficient beyond its valid scope while excluding dependencies required by the actual decision. |

---

## 12. Explanation

The AI answer may be linguistically coherent and locally useful.

It becomes structurally invalid when the user treats it as final authority while D4 or D5 dependencies required by the actual use are missing.

The error is not mere incompleteness.

The error is false sufficiency.

---

## 13. Falsification check

| Question | Answer |
|---|---|
| What would prove that the dependency is not D4/D5? | Showing that the use is purely educational and does not depend on current facts, jurisdiction or user-specific context. |
| What would prove that the actual use is inside valid scope? | Showing that the answer is used only as a draft or hypothesis. |
| What would prove that the framework includes or controls the dependency? | Showing verified retrieval, complete document access, current sources and domain review. |
| What would prove that the framework was not treated as sufficient? | Showing that the answer explicitly declares limits and requires verification. |
| What evidence is missing from this audit? | The concrete prompt, sources, domain and actual decision. |

---

## 14. Correction path

| Correction type | Required action |
|---|---|
| Limit scope | Mark the output as provisional. |
| Declare missing dependency | State missing current facts, sources, jurisdiction or user-specific constraints. |
| Include dependency | Retrieve and cite the required source/document/context. |
| Add evidence | Add current evidence or domain references. |
| Add domain expert review | Required for high-stakes cases. |
| Convert final answer into provisional answer | Yes. |
| Stop use until blocking dependency is resolved | Yes, if D5 applies. |

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | AI answer |
| Framework | Language model response |
| Actual use | Final authority for real decision |
| Valid scope | Draft/provisional support |
| Main excluded dependency | Source/current/context-specific dependency |
| Dependency level | D4 or D5 |
| Local closure | yes |
| Use beyond scope | yes |
| False sufficiency | yes |
| Final verdict | structural error |
| One-sentence conclusion | The answer is structurally invalid when used as final authority beyond the dependencies it preserves. |

---

# Audit 2 — Complex project plan treated as execution-ready

## Object audited

| Field | Answer |
|---|---|
| Name of object | Complex project plan treated as execution-ready |
| Type of object | project / protocol |
| Domain | complex project execution |
| Auditor | example audit |
| Date | not applicable |
| Version or source | generic case |

---

## 1. Object definition

| Question | Answer |
|---|---|
| What is the object? | A project plan containing an idea, roles, dates and general goals. |
| What claim, output, decision or action does it produce? | It claims or implies that the project is ready for real execution. |
| What does it appear to close, decide, explain, predict or authorize? | It appears to close the transition from concept to execution. |

---

## 2. Framework identification

| Question | Answer |
|---|---|
| What framework is being used? | An initial organizational plan or role map. |
| What assumptions does it rely on? | That named roles, intentions and dates are enough to make the project operational. |
| What does it include? | Goal, rough team structure, basic timeline, preliminary responsibilities. |
| What does it exclude? | Confirmations, safety chain, authority, logistics, budget, backup roles, failure modes, communication protocol. |
| Is the framework formal, empirical, procedural, statistical, linguistic, institutional or mixed? | Procedural and organizational. |

---

## 3. Actual use

| Question | Answer |
|---|---|
| What is the actual use? | Real-world execution involving people, timing, risk, logistics and external commitments. |
| Who or what relies on the output? | Team members, organizers, partners, public institutions, participants. |
| Is the use theoretical, practical, operational, legal, financial, medical, safety-critical or public? | Practical, operational, public and potentially safety-critical. |
| What happens if the output is wrong or insufficient? | Execution gaps, safety failures, role confusion, missed permissions, public failure or harm. |

---

## 4. Valid scope

| Question | Answer |
|---|---|
| What is the declared valid scope? | Early planning, concept definition and preliminary coordination. |
| What are the boundary conditions? | Roles are not yet confirmed; dependencies are not yet controlled. |
| What assumptions must remain true? | The plan is treated as provisional. |
| What cases are outside scope? | Real execution, public launch, safety-critical operation or binding commitment. |
| Is the actual use inside or outside this scope? | outside |

---

## 5. Local closure check

| Question | Answer |
|---|---|
| Does the framework present a closed output? | yes, if treated as ready |
| Is the output presented as complete, sufficient, final or decision-ready? | yes |
| Is uncertainty declared? | no or insufficiently |
| Are missing dependencies declared? | no or insufficiently |
| Closure verdict | local closure |

---

## 6. Dependency identification

| Candidate dependency | Type | Why it may matter |
|---|---|---|
| Role confirmation | operational / authority | Named people may not have accepted responsibility. |
| Safety protocol | safety | Execution may expose people to risk. |
| Communication chain | operational / human | Failure communication must be controlled. |
| Backup roles | operational | Absence or failure of one role can break execution. |
| Budget | resource | Execution may be impossible without funds. |
| Legal permissions | authority | Public or regulated activities may require authorization. |
| Weather / timing | temporal / safety | Timing may affect safety or feasibility. |

---

## 7. Dependency severity classification

| Dependency | Level | Reason for level | What would lower this level? |
|---|---|---|---|
| Role confirmation | D4 | Execution depends on real responsibility, not names alone. | Written confirmation and assignment exist. |
| Safety protocol | D5 in dangerous operations | Execution must not proceed if safety is uncontrolled. | The activity is non-risky or safety protocol exists. |
| Communication chain | D4 | Coordination failures can invalidate execution. | Chain is assigned and tested. |
| Backup roles | D3/D4 | May become critical if role absence blocks execution. | Redundancy is unnecessary or already assigned. |
| Budget | D4 | Lack of resources can make execution impossible. | Project does not require resources or funds are secured. |
| Legal permissions | D5 if legally required | Action cannot proceed without authorization. | No authorization is needed or permission is obtained. |
| Weather / timing | D4/D5 in exposed operations | Conditions can invalidate or stop execution. | The operation is not weather-sensitive. |

---

## 8. Excluded D4/D5 dependency check

| Question | Answer |
|---|---|
| Is there a D4 critical dependency? | yes |
| Is there a D5 blocking dependency? | possible |
| Which D4/D5 dependency is excluded? | Safety protocol, confirmations, authority, logistics or communication chain. |
| Is it included by the framework? | no |
| Is it preserved by the framework? | no |
| Is it declared as missing? | unclear or no |
| Is it controlled by another mechanism? | no |

---

## 9. Use-beyond-scope check

| Question | Answer |
|---|---|
| Is the actual use beyond the valid scope? | yes |
| Which scope boundary is exceeded? | Concept-stage planning is treated as execution readiness. |
| Is the scope violation declared? | no |
| Is the output still being used as sufficient? | yes |

---

## 10. False sufficiency check

| Question | Answer |
|---|---|
| Is the framework treated as sufficient? | yes |
| Is the missing dependency D4 or D5? | yes |
| Is the missing dependency required by the actual use? | yes |
| Is the missing dependency undeclared or uncontrolled? | yes |
| False sufficiency present? | yes |

---

## 11. Structural error verdict

| Required condition | Present? | Evidence |
|---|---|---|
| Local closure | yes | The plan is treated as ready. |
| Use beyond valid scope | yes | It moves from concept to execution. |
| Excluded D4/D5 dependency | yes | Safety, authority, confirmation or logistics are missing. |
| False sufficiency | yes | The plan is treated as enough. |

| Verdict | Answer |
|---|---|
| Final verdict | structural error |
| Reason | The plan is locally useful but structurally invalid if treated as execution-ready while excluding dependencies required for execution. |

---

## 12. Explanation

The project is not wrong because it is incomplete.

An early plan is supposed to be incomplete.

The structural error begins when the early plan is used as if it were execution-ready while D4/D5 operational dependencies remain uncontrolled.

---

## 13. Falsification check

| Question | Answer |
|---|---|
| What would prove that the dependency is not D4/D5? | Showing the actual use is only internal planning, not execution. |
| What would prove that the actual use is inside valid scope? | Showing that no real commitment, public action or safety-critical execution depends on it. |
| What would prove that the framework includes or controls the dependency? | Written confirmations, assigned decision authority, safety plan, logistics and backups. |
| What would prove that the framework was not treated as sufficient? | Clear declaration that the plan is provisional and not execution-ready. |
| What evidence is missing from this audit? | Actual project documents, confirmations, safety protocol, permissions and timeline. |

---

## 14. Correction path

| Correction type | Required action |
|---|---|
| Limit scope | Mark the plan as concept-stage only. |
| Declare missing dependency | List missing confirmations, permissions, safety and logistics. |
| Include dependency | Assign owners and deadlines for every D4/D5 dependency. |
| Add evidence | Add written confirmations and documents. |
| Add domain expert review | Required if safety, law, medical or logistics risks exist. |
| Convert final answer into provisional answer | Yes. |
| Stop use until blocking dependency is resolved | Yes, if D5 applies. |

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | Complex project plan |
| Framework | Initial organizational plan |
| Actual use | Real execution |
| Valid scope | Early planning |
| Main excluded dependency | Safety / authority / logistics / confirmation |
| Dependency level | D4 or D5 |
| Local closure | yes |
| Use beyond scope | yes |
| False sufficiency | yes |
| Final verdict | structural error |
| One-sentence conclusion | The plan becomes structurally invalid when concept-stage closure is treated as execution readiness. |

---

# Audit 3 — Formal theory presented as real-world sufficient

## Object audited

| Field | Answer |
|---|---|
| Name of object | Formal theory presented as real-world sufficient |
| Type of object | theory / model |
| Domain | theoretical-to-operational transition |
| Auditor | example audit |
| Date | not applicable |
| Version or source | generic case |

---

## 1. Object definition

| Question | Answer |
|---|---|
| What is the object? | A coherent formal theory or model. |
| What claim, output, decision or action does it produce? | It explains, predicts or structures an object inside its formal framework. |
| What does it appear to close, decide, explain, predict or authorize? | It appears to provide enough structure to justify real-world use. |

---

## 2. Framework identification

| Question | Answer |
|---|---|
| What framework is being used? | A formal or conceptual system with definitions, assumptions and internal rules. |
| What assumptions does it rely on? | That internal coherence is enough for the intended use. |
| What does it include? | Definitions, internal relations, theoretical claims, perhaps formal derivations. |
| What does it exclude? | Empirical validation, operational constraints, measurement conditions, domain-specific boundary cases, implementation limits. |
| Is the framework formal, empirical, procedural, statistical, linguistic, institutional or mixed? | Formal/conceptual, possibly mixed. |

---

## 3. Actual use

| Question | Answer |
|---|---|
| What is the actual use? | The theory is used to guide real-world action, decision, prediction, system design or public claim. |
| Who or what relies on the output? | Researchers, developers, operators, decision-makers or users. |
| Is the use theoretical, practical, operational, legal, financial, medical, safety-critical or public? | It moves from theoretical to practical or public. |
| What happens if the output is wrong or insufficient? | The theory may be overclaimed, misapplied or treated as validated when it is not. |

---

## 4. Valid scope

| Question | Answer |
|---|---|
| What is the declared valid scope? | Internal theoretical coherence. |
| What are the boundary conditions? | Definitions and assumptions of the theory. |
| What assumptions must remain true? | The theory is used only as a theoretical framework unless operational validation exists. |
| What cases are outside scope? | Real-world sufficiency, deployment, scientific validation or practical authority without evidence. |
| Is the actual use inside or outside this scope? | outside, if treated as real-world sufficient |

---

## 5. Local closure check

| Question | Answer |
|---|---|
| Does the framework present a closed output? | yes |
| Is the output presented as complete, sufficient, final or decision-ready? | yes, in the overclaimed version |
| Is uncertainty declared? | no or insufficiently |
| Are missing dependencies declared? | no or insufficiently |
| Closure verdict | local closure |

---

## 6. Dependency identification

| Candidate dependency | Type | Why it may matter |
|---|---|---|
| Empirical validation | evidential | Real-world validity requires evidence beyond internal coherence. |
| Measurement conditions | empirical / contextual | Theory may require measurable variables. |
| Operational constraints | operational | Implementation can fail despite theory. |
| Domain boundary cases | formal / contextual | Theory may not hold outside defined assumptions. |
| Comparison with existing frameworks | evidential / contextual | Novelty and usefulness require external comparison. |
| Falsification criteria | logical / evidential | A theory must define what would weaken it. |

---

## 7. Dependency severity classification

| Dependency | Level | Reason for level | What would lower this level? |
|---|---|---|---|
| Empirical validation | D4 if real-world claims are made | Operational reality requires evidence. | The claim remains purely theoretical. |
| Measurement conditions | D3/D4 | Without measurable variables, application may be impossible. | The theory is not presented as measurable. |
| Operational constraints | D4 | Real use depends on implementation feasibility. | No operational use is claimed. |
| Domain boundary cases | D4 | Boundary misuse can invalidate application. | Boundaries are declared and respected. |
| Comparison with existing frameworks | D3/D4 | Needed for novelty/usefulness claims. | No novelty or superiority claim is made. |
| Falsification criteria | D4 for scientific claims | Without limits, theory may be unfalsifiable. | The claim is only interpretive or exploratory. |

---

## 8. Excluded D4/D5 dependency check

| Question | Answer |
|---|---|
| Is there a D4 critical dependency? | yes, if real-world sufficiency is claimed |
| Is there a D5 blocking dependency? | possible in safety-critical applications |
| Which D4/D5 dependency is excluded? | Empirical validation, operational constraints, falsification or domain boundary control. |
| Is it included by the framework? | no or insufficiently |
| Is it preserved by the framework? | no or insufficiently |
| Is it declared as missing? | unclear or no |
| Is it controlled by another mechanism? | no |

---

## 9. Use-beyond-scope check

| Question | Answer |
|---|---|
| Is the actual use beyond the valid scope? | yes |
| Which scope boundary is exceeded? | Internal coherence is treated as real-world validity. |
| Is the scope violation declared? | no |
| Is the output still being used as sufficient? | yes |

---

## 10. False sufficiency check

| Question | Answer |
|---|---|
| Is the framework treated as sufficient? | yes |
| Is the missing dependency D4 or D5? | yes |
| Is the missing dependency required by the actual use? | yes |
| Is the missing dependency undeclared or uncontrolled? | yes |
| False sufficiency present? | yes |

---

## 11. Structural error verdict

| Required condition | Present? | Evidence |
|---|---|---|
| Local closure | yes | The theory presents internal closure. |
| Use beyond valid scope | yes | It is treated as real-world sufficient. |
| Excluded D4/D5 dependency | yes | Evidence, implementation, boundaries or falsification are missing. |
| False sufficiency | yes | Internal coherence is treated as enough. |

| Verdict | Answer |
|---|---|
| Final verdict | structural error |
| Reason | The theory is locally coherent but structurally invalid as real-world sufficient if it excludes dependencies required for real use. |

---

## 12. Explanation

The theory is not wrong because it is incomplete.

It may be internally valid and valuable.

The structural error appears only when internal theoretical closure is treated as sufficient for real-world validity without the dependencies required by that transition.

This is exactly the theory-to-reality bridge.

---

## 13. Falsification check

| Question | Answer |
|---|---|
| What would prove that the dependency is not D4/D5? | Showing the theory makes no operational, empirical, scientific or real-world sufficiency claim. |
| What would prove that the actual use is inside valid scope? | Showing the theory is used only internally or exploratorily. |
| What would prove that the framework includes or controls the dependency? | Evidence, tests, comparisons, boundary declarations and falsification criteria are present. |
| What would prove that the framework was not treated as sufficient? | The theory explicitly declares itself provisional and non-operational. |
| What evidence is missing from this audit? | The actual theory text, stated claims, validation evidence and intended use. |

---

## 14. Correction path

| Correction type | Required action |
|---|---|
| Limit scope | State that the theory is internally coherent but not yet operationally validated. |
| Declare missing dependency | Identify missing evidence, tests, boundaries or implementation constraints. |
| Include dependency | Add validation cases, negative cases, comparison and falsification conditions. |
| Add evidence | Provide case studies, experiments, audits or formal proofs. |
| Add domain expert review | Required if the theory enters a technical domain. |
| Convert final answer into provisional answer | Yes, until validation is added. |
| Stop use until blocking dependency is resolved | Yes, if used in safety-critical contexts. |

---

## 15. Theory-to-reality bridge

| Field | Answer |
|---|---|
| Internal theoretical claim | The theory is coherent inside its framework. |
| Declared scope | Internal theoretical validity. |
| Intended real use | Real-world explanation, prediction, decision or system design. |
| Dependencies required by that use | Evidence, boundary conditions, implementation constraints, comparison, falsification. |
| Dependencies already included | Depends on the theory. |
| Dependencies missing | Any required validation not yet supplied. |
| Can the theory be used as sufficient now? | no, unless those dependencies are included. |
| What must be added before real use? | Operational validation, declared scope, critical dependency control and falsification criteria. |

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | Formal theory/model |
| Framework | Internal theoretical system |
| Actual use | Real-world sufficiency |
| Valid scope | Internal coherence |
| Main excluded dependency | Evidence / operational validation / boundary control |
| Dependency level | D4, sometimes D5 |
| Local closure | yes |
| Use beyond scope | yes |
| False sufficiency | yes |
| Final verdict | structural error |
| One-sentence conclusion | A theory becomes structurally invalid when its internal closure is used as real-world sufficiency without the dependencies required by real use. |

---

# Negative audit — Provisional AI answer used correctly

## Purpose

This negative audit shows that the Law of Totality must not diagnose structural error when a partial framework is used honestly inside its valid scope.

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | Provisional AI answer |
| Framework | Language model response |
| Actual use | Draft, brainstorming or preliminary explanation |
| Valid scope | Provisional reasoning from available context |
| Main excluded dependency | Current source or complete context may be missing |
| Dependency level | D2/D3 unless final authority is claimed |
| Local closure | no |
| Use beyond scope | no |
| False sufficiency | no |
| Final verdict | no structural error |
| One-sentence conclusion | The answer is incomplete, but it is not structurally erroneous because it is not treated as sufficient beyond its scope. |

---

# Negative audit — Formal result used formally

## Purpose

This negative audit shows that local closure is allowed when it remains inside its declared formal system.

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | Formal mathematical result |
| Framework | Declared formal system |
| Actual use | Internal formal derivation |
| Valid scope | The formal system itself |
| Main excluded dependency | Real-world interpretation excluded |
| Dependency level | D0/D1 relative to internal formal use |
| Local closure | yes |
| Use beyond scope | no |
| False sufficiency | no |
| Final verdict | no structural error |
| One-sentence conclusion | The result is locally closed, but not structurally erroneous because it is not used beyond its declared scope. |

---

# Negative audit — Insufficient evidence

## Purpose

This audit shows that the correct verdict is sometimes neither yes nor no.

---

## Final audit summary

| Field | Answer |
|---|---|
| Object | Unspecified model failure |
| Framework | Unknown |
| Actual use | Unknown |
| Valid scope | Unknown |
| Main excluded dependency | Alleged missing factor |
| Dependency level | unclear |
| Local closure | unclear |
| Use beyond scope | unclear |
| False sufficiency | unclear |
| Final verdict | insufficient evidence |
| One-sentence conclusion | The Law of Totality cannot diagnose structural error until actual use, valid scope, dependency level and false sufficiency are established. |

---

# Final note

These example audits demonstrate the operational boundary of the Law of Totality.

It should diagnose structural error only when the four required conditions are established.

It should reject the diagnosis when legitimate partiality is used inside valid scope.

It should return insufficient evidence when the audit cannot establish the required conditions.
