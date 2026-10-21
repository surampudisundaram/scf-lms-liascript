<!--
author: Secure Controls Framework Council
email: info@securecontrolsframework.org
version: 2026.3.0
language: en
narrator: US English Female

comment: SCF-2026.3 Secure Controls Framework (Expanded Edition) - 10 modules,
50+ hours, built from the SCF-2026.3 OKF bundle.
-->
# SCF-2026.3 Secure Controls Framework (Expanded Edition)

This course teaches the Secure Controls Framework (SCF) as published in the **2026.3** release, in an expanded edition that adds two modules beyond the base seven: the risk and threat catalogs, and assessment practice with the capstone. The SCF is a metaframework: a single control catalog that maps hundreds of laws, regulations and frameworks onto one common control language.

The course is built strictly from the SCF-2026.3 source bundle. Figures quoted throughout are the published values, not estimates.

## Course at a glance

|  |  |
|---|---|
| Modules | 10 |
| Lessons | 56 |
| Knowledge checks | 60 |
| Estimated effort | 53 hours |
| Release | SCF 2026.3 |
| Format | LiAScript (offline-capable, self-assessing) |

## Module guide

| # | Module | Competency | Hours |
|---|---|---|---|
| 1 | Orientation & the SCR Model | catalog, versions | 6 |
| 2 | The Control Catalog | catalog | 6 |
| 3 | Focal Documents | documents | 5 |
| 4 | Assessment Objectives & Evidence Requests | sheets | 6 |
| 5 | Versions & Change Management | versions | 5 |
| 6 | The SCF Web Ecosystem | web | 5 |
| 7 | Conformity Assessment & Capstone | documents | 7 |
| 8 | Risk & Threat Catalogs | catalog | 4 |
| 9 | Assessment Practice & the Capstone | documents | 5 |
| 10 | Audit, Evidence & Capstone Execution | documents, sheets | 4 |

## How each module is built

Every module opens with its learning objectives, then works through its lessons, then closes with a six-question knowledge check. The knowledge check is self-assessing.

# Module 1 - Orientation & the SCR Model

Estimated effort: **6 hours**. Competency: **catalog, versions**.

## Learning objectives

- Explain what the Secure Controls Framework is, what it is not, and why it exists.

- Describe the SCF's three goals and the Security + Compliance + Resilience equation.

- Name the 34 SCF domains and locate any control within them.

- Distinguish Minimum Compliance Requirements from Discretionary Security Requirements.

- Trace how the SCF, the SCRMS and the SCR CAP fit together in the SCR ecosystem.

## 1.1 Why a Metaframework?

_50 minutes_

Most organizations do not fail because they lack security standards. They fail because they run half a dozen overlapping standards at once, each with its own control numbering, its own evidence vocabulary and its own audit calendar. The Secure Controls Framework (SCF) exists to collapse that duplication into a single, common control language.

The SCF is not just another framework. It is a **metaframework - a framework of frameworks**. It covers over 200 cybersecurity laws, regulations and frameworks with over 1,500 controls, and it is a free resource. Alongside the control catalog it defines a maturity model criteria set, an Evidence Request List (ERL), Assessment Objectives (AOs), and risk and threat catalogs.

Three goals drive the framework:

1. **Minimize an organization's attack surface.**
2. **Provide the roadmap for an organization to be secure, compliant and resilient.**
3. **Promote defensible evidence of reasonable practices.**

### Defensible evidence

Defensible evidence is the verifiable and objective proof that your organization's security, compliance and resilience activities actually occurred, were effective, and can withstand external scrutiny. It can be viewed as on-demand assurance for stakeholders, where assurance is evidence-based confidence and the demonstrable output of security, compliance and resilience activities.

> **The Rosetta Stone approach**
>
> The SCF normalizes disparate requirements found in laws, regulations and frameworks. These controls establish how organizations manage risks through preventing, detecting or lessening the ability of a particular threat from negatively impacting business processes.

### What a control is

In practical terms, a control is the power to influence or direct behaviors and the course of events. Controls are technical, administrative or physical safeguards. Within the SCF a control is a mechanism (a safeguard or countermeasure) designed to address protection needs specified by security requirements.

The SCF's three goals are stated plainly in the SCF Council's own framing: with cybersecurity we face a protracted war on an asymmetric battlefield, and security, compliance and resilience must become a unified objective rather than three competing ones.

### Key terms

- **Metaframework** - A framework that normalizes and cross-maps other frameworks.
- **Common Controls Framework (CCF)** - The normalized control set the SCF produces.
- **Defensible evidence** - Verifiable proof that practices occurred, were effective and withstand scrutiny.
- **Attack surface** - The set of points at which an unauthorized actor could gain access.

## 1.2 Security + Compliance + Resilience = A Unified Objective

_45 minutes_

The SCF treats security, compliance and resilience as a single combined objective. The shorthand used by the SCF Council is memorable:

**The SCR equation**

| Equation | Means |
|---|---|
| Security | Prevent |
| Compliance | Prove |
| Resilience | Survive |

Security without compliance is expensive and unprovable. Compliance without security is a paper exercise. Resilience without either is luck. The point of a unified objective is that an organization is not merely protected, but also meets its compliance requirements and can quickly bounce back from incidents.

### The Integrated Controls Management mindset

Cybersecurity is controls-centric, where controls are viewed as the nexus, or central pivoting point, for an organization's cybersecurity and data protection operations. This affects an entity's overall business rhythm, since the controls used to define secure practices have both direct and indirect impacts on the Technology Assets, Applications, Services and/or Data (TAASD) that business operations rely upon.

### The four questions the SCF forces you to answer

- **Who** - which people, processes, technologies, data and facilities are in scope?
- **What** - which control set applies?
- **Where** - which assessment boundary and geography?
- **When** - how often is it assessed?
- **Why** - which obligations drive the requirement?
- **How** - what mechanisms satisfy the requirement?

The SCF answers the *what* with a 1,500+ control catalog across 34 domains. The other questions are answered by the surrounding SCR ecosystem.

### Key terms

- **TAASD** - Technology Assets, Applications, Services and Data.
- **CIAS** - Confidentiality, Integrity, Availability and Safety - the SCF's evolution of the CIA Triad.
- **ICM** - Integrated Controls Management - treating controls as the pivot point of security operations.

## 1.3 The 34 Domains and the SCR Principles

_70 minutes_

The SCF established 34 common-sense principles to guide the development and oversight of a modern cybersecurity and data privacy program. The same 34 principles are organised as the 34 SCF **domains**: each domain carries a one-line principle and a longer principle intent that describes what the organisation is trying to achieve.

Every domain in 2026.3 is listed below with its control count, verified directly against the control catalog. The domain identifiers are stable, they are the join key for the whole framework, and they never change even when the controls inside them are renumbered.

**The 34 SCF domains and their 2026.3 control counts**

| # | ID | SCF Domain | Controls |
|---|---|---|---|
| 1 | GOV | Security, Compliance & Resilience Governance | 37 |
| 2 | AAT | Artificial Intelligence & Autonomous Technologies | 160 |
| 3 | AST | Asset Management | 64 |
| 4 | BCD | Business Continuity & Disaster Recovery | 61 |
| 5 | CAP | Capacity & Performance Planning | 8 |
| 6 | CHG | Change Management | 20 |
| 7 | CLD | Cloud Security | 19 |
| 8 | CPL | Compliance | 48 |
| 9 | CFG | Configuration Management | 58 |
| 10 | MON | Continuous Monitoring | 76 |
| 11 | CRY | Cryptographic Protections | 27 |
| 12 | DCH | Data Classification & Handling | 94 |
| 13 | EMB | Embedded Technology | 27 |
| 14 | END | Endpoint Security | 31 |
| 15 | HRS | Human Resources Security | 45 |
| 16 | IAC | Identification & Authentication | 123 |
| 17 | IRO | Incident Response | 48 |
| 18 | IAO | Information Assurance | 17 |
| 19 | MNT | Maintenance | 29 |
| 20 | MDM | Mobile Device Management | 10 |
| 21 | NET | Network Security | 103 |
| 22 | PES | Physical & Environmental Security | 51 |
| 23 | PRI | Data Privacy | 102 |
| 24 | PRM | Project & Resource Management | 15 |
| 25 | RSK | Risk Management | 35 |
| 26 | QTS | Quantum Security | 31 |
| 27 | SEA | Secure Engineering & Architecture | 40 |
| 28 | OPS | Security Operations | 11 |
| 29 | SAT | Security Awareness & Training | 22 |
| 30 | TDA | Technology Development & Acquisition | 74 |
| 31 | TPM | Third-Party Management | 43 |
| 32 | THR | Threat Management | 17 |
| 33 | VPM | Vulnerability & Patch Management | 32 |
| 34 | WEB | Web Security | 13 |

> **Reading the source numbering**
>
> The SCF Domain & Principles sheet prints the domain sequence with Quantum Security (QTS) positioned at 26 and Risk Management (RSK) at 25, while the remainder of the catalog numbers them 25 and 26 respectively. Always key off the three-letter identifier (QTS, RSK), never off the ordinal position in a table.

### Control weighting

The SCF assigns each control a value on a scale from 1 to 10, where 1 is the least important and 10 is the most important. These values are subjective, based on SCF contributor discussion, and exist to help prioritize controls.

- A control weighted **10** should be treated as a **material / key control**. A deficiency in it should be considered a material weakness.
- A control weighted **1** is a nice to have that does not materially affect risk.

One framing used by the Council for a weight of 10 was: *would you do business with an organization that did not have this control in place?*

### Key terms

- **Domain** - One of the 34 top-level groupings of the SCF control catalog.
- **SCR Principle** - The one-line statement of intent attached to each domain.
- **Control weighting** - A 1-10 subjective importance score used to prioritize controls.
- **Material / key control** - A control whose absence or deficiency is a material weakness.

## 1.4 Living Control Set, MCR and DSR

_55 minutes_

Minimizing an attack surface must address more than technical threats. The SCF process defines a **Living Control Set (LCS)** that specifies the Minimum Security Requirements (MSR) necessary to be secure, compliant and resilient. An LCS is built from two distinct kinds of requirement:

**Minimum Security Requirements decompose into MCR and DSR**

| Requirement type | Full name | Driven by | Focus |
|---|---|---|---|
| MCR | Minimum Compliance Requirements | Applicable laws, regulations and contracts | Compliance |
| DSR | Discretionary Security Requirements | Industry expectations and the organization's own risk tolerance | Security and resilience |

The distinction matters because it changes *who decides*. MCR is a floor set by somebody else - a regulator, a contract, a law. DSR is a choice made by the organization. An organization that cannot articulate its DSR is usually relying on MCR alone and will discover gaps the first time it faces a non-compliance event that no law anticipated.

### The nine SCRMS principles (PDCA)

The Secure, Compliant & Resilient Management System (SCRMS) operationalizes Plan-Do-Check-Act with nine steps. These are the reference sequence for turning a control catalog into a program:

1. Establish Context
2. Identify Applicable Controls
3. Define Maturity Expectations
4. Publish Governance Documentation
5. Assign Stakeholder Accountability
6. Prioritize Capabilities According To Risk
7. Maintain Situational Awareness
8. Manage Risk
9. Evolve Processes

> **One LCS, many mandates**
>
> Instead of rebuilding an entire compliance process or standing up a separate program for every new mandate - CMMC, HIPAA, GDPR, EU AI Act, NIS2, PCI DSS and whatever comes next - an organization implements a Living Control Set once. When the next mandate lands, those changes are absorbed into the LCS you already operate.

### Key terms

- **LCS** - Living Control Set - the tailored, maintained control set an organization actually runs.
- **MSR** - Minimum Security Requirements - MCR plus DSR.
- **MCR** - Minimum Compliance Requirements - the absolute minimum to comply.
- **DSR** - Discretionary Security Requirements - internally driven security and resilience choices.
- **SCRMS** - Secure, Compliant & Resilient Management System.

## 1.5 The SCR Ecosystem

_45 minutes_

Three SCF Council deliverables answer three different questions, and confusing them is the most common source of wasted effort:

**The three-part SCR answer**

| Artifact | Question it answers | Purpose |
|---|---|---|
| SCF | What? | A 1,500+ control catalog covering 34 domains. |
| SCRMS | How? | Operationalizes controls so the organization is secure, compliant and resilient. |
| SCR CAP | Prove it? | Third-party conformity validation against selected controls. |

Around those sit the governance bodies:

- **The Cyber AB** is the Accreditation Body for the SCR CAP.
- **The Cyber EF** is the engagement and stewardship layer for the SCR's ecosystem.
- **SAICO** (the SCR Assessor and Instructor Certification Organization) certifies the people who perform assessments.
- **The SCF Council** maintains the framework itself.

### The SCF is free - and that is deliberate

The SCF is free to help fix the broken nature of security, compliance and resilience practices that many organizations face. The quality of the SCF could easily justify a costly subscription service, but that would exclude most organizations and defeat the broader goal of improving practice on a macro scale. Contributors are volunteers; the work is sustained by sponsors.

The SCF is copyrighted material, but it leverages the **Creative Commons Attribution-NoDerivatives 4.0 International** public license. Attribution is required; creating derivative works - including using AI to transform SCF content into new policies, procedures, metrics, risks or threats - is prohibited. Read the SCF Terms & Conditions before you build commercial tooling on top of SCF content.

### Key terms

- **Cyber AB** - Accreditation Body for the SCR CAP.
- **Cyber EF** - Engagement and stewardship layer for the SCR ecosystem.
- **SAICO** - SCR Assessor and Instructor Certification Organization.
- **CC BY-ND 4.0** - The Creative Commons license under which the SCF is published.

## 1.6 Course Roadmap, Competencies and Mastery

_40 minutes_

This course is built on the SCF Competency Framework. Five competencies are assessed, each at a defined Bloom level and each with four mastery levels.

**The five SCF competencies assessed by this course**

| Competency | Description | Bloom level | Badge |
|---|---|---|---|
| Catalog | Control catalog knowledge | Understand | Catalog Badge |
| Documents | Document controls | Apply | Documents Badge |
| Sheets | Spreadsheet controls | Apply | - |
| Versions | Version control | Understand | - |
| Web | Web controls | Apply | - |

Mastery is reported on four levels - **Beginning** (basic awareness), **Developing** (working knowledge), **Proficient** (applied competence) and **Exemplary** (mastery). The assessment framework weights three components:

**Evaluation framework**

| Component | Weight | Mastery threshold | Instrument |
|---|---|---|---|
| Formative | 30% | 60% | Quiz |
| Summative | 40% | 70% | Exam |
| Capstone | 30% | 70% | Capstone project |

Retakes are allowed with a maximum of three attempts. The seven modules of this course map onto the five competencies and the capstone:

- **Module 1** - Orientation & the SCR Model (catalog, versions)
- **Module 2** - The Control Catalog (catalog)
- **Module 3** - Focal Documents (documents)
- **Module 4** - Assessment Objectives & Evidence Requests (sheets)
- **Module 5** - Versions & Change Management (versions)
- **Module 6** - The SCF Web Ecosystem (web)
- **Module 7** - Conformity Assessment & Capstone (all competencies)

> **Total study time**
>
> The course is estimated at 40 hours: 6 + 6 + 5 + 6 + 5 + 5 + 7 hours across the seven modules. Target audience: security professionals and auditors.

### Key terms

- **Competency** - A named capability assessed by the course (catalog, documents, sheets, versions, web).
- **Mastery level** - Beginning, Developing, Proficient or Exemplary.
- **Formative / Summative** - Low-stakes practice assessment vs. a graded end-of-course exam.

## Module 1 knowledge check

The SCF describes itself as a metaframework. What does that mean in practice?

<!-- data-randomize data-max-trials="3" -->
[( )] It is a framework that replaces all other frameworks in use.
[(X)] It normalizes and cross-maps over 200 laws, regulations and frameworks into one common control language.
[( )] It is a maturity model that supersedes NIST and ISO guidance.
[( )] It is a commercial GRC tool with a free tier.
[[?]] Think about the Rosetta Stone analogy used in the SCF Council material.
***
The SCF answers the *what* with a 1,500+ control catalog across 34 domains, and cross-maps those controls to over 200 laws, regulations and frameworks using Set Theory Relationship Mapping from NIST IR 8477. It does not replace the underlying frameworks.
***

How does the SCF summarize the Security + Compliance + Resilience equation?

<!-- data-randomize data-max-trials="3" -->
[( )] Security = Prove, Compliance = Prevent, Resilience = Survive
[( )] Security = Protect, Compliance = Document, Resilience = Recover
[(X)] Security = Prevent, Compliance = Prove, Resilience = Survive
[( )] Security = Prevent, Compliance = Prove, Resilience = Detect
***
Prevent / Prove / Survive is the equation used consistently across the SCF Council's own framing of the unified objective.
***

Minimum Security Requirements (MSR) are composed of which two requirement types?

<!-- data-randomize data-max-trials="3" -->
[( )] Mandatory Security Requirements and Discretionary Security Requirements
[(X)] Minimum Compliance Requirements (MCR) and Discretionary Security Requirements (DSR)
[( )] Minimum Control Requirements and Documented Security Requirements
[( )] Mandatory Evidence Requirements and Scoped Testing Requirements
***
MCR is the floor set by external obligations and focuses on compliance. DSR is set by the organization's own industry expectations and risk tolerance and focuses on security and resilience.
***

Which of the following are genuine deliverables of the Secure Controls Framework?

