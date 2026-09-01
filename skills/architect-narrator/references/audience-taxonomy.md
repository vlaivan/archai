# Audience Taxonomy

Stakeholder archetypes most commonly encountered in architecture communication. Each describes a recognisable pattern of role, knowledge, information need, and communication preference. Use it to orient audience profiling.

**How to use this taxonomy:**
1. Map the described audience to the closest archetype.
2. Use the archetype as a starting point — adjust for specifics provided.
3. Pay particular attention to *what good narration looks like* for each type.
4. Note that real stakeholders often blend archetypes — name the blend.

---

## Archetype 1 — Executive Sponsor

**Typical roles:** CEO, CFO, COO, board member, divisional director
**Management level:** Strategic
**Architectural knowledge:** Novice to informed — understands business impact, not architectural method
**Decision-making authority:** Investment decisions, strategic direction, organisational mandates

**Information need:**
Wants to understand the business significance of architectural choices, not the choices themselves. Needs to know: what is the risk or opportunity, what is being recommended, what does it cost in time and money, and what happens if we do nothing. Does not need to understand how the architecture works.

**Abstraction level:** Enterprise strategic
**Dimensions relevant:** Motivation, Strategy — translated into business language
**Dimensions to omit:** Information Systems, Technology (unless cost or risk is the point)

**Communication preferences:**
- Short. Fewer words, more weight per word.
- Recommendation-first. State what you want them to do before explaining why.
- Business language only. "Application portfolio rationalisation" → "reducing the number of systems we run and maintain."
- Risk and investment framing. What could go wrong? What does this protect or enable?
- Visual where possible, but only if the visual is self-explanatory without a guide.

**What good narration looks like:**
A one-page executive summary with a clear recommendation, three supporting reasons, a risk statement if they do not act, and a clear ask. Everything else is appendix material. The narrative sounds like a trusted senior advisor, not an analyst presenting findings.

**Common pitfalls:**
- Leading with the analysis before the conclusion
- Using architectural or IT vocabulary without translation
- Including more detail than is needed to support the decision
- Hedging the recommendation

---

## Archetype 2 — Business Leader

**Typical roles:** Business unit head, VP of function, domain owner, programme sponsor
**Management level:** Strategic to tactical
**Architectural knowledge:** Informed — understands that architecture has business implications, limited technical depth
**Decision-making authority:** Domain-level investment, process and organisational change, programme direction

**Information need:**
Wants to understand how architectural decisions affect their domain, their people, and their ability to deliver. Needs to know: what is changing, what does it mean for us specifically, what will be asked of us, and what do we get in return. Appreciates being treated as a peer, not a recipient.

**Abstraction level:** Domain tactical
**Dimensions relevant:** Motivation, Strategy, Business, Information (data ownership and access)
**Dimensions to omit:** Technology specifics; Information Systems at component level

**Communication preferences:**
- Domain-specific framing. Use their language, their processes, their examples.
- Change impact orientation. What will be different? For whom? When?
- Balanced. Acknowledge costs and disruption alongside benefits.
- Collaborative tone. "Here is what we are thinking — we need your input" lands better than "here is what is happening."

**What good narration looks like:**
A structured briefing that opens with what is happening and why the business leader should care, walks through the key implications for their domain, and closes with what is being asked of them and what support they will receive. The narrative sounds like a colleague, not a consultant.

**Common pitfalls:**
- Generic framing that does not address their specific domain
- Technology-heavy language
- Failing to acknowledge the burden change places on them
- Presenting conclusions without inviting engagement

---

## Archetype 3 — Programme or Project Manager

**Typical roles:** Programme manager, project manager, delivery lead, change manager
**Management level:** Tactical
**Architectural knowledge:** Informed to practitioner — understands dependencies, constraints, and the practical impact of architectural decisions on delivery
**Decision-making authority:** Delivery approach, resourcing, scheduling within programme scope

**Information need:**
Wants to understand what architecture means for how they plan and execute delivery. Needs to know: what are the dependencies, what are the constraints, what needs to happen in what order, and what are the risks to schedule or scope that architecture introduces or mitigates.

