# Extraction Guidance — recognising ArchiMate in source material

This reference is the *application* layer over the ArchiMate metamodel: how to recognise each element in real, often messy source material, how to handle content that does not map cleanly, and the mistakes to avoid. For what each element and relationship *is*, see the metamodel foundation:

📄 `../../architect-foundation-archimate/references/metamodel.md`

Read that for definitions; read this for how to spot them.

---

## Extraction signals by element

Phrases and patterns in source material that suggest a given element type. Signals are cues, not proof — classify on meaning, and carry the confidence tier the evidence supports.

**Motivation**

| Element | Signals in source material |
|---|---|
| Driver | "pressure to…", "the market is…", "regulatory requirement…", "the problem is…" |
| Assessment | "we assessed…", "the risk is…", "this is an opportunity to…" |
| Goal | "we want to…", "our aim is…", "the objective is…" |
| Outcome | "this will result in…", "the expected benefit is…" |
| Principle | "we always…", "it is our principle that…", "by policy…" |
| Requirement | "must…", "shall…", "it is required that…" |
| Constraint | "cannot…", "limited to…", "within the constraint of…" |
| Value | "value proposition", "this benefits X by…" |
| Meaning | "by X we mean…", glossary terms, defined concepts |
| Stakeholder | named parties with a stake in the outcome |

**Strategy**

| Element | Signals in source material |
|---|---|
| Resource | "our assets…", "we have…", "resources include…" |
| Capability | "we are able to…", "our capability to…", "competency in…" |
| Value Stream | end-to-end "from X to Y we…" value descriptions |
| Course of Action | "our strategy is to…", "we will approach this by…" |

**Business**

| Element | Signals in source material |
|---|---|
| Business Actor | named organisations, departments, companies |
| Business Role | "the [role] is responsible for…", job titles, function names |
| Business Collaboration | described joint activities, shared responsibilities |
| Business Process | step-by-step descriptions, workflows, named processes |
| Business Function | departmental functions, capability areas |
| Business Interaction | collaboration points, handoffs |
| Business Event | triggers, events that start or end processes |
| Business Service | services offered to others, business-facing interfaces |
| Business Object | named business entities and information concepts |
| Contract | agreements, SLAs, terms |
| Representation | documents, forms, reports used in the business |

**Application / Information Systems**

| Element | Signals in source material |
|---|---|
| Application Component | named systems, applications, tools, platforms |
| Application Collaboration | integration descriptions, system-to-system interactions |
| Application Function | features or functions of a system |
| Application Interaction | described integrations, API interactions |
| Application Process | automated workflows, batch processes |
| Application Event | system events, triggers, notifications |
| Application Service | APIs, integration endpoints, system services |
| Data Object | named data entities, datasets, databases, files |

**Technology**

| Element | Signals in source material |
|---|---|
| Node | servers, VMs, containers, cloud instances |
| Device | physical servers, network devices, end-user hardware |
| System Software | operating systems, middleware, databases, container platforms |
| Technology Service | infrastructure, platform, or cloud services |
| Technology Function | infrastructure capabilities, platform functions |
| Artifact | files, executables, configuration items, packages |
| Communication Network | networks, subnets, VPCs |
| Path | network connections, communication links |

**Implementation & Migration**

| Element | Signals in source material |
|---|---|
| Work Package | projects, workstreams, change initiatives |
| Deliverable | named deliverables, outputs, products of change |
| Implementation Event | go-live dates, milestones, decision gates |
| Plateau | named phases or versions, "as-is", "to-be", interim states |
| Gap | explicitly described differences between current and target |

---

## Mapping ambiguous content

| If the material says… | Consider… |
|---|---|
| "the system", without specifics | Application Component (Assumed) — note the ambiguity |
| a described process with no owner | Business Process (Inferred) — the owner is a gap |
| a named data entity, no layer context | Business Object if conceptual; Data Object if technical |
| a strategic intent, no specific element | Goal or Course of Action, depending on specificity |
| an integration between two systems | Application Interaction or Association |
| a team, department, or organisation | Business Actor |
| a person in a role | Business Role (optionally with a Business Actor assigned) |
| "a platform" | Application Component, Node, or System Software — decide from context |
| "a service" | business, application, or technology service — decide from context |

---

## Temporal perspective tagging

When material describes more than one state, tag each element:

- `current` — the existing state
- `target` — the desired future state
- `transition` — an intermediate state in a migration
- `unclear` — temporal perspective not determinable

---

## Common pitfalls

- **Classifying behaviour as structure.** Ask whether the thing *does* something (behaviour) or *is* something (structure).
- **Missing the motivation layer.** Even operational documents usually imply goals, drivers, and requirements — look for them.
- **Flattening hierarchies.** Composition and Aggregation are often implied rather than stated; capture them as Inferred rather than dropping them.
- **Ignoring Implementation & Migration.** If the material discusses change, projects, or transitions, those are architectural elements too.
- **Treating all "data" as Data Objects.** Conceptual information entities belong at the Business layer as Business Objects.
- **Forcing a fit.** When something does not map cleanly, offer the closest type with a caveat and record the mapping challenge — honest approximation over confident misclassification.