<!-- data-randomize data-max-trials="3" -->
[[X]] Maturity model criteria
[[X]] Evidence Request List (ERL)
[[X]] Assessment Objectives (AOs)
[[ ]] A commercially licensed automated configuration scanning tool
[[X]] Risk and threat catalogs
[[ ]] A certified body of individual cybersecurity auditors
***
The SCF defines maturity model criteria, the ERL, the AOs and the risk and threat catalogs. Auditor certification is handled by SAICO, not by the SCF itself, and the SCF publishes no scanning tool.
***

Which artifact answers the question "Prove it" in the SCR ecosystem?

<!-- data-randomize data-max-trials="3" -->
[( )] The SCF control catalog
[( )] The SCRMS
[(X)] The SCR CAP
[( )] The Cyber EF
***
The SCF answers *what*, the SCRMS answers *how*, and the SCR CAP answers *prove it* through third-party conformity validation.
***

Under the SCF Terms & Conditions, which statement about the Creative Commons license is correct?

<!-- data-randomize data-max-trials="3" -->
[( )] The SCF is public domain and may be modified freely with attribution.
[( )] Commercial redistribution of SCF-derived policies is permitted with attribution.
[(X)] Attribution is required, and creating derivative works - including AI-generated derivative content - is prohibited.
[( )] The SCF may only be used by organizations with fewer than 500 employees.
***
The SCF uses CC BY-ND 4.0. You must attribute; you may not remix, transform or build upon the material, and the prohibition expressly extends to using AI to turn SCF content into derivative policies, procedures, metrics, risks or threats.
***

# Module 2 - The Control Catalog

Estimated effort: **6 hours**. Competency: **catalog**.

## Learning objectives

- State how many controls the SCF 2026.3 catalog contains and how top-level and subcontrols are counted.

- Read and explain any SCF control statement, including its identifier structure.

- Locate controls by domain and subcontrol numbering.

- Distinguish a control objective from a control implementation.

- Apply control weighting and tailoring logic to a candidate control set.

## 2.1 Anatomy of the Catalog

_50 minutes_

The SCF 2026.3 control catalog contains **1,591 controls**. That total is made up of **812 top-level controls** and **779 subcontrols**, distributed across the 34 domains. Every one of the 1,591 controls carries at least one Assessment Objective.

**The SCF 2026.3 catalog at a glance**

| Measure | 2026.3 value |
|---|---|
| Domains | 34 |
| Controls (total) | 1,591 |
| Top-level controls | 812 |
| Subcontrols | 779 |
| Assessment Objectives | 6,446 |
| Evidence Requests | 422 |
| Focal Documents | 270 |

### Identifier anatomy

Control identifiers are stable, machine-friendly and hierarchical. A top-level control looks like `GOV-01`. A subcontrol extends it with a decimal suffix, as in `GOV-03.1`. The three-letter prefix is the domain identifier, the number is the sequence within the domain, and the decimal suffix marks a refinement of the parent control.

```text
GOV-03            Centralized Management of Security, Compliance & Resilience Controls
GOV-03.1          Secure Practices Alignment Justification
GOV-03.2          Standardized Terminology
GOV-03.3          Control Objectives
GOV-03.4          Assessment Objectives (AO)
```

Note that a subcontrol's number is *not* tied to its parent's number. `GOV-03.4` is the fourth subcontrol of `GOV-03`, but the parent `GOV-01` has no subcontrols at all in 2026.3. Treat the decimal as a local sequence, never as a percentage or a depth marker.

### Key terms

- **Top-level control** - A control with an identifier such as GOV-01.
- **Subcontrol** - A refinement of a parent control, e.g. GOV-03.1.

## 2.2 Reading a Control Statement

_55 minutes_

Almost every SCF control statement opens with **"Mechanisms exist to ..."**. This wording is deliberate, and the SCF Council has published the reasoning behind it.

The controls were written to be flexible and to meet the needs of organizations regardless of size or industry, which makes wording a challenge. Normalizing control wording produced three recognizable stems:

- "Mechanisms exist to..."
- "Automated mechanisms exist to..."
- "Physical security mechanisms exist to..."

The term *mechanism* is used because a mechanism can be (1) a manual process, (2) a technology solution, (3) an outsourced contract, or (4) a combination of those that come together to address the needs of the control. Smaller companies will often satisfy a control with a manual process; in Fortune 500 environments a technology solution will most often exist.

### Worked example: GOV-01

`GOV-01` - *Security, Compliance & Resilience Governance Policy*:

- Mechanisms exist to establish a formal, documented security, compliance and resilience governance policy that:
- (1) Conveys executive management's intent;
- (2) Provides organizational direction and expected behaviors;
- (3) Is reviewed at least annually; and
- (4) Is updated, as necessary, to adapt to evolving risks, threats and other changes that affect the organization.

> **Note the nested requirements**
>
> Controls frequently enumerate sub-requirements with (1), (2), (3). These are not illustrative - each numbered element is an assessable requirement that maps to Assessment Objectives. A control is only satisfied when every applicable element is addressed.

### A second worked example

`GOV-03.1` - *Secure Practices Alignment Justification*. Mechanisms exist to align the organization's Security, Compliance & Resilience Program (SCRP) with one or more industry-recognized frameworks that (1) support external scrutiny and (2) provide defensible justification for secure practices. Notice how the same sentence structure scales from a single sentence to a multi-clause requirement.

### Control objectives

A **control objective** describes targets or desired conditions to be met, designed to ensure that policy intent is met. Where applicable, control objectives are directly linked to an industry-recognized leading practice to align an organization with accepted due diligence and due care requirements. `GOV-03.3` - *Control Objectives* - is the control that makes this an explicit part of the catalog.

### Key terms

- **Mechanisms exist to** - The normalized stem of most SCF control statements.
- **Control objective** - A target condition that ensures policy intent is met.
- **Due diligence / due care** - The reasonable-care standards the SCF aligns to.

## 2.3 The Domain Landscape

_60 minutes_

Control counts vary enormously across domains, and the shape of the distribution tells you something about where the SCF Council placed its attention in 2026.3.

**Largest and smallest domains by control count**

| Domain | Controls | Domain | Controls |
|---|---|---|---|
| AAT | 160 | NET | 103 |
| IAC | 123 | PRI | 102 |
| DCH | 94 | MON | 76 |
| TDA | 74 | AST | 64 |
| BCD | 61 | CFG | 58 |
| PES | 51 | CPL | 48 |
| HRS | 45 | TPM | 43 |
| SEA | 40 | GOV | 37 |
| RSK | 35 | VPM | 32 |
| END | 31 | QTS | 31 |
| MON | 76 | SAT | 22 |

Three observations are worth carrying into your own scoping work.

1. **Identity and access dominates.** Identification & Authentication (123) and Data Privacy (102) together account for 225 controls. Identity is where most regulatory demand lands and where evidence is most often requested.
2. **AI is the largest single domain.** Artificial Intelligence & Autonomous Technologies (AAT) has 160 controls - more than double the next-largest domain. AI is now a first-class domain, not a set of addenda to other domains.
3. **Some domains are deliberately small.** Capacity & Performance Planning (CAP) has 8 controls and Mobile Device Management (MDM) has 10. Small domains are not low-value domains; they are domains where the behaviour is narrower.

> **Quantum Security is a good example**
>
> Quantum Security (QTS) holds 31 controls - comparable to Endpoint Security - even though the underlying topic is nascent. Its domain principle covers cryptographic inventory, prioritization, migration planning and cryptographic agility for Cryptographically Relevant Quantum Computers (CRQCs).

### Key terms

- **AAT** - Artificial Intelligence & Autonomous Technologies - the largest SCF domain at 160 controls.
- **NPE** - Non-Person Entity - devices, applications, service accounts and AI agents.
- **CRQC** - Cryptographically Relevant Quantum Computer.

## 2.4 Tailoring, Weighting and Compensating Controls

_55 minutes_

**Tailoring is required - not all controls are applicable.** The SCF provides a column in the spreadsheet labelled *Minimum Security Requirements (MSR) MCR + MSR* that assists the tailoring process.

The published tailoring procedure is deliberately spreadsheet-native, because the SCF is fundamentally an Excel workbook:

1. Hide or delete the columns containing laws, regulations or frameworks that are not applicable to your organization.
2. In the **MCR** column, put an "x" to mark a control as a *must have*. In the **DSR** column, put an "x" to mark it as a *nice to have*.
3. Unfilter that column and repeat for the next law, regulation or framework.
4. The MSR + DSR column now marks each control that is applicable for your needs.

The result is a SCF control set tailored for your specific needs - a Living Control Set.

### Three tiers of obligation

**Where obligations come from**

| Tier | Source | Effect |
|---|---|---|
| Statutory requirements | Law | Mandatory. Non-compliance is a legal exposure. |
| Regulatory requirements | Regulator | Mandatory within the regulator's jurisdiction. |
| Contractual requirements | Customer, partner, contract | Mandatory once you have signed. |

### Compensating controls

A **compensating control** is an alternative security, compliance and/or resilience control implemented in lieu of the deficient control that provides equivalent or comparable protection. Compensating controls include physical, administrative and/or technical safeguards employed in lieu of the deficient control, and reduce risk in a manner that is equivalent to, or comparable to, the protection offered if the deficient control were operational and effective.

A compensating control is not an excuse. Three things must hold for it to be accepted:

- It is **applicable** to the deficiency.
- It is **reasonable** in the circumstances.
- It is **implemented and operating properly** - not merely planned.

> **Materiality still applies**
>
> The Council's guidance is that a compensating control for a *non-material* control is generally acceptable. For a material control, a compensating control must be validated by the assessor and cannot simply be asserted by the organization.

### Key terms

- **Tailoring** - Selecting the subset of the catalog that applies to your obligations and risk.
- **Compensating control** - An alternative control providing equivalent or comparable protection.
- **LCS** - Living Control Set - the tailored output of the MSR + DSR exercise.

## 2.5 Control Objectives and the Maturity Model

_45 minutes_

A control tells you *what* must be true. A **control objective** tells you *what good looks like*, and it is the bridge between a catalog entry and a maturity assessment.

The SCF's capability maturity model is the **Secure, Compliant & Resilient Capability Maturity Model (SCR-CMM)**. It is a well-established six-level model, applied in a nested fashion:

**SCR-CMM capability maturity levels**

| Level | Name | Meaning |
|---|---|---|
| L0 | Not Performed | No control activity exists. |
| L1 | Performed Informally | Ad hoc activity, no documented process. |
| L2 | Planned & Tracked | Documented and monitored, but not defined. |
| L3 | Well Defined | Documented, approved, consistently applied across the organization. |
| L4 | Quantitatively Controlled | Measured and controlled against defined targets. |
| L5 | Continuously Improving | Measured, controlled and actively improved. |

The model nests two concerns: **maturity** (governance) and **assurance** (security). The Council's guidance treats these as complementary rather than competing - you cannot have a mature governance function without an assurance capability, and a well-run assurance function that nobody governs produces evidence nobody acts on.

### Maturity Level Criteria

**MLC** (Maturity Level Criteria) are specific to each maturity level and define reasonable staffing, technologies and processes to implement the desired level of maturity. This is why a maturity target is not a free-floating number: an L3 claim has to name the staffing, tooling and process evidence that supports it.

### Key terms

- **SCR-CMM** - Secure, Compliant & Resilient Capability Maturity Model.
- **MLC** - Maturity Level Criteria - the staffing, technology and process evidence for a level.
- **L0-L5** - The six SCR-CMM capability maturity levels.

## Module 2 knowledge check

How many controls does the SCF 2026.3 catalog contain, and how do they break down?

<!-- data-randomize data-max-trials="3" -->
[( )] 1,500 controls, all of them top-level
[(X)] 1,591 controls - 812 top-level and 779 subcontrols
[( )] 1,591 controls - 812 subcontrols and 779 top-level
[( )] 1,457 controls, all of them renumbered in 2026.3
[[?]] 812 + 779 should equal the total.
***
1,591 = 812 top-level controls + 779 subcontrols. The figure 1,457 is the number of controls that were *renumbered* in 2026.3, which is a common confusion when reading the errata column.
***

In the identifier `GOV-03.4`, what does the `4` represent?

<!-- data-randomize data-max-trials="3" -->
[( )] The depth of nesting in the domain hierarchy
[( )] The severity weight of the control
[(X)] The fourth subcontrol of parent control GOV-03
[( )] The assessment objective index for the control
***
The decimal suffix is a local sequence within the parent control. It carries no severity, weight or depth meaning, and the numbering is not contiguous across the domain.
***

A control begins "Mechanisms exist to...". Which is the SCF Council's stated reason for this wording?

<!-- data-randomize data-max-trials="3" -->
[( )] To imply that technology solutions are always required
[(X)] Because a mechanism may be a manual process, a technology solution, an outsourced contract, or a combination
[( )] To ensure every control statement fits on a single line in the spreadsheet
[( )] To avoid the SCF stating requirements that only large organizations can meet
***
The intent is flexibility across organization sizes. Manual processes are explicitly acceptable; in Fortune 500 environments a technology solution will most often exist.
***

Which statements about a compensating control are correct under the SCR CAP body of knowledge?

<!-- data-randomize data-max-trials="3" -->
[[X]] It must be applicable to the deficiency it covers.
[[X]] It must be reasonable in the circumstances.
[[X]] It must be implemented and operating properly.
[[ ]] It must be a technology solution - manual processes are never acceptable.
[[ ]] It may be planned and scheduled for implementation in the next assessment cycle.
***
All three validation tests must be met. A compensating control that is merely planned is not accepted, and a manual process is a legitimate mechanism.
***

Which SCF domain contains the most controls in 2026.3?

<!-- data-randomize data-max-trials="3" -->
[( )] Network Security (103)
[( )] Identification & Authentication (123)
[(X)] Artificial Intelligence & Autonomous Technologies (160)
[( )] Data Privacy (102)
***
AAT has 160 controls - more than double the next-largest domain, IAC at 123. AI is now a first-class SCF domain rather than a set of addenda elsewhere in the catalog.
***

What does a control weighted 10 in the SCF mean in practice?

<!-- data-randomize data-max-trials="3" -->
[( )] It is a control that must be implemented within the first 10 days of the program.
[( )] It is a control that attracts 10 Assessment Objectives.
[(X)] It is a material / key control whose absence or deficiency should be considered a material weakness
[( )] It is a control that is assessed at SCR CAP Comprehensive rigor.
***
The 1-10 weighting is a subjective prioritization aid. A 10 means material or key; a 1 means nice to have and not materially affecting risk.
***

# Module 3 - Focal Documents

Estimated effort: **5 hours**. Competency: **documents**.

## Learning objectives

- Explain what a Focal Document is and how the SCF indexes it.

- Read the Focal Document record: geography, FDI, FDN, FDS and STRM URL.

- Describe Set Theory Relationship Mapping and the five STRM relationship types.

- Use the Unified Scoping Guide to define an assessment boundary.

- Navigate a STRM document to find the controls behind a requirement.

## 3.1 What a Focal Document Is

_45 minutes_

A **Focal Document (FD)** is an authoritative external source - a law, regulation, standard, framework or guidance document - that the SCF maps its controls onto. The SCF 2026.3 release contains **270 focal documents**.

Each focal document is recorded with four identifiers plus its mapping document URL:

**Anatomy of a Focal Document record**

| Field | Meaning |
|---|---|
| Geography | Which part of the world the document applies to. |
| FDI - Focal Document Identifier | The SCF's stable machine identifier for the document. |
| FDN - Focal Document Name | The human-readable title of the document. |
| FDS - Focal Document Source | The publisher or standards body. |
| STRM URL | The Set Theory Relationship Mapping document showing which SCF controls relate to it. |

The FDI is the join key. It appears in the directory names of the STRM documents, so a document like `scf-strm-general-mitre-att-ck-16-1` maps to the MITRE ATT&CK 16.1 focal document. The FDI is deliberately lowercase and hyphenated so it can be used directly in file paths and URLs.

### Key terms

- **FD** - Focal Document - an external law, regulation, standard or framework.
- **FDI** - Focal Document Identifier - the SCF's stable identifier for an FD.
- **STRM** - Set Theory Relationship Mapping - the SCF's crosswalk document for an FD.

## 3.2 The Global Coverage Map

_45 minutes_

The 270 focal documents are distributed across five geographies. The distribution is a direct reflection of where regulatory demand is concentrated, and it is a useful sanity check on your own scoping assumptions.

**Focal document coverage by geography (270 total)**

| Geography | Focal documents | Share of total |
|---|---|---|
| General (global) | 93 | 34% |
| United States | 77 | 29% |
| EMEA | 53 | 20% |
| APAC | 36 | 13% |
| Americas (excluding US) | 11 | 4% |

The **General** category is the largest because it holds the standards bodies whose work is internationally recognized - ISO/IEC, NIST, CIS, BSI, AICPA, ISACA, OWASP, PCI SSC and others. These are the documents that carry the largest weight in a Tailored Living Control Set because they are referenced by customer contracts and by many regulators indirectly.

The **United States** category at 77 documents is the largest single national block, and it includes the full Federal and State series: federal law (SOX, HIPAA, GLBA, FERPA, COPPA, FTC Act), federal standards (NIST SP 800-53/171/800 and the CSF 2.0), sector regulators (SEC, FINRA, FERC, FDA, CMS, DOE, TSA, CISA) and a long tail of state privacy laws and state security control catalogues.