**Abstraction level:** Domain tactical to solution operational
**Dimensions relevant:** Business, Information Systems, Implementation & Migration
**Dimensions to omit:** Deep motivation and strategy (unless it affects scope); low-level technology specifics

**Communication preferences:**
- Concrete and actionable. Findings need to translate into things they can plan for.
- Dependency-explicit. Always name what depends on what.
- Timeline-aware. Frame everything in relation to delivery phases and milestones.
- Risk-forward. Name the architectural risks to delivery clearly.

**What good narration looks like:**
A structured briefing that walks through the architectural picture as it relates to the programme: what exists today that affects delivery, what is changing and when, what the key dependencies and risks are, and what architectural support or decisions are needed to keep delivery on track. Diagram-heavy if appropriate.

**Common pitfalls:**
- Abstract or strategic framing that does not connect to delivery
- Burying dependencies in prose rather than making them explicit
- Omitting timelines and sequencing

---

## Archetype 4 — Domain Architect

**Typical roles:** Business architect, information architect, application architect, solution architect, enterprise architect (peer-level)
**Management level:** Tactical to operational
**Architectural knowledge:** Practitioner to expert — speaks ArchiMate, understands frameworks, can engage with architectural reasoning directly
**Decision-making authority:** Architectural decisions within domain or solution scope

**Information need:**
Wants to understand the architectural substance. Needs to see the actual findings, the reasoning, the gaps, and the options — not a translated summary. Is a peer; treat them as one. Interested in what was discovered, how it was interpreted, and what the key architectural questions are.

**Abstraction level:** Domain tactical to solution operational
**Dimensions relevant:** All — depending on the architectural domain in focus

**Communication preferences:**
- Architecture-literate language. ArchiMate types, layer names, and relationship patterns are appropriate.
- Reasoning-visible. Show the analytical basis for conclusions.
- Precision over accessibility. Accuracy matters more than readability.
- Collaborative and exploratory. "Here is what we found and how we interpreted it — what do you see?" is appropriate.

**What good narration looks like:**
A structured technical briefing or review document that presents the architectural findings with their analytical basis visible, names the key judgement calls and their rationale, and opens questions for peer review. The narrative sounds like a colleague presenting work for peer challenge.

**Common pitfalls:**
- Over-simplifying for a sophisticated audience
- Hiding the reasoning behind polished conclusions
- Failing to invite challenge and alternative interpretation

---

## Archetype 5 — Technology Lead

**Typical roles:** CTO, Head of Engineering, Platform Lead, Technical Architect, IT Operations Manager
**Management level:** Tactical to operational
**Architectural knowledge:** Expert in technology; variable in architectural method
**Decision-making authority:** Technology stack, platform decisions, engineering standards, operational capability

**Information need:**
Wants to understand what architecture means for technology and engineering decisions. Needs to know: what does the current technology landscape look like architecturally, where are the constraints and risks, what are the proposed changes, and what is the rationale. Appreciates precision; is sensitive to architectural overreach into engineering territory.

**Abstraction level:** Domain tactical to solution operational
**Dimensions relevant:** Information Systems, Technology, Implementation & Migration
**Dimensions to omit:** Motivation and strategy details (present conclusions only); business process depth

**Communication preferences:**
- Technically precise. Imprecise technology claims undermine credibility.
- Boundary-respecting. Frame architectural recommendations clearly; do not prescribe engineering solutions.
- Evidence-based. Show the basis for technology-layer findings.
- Risk-and-debt orientation. Technology debt, operational risk, and constraint language resonates.

**What good narration looks like:**
A structured technical summary covering the relevant technology landscape findings, the architectural risks and constraints, and the key decisions or recommendations — with clear boundaries between what architecture is recommending and what is a technology/engineering decision. Honest about what is known, inferred, and unknown.

**Common pitfalls:**
- Overstepping into engineering prescription
- Imprecise technology language that signals unfamiliarity
- Omitting the operational implications of architectural changes

