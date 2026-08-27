# ArchiMate Metamodel Reference

The element types, relationships, and layer structure of ArchiMate 3.x, as used across Archai. This is a practitioner-oriented working reference, not the authoritative specification — for that, refer to The Open Group ArchiMate 3.x documentation. It is intentionally selective, covering the elements most commonly encountered in architecture work; less common elements (for example Junction, Grouping, Location) are valid and may be used where appropriate.

This reference is *usage-neutral*: it defines what each element and relationship is, not how any one skill should recognise, produce, or render it. Skills that consume it add their own application guidance — how to spot an element in source material, how to serialise it to a file format — in their own bodies.

---

## Layers and aspects

ArchiMate organises architectural elements across **layers** (levels of the enterprise) and **aspects** (what kind of element it is).

**Layers:**

- **Motivation** — the drivers, goals, principles, and requirements behind architectural decisions (sits above the core layers).
- **Strategy** — strategic direction, capabilities, and value creation.
- **Business** — processes, functions, roles, services, and organisational structure.
- **Application / Information Systems** — software components and the information they process.
- **Technology** — infrastructure, platforms, and technical components.
- **Implementation & Migration** — change, programmes, transitions, and plateaus.

**Aspects** (within each core layer):

- **Active structure** — entities that perform behaviour (actors, roles, components, nodes).
- **Behaviour** — what active structures do (processes, functions, services, events).
- **Passive structure** — objects that behaviour acts upon (business objects, data objects, artifacts).

The information / data aspect sits primarily in the Application layer as **Data Objects**, but conceptual-level information entities appear at the Business layer as **Business Objects**.

---

## Motivation layer

Captures the *why* — the drivers, intentions, and rationale behind architectural decisions.

| Element | Description |
|---|---|
| **Driver** | An external or internal condition that motivates change. |
| **Assessment** | An evaluation of a driver — a SWOT result, a risk, an opportunity. |
| **Goal** | A high-level statement of intent or direction. |
| **Outcome** | An end result expected from achieving goals. |
| **Principle** | A normative statement that guides decisions. |
| **Requirement** | A need that must be satisfied by the architecture. |
| **Constraint** | A restriction on the way the architecture may be realised. |
| **Value** | The worth of an outcome to a stakeholder. |
| **Meaning** | A shared understanding or definition of a concept. |
| **Stakeholder** | A role with an interest in the architecture and its outcomes. |

---

## Strategy layer

Captures the *what* at a high level — strategic direction, capabilities, and value creation.

| Element | Description |
|---|---|
| **Resource** | An asset — tangible or intangible — available for strategic use. |
| **Capability** | An ability an organisation possesses to achieve an outcome. |
| **Value Stream** | A sequence of value-adding activities delivering an overall result to a stakeholder. |
| **Course of Action** | A strategic approach or plan for achieving goals. |

---

## Business layer

Captures the *how* at the organisational level — processes, functions, roles, services, and the information used in business operations.

**Active structure:**

| Element | Description |
|---|---|
| **Business Actor** | An organisational entity — a person, department, or organisation. |
| **Business Role** | A responsibility, played by an actor, for performing specific behaviour. |
| **Business Collaboration** | An aggregate of two or more roles working together. |

**Behaviour:**

| Element | Description |
|---|---|
| **Business Process** | A sequence of behaviours producing a defined result. |
| **Business Function** | A grouping of behaviour by required competency or resource. |
| **Business Interaction** | A unit of collective behaviour performed by a collaboration. |
| **Business Event** | A state change that triggers or is produced by behaviour. |
| **Business Service** | An explicitly defined, externally visible result of behaviour. |

**Passive structure:**

| Element | Description |
|---|---|
| **Business Object** | A concept relevant to the business, used within its behaviour. |
| **Contract** | A formal or informal specification of an agreement. |
| **Representation** | A perceptible form of information — a document, form, or report. |

---

## Application / Information Systems layer

Captures the software and information systems that support business operations.

**Active structure:**

| Element | Description |
|---|---|
| **Application Component** | A modular, deployable unit of software. |
| **Application Collaboration** | An aggregate of two or more components that interact. |

**Behaviour:**

| Element | Description |
|---|---|
| **Application Function** | Automated behaviour performed by a component. |
| **Application Interaction** | Collective behaviour of an application collaboration. |
| **Application Process** | A sequence of automated behaviours. |
| **Application Event** | A state change in an application context. |
| **Application Service** | An explicitly defined, externally visible automated behaviour. |

**Passive structure:**

| Element | Description |
|---|---|
| **Data Object** | A structured unit of data, produced or used by application behaviour. |

---

## Technology layer

Captures the infrastructure that hosts and supports applications.

**Active structure:**

| Element | Description |
|---|---|
| **Node** | A computational or physical resource that hosts other elements. |
| **Device** | A physical hardware resource. |
| **System Software** | Software that provides a technology environment or platform. |
| **Technology Collaboration** | An aggregate of two or more nodes that interact. |

**Behaviour:**

| Element | Description |
|---|---|
| **Technology Function** | Automated behaviour performed by a node. |
| **Technology Process** | A sequence of technology-level behaviours. |
| **Technology Service** | An explicitly defined, externally visible technology behaviour. |
| **Technology Interaction** | Collective behaviour of a technology collaboration. |
| **Technology Event** | A state change in a technology context. |

**Passive structure:**

| Element | Description |
|---|---|
| **Artifact** | A physical piece of information — a file, executable, or configuration item. |
| **Communication Network** | A set of connected nodes over which communication passes. |
| **Path** | A link that enables communication or movement between nodes. |

---

## Implementation & Migration layer

Captures change, transition, and programme-level concerns.

| Element | Description |
|---|---|
| **Work Package** | A defined unit of change activity — a project or workstream. |
| **Deliverable** | A precisely defined output of a work package. |
| **Implementation Event** | A milestone or trigger within a change programme. |
| **Plateau** | A relatively stable state of the architecture over a period. |
| **Gap** | The difference between two plateaus — a current and a target state. |

---

## Relationships

ArchiMate defines a rich set of relationships. These are the most frequently encountered.

| Relationship | Notation | Description |
|---|---|---|
| **Composition** | closed diamond | A whole is composed of parts; the parts cannot exist without the whole. |
| **Aggregation** | open diamond | A whole groups parts that can exist independently. |
| **Assignment** | filled circle to filled arrowhead | An active structure element is assigned to the behaviour it performs (or a role to an actor). |
| **Realization** | dashed line, hollow arrowhead | A more concrete element realises a more abstract one (a process realises a service; an application realises a requirement). |
| **Serving** | open arrowhead | An element provides its functionality to another (a service serves a process). |
| **Access** | dashed line, open arrowhead | Behaviour accesses a passive structure element — reads, writes, or both. |
| **Influence** | dashed line, open arrowhead | An element affects the achievement or realisation of another (a driver influences a goal). |
| **Association** | plain line | An unspecified or general relationship, used when no more specific type applies. |
| **Triggering** | solid line, filled arrowhead | A temporal or causal sequence — one element triggers another. |
| **Flow** | dashed line, filled arrowhead | A transfer of information, value, or goods from one element to another. |
| **Specialization** | solid line, hollow triangle | A specific element is a particular kind of a general one. |

Relationships across layers are common and valid — for example, an Application Component *serving* a Business Process, or a Business Process *realising* a Business Service.

---

*Aligned with ArchiMate 3.x as specified by The Open Group. Selective by design.*