> **Counting note**
>
> Some focal documents map to more than one STRM document or are represented by a sub-document variant - for example a standard with multiple implementation levels produces a separate FDI for each level. Count FDIs, not publishers, when you are reconciling against the catalogue.

### Key terms

- **General geography** - Internationally recognized standards and frameworks - 93 documents.
- **US geography** - US federal law, standards, regulator rules and state laws - 77 documents.
- **EMEA / APAC / Americas** - Regional blocks of 53, 36 and 11 documents respectively.

## 3.3 Set Theory Relationship Mapping

_55 minutes_

The SCF leverages NIST IR 8477's concepts for Set Theory Relationship Mapping (STRM) to conduct crosswalk mapping. NIST IR 8477 is the gold standard for how to perform this type of mapping, and using it is what gives the SCF mappings defensibility that other crosswalks lack.

Every FD has a dedicated STRM document that states, relationship by relationship, how the external requirement relates to SCF controls. Five relationship types are used:

**The five STRM relationship types (NIST IR 8477)**

| # | Relationship type | Meaning |
|---|---|---|
| 1 | SUBSET OF | The external requirement is a subset of the SCF control. |
| 2 | INTERSECTS WITH | The external requirement and the SCF control share some but not all content. |
| 3 | EQUAL | The external requirement and the SCF control are equivalent in substance. |
| 4 | SUPERSET OF | The external requirement covers more than the SCF control. |
| 5 | NO RELATIONSHIP | The external requirement has no substantive relationship to the SCF control. |

Saying *no relationship* is a deliberate and valuable outcome. Many crosswalk tools only record matches, which makes their output look denser and more useful than it is. The SCF records the negative case explicitly, so a reader can see the actual size of the mapping surface.

### Expert-Derived Content vs Natural Language Processing

The STRM documents are built with a hybrid approach. **Expert-Derived Content (EDC)** captures the judgment of a human analyst, and **Natural Language Processing (NLP)** supports the identification of candidate relationships at scale. The EDC is what makes the mapping defensible in front of an assessor; the NLP is what makes it reproducible across 270 documents.

### Key terms

- **STRM** - Set Theory Relationship Mapping - the SCF's NIST IR 8477 based crosswalk method.
- **SUBSET OF / SUPERSET OF** - Relationships where one side's scope is strictly narrower or wider.
- **NO RELATIONSHIP** - An explicitly recorded negative crosswalk result.
- **EDC / NLP** - Expert-Derived Content and Natural Language Processing - the hybrid mapping method.

## 3.4 Scoping with the Unified Scoping Guide

_55 minutes_

Before you can assess a control you must decide what is in the assessment boundary. For the SCR CAP, the authoritative guidance is the **Unified Scoping Guide (USG)**, a free resource published at unifiedscopingguide.com. The USG *shall* be used to define the scope of the SCR CAP for an organization seeking assessment and for the assessment boundary itself.

The USG categorizes system components along three factors:

1. Whether sensitive or regulated data is being **stored, processed or transmitted**.
2. The **functionality** the component provides - access control, logging, antimalware, and so on.
3. The **connectivity** between the system and the sensitive / regulated data environment.

The USG applies to sensitive data types including Artificial Intelligence and Machine Learning system data, Attorney-Client Privilege Information, Biometric Data, Cardholder Data, Consumer Health Data, Controlled Unclassified Information, Critical Infrastructure Information, Export Controlled Data (ITAR/EAR), Federal Contract Information, Federal Tax Information, Intellectual Property, Operational Technology data, Personal Data / sensitive Personal Data, Protected Health Information, Criminal Justice Information, Student Educational Records (FERPA) and Threat Intelligence (TLP-marked).

### The ten USG zones

**The ten USG scoping zones**

| Zone | Name | What it covers |
|---|---|---|
| 1 | Sensitive Data Assets (SDA) | Systems, services and applications that directly P/S/T sensitive or regulated data. |
| 2 | Segmenting | Segmenting systems that provide access, e.g. firewalls and hypervisors. |
| 3 | Security Tools | Tools that directly impact the integrity of zone 1 and 2 assets, e.g. Active Directory, centralized antimalware, vulnerability scanners, IPS/IDS. |
| 4 | Connected | Anything with a direct or indirect connection into the sensitive data environment. |
| 5 | Out-of-Scope | Systems completely isolated from the sensitive data systems. |
| 6 | Enterprise-Wide | The organization's overall corporate security program, cyber and physical. |
| 7 | External Service Provider (ESP) | Supply-chain security with flow-down of contractual requirements. |
| 8 | Subcontractors | Third parties executing part of the contract who may create, access, receive, store or transmit regulated data. |
| 9 | Cloud Service Provider (CSP) | An ESP that offers cloud computing services. |
| 10 | Personal / physical premises | The locations and the people that operate within the boundary. |

> **The connected rule is the expensive one**
>
> Zone 4 is where scoping projects blow up. If a system *can* impact the security of sensitive data - name resolution, web redirection servers - it is in scope. Zone 5 (fully isolated) is the only reliable exclusion, and proving isolation is expensive.

### Key terms

- **USG** - Unified Scoping Guide - the authoritative scoping guidance for the SCR CAP.
- **Assessment boundary** - The scope of control implementation to which assessment is applied.
- **ESP / CSP** - External Service Provider / Cloud Service Provider - USG zones 7 and 9.
- **SDA** - Sensitive Data Assets - USG zone 1.

## 3.5 Working Practice: From Requirement to Controls

_50 minutes_

Putting modules 2 and 3 together produces the workflow most practitioners use every day.

1. **Start from the obligation.** Name the focal document - say GDPR Article 32 - and note its geography and FDI.
2. **Open the STRM document** for that FDI. It lists the external requirement text alongside the relationship type and the SCF control identifier for each mapping.
3. **Collect the SCF control set.** Note every control where the relationship is SUBSET OF, EQUAL or INTERSECTS WITH. NO RELATIONSHIP entries are dropped; SUPERSET OF entries usually mean the SCF control covers the requirement plus more, so you keep it but record the scope difference.
4. **Separate MCR from DSR.** Controls that carry the obligation into your minimum set are MCR. Controls that strengthen the posture beyond the obligation are candidates for DSR.
5. **Pull the Assessment Objectives** for each retained control and build the evidence request list from them.

The step most often skipped is step 5. Selecting a control without its AOs gives you a requirement but no way to know what evidence will satisfy it.

> **Use the notes column**
>
> The STRM documents carry a notes column that records specific errata for that mapping. When a control was renumbered in 2026.3, the note tells you which legacy identifier the mapping used to reference. This is the bridge that keeps crosswalks working across a release.

### Key terms

- **Obligation-to-control workflow** - Focal document -> STRM -> controls -> AOs -> evidence.
- **Legacy identifier** - The pre-2026.3 control number, retained for crosswalk continuity.

## Module 3 knowledge check

How many focal documents does the SCF 2026.3 release index?

<!-- data-randomize data-max-trials="3" -->
[( )] 250
[(X)] 270
[( )] 268
[( )] 300
***
270 focal documents, distributed as 93 General, 77 US, 53 EMEA, 36 APAC and 11 Americas. 268 is the count of STRM directories when two documents without an available STRM are excluded - a different measurement of the same release.
***

Which field in a Focal Document record is the SCF's stable, machine-readable identifier?

<!-- data-randomize data-max-trials="3" -->
[( )] The Focal Document Name (FDN)
[( )] The Focal Document Source (FDS)
[(X)] The Focal Document Identifier (FDI)
[( )] The STRM URL
***
The FDI is the join key used in file paths and URLs, e.g. `general-mitre-att-ck-16-1`. The FDN is the human-readable title and the FDS is the publisher.
***

Which of these are STRM relationship types defined by the SCF from NIST IR 8477?

<!-- data-randomize data-max-trials="3" -->
[[X]] SUBSET OF
[[X]] INTERSECTS WITH
[[X]] NO RELATIONSHIP
[[ ]] PARTIALLY COMPLIANT
[[X]] EQUAL
[[ ]] MATERIAL OVERLAP
***
The five types are SUBSET OF, INTERSECTS WITH, EQUAL, SUPERSET OF and NO RELATIONSHIP. Recording the negative case explicitly is what makes the mapping honest about its size.
***

Which document is the authoritative guidance for defining the scope of an SCR CAP assessment?

<!-- data-randomize data-max-trials="3" -->
[( )] The NIST SP 800-53 control catalogue
[( )] The SCF Overview & Instructions document
[(X)] The Unified Scoping Guide (USG)
[( )] The SCF Control Assurance Tool (CAT)
***
The SCR CAP body of knowledge states that the Unified Scoping Guide shall be used to define the scope of the SCR CAP for an OSA and the assessment boundary.
***

Which USG zone contains systems that are completely isolated from the sensitive data environment?

<!-- data-randomize data-max-trials="3" -->
[( )] Zone 1 - Sensitive Data Assets
[( )] Zone 2 - Segmenting
[(X)] Zone 5 - Out-of-Scope
[( )] Zone 4 - Connected
***
Zone 5 is the only reliable exclusion zone. Zone 4 (Connected) captures anything with a direct or indirect connection into the sensitive data environment, including systems that can affect its security such as name resolution or web redirection servers.
***

An external requirement is broader in scope than an SCF control. Which STRM relationship applies?

<!-- data-randomize data-max-trials="3" -->
[( )] SUBSET OF
[( )] INTERSECTS WITH
[(X)] SUPERSET OF
[( )] EQUAL
***
SUPERSET OF means the external requirement covers more than the SCF control. In practice you usually retain the control but record the scope difference, because the SCF control is a narrower, testable expression of the requirement.
***

# Module 4 - Assessment Objectives & Evidence Requests

Estimated effort: **6 hours**. Competency: **sheets**.

## Learning objectives

- Explain what an Assessment Objective is and how it differs from a control statement.

- Read the AO sheet, including reciprocal AOs, SDP, PPTDF applicability and assessment rigor.

- Explain how an AO Origin records where an objective came from.

- Describe the Evidence Request List, its 30 Areas of Focus and how ERLs link to controls.

- Build an evidence request list from a set of selected SCF controls.

## 4.1 What an Assessment Objective Is

_50 minutes_

An **Assessment Objective (AO)** is an objective statement that establishes the desired outcome for the assessment of a specific control. There may be multiple AOs associated with a control. The SCF 2026.3 release defines **6,446 Assessment Objectives** across **all 1,591 controls**.

**Assessment Objective coverage across the 2026.3 catalog**

| Measure | Value |
|---|---|
| Assessment Objectives | 6,446 |
| Controls with at least one AO | 1,591 (100%) |
| Median AOs per control | 2 |
| Maximum AOs per control | 65 (IAO-09) |
| Minimum AOs per control | 1 |

The AO text is written as a completion statement. A control says *what must exist*; an AO says *what an assessor must be able to determine*. Read them together:

```text
CONTROL  GOV-01  Security, Compliance & Resilience Governance Policy
  Mechanism: a formal, documented governance policy

AO  GOV-01_A01
  A formal, documented security, compliance and resilience governance policy is
  approved by executive management, or a formally delegated authority, and
  conveys executive management's intent for security, compliance and
  resilience governance.

AO  GOV-01_A04
  The security, compliance and resilience governance policy is reviewed at
  least annually.
```

The standard AO framing is: *the assessor shall examine, interview, and/or test to determine if appropriately scoped evidence exists to support the claim that:* ... and then the objective.

> **Why the median matters**
>
> A median of two AOs per control means most controls are deliberately simple to assess. The distribution is highly skewed: IAO-09 (Information Assurance) carries 65 AOs because assurance controls are inherently multi-part, while many WEB controls carry a single AO.

### Key terms

- **AO** - Assessment Objective - an objective statement establishing the desired assessment outcome.
- **AO Origin** - The source that produced an AO, e.g. SCF Created or a NIST 53A objective.
- **Reciprocal AO** - An equivalent objective in another standard, used to avoid re-assessment.

## 4.2 The AO Sheet

_55 minutes_

The assessment objectives sheet carries 23 columns. Not all of them are used on every row, but you need to know which columns carry decision-relevant information when you are scoping or assessing.

**The AO sheet's decision-relevant columns**

| Column | What it tells you |
|---|---|
| SCF # | The control the objective belongs to. |
| SCF AO # | The objective's own identifier, e.g. GOV-01_A04. |
| SCF Assessment Objective (AO) | The objective statement itself. |
| Reciprocal AOs | Equivalent objectives in other frameworks - reuse evidence. |
| SCF Defined Parameters (SDP) | Recommended minimums, e.g. 'at least annually'. |
| PPTDF Applicability | People, Process, Technology, Data, Facilities and/or AI applicability. |
| SCR CAP Assessment Rigor (AR) | The rigor level the objective is assessed at. |
| SCF Assessment Objective (AO) Origin(s) | Where the objective came from. |
| Legacy SCF # | The pre-2026.3 control identifier. |
| CMMC Level 1 AOs | CMMC-specific objective mapping. |
| NIST 800-53A / 800-171A / 800-171A R3 / 800-172A | Reciprocal NIST objective identifiers. |
| Asset Type examine/interview/test | The assessment method verbs for this objective. |
| Assessment Procedure | The procedure the assessor performs. |
| Expected Result(s) | What a passing result looks like. |
| Assessment Status | met / not met / not tested. |
| Inherited y/n | Whether the control is inherited from another entity. |
| Assessment Frequency | How often the objective is re-assessed. |
| Last Date Assessed / Assessment Performed By | Assessment record keeping. |

### SDP - the parameter that makes an AO testable

SCF Defined Parameters are the recommended minimums that make an objective measurable. Compare these two AO texts from `GOV-01`:

```text
GOV-01_A01  ... is approved by executive management ... and conveys
             executive management's intent ...

GOV-01_A04  ... is reviewed at least annually.
             SDP: at least annually
```

Without the SDP, 'reviewed periodically' is untestable. With it, 'reviewed at least annually' gives an assessor a binary, defensible pass/fail. Always read the SDP column before drafting an evidence request.

### Key terms

- **SDP** - SCF Defined Parameters - the recommended minimums that make an objective measurable.
- **PPTDF Applicability** - Which of People, Process, Technology, Data, Facilities and/or AI the objective touches.
- **Reciprocal AO** - An equivalent objective in another standard; evidence can be reused.

## 4.3 AO Origins and Reciprocal Objectives

_45 minutes_

The **AO Origin** column records where an objective came from. Objectives marked *SCF Created* were written by the Council. Others were imported from a source framework and then normalized into the SCF's objective language.

The reciprocal columns do the same job for NIST: the sheet carries CMMC Level 1 AOs plus NIST 800-53A, 800-171A, 800-171A R3 and 800-172A identifiers against individual objectives. An objective with a reciprocal NIST identifier can typically be satisfied with the same evidence that satisfies the NIST control - which is the single largest source of assessment efficiency in the whole framework.

A worked pairing from the AO sheet:

**GOV-02 objectives, their origins and NIST reciprocals**

| SCF AO | Origin | Reciprocal NIST 800-53A |
|---|---|---|
| GOV-02_A01 | 53A_R5_PM-01a.[01] | Governance policy is documented and approved. |
| GOV-02_A02 | 53A_R5_PM-01a.02[03] | Management commitment to the program is addressed. |
| GOV-02_A04 | 53A_R5_PM-01c.[01] | The governance program is protected from unauthorized disclosure. |
| GOV-02_A06 | 53A_R5_PM-01a.[02] | The governance program is disseminated. |

> **Practice tip**
>
> When building an evidence request list, sort by the reciprocal columns first. Objectives that map to a NIST control you already have evidence for are the cheapest wins in the assessment plan - and they are the ones most often duplicated by accident when each framework is assessed separately.

### Key terms

- **AO Origin** - The source of an objective - SCF Created, or an imported NIST 53A objective.
- **53A_R5** - NIST SP 800-53A revision 5 assessment procedure identifiers.

## 4.4 The Evidence Request List

_55 minutes_

The **Evidence Request List (ERL)** is a finite list of supporting evidence used in an audit or assessment. The SCF 2026.3 release defines **422 ERLs** grouped into **30 Areas of Focus**.

Each ERL record carries an identifier, its Area of Focus, the artifact name, a description of what the artifact must show, the SCF controls it maps to, and the legacy control mappings.

```text
ERL #   E-AAT-01
Area   Artificial Intelligence (AI) & Autonomous Technologies Governance
Artifact  Artificial Intelligence and Autonomous Technologies (AAT) Governance Program
Description  Documented evidence of a governance program for Artificial
             Intelligence and Autonomous Technologies (AAT).
SCF control mappings   AAT-02, AAT-05, AAT-08
Legacy mappings        AAT-01
```

### Where the evidence burden sits

**ERL counts across the 30 Areas of Focus (top and bottom shown)**

| Area of Focus | ERLs |
|---|---|
| Security, Compliance & Resilience Governance | 58 |
| Asset Management | 47 |
| Human Resources | 30 |
| Technology Design & Acquisition | 22 |
| Business Continuity | 19 |
| Data Protection | 19 |
| Identity & Access Management | 18 |
| Compliance | 16 |
| Risk Management | 15 |
| Secure Engineering & Architecture | 2 |
| Security Operations | 2 |

The distribution is a practical planning tool. Governance carries 58 ERLs because a governance program is largely documentary; Security Operations carries 2 because operational effectiveness is demonstrated by observation rather than by artifact.

### Key terms