---

## Archetype 6 — Operational Specialist

**Typical roles:** Business analyst, developer, data engineer, system administrator, process owner
**Management level:** Operational
**Architectural knowledge:** Novice to informed — may have deep domain expertise but limited architectural framework knowledge
**Decision-making authority:** Operational decisions within their domain of expertise

**Information need:**
Wants to understand what this means for their work, their systems, or their processes. Needs concrete, specific information relevant to their area. Does not need the full architectural picture — needs the part that touches them.

**Abstraction level:** Solution operational
**Dimensions relevant:** Depends on specialism — Business for process specialists; Information Systems for developers; Technology for infrastructure specialists

**Communication preferences:**
- Specific and contextual. Generic statements are not useful; named systems, processes, and roles are.
- Impact-oriented. What changes for me? What do I need to do differently?
- Jargon-appropriate to their specialism. Use their domain language, not architectural language.
- Not over-burdened. They do not need strategic context unless it directly affects their work.

**What good narration looks like:**
A focused briefing or guidance document that explains the relevant architectural context, its specific implications for this person's area of work, and what they need to know or do. Clear, concrete, and bounded.

**Common pitfalls:**
- Too much strategic context that is not relevant to their work
- Architectural vocabulary without translation
- Failing to name the specific systems, processes, or roles that are affected

---

## Archetype 7 — Governance or Audit Body

**Typical roles:** Architecture Review Board, IT Governance Committee, Risk Committee, Internal Audit, Compliance Officer
**Management level:** Strategic to tactical
**Architectural knowledge:** Informed to practitioner — understands principles, standards, and the framework context
**Decision-making authority:** Approval, compliance ruling, risk acceptance or rejection

**Information need:**
Wants to understand whether the architecture is coherent, compliant, and appropriately governed. Needs to know: how this relates to standards and principles, what risks are present and how they are being managed, and what decisions or approvals are being sought.

**Abstraction level:** Enterprise strategic to domain tactical
**Dimensions relevant:** Motivation (principles and requirements), all dimensions at a summary level for compliance checking

**Communication preferences:**
- Standards-anchored. Reference the relevant principles, policies, or frameworks explicitly.
- Structured for decision. Present what is being submitted, what it is asking for, and the basis for the request.
- Balanced risk presentation. Do not minimise risks; present them with mitigations.
- Formal register. This is a governance submission, not a briefing.

**What good narration looks like:**
A formal structured submission — executive summary, architecture description at the appropriate level of abstraction, compliance and risk assessment against relevant standards, and a clear decision request. Appendices with supporting detail for members who want to go deeper.

**Common pitfalls:**
- Informal tone in a formal governance context
- Failing to reference the relevant standards and principles
- Presenting the recommendation without the risk assessment

---

## Blended archetypes

Real stakeholders often combine archetypes. Common blends:

| Blend | Example | Implication |
|---|---|---|
| Executive Sponsor + Business Leader | CFO who actively manages a major business domain | Both strategic framing and domain-specific impact needed |
| Domain Architect + Technology Lead | Enterprise Architect with strong infrastructure background | Full technical depth appropriate; boundary-setting still matters |
| Programme Manager + Domain Architect | Technical programme manager who designs as well as delivers | Delivery orientation plus architectural substance |
| Business Leader + Governance Body | Business unit head sitting on Architecture Review Board | Domain impact framing plus governance structure |

When a blend is identified, note it explicitly and decide which archetype is dominant for *this specific communication*.

---

## Abstraction level reference

| Level | Focus | Typical dimensions | Avoid |
|---|---|---|---|
| **Enterprise strategic** | Direction, investment, capability, risk | Motivation, Strategy | Implementation detail, system names, technical specifics |
| **Domain tactical** | Capability gaps, change impacts, domain design | Business, Information, Information Systems at capability level | Low-level technical; enterprise-wide context unless relevant |
| **Solution operational** | System specifics, integrations, design decisions | Information Systems, Technology, Implementation | Strategic framing; domain-wide scope unless directly relevant |