- **ERL** - Evidence Request List - a finite list of supporting evidence for audit or assessment.
- **Area of Focus** - One of the 30 groupings the ERLs are organized into.
- **ERL artifact** - The specific document or record being requested.

## 4.5 From Controls to Evidence

_55 minutes_

AOs and ERLs are two views of the same assessment problem, and the relationship between them is what makes the SCF sheets usable together.

**AOs and ERLs side by side**

|  | Assessment Objective | Evidence Request |
|---|---|---|
| Granularity | Per control - one or more per control. | Per artifact - many ERLs may map to one control. |
| Question answered | Has the control been implemented and is it operating? | What artifact will demonstrate it? |
| Written by | SCF Council and source frameworks. | Practitioners, informed by the catalog. |
| Typical count | 6,446 objectives. | 422 ERL artifacts. |
| How they link | An AO names the outcome. | An ERL names the proof and lists the control mappings. |

The workflow for building your own evidence request list:

1. Select the controls in scope (Module 2 tailoring, Module 3 scoping).
2. Pull every AO for those controls and sort by SDP - the parameters tell you what 'done' means.
3. Group the AOs by the artifact that would satisfy them; this produces your candidate ERLs.
4. Cross-check against the published ERL for the matching Area of Focus - the SCF has already done this grouping for you.
5. Assign a collection method and owner to each ERL, and record the reciprocal NIST or CMMC objectives you can satisfy from evidence you already hold.

The last step is where the effort compounds. Once the ERL-to-AO mapping is explicit, a single artifact satisfies many objectives at once - and the second assessment cycle is dramatically cheaper than the first.

### Key terms

- **Evidence-to-AO mapping** - The explicit link between a requested artifact and the objectives it satisfies.
- **Collection method** - How an artifact is gathered: interview, examine, test, or automated collection.

## Module 4 knowledge check

How many Assessment Objectives does SCF 2026.3 define?

<!-- data-randomize data-max-trials="3" -->
[( )] 1,591
[( )] 422
[(X)] 6,446
[( )] 30
***
6,446 AOs cover all 1,591 controls. 422 is the Evidence Request List count and 30 is the number of ERL Areas of Focus.
***

What is the median number of Assessment Objectives per control?

<!-- data-randomize data-max-trials="3" -->
[( )] 1
[(X)] 2
[( )] 4
[( )] 65
***
The median is 2, with a minimum of 1. The maximum is 65, on IAO-09 - the distribution is heavily skewed by assurance controls that are inherently multi-part.
***

What does the SCF Defined Parameters (SDP) column add to an Assessment Objective?

<!-- data-randomize data-max-trials="3" -->
[( )] The name of the assessor who signed off the objective
[( )] The severity rating of the underlying control
[(X)] The recommended minimums that make the objective measurable and testable
[( )] The legacy control number the objective replaced
***
SDP turns an untestable phrase like 'reviewed periodically' into 'reviewed at least annually' - a binary, defensible pass/fail condition.
***

Which columns on the Assessment Objectives sheet help you avoid duplicating evidence collection?

<!-- data-randomize data-max-trials="3" -->
[[X]] Reciprocal AOs
[[X]] NIST 800-53A / 800-171A / 800-172A identifiers
[[X]] CMMC Level 1 AOs
[[ ]] Last Date Assessed
[[ ]] Assessment Performed By
***
The reciprocal columns let you reuse evidence you already hold for another framework. Last Date Assessed and Assessment Performed By are assessment record-keeping fields, not reuse aids.
***

How many Evidence Requests are defined in SCF 2026.3, and into how many Areas of Focus?

<!-- data-randomize data-max-trials="3" -->
[( )] 1,591 controls across 34 domains
[(X)] 422 ERLs across 30 Areas of Focus
[( )] 422 ERLs across 34 Areas of Focus
[( )] 270 ERLs across 30 Areas of Focus
***
422 ERLs across 30 Areas of Focus. 34 is the number of SCF domains - the ERL grouping does not mirror the domain structure one-to-one.
***

Which Area of Focus carries the largest number of Evidence Requests?

<!-- data-randomize data-max-trials="3" -->
[( )] Asset Management (47)
[( )] Human Resources (30)
[(X)] Security, Compliance & Resilience Governance (58)
[( )] Identity & Access Management (18)
***
Governance carries 58 ERLs because a governance program is largely documentary. Security Operations, at the other end, carries 2.
***

# Module 5 - Versions & Change Management

Estimated effort: **5 hours**. Competency: **versions**.

## Learning objectives

- Describe the SCF release cadence and explain why version discipline is part of the control set.

- Quantify what changed in the 2026.3 reorganization using the published errata tallies.

- Trace any deprecated 2026.2 control to its 2026.3 merge target.

- Read the Legacy SCF # column, the ERRATA tab and the STRM notes column to establish control identity.

- Migrate an organization's own control set, evidence and GRC records across a renumbering.

## 5.1 The SCF Release Cadence

_45 minutes_

The Secure Controls Framework is a **living control set**, not a document. It is published by the SCF Council on a quarterly cadence - one update per quarter, four per year - with out-of-cycle releases when circumstances demand them. The stated goal is to publish on a quarterly basis, and the general cadence is one update per quarter.

The scale of the framework explains the churn. Over the eight-plus years of its life the SCF expanded from a few dozen laws, regulations and frameworks to **over 250**. Each addition lands somewhere in the catalog, and each addition changes the context of the controls around it.

SCF 2026.3 - the release this course is built on - is the clearest example of that churn. It is the first release to carry a **SIGNIFICANT CHANGE** affecting legacy control numbering, and it was driven by two stated goals:

1. **Merging and deprecating controls that were duplicative**; and
2. **Reorganizing controls to create efficient organization within the most applicable domain.**

The 34 SCF domains did not change. What changed was everything inside them.

> **Why this matters to you**
>
> Every control number in the SCF is a foreign key. It appears in your policies, your GRC platform, your evidence folders, your tickets, your audit workpapers, your crosswalks to NIST and ISO and CMMC, and your board reporting. A renumbering is not a cosmetic event - it is a change to a primary key that your whole system depends on.

This is why the SCF publishes mappings. The Council's own position is that the only constant in life is change, and even the SCF has to keep evolving as laws, regulations and frameworks are added to the landscape. Minimizing disruption is an explicit design goal: the current-to-legacy mapping is built directly into the SCF and detailed in the download tabs.

- **Quarterly** - the standard release cadence.
- **Out-of-cycle** - possible, but the goal is quarterly publication.
- **34 domains** - unchanged in 2026.3.
- **250+** - laws, regulations and frameworks now covered.

### Key terms

- **Living Control Set (LCS)** - An authoritative, point-in-time definition of what reasonable security, compliance and resilience means for an entity - instantiated from MCR, DSR, risk appetite and materiality criteria.
- **Release cadence** - The quarterly publication rhythm of the SCF.

## 5.2 What Actually Changed in 2026.3

_55 minutes_

The Change Overview sheet of the 2026.3 workbook carries one row per control - **1,591 rows** - and each row records the control's domain, name, new number, description, **Legacy SCF #** and a set of **errata tags** for 2026.3. Those tags are the machine-readable statement of what the Council did.

**Errata tags recorded in the 2026.3 Change Overview sheet**

| Errata tag | Controls | What it means |
|---|---|---|
| renumbered | 1,457 | The control kept its identity but was given a new SCF number. |
| wordsmithed | 204 | The control statement's wording was changed. |
| renamed | 185 | The control's name was changed. |
| moved domains | 99 | The control was relocated into a different SCF domain. |
| new control | 80 | A control that did not exist before was added. |
| merged old | 22 | The control absorbed one or more deprecated controls. |
| (no errata tag) | 27 | The control was untouched by the 2026.3 reorganization. |

Those figures are not independent - they compose. Start from the whole:

- **1,591** controls in the 2026.3 catalog - **812** top-level and **779** subcontrols.
- **80** are new controls. Every one of them has a Legacy SCF # of **NONE**, because there is nothing to map from.
- That leaves **1,511** controls that carry a legacy mapping.
- **1,457** of those 1,511 were renumbered, so **54** controls kept their existing number.
- Of those 54, **27** have no errata tag at all - genuinely untouched - and **27** carry a non-renumbering tag such as *wordsmithed* or *merged old*.

And on the other side of the ledger, de-duplication removed controls outright:

**23 deprecated controls were removed.** Each one was merged into a surviving control, and each merge is recorded so you can find where its requirements went.

> **Reading the arithmetic**
>
> 1,457 renumbered + 80 new + 54 unchanged = 1,591. The 54 unchanged split into 27 completely untouched controls and 27 controls that kept their number but were renamed, reworded, moved between domains, or absorbed a deprecated control.

### Key terms

- **Errata tag** - A machine-readable marker in the Change Overview sheet recording the type of change made to a control in a release.
- **Deprecated control** - A control removed by the de-duplication effort, with its requirements merged into a surviving control.

## 5.3 The 23 Deprecated Controls and Where They Went

_50 minutes_

The READ THIS sheet publishes the complete deprecation list: the name of each retired control, its legacy number, and the 2026.3 control it was merged into. This is the table you use when a colleague asks, "we had a control for that - is it gone?"

**All 23 controls deprecated and removed in SCF 2026.3, with their merge targets**

| Deprecated control | Legacy # | Merged into |
|---|---|---|
| Component Disposal | TDA-11.2 | AST-22 |
| Governing Access Restriction for Change | END-03.2 | CHG-04.1 |
| Prohibit Installation Without Privileged Status | END-03 | CHG-04.2 |
| Restrict Configuration By Users | NET-15.3 | CHG-04.2 |
| Two-Person Rule | HRS-12.1 | CHG-04.3 |
| Unauthorized Installation Alerts | CFG-05.1 | CHG-12 |
| Approved Baseline Deviations | AST-02.4 | CFG-06 |
| Automated Configuration Enforcement | CFG-06 | CFG-08.2 |
| User-Installed Software | CFG-05 | CFG-12 |
| Prevent Program Execution | SEA-06 | CFG-14 |
| Information Disposal | DCH-21 | DCH-17 |
| Data Anonymization | PRI-05.3 | DCH-36 |
| Phishing & Spam Protection Centralized Management | END-08.1 | END-03.1 |
| Automatic Spam and Phishing Protection Updates | END-08.2 | END-03.2 |
| Usage Conditions | IAC-15.8 | IAC-07 |
| Automated Authentication Through Cryptographic Modules | CRY-02 | IAC-38 |
| Limit Personal Data (PD) Dissemination | SEA-09.1 | PRI-17 |
| Primary Source Collection | DCH-22.3 | PRI-32 |
| Alternative Security Measures | BCD-07 | RSK-18 |
| Layered Network Defenses | NET-02 | SEA-06 |
| Trusted Path | END-09 | SEA-27 |
| Ports, Protocols & Services In Use | TDA-02.1 | TDA-08.4 |
| Insider Threat Response Capability | IRO-02.2 | THR-15 |

Two patterns jump out of this table, and both matter when you migrate.

**First, the moves are not always lateral.** Several controls crossed domains in the process, which is exactly what the reorganization was designed to do - place each control in the domain where it is most applicable. Trusted Path moved from Endpoint Security (END-09) into Secure Engineering & Architecture as SEA-27. Layered Network Defenses moved from Network Security (NET-02) into SEA-06. Information Disposal moved from Data Classification & Handling (DCH-21) into DCH-17.

**Second, the retirement is not always a simple rename.** A deprecated control's requirements are now expressed inside a different control, and sometimes with a different name and a different scope. 'Trusted Path' became 'Secure Log-On Procedures (Trusted Path)'. 'Alternative Security Measures' became 'Compensating Countermeasures' in the Risk Management domain (RSK-18). Your policy that referenced the old name now describes something that is expressed at a different control, and possibly in a different domain.

### Key terms

- **Merge target** - The surviving control into which a deprecated control's requirements were merged.

## 5.4 Using the Legacy Mapping

_50 minutes_

The mapping is **many-to-one**. A single 2026.3 control can absorb several legacy controls, and the Legacy SCF # cell contains a newline-separated list when it does. Exactly **22** controls in 2026.3 carry a multi-value legacy cell - and those 22 are precisely the controls tagged *merged old*.

**The 22 controls that absorbed deprecated controls in 2026.3**

| 2026.3 control | Absorbed legacy controls |
|---|---|
| CHG-04.2 Role-Based Permissions To Implement Changes | END-03, CHG-04.4, NET-15.3 |
| CHG-04.1 Access Restriction For Change | CHG-04, END-03.2 |
| CHG-04.3 Dual Authorization for Changes To Critical / Sensitive TAAS | CHG-04.3, HRS-12.1 |
| CHG-12 Unauthorized Software Installation Alerts | CFG-05.1, END-03.1 |
| CFG-06 Approved Configuration Deviations | AST-02.4, CFG-02.7 |
| CFG-08.2 Integrity Assurance & Enforcement (IAE) | CFG-06, CFG-06.1 |
| CFG-12 Restrict Roles Permitted To Install Software | CFG-05, CFG-05.2 |
| CFG-14 Prevent Unauthorized Software Execution | CFG-03.2, SEA-06 |
| DCH-17 Digital & Non-Digital Media Disposal | DCH-08, DCH-21 |
| DCH-36 De-Identification (Anonymization) | DCH-23, PRI-05.3 |
| END-03.1 Centralized Management of Endpoint Protection Mechanisms | END-04.3, END-08.1 |
| END-03.2 Automatic Endpoint Protection Mechanism Updates | END-04.1, END-08.2 |
| IAC-07 Attribute-Based Access Control (ABAC) | IAC-15.8, IAC-29 |
| IAC-38 Cryptographic Module Authentication | CRY-02, IAC-12 |
| PRI-17 Limiting Personal Data (PD) Disclosures | PRI-01.7, SEA-09.1 |
| PRI-32 Primary Source Collection For Personal Data (PD) | DCH-22.3, PRI-04.2 |
| RSK-18 Compensating Countermeasures | BCD-07, RSK-06.2 |
| SEA-06 Defense-in-Depth (DiD) Architecture | NET-02, SEA-03 |
| SEA-27 Secure Log-On Procedures (Trusted Path) | END-09, SEA-17 |
| TDA-08.4 Identification & Justification of Ports, Protocols & Services | TDA-02.1, TDA-02.5 |
| THR-15 Insider Threat Program | IRO-02.2, THR-04 |
| AST-22 Secure Disposal, Destruction or Re-Use of Equipment | AST-09, TDA-11.2 |

**How to establish control identity across versions.** There is a deterministic procedure, and it does not require guessing:

1. Take the **legacy number** of the control you care about.
2. Look it up in the **Legacy SCF #** column of the 2026.3 Change Overview sheet (or the ERRATA tab of the workbook).
3. If it appears, that row's **SCF #** is the 2026.3 identity of the same control.
4. If it does not appear, the control was **deprecated**. Read the READ THIS sheet's deprecation table to find the **merge target** - that is where the requirement now lives.
5. Finally, read the **errata tag** on the row. It tells you whether the requirement's *content* changed, not just its number.

Step 5 is the one practitioners skip, and it is the one that bites. A control that was only *renumbered* has the same requirement text, so your existing evidence still satisfies it. A control that was *wordsmithed* may have a different test. A control that was *renamed* or *moved domains* may need your policy, crosswalk or ownership record to be rewritten even though the underlying requirement is unchanged.

> **The re-keying trap**
>
> When you re-key your GRC records, do not treat this as 'find and replace' on the number alone. A control that absorbed two legacy controls needs both legacy evidence streams merged and re-tested against the new statement - not just relabelled. And a control whose *name* changed but whose *number* did not - 27 of them in 2026.3 - will break any automation that keys on name.

### Key terms

- **Many-to-one mapping** - The case where one 2026.3 control absorbs two or more legacy controls; 22 such controls exist in 2026.3.
- **Re-keying** - Re-pointing your GRC records, evidence and crosswalks at the new control identity without changing the underlying requirement.

## 5.5 Where the Change Information Lives

_40 minutes_

Four places in the SCF tell you what changed. You need all four, because each answers a different question.

**The four authoritative sources of change information**

| Source | The question it answers |
|---|---|
| READ THIS sheet | What is the shape of the change, which controls were deprecated, and where each one went? |
| Change Overview sheet | What is the 2026.3 identity, description, legacy number and errata tag of every one of the 1,591 controls? |
| ERRATA tab of the workbook | The release-level summary of what changed in this version, with the detail behind each entry. |
| Notes column of each STRM document | How the mapping for that specific law, regulation or framework was affected by the change. |

The STRM notes column is the one most practitioners never open, and it is the one that answers the question that actually matters: *does this particular framework mapping still hold?* When NIST 800-53 R5 is re-crosswalked, the change is recorded against the mapping, not just against the control. The Council's guidance is explicit - for detailed changes, review the ERRATA tab within the SCF spreadsheet **or the notes column on the specific Set Theory Relationship Mapping document**.

The risk and threat catalogs were updated in the same release. Scroll to the right of the SCF spreadsheet and you find risks and threats mapped to individual controls as **Likely**, **Possible** or **Unlikely**. The Council positions this as *a starting point for your own customization, built to make risk management discussions more efficient* - which is an important caveat. It is a default, not a finding. Your own materiality analysis governs.

### Key terms

- **STRM notes column** - The per-mapping change record carried on each Set Theory Relationship Mapping document.
- **Likely / Possible / Unlikely** - The three-valued mapping used to connect risks and threats to individual controls.

## 5.6 Migrating Your Own Control Set

_50 minutes_

Here is the procedure. It is written to be executable on a Tuesday morning by a team that did not build the SCF and does not want to.

1. **Freeze and version your own artifacts.** Before touching anything, tag your current control set, crosswalks and policy-to-control mappings with the SCF version they were built against. A migration without a known starting version is an archaeology project.
2. **Build the crosswalk from the Legacy SCF # column.** Map every control in your set to its 2026.3 identity. Handle the three cases separately: renumbered (straight re-key), deprecated (redirect to the merge target), and new (no predecessor - decide if you now need them).
3. **Re-baseline your MCR and DSR selections.** The MSR column is the tailoring surface. Re-run your scoping decisions against the 2026.3 numbering. A control that was merely renumbered usually keeps its selection; a control that absorbed another may now carry a wider scope than your original selection reflected.
4. **Re-validate only where the content changed.** Renumbering alone does not invalidate evidence. Concentrate re-testing on controls tagged *wordsmithed*, *renamed* or *moved domains*, and on the 22 merge targets, where the statement may now test something your old evidence never covered.
5. **Re-point your crosswalks to the LRFs, not to the numbers.** Because the SCF's own mappings to NIST, ISO, CMMC and the rest are maintained by the Council, you should reference the SCF's current crosswalk rather than maintaining your own copy of a number-to-number translation. Maintain your own mapping only where you add something the SCF does not cover.
6. **Update your evidence labels, not your evidence.** Relabel folders, tickets and workpapers with the new control ID and record the legacy ID alongside it. Only re-collect where the requirement itself changed.
7. **Record the decision.** Write a short migration record: SCF version, date, the mapping you applied, the controls you re-tested and why. This is the artifact an auditor will ask for when the evidence spans two catalog versions.

Step 5 is the step that scales. Every organization that maintains its own NIST-to-SCF crosswalk is doing work the Council already does, for 250+ frameworks, four times a year. Re-point at the SCF's own mapping and you inherit the maintenance.

> **The 27 controls to watch**
>
> 27 controls in 2026.3 kept their number but were renamed, reworded, moved between domains, or absorbed a deprecated control. They are invisible to number-based diffing, so a script that compares control *numbers* between versions will report "no change" for them. Always diff the description and the errata tag, not just the identifier.

### Key terms

- **Migration record** - The dated artifact recording which SCF version a control set was re-based on and what was re-tested as a result.
- **MSR** - Minimum Security Requirements - the combined MCR + DSR selection.

## Module 5 knowledge check

What is the general release cadence of the Secure Controls Framework?

<!-- data-randomize data-max-trials="3" -->
[(X)] One update per quarter, with occasional out-of-cycle releases
[( )] One update per year
[( )] Monthly releases
[( )] Updates only when a new law or regulation is enacted
***
The stated goal is to publish on a quarterly basis - four updates a year. Out-of-cycle updates may occur, but quarterly is the general cadence.
***

How many controls in SCF 2026.3 were renumbered?

<!-- data-randomize data-max-trials="3" -->
[( )] 204
[( )] 1,511
[(X)] 1,457
[( )] 1,591
***
1,457 of the 1,511 controls that carry a legacy mapping were renumbered. 204 controls were wordsmithed, 185 renamed and 99 moved between domains.
***

Your organization tracked the legacy control NET-02 (Layered Network Defenses). Where do its requirements live in SCF 2026.3?

<!-- data-randomize data-max-trials="3" -->
[( )] NET-02 was retired with no successor
[( )] SEA-06 Defense-in-Depth (DiD) Architecture
[(X)] SEA-06 Defense-in-Depth (DiD) Architecture, which absorbed NET-02
[( )] NET-27
***
NET-02 was one of the 23 deprecated controls. It was merged into SEA-06, which is also the destination for the legacy SEA-03. Note the domain move: Network Security into Secure Engineering & Architecture.
***

Which statements about the 2026.3 reorganization are correct?

<!-- data-randomize data-max-trials="3" -->
[[X]] The 34 SCF domains are unchanged
[[X]] 23 controls were deprecated and removed
[[X]] 80 controls are new and all have a Legacy SCF # of NONE
[[ ]] Every control in the catalog was renumbered
[[ ]] The 2026.3 release changed the number of SCF domains
***
The 23 deprecations and the 80 new controls are both correct, and all 80 new controls carry a legacy value of NONE because there is nothing to map from. But renumbering was not universal - 54 controls kept their number.
***

Why does the Legacy SCF # column sometimes contain several control numbers separated by line breaks?

<!-- data-randomize data-max-trials="3" -->
[( )] It records the controls that share a common implementation
[(X)] Because one 2026.3 control absorbed two or more deprecated controls
[( )] It records the reciprocal assessment objectives
[( )] It records the control's domain migration history
***
22 controls in 2026.3 carry a multi-value legacy cell - exactly the 22 controls tagged 'merged old'. CHG-04.2, for example, absorbed END-03, CHG-04.4 and NET-15.3.
***

A control's number did not change in 2026.3, but it was tagged 'wordsmithed'. What is the correct migration action?

<!-- data-randomize data-max-trials="3" -->
[(X)] Re-validate the requirement against the new wording, because the test may have changed
[( )] Nothing - the control number is unchanged, so the evidence still stands
[( )] Treat the control as a new control with no legacy mapping
[( )] Deprecate the control and redirect it to its merge target
***
Number stability is not requirement stability. A reworded control may test something the old evidence never covered. This is why you diff descriptions and errata tags, not just identifiers.
***

# Module 6 - The SCF Web Ecosystem

Estimated effort: **5 hours**. Competency: **web**.

## Learning objectives

- Locate and download the SCF in its published formats, and navigate its tabs and download pages.

- Use the Set Theory Relationship Mapping (STRM) library to reason about coverage of a given framework.

- Apply the Risk and Threat Catalogs to a control set using the published risk test and threat test.

- Navigate the SCF Marketplace, SCF Connect, the community resources and the individual certification paths.

- State the obligations imposed by the CC BY-ND 4.0 licence that governs SCF content.

## 6.1 The SCF as a Free Web Resource

_45 minutes_

The SCF is **free**. That is a deliberate design decision by the SCF Council, not a trial or a freemium tier. The stated rationale is that the SCF helps fix the broken nature of security, compliance and resilience practices, and that a costly subscription service would exclude most organizations and defeat the broader goal.

The Council is explicit that the work is volunteer-led and sustained by sponsors. The cost model is: free content, paid services around it.

You access the SCF in one of two ways:

1. **Download the Excel version** from the SCF website - the SCF download page publishes the workbook in **XLSX, JSON and other content**; or
2. **Use a GRC tool** such as SCF Connect, or others listed on the SCF Marketplace.

The workbook is the authoritative artifact. Its tabs include the control catalog, the Assessment Objectives, the Evidence Request List, the Focal Documents, the risk and threat catalogs, the ERRATA tab, and the domains-and-principles reference. Every tab in this course was projected from one of those tabs.

> **The Excel reality**
>
> The Council is candid: the SCF is fundamentally an Excel spreadsheet, and you can use your Excel skills to manually filter the requirements. The recommended tailoring flow is: hide or delete the mapping columns for frameworks that do not apply to you, then mark an 'x' in the MCR column for must-have controls and in the DSR column for nice-to-have controls. The MSR + DSR column populates automatically. A careful organization does this filtering in a GRC tool rather than in the file, but the file remains the source of truth.

Because the SCF is free and the tooling around it is not, the economic decision most organizations reach is: use the workbook as the source, and pay for the tool that keeps your own control set, evidence and audit trail in sync with it.

### Key terms

- **SCF download** - The published SCF artifacts - XLSX, JSON and other content - offered at securecontrolsframework.com/free-content/scf-download.
- **SCF Connect** - A GRC tool built on SCF content; short-term SCF Connect access is built into SCR CAP 3PAAC services.

## 6.2 The Set Theory Relationship Mapping Library

_55 minutes_

For every law, regulation and framework the SCF covers, the Council publishes a **Set Theory Relationship Mapping (STRM)** document. This bundle contains **268** of them.

The name is the concept. Think of the SCF control set as a universal set. Each law, regulation or framework (LRF) is a subset of requirements. The STRM document is the statement of the relationship between that subset and the universal set - which SCF controls satisfy which LRF requirements, and how completely.

**STRM library coverage in this bundle**

| Dimension | Value |
|---|---|
| STRM documents in this bundle | 268 |
| Focal Documents (the LRF list) | 270 |
| Coverage | General 91, US 77, EMEA 53, APAC 36, Americas 11 (STRM) |
| Focal Document geographies | General 93, US 77, EMEA 53, APAC 36, Americas 11 |

The structure of an STRM document is consistent, and once you have read one you have read them all. Each one maps LRF requirement identifiers to SCF controls, and it carries the mapping notes that tell you how and when the mapping was made. Those notes are also where the 2026.3 change record for that particular mapping lives.

The practical value of the STRM library is that it lets you answer the coverage question in either direction:

- **Forward** - "we must comply with X. Which SCF controls do we need?" Follow the STRM for X.
- **Reverse** - "we already implement these 40 SCF controls. Which LRF requirements do they cover, and which do we still have a gap against?" Follow the crosswalk columns for those controls.

The reverse direction is the one that pays for the tool. It is the basis for building a single evidence store that serves many frameworks at once, and it is the mechanism behind the SCR CAP's metaframework claim - one conformity assessment spanning multiple laws, regulations and frameworks.

> **A caveat on the mapping itself**
>
> The Council is upfront that the control crosswalking relies on expert-derived human assessment and is not infallible. Treat an STRM mapping as a well-reasoned expert opinion, not as ground truth - and where a regulator's interpretation differs from the mapping, the regulator's interpretation governs.

### Key terms

- **STRM** - Set Theory Relationship Mapping - the per-LRF document mapping that framework's requirements to SCF controls.
- **LRF** - Law, Regulation and Framework - the SCF's term for the external requirements it maps to.

## 6.3 The Risk and Threat Catalogs

_50 minutes_

SCF 2026.3 ships two catalogs that most practitioners never open, and they are among the most immediately useful artifacts in the whole framework.

**The SCF risk and threat catalogs**

| Catalog | Contents | The test it applies |
|---|---|---|
| Risk Catalog | 65 risks in 14 risk groupings | If the control is deficient, fails, is bypassed or otherwise does not achieve its intended outcome, what adverse consequence or organizational exposure could result? |
| Threat Catalog | 45 threats - 14 natural, 31 man-made | Can this natural or man-made event cause the control to become unavailable, degraded, bypassed, ineffective or otherwise unable to achieve its intended outcome? |

The risk groupings and their sizes:

**All 65 risks by grouping**

| Risk grouping | Risks | Risk grouping | Risks |
|---|---|---|---|
| Exposure | 11 | Incident Response | 4 |
| Governance | 10 | Asset Management | 3 |
| Supply Chain | 7 | Operational Resilience | 2 |
| Access Control | 5 | Situational Awareness | 2 |
| Business Continuity | 5 | Safety | 2 |
| AI & Autonomous Technologies | 6 | Operational Technology | 1 |
| Information Protection | 6 | Personnel | 1 |

The distinction between the two tests is the point. A **risk** is what you are exposed to if the control fails - R-AC-4 Unauthorized Access, R-SC-1 through R-SC-7 for supply chain, R-AI-1 through R-AI-6 for AI and autonomous technologies. A **threat** is the event that makes the control fail - MT-2 Malicious Cyber Activity, NT-7 Pandemic (Disease) Outbreaks, MT-28 Harvest Now / Decrypt Later, MT-31 Cryptographic Compromise / Cryptanalytic Capability Advancement.

Risks carry a **NIST CSF function** classification, so you can see whether a control's risk exposure is a Protect, Recover, Identify, Respond or Govern concern. Both catalogs carry **materiality consideration** columns that prompt you against four financial thresholds:

- at least **5% of pre-tax income**;
- at least **0.5% of total assets**;
- at least **1% of total equity**; and
- at least **0.5% of total revenue**.

These thresholds are unfilled **Unknown** in the published catalog. That is deliberate - the materiality decision is the organization's to make, and the catalog provides the prompt, not the answer. The Council describes the mapping of risks and threats to individual controls as **Likely**, **Possible** or **Unlikely**, and positions it as *a starting point for your own customization*.

This is the practical payoff. Your assessor-facing findings, your risk register and your control gaps all speak the same language once you adopt the catalog's risk groupings, because a finding can be written as "deficiency in CHG-04.3 exposes the organization to R-BC-4 and R-AC-4."

### Key terms

- **Risk test** - The catalog's question about what happens when a control fails.
- **Threat test** - The catalog's question about what can make a control fail.
- **Materiality consideration** - The four financial thresholds used to prompt a materiality judgment on a risk or threat.

## 6.4 Marketplace, Community and the Professional Path

_45 minutes_

The SCF ecosystem has a commercial and a community side, and knowing where each thing lives saves time.

**The commercial and community surface of the SCF**

| Resource | What it is for |
|---|---|
| SCF Marketplace | A non-exclusive listing of security, compliance and resilience professionals who can help an organization set up or operationalize its control set. |
| SCF Discord server | Where practitioners ask questions of the Council and each other. |
| SCF Connect | A GRC tool carrying SCF content. Short-term SCF Connect access is built into SCR CAP 3PAAC services for organizations that do not already run a CAT. |
| training.securecontrolsframework.com | Individual-level training and the four individual SCF certifications. |

The Council is clear-eyed about the boundary between free and paid. *While the SCF Council gives away the SCF for free, if you want a consultant to take you through setting up or operationalizing your control set, you will have to pay for that service.*

Four individual certifications exist, each with a distinct role:

- **SCR Practitioner** - implements SCF controls that align with the SCF recommended practices and structure, and maintains an organization's security, compliance and resilience program.
- **SCR Architect** - designs SCF-based programs capable of addressing the tactical, operational and strategic needs of the organization across its People, Processes, Technologies, Data and Facilities (PPTDF-AI) considerations.
- **SCR Assessor** - works for a SCF Third-Party Assessment Organization (3PAO) to perform conformity assessments as part of the SCR CAP.
- **SCR Trainer** - works for a SCF Licensed Training Provider to deliver SCF-approved training. The Council notes this role is expected to be available in 2027.

Two more names recur, and the Council explains both. The **Cyber AB** is the Accreditation Body for the SCR CAP. The **Cyber EF** is the engagement and stewardship layer for the SCR's ecosystem. **SAICO** - the SCR Assessor and Instructor Certification Organization - certifies the individuals who do the assessing.

### Key terms

- **Cyber AB** - The Accreditation Body for the SCR CAP.
- **Cyber EF** - The engagement and stewardship layer for the SCR ecosystem.
- **SAICO** - SCR Assessor and Instructor Certification Organization.
- **3PAO** - Third-Party Assessment Organization - the firm that performs SCR CAP assessments.

## 6.5 Licensing: What CC BY-ND 4.0 Actually Requires

_50 minutes_

The SCF is copyrighted material, but it leverages the **Creative Commons Attribution-NoDerivatives 4.0 International Public License (CC BY-ND 4.0)**. The licence exists to maintain the integrity of the SCF while keeping it freely usable. Both halves of that licence create obligations, and the second one surprises people.

**Attribution.** You must give appropriate credit, provide a link to the licence, and indicate if changes were made. You may do so in any reasonable manner, but not in a way that suggests the licensor endorses you or your use. The Council's own example of adequate attribution is simple: stating that SCF controls are used in your solution - so a GRC platform that includes SCF content must say that SCF controls are used.

**NoDerivatives.** If you remix, transform, or build upon the material, you may not distribute the modified material. The Council's example of what this prohibits: leveraging SCF material to create a derivative solution such as "SCF 2.0".

> **The AI clause - read this one carefully**
>
> The NoDerivatives prohibition explicitly includes using **Artificial Intelligence (AI) or similar technologies** to leverage SCF content to generate policies, standards, procedures, metrics, risks, threats or other derivative content. This is not an incidental mention - it is a named prohibition. If you are evaluating whether a given workflow is permitted, that sentence is the governing constraint, and it applies to the content of this course as much as to the raw catalog.

What this means in practice, for four common situations:

**How the licence applies to common SCF use cases**

| Situation | Permitted? |
|---|---|
| Downloading the SCF and implementing its controls in your own environment | Yes |
| Building a GRC tool that loads SCF content and credits it | Yes, with attribution |
| Publishing a modified SCF catalog, even for free | No - that is a derivative work |
| Generating a new policy set from SCF content with AI tooling and distributing it | No - the NoDerivatives prohibition names AI transformation explicitly |

The practical takeaway for this course: the SCF is designed to be *used*, not *remixed*. Read your own licence position before you build anything commercial on top of SCF content, and read the SCF Terms & Conditions rather than working from the summary above.

### Key terms

- **CC BY-ND 4.0** - The Creative Commons Attribution-NoDerivatives 4.0 International Public Licence under which the SCF is published.
- **Attribution** - The requirement to give appropriate credit, link the licence and indicate any changes.

## 6.6 The Wider SCF Family

_45 minutes_

The SCF does not stand alone. Knowing the family tree tells you which artifact answers which question - and prevents you from reaching for a maturity model when you needed a control catalog, or vice versa.

**The three core questions the SCF family answers**

| Artifact | The question it answers | What it is |
|---|---|---|
| SCF | What? | The control catalog - 1,591 controls across 34 domains, plus AOs, ERLs and focal documents. |
| SCRMS | How? | The Secure, Compliant & Resilient Management System - how you operationalize controls, built on a Plan-Do-Check-Act cycle. |
| SCR CAP | Prove it? | The SCR Conformity Assessment Program - third-party conformity validation, with a Report on Conformity. |

Around those three sit a set of supporting artifacts:

- **CDPAS** - the Cybersecurity & Data Protection Assessment Standards, a cohesive set of standards normalizing third-party assessment, attestation and certification services. The Council quotes NIST's definition of a standard: *a document, established by consensus and approved by a recognized body, which provides for common and repeated use, rules, guidelines or characteristics for activities or their results*.
- **SCR-CMM** - the Secure, Compliant & Resilient Capability Maturity Model, with six levels (L0 Not Performed, L1 Performed Informally, L2 Planned & Tracked, L3 Well Defined, L4 Quantitatively Controlled, L5 Continuously Improving) and Maturity Level Criteria (MLC) defining reasonable staffing, technology and practice for each level.
- **C|P-RMM** - the Secure, Compliant & Resilient Risk Management Model.
- **DPMP** - the SCF Data Privacy Management Principles.
- **MADSS** - Mergers, Acquisitions & Divestitures Security Standards.
- **SCR CAP BoK and SCF Assessment Guides** - the Body of Knowledge describing 3PAAC activities, and LRF-specific assessment guidance.

The **SCRMS** is worth one more note, because its structure is the backbone of everything you will do with the catalog. It uses a **Plan-Do-Check-Act** approach:

1. **Plan** - the process of conducting due diligence. It defines the policies, standards and controls for the entity, and directly influences what tools and services get purchased.
2. **Do** - the process of conducting due care. Procedures (control activities) are where controls are actually implemented and performed.
3. **Check** - situational awareness, achieved through reporting, metrics and the results of audits and assessments.
4. **Act** - risk management: addressing real deficiencies that currently exist, and possible threats to the entity.

The same cycle appears in the maturity model, in the CAP's three-year certification lifecycle, and in the assessment methods. Learning it once pays for itself across all three.

### Key terms

- **SCRMS** - Secure, Compliant & Resilient Management System - the 'How?' of the SCR ecosystem.
- **SCR-CMM** - Secure, Compliant & Resilient Capability Maturity Model - six levels, L0 through L5.
- **MLC** - Maturity Level Criteria - the staffing, technology and practice expectations for each maturity level.
- **CDPAS** - Cybersecurity & Data Protection Assessment Standards - the standards governing 3PAAC services.

## Module 6 knowledge check

How many Set Theory Relationship Mapping (STRM) documents are in the SCF 2026.3 bundle?

<!-- data-randomize data-max-trials="3" -->
[( )] 250
[(X)] 268
[( )] 1,591
[( )] 270
***
268 STRM documents. 270 is the number of Focal Documents - the LRF list - which is a different artifact. The two do not correspond one-to-one.
***

What is the SCF's risk test?

<!-- data-randomize data-max-trials="3" -->
[(X)] If the control is deficient, fails, is bypassed or otherwise does not achieve its intended outcome, what adverse consequence or organizational exposure could result?
[( )] Can this natural or man-made event cause the control to become unavailable, degraded, bypassed or ineffective?
[( )] Does this control satisfy the requirements of the applicable law, regulation or framework?
[( )] Is the control implemented consistently across the assessed boundary?
***
That is the risk test, verbatim from the Risk Catalog. The wording you were probably thinking of - about natural or man-made events making a control ineffective - is the threat test.
***

Which facts about the SCF Risk and Threat Catalogs are correct?

<!-- data-randomize data-max-trials="3" -->
[[X]] The Risk Catalog contains 65 risks in 14 risk groupings
[[X]] The Threat Catalog contains 45 threats - 14 natural and 31 man-made
[[X]] Risks are classified against a NIST CSF function
[[ ]] The Risk Catalog contains 1,591 risks, one per control
[[ ]] The materiality thresholds are pre-filled with a dollar value for every risk
***
65 risks across 14 groupings, 45 threats split 14 natural / 31 man-made, and each risk carries a NIST CSF function. The materiality consideration columns are deliberately left as Unknown - the judgment belongs to the organization.
***

Under the SCF's CC BY-ND 4.0 licence, which activity is explicitly prohibited?

<!-- data-randomize data-max-trials="3" -->
[( )] Downloading the SCF workbook and implementing its controls internally
[( )] Building a GRC tool that includes SCF content and provides attribution
[(X)] Using AI to generate a derivative set of policies from SCF content and distributing it
[( )] Implementing SCF controls in your own environment and stating that SCF controls are used
***
The NoDerivatives prohibition explicitly extends to using AI or similar technologies to leverage SCF content to generate policies, standards, procedures, metrics, risks or threats. Attribution and internal implementation are both permitted.
***

Which artifact answers the question "How do we operationalize the controls?"

<!-- data-randomize data-max-trials="3" -->
[( )] The SCF control catalog
[(X)] The SCRMS - the Secure, Compliant & Resilient Management System
[( )] The STRM library
[( )] The Evidence Request List
***
The SCF answers 'What?', the SCRMS answers 'How?', and the SCR CAP answers 'Prove it?'. The SCRMS is built on a Plan-Do-Check-Act cycle.
***

How many individual-level SCF certifications are described, and which one performs conformity assessments for a 3PAO?

<!-- data-randomize data-max-trials="3" -->
[( )] Three certifications; the SCR Trainer performs the assessments
[(X)] Four certifications; the SCR Assessor performs the assessments
[( )] Four certifications; the SCR Architect performs the assessments
[( )] Five certifications; the SCR Practitioner performs the assessments
***
Four: SCR Practitioner, SCR Architect, SCR Assessor and SCR Trainer (the last expected in 2027). The SCR Assessor works for a SCF 3PAO performing SCR CAP conformity assessments.
***

# Module 7 - Conformity Assessment & Capstone

Estimated effort: **7 hours**. Competency: **documents**.

## Learning objectives

- Describe the SCR Conformity Assessment Program, its actors and the assessment boundary concept.

- Apply the four control-level designations and the roll-up rule that turns AO findings into a control status.

- Distinguish the four conformity designations and the numeric thresholds that separate them.

- Select an assessment rigor level and an assessment method appropriate to the control set being assessed.

- Scope an assessment boundary using the ten zones of the Unified Scoping Guide.

- Produce the capstone Assessment Report and Control Matrix and defend them against the rubric.

## 7.1 What Conformity Assessment Is, and Who Does It

_55 minutes_

A control catalog tells you what good looks like. **Conformity assessment** is the activity of demonstrating, to an independent party, that the controls are actually implemented and operating for a defined scope. The SCF's answer to that question is the **Secure, Compliant & Resilient Conformity Assessment Program (SCR CAP)**.

The SCR CAP is an **organization-level** conformity assessment. It uses the SCF's metaframework nature so that one assessment can span multiple laws, regulations and frameworks at once - rather than running three separate audits against three separate control sets. The Council is explicit that this is what distinguishes the SCR CAP from single-focused certifications such as ISO 27001, CMMC or FedRAMP.

**The actors in the SCR CAP**

| Role | Who they are |
|---|---|
| OSA | Organization Seeking Assessment - the organization being assessed. |
| 3PAAC | Third-Party Assessment, Attestation and Certification Services - the service category. |
| 3PAO | Third-Party Assessment Organization - the company that performs the assessment. |
| SCR Assessor | The individual who performs assessment work for a 3PAO. |
| ATL | Assessment Team Lead - the 3PAO individual assigned to lead the assessment team. |
| ATE | Assessment Technical Expert - a team member with the subject matter expertise for a specific part of the assessment, reporting to the ATL. |
| SAICO | SCR Assessor and Instructor Certification Organization - the body that certifies SCR Assessors and 3PAOs. |
| Cyber AB | The Accreditation Body for the SCR CAP. |

The output of a conformity assessment is the **Report on Conformity (ROC)**, presented in two formats:

- The **Technical Assessment Report (TAR)** - comprehensive and technical, not meant to be shared externally because it may contain sensitive controls information for internal audiences only; and
- The **Executive Assessment Report (EAR)** - a high-level overview ideal for sharing with clients and other third parties.

The SCF Control Assurance Tool (CAT) platform generates the SCF Council-approved TAR and EAR reports on completion of the assessment. The Council and the Cyber AB control the formatting for all SCR CAP report formats.

Two operating models sit alongside the point-in-time assessment:

**CICA - Continuous Incremental Conformity Assessment** is an alternative to a point-in-time assessment that reflects the realities of continuous change within organizations. It uses an incremental methodology, similar in concept to how incremental backups augment a full backup to provide an efficient way to ensure data is protected: instead of reassessing each control, CICA focuses on the parts of the environment or control set that have **changed** since the last full or incremental assessment. This lets an organization adopt a monthly, quarterly or annual assessment cadence that focuses on change, and it means a full assessment is required only every three years.

**CASA - Continuous Assurance & Situational Awareness** allows third-party visibility of security, compliance and resilience control conformity and potential risk exposure. It is the distributed architecture through which CATs operate as the automated mechanism.

### Key terms

- **OSA** - Organization Seeking Assessment.
- **3PAAC** - Third-Party Assessment, Attestation and Certification Services.
- **ROC** - Report on Conformity - the assessment output, delivered as a TAR and an EAR.
- **CICA** - Continuous Incremental Conformity Assessment - a change-focused alternative to point-in-time assessment.
- **CASA** - Continuous Assurance & Situational Awareness - third-party visibility into control conformity.
- **CAT** - Control Assurance Tool - the platform 3PAOs use to perform assessments and generate the TAR and EAR.

## 7.2 Control-Level Designations

_55 minutes_

Assessment findings land at two levels. First, each **Assessment Objective** is designated. Then the AO findings roll up into a **control** designation. Getting this hierarchy right is the difference between a defensible report and a spreadsheet of opinions.

There are **four** possible control-level designations:

**The four control-level designations in the SCR CAP**

| Designation | Polarity | Meaning |
|---|---|---|
| Satisfactory | Positive | All applicable AOs are Satisfactory, N/A, or a compensating control that is validated as applicable, reasonable, and implemented and operating properly. |
| Deficient | Negative | One or more applicable AOs are Deficient, or a compensating control cannot be validated as applicable, reasonable, and implemented and operating properly. |
| Compensating Control | Neutral | Another control, or controls, sufficiently reduce the risk associated with the control, and the compensating control is validated as applicable, reasonable, and implemented and operating properly. |
| Not Applicable (N/A) | Neutral | The control, or AO, does not apply. |

The roll-up rule is simple and absolute:

**For a SCF control to be designated as Satisfactory, each of the control's applicable AOs must be designated as Satisfactory, Compensating Control, or N/A.** One Deficient AO makes the whole control Deficient.

That is why the **AO sheet is the working unit of assessment**, not the control. The 6,446 Assessment Objectives and their SCF Defined Parameters are what you actually test. The control is the reporting unit.

A **compensating control** is an alternative set of controls implemented in lieu of the deficient control, providing equivalent or comparable protection. For it to be validated, three conditions must hold:

1. It is **Applicable** - it addresses the same risk in the same context;
2. It is **Reasonable** - it is proportionate and appropriate for the risk; and
3. It is **Implemented and operating properly** - it exists and works, not merely on paper.

A control that is itself deficient is **not capable of having compensating controls**. You cannot compensate a failure with another failure.

> **The re-evaluation window**
>
> A control designated as Deficient may be re-evaluated **during the course of the assessment and for up to ten (10) business days following the active assessment period**, provided that additional evidence is available to demonstrate the control is satisfied, that evidence cannot change or limit the effectiveness of other requirements already scored Satisfactory, and the ROC has not yet been delivered to the OSA. That window is short, deliberate, and closes when the ROC is delivered.

### Key terms

- **Satisfactory** - Positive control designation - all applicable AOs satisfied.
- **Deficient** - Negative control designation - one or more applicable AOs failed.
- **Compensating Control** - Neutral designation - an alternative control validated as applicable, reasonable and operating properly.
- **Roll-up rule** - The rule that a control is Satisfactory only if every applicable AO is Satisfactory, Compensating Control or N/A.

## 7.3 Conformity Designations and the Numeric Thresholds

_55 minutes_

At the assessment boundary level, the 3PAO produces a written ROC defending a single **conformity designation**. There are four, and they are separated by hard numeric thresholds on the percentage of assessed controls meeting the criteria.

**The four conformity designations and their thresholds**

| Designation | Threshold | Outcome |
|---|---|---|
| Strictly Conforms | 100% of assessed controls | Passing |
| Conforms | at least 80% | Passing |
| Significant Deficiency | at least 70%, but less than 80% | Failing |
| Material Weakness | less than 70% | Failing |

**Strictly Conforms** is the positive outcome where one hundred percent of the assessed controls have reasonable evidence to conclude that the controls are met and operational, that any control designated N/A is validated as such by the SCR Assessor, and that any compensating controls are validated as applicable, reasonable, and implemented and operating properly.

**Conforms** is the same test at 80% or above, with one additional condition: any assessed control deficiency is **not material** to the OSA's cybersecurity and data privacy program.

**Significant Deficiency** is a negative outcome indicating **limited conformity** due to a systemic problem within the OSA's program. It requires that at least 70% but less than 80% of assessed controls meet the criteria, and that the program has systemic problems inherent in the overall function of a team, department, project, application, service and/or vendor rather than a specific isolated factor - requiring **limited changes to personnel, technology and/or practices** to correct the deficient controls.

**Material Weakness** is the negative outcome where the OSA cannot demonstrate conformity. It covers the case where one or more **material controls** is deficient.

All four designations - including the passing ones - require that the assessed controls provide reasonable assurance that the OSA's cybersecurity and data privacy program provides adequate security, where it:

- adheres to a **defined and documented risk tolerance**;
- **mitigates material** cybersecurity and/or data privacy risks;
- is **designed to detect and protect against material** cybersecurity and/or data privacy threats; and
- is **prepared to respond to material** incidents.

This last block is the part that surprises people. You cannot pass a conformity assessment on control implementation alone. The program has to be coherent - a documented risk tolerance, risk mitigation, threat detection and protection, and incident response readiness. That is why the SCF catalog contains 37 governance controls and 48 compliance controls: they are not paperwork, they are the substrate the designation rests on.

> **Weighting the threshold**
>
> The percentages apply to **assessed controls** - the controls you put in scope, not all 1,591. Scoping is therefore not an administrative step; it determines the number the designation is computed from. And because the SCF weights controls from 1 to 10, with a 10 being a material or key control whose absence is a material weakness, the composition of your assessed set matters as much as its size.

### Key terms

- **Strictly Conforms** - Passing designation requiring 100% of assessed controls to meet the criteria.
- **Conforms** - Passing designation requiring at least 80% of assessed controls to meet the criteria.
- **Significant Deficiency** - Failing designation indicating limited conformity due to a systemic program problem (70% to under 80%).
- **Material Weakness** - Failing designation where the OSA cannot demonstrate conformity (under 70%).
- **Material control** - A control the SCF weights at 10 - the absence of which is considered a material weakness.

## 7.4 Assessment Rigor and Assessment Methods

_50 minutes_

Two independent axes determine the depth of an assessment: **rigor** (how deep the assessor goes) and **method** (how the evidence is obtained). The BoK is explicit that at the discretion of the OSA and by agreement of the 3PAO, any method may use any level of rigor - but it also states the prescribed pairing, and that pairing is what you will see in practice.

**The prescribed rigor and method pairings**

| Rigor level | Method | Basis |
|---|---|---|
| Standard | MPIT - Manual Point In Time | Manual evaluation at a specific point in time. |
| Enhanced | APIT - Automated Point In Time | Automation augments a traditional assessment, comparing desired state to current state via machine-readable configurations and/or assessment evidence. |
| Comprehensive | AEHR - Automated Evidence with Human Review | Ongoing continuous assessment, with recurring human review validating automated results. |

The three methods in detail:

**MPIT (Manual Point In Time)** is the traditional assessment methodology. It is relevant to a specific point in time - the time at which the control was evaluated - and the assessment is performed by people.

**APIT (Automated Point In Time)** uses automation to augment a traditional assessment methodology, comparing the desired state of conformity against the current state via machine-readable configurations and/or assessment evidence. It is still relevant to a point in time, but in situations where technology cannot evaluate evidence, the evidence is manually reviewed - and the combined output of automated and manual reviews of artifacts is used to derive a finding.

**AEHR (Automated Evidence with Human Review)** is used for ongoing, continuous control assessments. AAT continuously evaluates controls by comparing the desired state of conformity against the current state through machine-readable configurations and/or assessment evidence, and recurring human reviews evaluate the legitimacy of the automated results and validate the automated evidence review process to derive a finding.

The **rigor** levels describe the depth of understanding obtained:

- **Standard rigor** provides a level of understanding of the administrative, technical and physical security and/or data protection controls that represents sufficient due care in the evaluation of those controls.
- **Enhanced rigor** provides a deeper level of understanding and is appropriate for APIT, where automation carries more of the evidentiary load and therefore requires more validation.
- **Comprehensive rigor** provides the deepest level of understanding and is appropriate for AEHR, where the assessment is continuous and human review is validating automated output on a recurring basis.

The **Statement of Work (SOW)** between the 3PAO and the OSA is expected to capture the assessment method, because that establishes the context for expected assessor involvement and related costs. A 3PAO may offer a single method - MPIT alone is acceptable - but must have procedures developed for each method it offers.

> **The CICA connection**
>
> The methods are not only about depth - they are about cadence. AEHR is the engine behind CICA, and the assumption behind the triennial assessment is that on the tri-annual assessment, controls monitored by automation will require minimal scrutiny, based on the historical evidence of conformity during the certification period. The intent is to reduce the financial and labour burden of re-establishing the conformity baseline every three years.

### Key terms

- **MPIT** - Manual Point In Time - the traditional, people-performed point-in-time assessment.
- **APIT** - Automated Point In Time - automation augmented with manual review where technology cannot evaluate evidence.
- **AEHR** - Automated Evidence with Human Review - continuous assessment with recurring human validation.
- **SOW** - Statement of Work between the 3PAO and the OSA, expected to capture the assessment method.

## 7.5 Scoping the Assessment Boundary with the USG

_45 minutes_

The assessment boundary is the population the percentage thresholds are computed over, so scoping is the highest-leverage decision in the whole engagement. The SCR CAP **recognizes the Unified Scoping Guide (USG) as the authoritative guidance for determining scope**, and the USG shall be used to define the scope of the SCR CAP for an OSA and the assessment boundary.

The USG is a free resource intended to help organizations define the scope of the sensitive and regulated data where it applies. It organizes that scope into **ten zones**.

**The ten USG scoping zones**

| Zone | Name | What it captures |
|---|---|---|
| 1 | Sensitive Data Assets (SDA) | Systems, services and applications that directly process, store or transmit sensitive/regulated data. |
| 2 | Segmenting | Segmenting systems that provide access - firewalls, hypervisors and similar. |
| 3 | Security Tools | Security tools that directly impact the integrity of zone 1 and zone 2 assets. |
| 4 | Connected | Connected systems - embedded technologies, applications and supporting infrastructure. |
| 5 | Out-of-Scope | Systems completely isolated from the sensitive/regulated data in scope. |
| 6 | Enterprise-Wide | The organization's overall corporate security program - cyber and physical. |
| 7 | External Service Provider (ESP) | Supply-chain security and the flow down of requirements to suppliers. |
| 8 | Subcontractors | Third-party organizations party to the ESPs in scope. |
| 9 | Cloud Service Providers (CSP) | CSPs, a specialized form of ESP. |
| 10 | Technology Dependencies | Technology-based dependency relationships for in-scope assets. |

Note what zone 5 does. It is not a gap - it is the *declared* out-of-scope set, and it is the artifact that proves you considered isolation rather than assuming it. And note that zones 6 through 9 pull enterprise-wide governance and the full supply chain into the boundary, which is exactly what makes the SCR CAP a multi-framework assessment rather than a single-product one.

The USG also distinguishes between **Person Entities (PE)** and **Non-Person Entities (NPE)** - devices, applications, service accounts and AI agents. In 2026.3 an AI agent is an NPE, and the agent-specific controls in the AAT domain give you the hooks to treat it as one.

### Key terms

- **USG** - Unified Scoping Guide - the authoritative scoping guidance recognized by the SCR CAP.
- **SDA** - Sensitive Data Assets - USG zone 1.
- **PE / NPE** - Person Entity / Non-Person Entity - the USG's distinction between people and everything else that holds an identity.

## 7.6 The Three-Year Certification Lifecycle

_45 minutes_

A SCR Certified certification runs for **three years** from the date of the ROC. The lifecycle is structured so that the burden is front-loaded, not back-loaded.

**The SCR Certified three-year certification lifecycle**

| Year | What is required |
|---|---|
| Year 1 | Ongoing due care activities to maintain conformity - ongoing maintenance, change management, managing compliance requirements. The date of the ROC starts the lifecycle. |
| Year 2 | Ongoing due care activities, plus - no later than the first anniversary of the ROC date - an internal assessment and a self-attestation that the OSA continues to conform with applicable controls. |
| Year 3 | Ongoing due care activities, plus - no later than the second anniversary of the ROC date - an internal assessment and a self-attestation that the OSA continues to conform with applicable controls. |
| End of Year 3 | The original certification expires. A new third-party assessment by a SCR 3PAO is required to issue a new SCR Certified certification. |

Throughout the lifecycle, it remains the OSA's responsibility to ensure applicable controls are implemented and governed to maintain conformity. The certification does not delegate the organization's obligations; it periodically tests them.

The mechanism that can interrupt a certification is a **significant change**. The SCR CAP identifies **three tiers of change**:

- **Normal Change** - normal operational activity: routine operational, administrative, maintenance or technology change that does not reasonably alter the assessment boundary, applicable controls, control applicability, control implementation, control ownership or inheritance, risk conditions, or the continued representativeness of the assessment evidence. Routine patching, normal vulnerability remediation, like-for-like hardware replacement, ordinary employee turnover, firewall-rule maintenance, certificate renewal, normal cloud scaling, and routine configuration changes under established change management all sit here.
- **Material Change** - has the reasonable potential to affect the basis for certification. It requires a documented impact analysis. Where the impact analysis shows the boundary, controls, operation, ownership and risk conditions remain materially consistent and the evidence remains sufficient, the certification may remain valid.
- **Significant Change** - actually affects that basis sufficiently that continued reliance on the certification is no longer justified. A material scoping error discovered after certification, discovery of a Material Weakness, a change in certification applicability, a material change in the workforce operating model, material governance restructuring, replacement of common controls, or material outsourcing of controls are all examples.

Where the impact analysis shows that one or more of the material-change conditions are no longer satisfied to the extent that the previous conformity determination cannot reasonably be relied upon, the change is classified as a Significant Change and the Significant Change requirements apply.

> **Version discipline meets certification**
>
> This is where Module 5 and Module 7 meet. A significant change includes a material scoping error discovered after certification - and an SCF version upgrade that changes the assessed control set is a scoping question. The 2026.3 reorganization renumbered 1,457 controls and deprecated 23 others. If your certified assessment boundary was defined against 2026.2 control numbers, you need a documented impact analysis showing that the assessed control set remains materially equivalent - not a silent re-key.

### Key terms

- **Normal Change** - Routine change that does not reasonably alter the basis for the certification decision.
- **Material Change** - Change with the reasonable potential to affect the basis for certification; requires a documented impact analysis.
- **Significant Change** - Change that actually affects the basis for certification sufficiently that continued reliance is no longer justified.

## 7.7 Your Capstone

_60 minutes_

The capstone is the culminating assessment of the course, and it is a real piece of professional work rather than a quiz. The problem statement is direct: **design and implement a control assessment for an organization.**

**Capstone deliverables and weighting**

| Deliverable | Format | Weight |
|---|---|---|
| Assessment Report | document | 50% |
| Control Matrix | code | 50% |

The **Assessment Report** is your conformity assessment document. It should contain a scope and assessment boundary, the control set with its AO-level designations, the resulting control-level and conformity-level designations, the evidence basis, and the findings. The **Control Matrix** is the machine-readable spine underneath it - the mapping from controls to Assessment Objectives to evidence to findings, in a form an assessor or a script can consume.

The evaluation rubric has a single criterion, **Accuracy**, weighted at 100%, with four levels mapped onto the mastery levels:

**The capstone rubric - criterion: Accuracy**

| Mastery level | Rubric level | What it means |
|---|---|---|
| Beginning | Errors | The assessment contains material factual errors. |
| Developing | Partial | The assessment is partially correct but incomplete or inconsistently applied. |
| Proficient | Good | The assessment is correct and applied consistently. |
| Exemplary | Excellent | The assessment is correct, complete, and the reasoning is defensible to an assessor. |

Accuracy is the whole rubric, which tells you where to spend your effort. A beautifully written report that mis-states a control number, mis-applies a designation or mis-computes a threshold scores Errors. Verify every identifier and every number against the source sheets before you submit.

The capstone is also a collaborative assessment:

- **Peer review is enabled, with a minimum of two reviewers.** Your work is reviewed by at least two peers before it is graded.
- **Self-reflection** is part of the deliverable - reflect on learning.
- **A defense presentation is required**: 15 minutes, before a **panel of three**.

The mastery threshold for the capstone is **70**. The capstone carries 30% of the course grade; the summative exam carries 40% at a threshold of 70, and the formative quizzes carry 30% at a threshold of 60. Retakes are allowed, with a maximum of three attempts.

A capstone that scores well tends to share four properties, and they are all discipline rather than brilliance:

1. **Every control identifier and count is verified against the source sheets** - 1,591 controls, 6,446 AOs, 422 ERLs, 270 focal documents, 268 STRM documents, 65 risks, 45 threats.
2. **The scope is stated using the USG zones**, so the assessed set is explicit and defensible before any finding is written.
3. **The AO-level designations are shown**, not just the control-level roll-up, because that is where the evidence actually is.
4. **The conformity designation is computed from the published thresholds**, with the arithmetic visible: 100% / 80% / 70%.

### Key terms

- **Capstone** - The course's culminating project - an Assessment Report (50%) and a Control Matrix (50%).
- **Control Matrix** - The machine-readable mapping of controls to Assessment Objectives, evidence and findings.
- **Defense presentation** - A required 15-minute presentation to a panel of three.

## 7.8 Capstone Clinic

_55 minutes_

This session is working time with the rubric in front of you. Use it to close the gaps that the rubric is most likely to expose.

**Self-check against the source.** Before your peer review, confirm each of these against the bundled sheets rather than from memory:

- The control identifiers you cite exist in the 2026.3 catalog, and the number of controls in your scoped set matches the number you state.
- Every AO you cite exists for the control you cite it under.
- Every ERL you request exists, and its Area of Focus is stated correctly.
- Every focal document and STRM you rely on is one of the 270 / 268, and you have not attributed a mapping to the wrong framework.
- Any risk or threat you cite exists in the Risk / Threat Catalogs, with the correct grouping.
- Any 2026.3 change you reference - a renumbering, a merge target, a deprecated control - matches the Change Overview and READ THIS sheets exactly.

**Check your designations against the rules.** Two failure modes account for most inaccurate capstone reports:

1. **Roll-up errors.** A control marked Satisfactory where one applicable AO is Deficient. Walk your AO designations up to the control and back down again.
2. **Threshold errors.** Conforming at 78%, or calling a 100% result Significant Deficiency. The four thresholds are 100 / 80 / 70 and they do not have gaps in them.

**Peer review with intent.** Your two reviewers are not there to approve. Give them a specific instruction - for example, "verify every control identifier and the conformity arithmetic" - and ask them for findings, not a verdict. The peer review step is the cheapest error-detection mechanism in the whole course, and it is skipped most often by people who then discover the same error in the defense.

**The defense is a technical defense.** Fifteen minutes, three panellists, and the questions will be about *why* - why this scope, why this designation, why this evidence is sufficient, why this risk applies to this control. Every claim in your report should be one you can source and one you can defend. That is the entire standard.

> **One closing rule**
>
> The capstone is an **assessment of an organization you design**, not a redistribution of SCF content. Build your report, matrix and supporting artifacts around the SCF - cite it, credit it, point to it - but do not publish a modified SCF catalog, a generated SCF-derived policy library, or a transformed copy of the SCF sheets. The NoDerivatives licence in Module 6 applies to your capstone deliverables as much as it applies to the framework.

### Key terms

- **Self-check** - The pre-peer-review verification pass against the bundled source sheets.
- **Peer review** - A review by a minimum of two peers, conducted before grading.

## Module 7 knowledge check

A control has three applicable Assessment Objectives. One is Satisfactory, one is Compensating Control, and one is Deficient. What is the control-level designation?

<!-- data-randomize data-max-trials="3" -->
[( )] Satisfactory
[( )] Compensating Control
[(X)] Deficient
[( )] Not Applicable
***
A control is Satisfactory only if every applicable AO is Satisfactory, Compensating Control or N/A. A single Deficient AO makes the whole control Deficient.
***

An assessment finds that 78% of the assessed controls meet the conformity criteria. What is the conformity designation?

<!-- data-randomize data-max-trials="3" -->
[( )] Strictly Conforms
[( )] Conforms
[(X)] Significant Deficiency
[( )] Material Weakness
***
Significant Deficiency covers at least 70% but less than 80%. 78% falls in that band. Conforms requires at least 80%; Strictly Conforms requires 100%.
***

Which statements about a compensating control are correct?

<!-- data-randomize data-max-trials="3" -->
[[X]] It must be validated as applicable, reasonable, and implemented and operating properly
[[X]] It cannot itself be a deficient control
[[X]] It provides equivalent or comparable protection to the deficient control
[[ ]] It removes the requirement to test the underlying control's AOs
[[ ]] It must be a control from a different SCF domain
***
The three validation conditions and the equivalent-or-comparable protection test come straight from the BoK. A deficient control cannot be used to compensate, and there is no cross-domain requirement.
***

Which assessment method is characterized by continuous evaluation with recurring human review validating automated results?

<!-- data-randomize data-max-trials="3" -->
[( )] MPIT
[( )] APIT
[(X)] AEHR
[( )] CICA
***
AEHR - Automated Evidence with Human Review - is the continuous method and pairs with Comprehensive rigor. CICA is the incremental assessment cadence built on top of automated evidence, not a method itself.
***

What is the deadline for re-evaluating a control designated Deficient with additional evidence?

<!-- data-randomize data-max-trials="3" -->
[( )] Any time before the ROC is published
[( )] Within 30 business days of the assessment
[(X)] During the assessment and for up to ten business days after the active assessment period
[( )] There is no re-evaluation window
***
The window is during the assessment and up to ten business days following the active assessment period - and only while the ROC has not yet been delivered to the OSA.
***

Which are the capstone's deliverables and requirements?

<!-- data-randomize data-max-trials="3" -->
[[X]] An Assessment Report worth 50%
[[X]] A Control Matrix worth 50%
[[X]] A 15-minute defense presentation to a panel of three
[[X]] Peer review by a minimum of two reviewers
[[ ]] A published tool conforming to the SCF's own CC BY-ND 4.0 NoDerivatives restriction
[[ ]] A 40-page written examination
***
The two deliverables carry 50% each, and the defense and peer review are both required. The scoring is done by your peers and the panel, not by a published tool - and the CC BY-ND restriction is a licence constraint on the SCF content, not a grading instrument.
***

# Module 8 - Risk & Threat Catalogs

Estimated effort: **4 hours**. Competency: **catalog**.

## Learning objectives

- Explain why the SCF publishes risk and threat catalogs alongside the control catalog.

- Name the 14 risk groupings and the total number of cataloged risks.

- Distinguish the 14 natural threats from the 31 man-made threats.

- Map a risk to the controls that address it using the STRM relationship.

- Use the risk and threat catalogs to justify a control's inclusion in a Living Control Set.

## 8.1 Why a Risk and Threat Catalog

_40 minutes_

A control catalog tells you what to do. A risk and threat catalog tells you why the control exists and what it is defending against. The SCF publishes both.

The SCF 2026.3 release catalogs 65 risks grouped into 14 risk groupings, and 45 threats split into 14 natural threats and 31 man-made threats.

- 65 risks in 14 groupings.
- 45 threats: 14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31).
- Each risk and threat is cross-mapped to SCF controls through Set Theory Relationship Mapping.

### Key terms

- **Risk grouping** - A category collecting related risks.
- **Natural threat** - Threat from natural phenomena - 14 cataloged.
- **Man-made threat** - Threat from human action - 31 cataloged.

## 8.2 The 14 Risk Groupings

_45 minutes_

The 65 risks are distributed across 14 groupings. Exposure and Governance dominate.

**Risk distribution across 14 groupings (65 total)**

| # | Risk grouping | Risks |
|---|---|---|
| 1 | Exposure | 11 |
| 2 | Governance | 10 |
| 3 | Supply Chain | 7 |
| 4 | AAT | 6 |
| 5 | Information Protection | 6 |
| 6 | Access Control | 5 |
| 7 | Business Continuity | 5 |
| 8 | Incident Response | 4 |
| 9 | Asset Management | 3 |
| 10 | Operational Resilience | 2 |
| 11 | Situational Awareness | 2 |
| 12 | Safety | 2 |
| 13 | Operational Technology | 1 |
| 14 | Personnel | 1 |

### Key terms

- **Risk** - A potential event negatively impacting an objective.

## 8.3 The 45 Threats

_40 minutes_

The SCF catalogs 45 threats split into two families.

**Threat families in SCF 2026.3**

| Family | Count | Identifier range |
|---|---|---|
| Natural | 14 | NT-1 to NT-14 |
| Man-made | 31 | MT-1 to MT-31 |

Man-made threats are more than twice natural. Natural threats still matter for BCD and PES domains.

### Key terms

- **Natural threat** - NT-1 to NT-14.
- **Man-made threat** - MT-1 to MT-31.

## 8.4 From Risk to Control: The Justification Loop

_45 minutes_

The loop that turns a tailored control set into a defensible one.

1. Name the risk from the catalog (one of 65, in one of 14 groupings).
2. Name the threat that realizes it (one of 45).
3. Find the controls that address the pair via STRM or domain structure.
4. Record the justification: risk, threat, control, evidence.

**The risk-to-control justification loop**

| Step | Artifact | Output |
|---|---|---|
| 1 | Risk catalog | Named risk + grouping |
| 2 | Threat catalog | Named threat + family |
| 3 | Control catalog / STRM | Control identifier(s) |
| 4 | Living Control Set | Risk -> threat -> control -> evidence row |

### Key terms

- **Justification** - Traceable link from risk and threat to control and evidence.

## Module 8 knowledge check

How many risks does the SCF 2026.3 catalog contain, and into how many groupings?

<!-- data-randomize data-max-trials="3" -->
[( )] 45 risks in 14 groupings
[( )] 65 risks in 5 groupings
[(X)] 65 risks in 14 groupings
[( )] 31 risks in 14 groupings
***
65 risks across 14 groupings. 45 is the threat count.
***

Which risk grouping is the largest?

<!-- data-randomize data-max-trials="3" -->
[( )] Governance (10)
[( )] Supply Chain (7)
[(X)] Exposure (11)
[( )] Information Protection (6)
***
Exposure has 11 risks.
***

How are the 45 cataloged threats split?

<!-- data-randomize data-max-trials="3" -->
[( )] 22 natural and 23 man-made
[(X)] 14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31)
[( )] 31 natural and 14 man-made
[( )] 14 natural and 14 man-made
***
14 natural, 31 man-made.
***

Which statements about the risk and threat catalogs are correct?

<!-- data-randomize data-max-trials="3" -->
[[X]] They are part of the free SCF 2026.3 published material
[[X]] They are cross-mapped to SCF controls using STRM
[[X]] They provide the vocabulary for justifying a control's inclusion
[[ ]] They are only available via subscription
[[ ]] They replace the need for a separate risk assessment
***
Free, CC BY-ND 4.0, cross-mapped via STRM. They support but don't replace risk assessment.
***

Which risk grouping contains exactly one risk?

<!-- data-randomize data-max-trials="3" -->
[( )] Operational Resilience
[( )] Situational Awareness
[(X)] Operational Technology (and Personnel)
[( )] Safety
***
Two groupings have a single risk: Operational Technology and Personnel.
***

An organization wants to justify a control not driven by external obligation. Which catalog supports this?

<!-- data-randomize data-max-trials="3" -->
[( )] The Focal Document index
[(X)] The risk and threat catalogs
[( )] The Evidence Request List
[( )] The STRM document
***
DSR controls are justified by internal risk appetite. Risk/threat catalogs are the vocabulary.
***

# Module 9 - Assessment Practice & the Capstone

Estimated effort: **5 hours**. Competency: **documents**.

## Learning objectives

- Explain the difference between control-level and conformity-level designations.

- State the four control designations and the four conformity designations with their thresholds.

- Describe the three assessment methods and their rigor pairings.

- Explain the re-evaluation window and when a compensating control is acceptable.

- Describe the three-year certification lifecycle and the capstone deliverables.

## 9.1 Control-Level vs Conformity-Level Designations

_45 minutes_

Two designation systems: control-level (single control) and conformity-level (whole assessment).

**The two designation systems**

| Level | Designations | What it describes |
|---|---|---|
| Control | Satisfactory / Deficient / Compensating Control / N/A | Whether one control's AOs are met. |
| Conformity | Strictly Conforms / Conforms / Significant Deficiency / Material Weakness | Percentage of controls meeting criteria. |

A control is Satisfactory only if every applicable AO is Satisfactory, Compensating Control, or N/A.

### Key terms

- **Control-level designation** - Satisfactory/Deficient/Compensating/N/A for one control.
- **Conformity-level designation** - Strictly Conforms/Conforms/Sig Def/Material Weakness for the whole assessment.

## 9.2 Conformity Thresholds

_40 minutes_

Four conformity designations defined by percentage of assessed controls meeting criteria.

**Conformity designations and thresholds**

| Designation | Threshold | Meaning |
|---|---|---|
| Strictly Conforms | 100% | Every assessed control meets the criteria. |
| Conforms | >= 80% | At least 80% of assessed controls meet the criteria. |
| Significant Deficiency | >= 70% and < 80% | A material gap requiring remediation. |
| Material Weakness | < 70% | A serious failure of the control environment. |

### Key terms

- **Material Weakness** - A conformity designation below 70%.

## 9.3 Assessment Rigor and Methods

_50 minutes_

Two independent dimensions: rigor (how deep) and method (how evidence is gathered).

**Assessment rigor levels**

| Rigor | Depth | Typical use |
|---|---|---|
| Standard | Baseline testing | Routine surveillance assessments. |
| Enhanced | Deeper testing with more evidence | Higher-risk controls. |
| Comprehensive | Continuous, automated, human-reviewed | Critical/material controls. |

**Assessment methods**

| Method | Abbrev | Character | Typical pairing |
|---|---|---|---|
| Manual Performance of Independent Testing | MPIT | Point-in-time human testing | Standard or Enhanced |
| Automated Performance of Independent Testing | APIT | Automated testing at a point in time | Standard or Enhanced |
| Automated Evidence with Human Review | AEHR | Continuous automated with human review | Comprehensive |
| Continuous Independent Conformity Assessment | CICA | Incremental on automated evidence | Any |

### Key terms

- **MPIT** - Manual point-in-time testing.
- **APIT** - Automated point-in-time testing.
- **AEHR** - Continuous automated with human review.
- **CICA** - Incremental on automated evidence.

## 9.4 Re-evaluation and Compensating Controls

_45 minutes_

Two mechanisms keep an assessment honest: the re-evaluation window and compensating controls.

> **Re-evaluation window**
>
> A Deficient control can be re-evaluated with additional evidence during the assessment and for up to 10 business days after - only while ROC not yet delivered.

A compensating control must be: applicable, reasonable, and implemented and operating properly.

### Key terms

- **Re-evaluation window** - During assessment + up to 10 business days, before ROC delivery.
- **Compensating control** - Alternative providing equivalent/comparable protection.

## 9.5 The Three-Year Certification Lifecycle

_40 minutes_

An SCR CAP certification runs on a three-year cycle.

**Three-year certification lifecycle**

| Year | Activity | Deadline |
|---|---|---|
| Year 1 | Full conformity assessment, ROC issued | Assessment start |
| Year 2 | Self-attestation by OSA | First anniversary |
| Year 3 | Self-attestation by OSA | Second anniversary |
| End of Year 3 | Certification expires | End of third year |

### Key terms

- **Self-attestation** - Signed statement by OSA that control environment has not degraded.

## 9.6 Your Capstone

_60 minutes_

The capstone has two deliverables weighted equally, plus defense and peer review.

**Capstone deliverables**

| Deliverable | Format | Weight |
|---|---|---|
| Assessment Report | Document | 50% |
| Control Matrix | Spreadsheet/code | 50% |

- Defense presentation: 15 minutes to a panel of three.
- Peer review: minimum two reviewers.
- Rubric: Accuracy (Errors/Partial/Good/Excellent) at 100% weight.
- Mastery threshold: 70%.

> **Evaluation framework**
>
> Formative 30% (threshold 60), Summative 40% (threshold 70), Capstone 30% (threshold 70). Retakes allowed, max 3 attempts.

### Key terms

- **Capstone** - The graded end-of-course project.
- **Peer review** - Review by min 2 peers.

## Module 9 knowledge check

A control has 3 applicable AOs: Satisfactory, Compensating, Deficient. Designation?

<!-- data-randomize data-max-trials="3" -->
[( )] Satisfactory
[( )] Compensating Control
[(X)] Deficient
[( )] N/A
***
A single Deficient AO makes the whole control Deficient.
***

78% of controls meet criteria. Conformity designation?

<!-- data-randomize data-max-trials="3" -->
[( )] Strictly Conforms
[( )] Conforms
[(X)] Significant Deficiency
[( )] Material Weakness
***
Significant Deficiency = 70-<80%. 78% falls in that band.
***

Which statements about compensating controls are correct?

<!-- data-randomize data-max-trials="3" -->
[[X]] Must be applicable, reasonable, and implemented/operating
[[X]] Cannot be a deficient control
[[X]] Provides equivalent/comparable protection
[[ ]] Removes requirement to test underlying AOs
[[ ]] Must be from different domain
***
Three validation conditions from the BoK.
***

Which method is continuous with recurring human review?

<!-- data-randomize data-max-trials="3" -->
[( )] MPIT
[( )] APIT
[(X)] AEHR
[( )] CICA
***
AEHR pairs with Comprehensive rigor.
***

Deadline for re-evaluating a Deficient control?

<!-- data-randomize data-max-trials="3" -->
[( )] Any time before ROC published
[( )] Within 30 business days
[(X)] During assessment + up to 10 business days after
[( )] No re-evaluation window
***
Window closes when ROC delivered to OSA.
***

Capstone deliverables and requirements?

<!-- data-randomize data-max-trials="3" -->
[[X]] Assessment Report 50%
[[X]] Control Matrix 50%
[[X]] 15-min defense to panel of 3
[[X]] Peer review min 2 reviewers
[[ ]] Published tool per CC BY-ND
[[ ]] 40-page written exam
***
Two deliverables 50% each, defense and peer review required.
***

# Module 10 - Audit, Evidence & Capstone Execution

Estimated effort: **4 hours**. Competency: **documents, sheets**.

## Learning objectives

- Explain the eight-phase SCF lifecycle from focal documents to capstone mastery.

- Map an evidence request (ERL) to its assessment objectives and controls.

- Apply the audit observation tagging convention to a finding.

- Describe the conformity assessment execution and reporting process.

- Complete the capstone deliverables to the published rubric.

## 10.1 The Eight-Phase SCF Lifecycle

_40 minutes_

The SCF lifecycle runs from source frameworks to certified mastery.

**The eight-phase SCF lifecycle**

| Phase | Name | Key artifacts | Audit tag |
|---|---|---|---|
| 0 | Source frameworks | Focal Documents (270), STRM crosswalks | [FD-<FDI>] |
| 1 | Control catalog | 1,591 controls, 34 domains, SCR-CMM L0-L5 | [CTL-<ID>] |
| 2 | Tailoring | Living Control Set (MCR/DSR) | [LCS], [TAILOR] |
| 3 | Scoping | USG zones 1-10 | [ZONE-<n>] |
| 4 | Assessment objectives | 6,446 AOs, SDP, rigor | [AO-<ID>] |
| 5 | Evidence | 422 ERLs, 30 areas of focus | [ERL-<n>] |
| 6 | Risk & threat | 65 risks, 14 groupings, 45 threats | [RISK-<id>], [THR-<id>] |
| 7 | Assessment execution | Designations, ROC, certification | [CTL-DESIG], [CONF-DESIG] |
| 8 | Capstone & mastery | Assessment Report, Control Matrix, defense | [CAP-REPORT], [CAP-MATRIX] |

### Key terms

- **Lifecycle phase** - One of eight phases from source frameworks to mastery.
- **Audit tag** - Standardized tag for tagging evidence and observations.

## 10.2 Audit Observation Tagging Convention

_45 minutes_

Every audit finding is tagged with a standard structure for traceability.

```text
[AUDIT-OBSERVATION]
  Evidence ID:      ERL-<n> / AO-<id> / CTL-<id>
  Phase:            0-8
  Status:           Provided | Missing | Partial | N/A
  Observation:      <finding text>
  Risk ref:         [RISK-<id>] [RG-<name>]
  Threat ref:       [THR-<id>] [NT/MT-<n>]
  Designation:      [CTL-DESIG] / [CONF-DESIG]
  Gap/Remediation:  <action required>
```

> **Disposition codes**
>
> P = Pass, F = Fail, CC = Compensating Control, NA = Not Applicable, PND = Pending.

### Key terms

- **Disposition** - P/F/CC/NA/PND.
- **ROC** - Report of Conformity.

## 10.3 Conformity Assessment Execution

_50 minutes_

The SCR CAP assessment runs in a fixed sequence.

1. Scoping - define boundary using USG (zones 1-10).
2. Control selection - identify in-scope controls from tailored LCS.
3. AO review - pull AOs; note SDP minimums.
4. Evidence collection - request artifacts per ERL; record method.
5. Testing - MPIT/APIT/AEHR at Standard/Enhanced/Comprehensive rigor.
6. Control designation - Satisfactory/Deficient/Compensating/N/A per control.
7. Conformity designation - Strictly Conforms/Conforms/Sig Def/Material Weakness.
8. ROC delivery - Report of Conformity issued to OSA.
9. Certification - 3-year cycle: Year 1 full, Year 2 self-attest, Year 3 self-attest.

### Key terms

- **OSA** - Organization Seeking Assessment.
- **CAB** - Conformity Assessment Body.

## 10.4 Capstone: Assessment Report & Control Matrix

_60 minutes_

The capstone has two deliverables weighted equally, plus defense and peer review.

**Capstone deliverables**

| Deliverable | Format | Weight | Key content |
|---|---|---|---|
| Assessment Report | Document | 50% | Scope, methodology, findings, designations, recommendations |
| Control Matrix | Spreadsheet/code | 50% | Control-to-evidence mapping, AO results, dispositions |

- Defense: 15 minutes to panel of 3.
- Peer review: min 2 reviewers.
- Rubric: Accuracy (Errors/Partial/Good/Excellent) at 100% weight.
- Mastery threshold: 70%.

> **Evaluation framework**
>
> Formative 30% (threshold 60), Summative 40% (threshold 70), Capstone 30% (threshold 70). Retakes allowed, max 3 attempts.

### Key terms

- **Capstone** - The graded end-of-course project.
- **Peer review** - Review by min 2 peers.

## 10.5 Capstone Examples: Student Submissions

_30 minutes_

Anonymized examples from a cohort of ten students who completed the capstone.

**Sample capstone cohort (10 students)**

| Student | Assessment Report | Control Matrix | Overall | Result |
|---|---|---|---|---|
| Alice Chen | 92 | 88 | 90 | Pass |
| Bob Martinez | 78 | 72 | 75 | Pass |
| Carol Johnson | 95 | 91 | 93 | Pass |
| David Park | 68 | 62 | 65 | Fail |
| Eve Williams | 85 | 80 | 82.5 | Pass |
| Frank Lee | 60 | 55 | 57.5 | Fail |
| Grace Kim | 88 | 84 | 86 | Pass |
| Henry Brown | 72 | 68 | 70 | Pass |
| Ivy Taylor | 90 | 86 | 88 | Pass |
| Jack Wilson | 65 | 60 | 62.5 | Fail |

Three patterns emerged:

1. High performers (Alice, Carol, Ivy, Grace) scored above 85 on both. Their reports clearly mapped each control to evidence; their matrices included AO-to-evidence traceability.
2. Borderline passes (Bob, Eve, Henry) scored 70-85. Common gap: Control Matrix listed controls but omitted reciprocal AO references.
3. Failures (David, Frank, Jack) scored below 70. Root causes: (1) reports describing controls without citing evidence, (2) matrices including controls outside the assessment boundary.

**Sample peer review scores**

| Submission | Reviewer 1 | Reviewer 2 | Avg Peer Score |
|---|---|---|---|
| Alice Chen | 92 | 88 | 90 |
| Carol Johnson | 94 | 90 | 92 |
| David Park | 65 | 60 | 62.5 |
| Jack Wilson | 58 | 55 | 56.5 |

**Sample defense presentation scores (panel of 3)**

| Submission | Panel 1 | Panel 2 | Panel 3 | Avg Defense |
|---|---|---|---|---|
| Alice Chen | 95 | 92 | 90 | 92.3 |
| Carol Johnson | 96 | 94 | 92 | 94 |
| David Park | 68 | 65 | 62 | 65 |
| Jack Wilson | 60 | 58 | 55 | 57.7 |

> **Learning from failure**
>
> The most common capstone failure is not lack of knowledge but lack of traceability. An Assessment Report that says 'GOV-01 is implemented' without citing the evidence artifact, the AO it satisfies, and the collection method is a report an assessor cannot verify.

### Key terms

- **Traceability** - The ability to trace a control claim to its evidence, AO and collection method.
- **Peer review** - Review by min 2 peers, required for submission.

## Module 10 knowledge check

How many phases does the SCF lifecycle have?

<!-- data-randomize data-max-trials="3" -->
[( )] 5
[( )] 7
[(X)] 9 (phases 0-8)
[( )] 12
***
Eight phases numbered 0-8.
***

Which disposition code indicates a compensating control was accepted?

<!-- data-randomize data-max-trials="3" -->
[( )] P
[( )] F
[(X)] CC
[( )] NA
***
P=Pass, F=Fail, CC=Compensating Control, NA=Not Applicable, PND=Pending.
***

Which are the capstone deliverables and requirements?

<!-- data-randomize data-max-trials="3" -->
[[X]] Assessment Report 50%
[[X]] Control Matrix 50%
[[X]] 15-min defense to panel of 3
[[X]] Peer review min 2 reviewers
[[ ]] Published tool per CC BY-ND
[[ ]] 40-page written exam
***
Two deliverables 50% each, defense and peer review required.
***

In which order does the conformity assessment execute?

<!-- data-randomize data-max-trials="3" -->
[( )] Evidence -> scoping -> testing -> ROC
[(X)] Scoping -> control selection -> AO review -> evidence -> testing -> designation -> ROC -> certification
[( )] Testing -> scoping -> evidence -> designation
[( )] Certification -> ROC -> testing -> scoping
***
Scoping comes first (USG zones).
***

Conformity designation for 75% of controls meeting criteria?

<!-- data-randomize data-max-trials="3" -->
[( )] Conforms
[(X)] Significant Deficiency
[( )] Material Weakness
[( )] Strictly Conforms
***
Significant Deficiency = 70-<80%.
***

Re-evaluation window for a Deficient control?

<!-- data-randomize data-max-trials="3" -->
[( )] Any time before ROC published
[( )] Within 30 business days
[(X)] During assessment + up to 10 business days after
[( )] No re-evaluation window
***
Window closes when ROC delivered to OSA.
***
