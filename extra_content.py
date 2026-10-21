# -*- coding: utf-8 -*-
"""Extra course content for the SCF-2026.3 LiAScript expansion.

Sourced from the verified facts in
D:\\Secure Controls Framework\\scf_lms_bundle_v2 (read-only). No content invented.
Appended to the base 7 modules at build time.
"""
import sys, os
sys.path.insert(0, r"D:\Secure Controls Framework\scf_lms_bundle_v2\build")
# reuse the block helpers by importing them from the bundle's course_content
import importlib.util
spec = importlib.util.spec_from_file_location("cc", r"D:\Secure Controls Framework\course_content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)
H, P, UL, OL, TBL, NOTE, CODE, Q = cc.H, cc.P, cc.UL, cc.OL, cc.TBL, cc.NOTE, cc.CODE, cc.Q


MODULE_8 = {
    "id": 8,
    "slug": "risk-threat-catalogs",
    "title": "Risk & Threat Catalogs",
    "hours": 4,
    "competencies": ["catalog"],
    "objectives": [
        "Explain why the SCF publishes risk and threat catalogs alongside the control catalog.",
        "Name the 14 risk groupings and the total number of cataloged risks.",
        "Distinguish the 14 natural threats from the 31 man-made threats.",
        "Map a risk to the controls that address it using the STRM relationship.",
        "Use the risk and threat catalogs to justify a control's inclusion in a Living Control Set.",
    ],
    "lessons": [
        {
            "id": "8.1",
            "title": "Why a Risk and Threat Catalog",
            "minutes": 40,
            "blocks": [
                P("A control catalog tells you what to do. A risk and threat catalog tells you why the control "
                  "exists and what it is defending against. The SCF publishes both, and the relationship between "
                  "them is what makes a control set defensible rather than a checklist."),
                P("The SCF 2026.3 release catalogs **65 risks** grouped into **14 risk groupings**, and "
                  "**45 threats** split into **14 natural threats** and **31 man-made threats**. These are the "
                  "same risks and threats the SCF's controls are written to address, and they are the vocabulary "
                  "the SCF Council uses when it explains why a control carries the weight it does."),
                NOTE("Source of truth",
                     "Every figure in this module is taken from the SCF-2026.3 risk-catalog.md and "
                     "threat-catalog.md sheets in the OKF bundle. The risk and threat catalogs are part of the "
                     "SCF's free published material under CC BY-ND 4.0."),
                UL([
                    "**65 risks** in **14 groupings**.",
                    "**45 threats**: 14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31).",
                    "Each risk and threat is cross-mapped to SCF controls through the same Set Theory "
                    "Relationship Mapping used for focal documents.",
                ]),
            ],
            "terms": [
                ("Risk grouping", "A category that collects related risks, e.g. Exposure, Governance, Supply Chain."),
                ("Natural threat", "A threat arising from natural phenomena - 14 cataloged, NT-1 to NT-14."),
                ("Man-made threat", "A threat arising from human action - 31 cataloged, MT-1 to MT-31."),
            ],
        },
        {
            "id": "8.2",
            "title": "The 14 Risk Groupings",
            "minutes": 45,
            "blocks": [
                P("The 65 risks are distributed across 14 groupings. The distribution is itself informative: "
                  "Exposure and Governance dominate, which mirrors where most organizations actually lose control "
                  "of their posture."),
                TBL(["#", "Risk grouping", "Risks"], [
                    ["1", "Exposure", "11"],
                    ["2", "Governance", "10"],
                    ["3", "Supply Chain", "7"],
                    ["4", "Artificial Intelligence & Autonomous Technologies", "6"],
                    ["5", "Information Protection", "6"],
                    ["6", "Access Control", "5"],
                    ["7", "Business Continuity", "5"],
                    ["8", "Incident Response", "4"],
                    ["9", "Asset Management", "3"],
                    ["10", "Operational Resilience", "2"],
                    ["11", "Situational Awareness", "2"],
                    ["12", "Safety", "2"],
                    ["13", "Operational Technology", "1"],
                    ["14", "Personnel", "1"],
                ], caption="Risk distribution across the 14 groupings (65 risks total)"),
                P("Three observations carry into scoping work:"),
                OL([
                    "**Exposure (11) is the largest grouping** - it captures the risks that come from being "
                    "visible and reachable, which is where most external-facing controls earn their weight.",
                    "**Governance (10) is close behind** - governance failures are the second-most-common "
                    "source of material weakness, which is why GOV-domain controls carry weight 10 so often.",
                    "**Supply Chain (7)** reflects the SCF Council's view that third-party risk is now a "
                    "first-class concern, not an appendix to internal controls.",
                ]),
            ],
            "terms": [
                ("Risk", "A potential event or condition that, if it occurs, negatively impacts an objective."),
                ("Exposure", "The largest risk grouping - risks arising from being visible and reachable."),
            ],
        },
        {
            "id": "8.3",
            "title": "The 45 Threats: Natural and Man-Made",
            "minutes": 40,
            "blocks": [
                P("The SCF catalogs 45 threats, split into two families. The split matters because the controls "
                  "that address a natural threat (flood, earthquake, pandemic) are different in kind from those "
                  "that address a man-made one (insider, attacker, vendor failure)."),
                TBL(["Family", "Count", "Identifier range", "Examples of scope"], [
                    ["Natural", "14", "NT-1 to NT-14", "Weather, geological, biological, environmental events"],
                    ["Man-made", "31", "MT-1 to MT-31", "Insider, external attacker, vendor, process failure, error"],
                ], caption="Threat families in the SCF 2026.3 catalog"),
                P("The man-made family is more than twice the size of the natural family, which is consistent "
                  "with where most organizations' actual loss events come from. The natural family still matters "
                  "because it drives the Business Continuity and Physical & Environmental Security domains, and "
                  "because a control set that ignores natural threats cannot claim resilience."),
                NOTE("Using the catalogs",
                     "When you justify a control's inclusion to an assessor or to a board, the risk and threat "
                     "catalogs are the vocabulary. 'This control addresses risk X, which is in grouping Y, "
                     "and threat Z (man-made, MT-n)' is a defensible, auditable sentence."),
            ],
            "terms": [
                ("Natural threat", "NT-1 to NT-14 - phenomena such as weather, geology, biology."),
                ("Man-made threat", "MT-1 to MT-31 - human action, error or intent."),
            ],
        },
        {
            "id": "8.4",
            "title": "From Risk to Control: The Justification Loop",
            "minutes": 45,
            "blocks": [
                P("The reason the catalogs exist is to close the loop between a risk statement and a control. "
                  "The loop has four steps and it is the same loop the SCF Council uses when it adds or "
                  "renumbers controls."),
                OL([
                    "**Name the risk** from the catalog (one of the 65, in one of the 14 groupings).",
                    "**Name the threat** that realizes it (one of the 45, natural or man-made).",
                    "**Find the controls** that address the risk/threat pair, using the STRM crosswalk or the "
                    "domain structure of the catalog.",
                    "**Record the justification** in your Living Control Set: risk, threat, control, evidence.",
                ]),
                P("This loop is what turns a tailored control set into a defensible one. A control that cannot "
                  "be traced to a risk and a threat in the catalog is a control you are running on habit, and "
                  "habit is not evidence."),
                TBL(["Step", "Artifact", "Output"], [
                    ["1", "Risk catalog", "Named risk + grouping"],
                    ["2", "Threat catalog", "Named threat + family"],
                    ["3", "Control catalog / STRM", "Control identifier(s)"],
                    ["4", "Living Control Set (LCS)", "Risk -> threat -> control -> evidence row"],
                ], caption="The risk-to-control justification loop"),
            ],
            "terms": [
                ("Living Control Set (LCS)", "The tailored, maintained control set an organization actually runs."),
                ("Justification", "The traceable link from a risk and threat to a control and its evidence."),
            ],
        },
    ],
    "questions": [
        Q("m8q1", "single",
          "How many risks does the SCF 2026.3 catalog contain, and into how many groupings?",
          [("Wrong", "45 risks in 14 groupings"),
           ("Wrong", "65 risks in 5 groupings"),
           ("Correct", "65 risks in 14 groupings"),
           ("Wrong", "31 risks in 14 groupings")],
          explain="65 risks across 14 groupings. 45 is the threat count, not the risk count.",
          competency="catalog"),
        Q("m8q2", "single",
          "Which risk grouping is the largest in the SCF 2026.3 catalog?",
          [("Wrong", "Governance (10)"),
           ("Wrong", "Supply Chain (7)"),
           ("Correct", "Exposure (11)"),
           ("Wrong", "Information Protection (6)")],
          explain="Exposure has 11 risks, Governance 10, Supply Chain 7. Exposure captures risks arising from "
                  "being visible and reachable.",
          competency="catalog"),
        Q("m8q3", "single",
          "How are the 45 cataloged threats split between natural and man-made?",
          [("Wrong", "22 natural and 23 man-made"),
           ("Correct", "14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31)"),
           ("Wrong", "31 natural and 14 man-made"),
           ("Wrong", "14 natural and 14 man-made")],
          explain="14 natural threats (NT-1..NT-14) and 31 man-made threats (MT-1..MT-31). Man-made threats are "
                  "more than twice as numerous, which matches where most loss events originate.",
          competency="catalog"),
        Q("m8q4", "multi",
          "Which statements about the risk and threat catalogs are correct?",
          [("Correct", "They are part of the free SCF 2026.3 published material"),
           ("Correct", "They are cross-mapped to SCF controls using Set Theory Relationship Mapping"),
           ("Correct", "They provide the vocabulary for justifying a control's inclusion"),
           ("Wrong", "They are only available to organizations paying for an SCF subscription"),
           ("Wrong", "They replace the need for a separate risk assessment")],
          explain="The catalogs are free, CC BY-ND 4.0 published material, cross-mapped via STRM. They support "
                  "but do not replace an organization's own risk assessment.",
          competency="catalog"),
        Q("m8q5", "single",
          "An organization wants to justify running a control that is not driven by any external obligation. "
          "Which catalog best supports that justification?",
          [("Wrong", "The Focal Document index"),
           ("Correct", "The risk and threat catalogs"),
           ("Wrong", "The Evidence Request List"),
           ("Wrong", "The STRM document for that control")],
          explain="DSR controls are justified by internal risk appetite, and the risk/threat catalogs are the "
                  "vocabulary for that justification. Focal documents and STRMs support MCR, not DSR.",
          competency="catalog"),
        Q("m8q6", "single",
          "Which risk grouping contains exactly one risk?",
          [("Wrong", "Operational Resilience"),
           ("Wrong", "Situational Awareness"),
           ("Correct", "Operational Technology (and Personnel)"),
           ("Wrong", "Safety")],
          explain="Two groupings contain a single risk: Operational Technology (1) and Personnel (1). Safety has 2, "
                  "Situational Awareness has 2, Operational Resilience has 2.",
          competency="catalog"),
    ],
}

MODULE_9 = {
    "id": 9,
    "slug": "assessment-practice",
    "title": "Assessment Practice & the Capstone",
    "hours": 5,
    "competencies": ["documents"],
    "objectives": [
        "Explain the difference between control-level and conformity-level designations.",
        "State the four control designations and the four conformity designations with their thresholds.",
        "Describe the three assessment methods and their rigor pairings.",
        "Explain the re-evaluation window and when a compensating control is acceptable.",
        "Describe the three-year certification lifecycle and the capstone deliverables.",
    ],
    "lessons": [
        {
            "id": "9.1",
            "title": "Control-Level vs Conformity-Level Designations",
            "minutes": 45,
            "blocks": [
                P("Two different designation systems are used in a conformity assessment, and confusing them is "
                  "the most common source of misreported results. **Control-level** designations describe a single "
                  "control. **Conformity-level** designations describe the whole assessment."),
                TBL(["Level", "Designations", "What it describes"], [
                    ["Control", "Satisfactory / Deficient / Compensating Control / N/A",
                     "Whether one control's AOs are met."],
                    ["Conformity", "Strictly Conforms / Conforms / Significant Deficiency / Material Weakness",
                     "The percentage of controls that meet the criteria."],
                ], caption="The two designation systems"),
                P("A control is **Satisfactory** only if every applicable Assessment Objective is Satisfactory, "
                  "Compensating Control or N/A. A single Deficient AO makes the whole control Deficient. The "
                  "conformity designation is then computed from the count of Satisfactory controls."),
            ],
            "terms": [
                ("Control-level designation", "Satisfactory / Deficient / Compensating Control / N/A for one control."),
                ("Conformity-level designation", "Strictly Conforms / Conforms / Significant Deficiency / Material Weakness for the whole assessment."),
            ],
        },
        {
            "id": "9.2",
            "title": "Conformity Thresholds",
            "minutes": 40,
            "blocks": [
                P("The four conformity designations are defined by the percentage of assessed controls that meet "
                  "the conformity criteria. The thresholds are fixed and published in the CAP body of knowledge."),
                TBL(["Designation", "Threshold", "Meaning"], [
                    ["Strictly Conforms", "100%", "Every assessed control meets the criteria."],
                    ["Conforms", ">= 80%", "At least 80% of assessed controls meet the criteria."],
                    ["Significant Deficiency", ">= 70% and < 80%", "A material gap requiring remediation."],
                    ["Material Weakness", "< 70%", "A serious failure of the control environment."],
                ], caption="Conformity designations and their thresholds"),
                NOTE("Reporting consequence",
                     "A Significant Deficiency or Material Weakness designation is not a private finding. It is "
                     "reported to the OSA and, depending on the SCR CAP terms, may be reportable to regulators "
                     "or to the OSA's customers under contractual obligations."),
            ],
            "terms": [
                ("OSA", "Organization Seeking Assessment - the entity being assessed."),
                ("Material Weakness", "A conformity designation below 70% of assessed controls meeting criteria."),
            ],
        },
        {
            "id": "9.3",
            "title": "Assessment Rigor and Methods",
            "minutes": 50,
            "blocks": [
                P("Every assessment has two independent dimensions: **rigor** (how deep) and **method** (how "
                  "evidence is gathered). Any method can be used with any rigor; the published pairings are "
                  "guidance, not constraints."),
                TBL(["Rigor", "Depth", "Typical use"], [
                    ["Standard", "Baseline testing of the control", "Routine surveillance assessments."],
                    ["Enhanced", "Deeper testing with more evidence", "Higher-risk controls or new implementations."],
                    ["Comprehensive", "Continuous, automated, human-reviewed", "Critical / material controls."],
                ], caption="Assessment rigor levels"),
                TBL(["Method", "Abbreviation", "Character", "Typical rigor pairing"], [
                    ["Manual Performance of Independent Testing", "MPIT", "Point-in-time human testing",
                     "Standard or Enhanced"],
                    ["Automated Performance of Independent Testing", "APIT", "Automated testing at a point in time",
                     "Standard or Enhanced"],
                    ["Automated Evidence with Human Review", "AEHR", "Continuous automated with recurring human review",
                     "Comprehensive"],
                ], caption="Assessment methods and their character"),
                P("The practical consequence: an assessor can run a Comprehensive assessment using MPIT if the "
                  "circumstances warrant it, and the BoK does not prohibit it. The pairing table is guidance for "
                  "planning, not a rule."),
            ],
            "terms": [
                ("MPIT", "Manual Performance of Independent Testing - point-in-time human testing."),
                ("APIT", "Automated Performance of Independent Testing - automated testing at a point in time."),
                ("AEHR", "Automated Evidence with Human Review - continuous automated with recurring human review."),
                ("CICA", "Continuous Independent Conformity Assessment - incremental assessment built on automated evidence."),
            ],
        },
        {
            "id": "9.4",
            "title": "Re-evaluation and Compensating Controls",
            "minutes": 45,
            "blocks": [
                P("Two mechanisms keep an assessment honest after the first pass: the **re-evaluation window** and "
                  "**compensating controls**."),
                NOTE("Re-evaluation window",
                     "A control designated Deficient can be re-evaluated with additional evidence during the "
                     "assessment and for up to ten business days following the active assessment period - and "
                     "only while the Report of Conformity (ROC) has not yet been delivered to the OSA. After "
                     "delivery, the designation stands."),
                P("A **compensating control** is an alternative control implemented in lieu of the deficient one "
                  "that provides equivalent or comparable protection. Three conditions must hold:"),
                UL([
                    "It is **applicable** to the deficiency.",
                    "It is **reasonable** in the circumstances.",
                    "It is **implemented and operating properly** - not merely planned.",
                ]),
                P("A deficient control cannot itself be used as a compensating control, and there is no "
                  "cross-domain requirement. For a material control, a compensating control must be validated by "
                  "the assessor and cannot simply be asserted by the organization."),
            ],
            "terms": [
                ("Re-evaluation window", "During the assessment plus up to 10 business days after, before ROC delivery."),
                ("Compensating control", "An alternative control providing equivalent or comparable protection."),
                ("ROC", "Report of Conformity - the deliverable of a conformity assessment."),
            ],
        },
        {
            "id": "9.5",
            "title": "The Three-Year Certification Lifecycle",
            "minutes": 40,
            "blocks": [
                P("An SCR CAP certification runs on a three-year cycle. The cycle exists to balance assurance "
                  "depth with cost: a full assessment in year one, lighter checks in years two and three, then "
                  "re-assessment."),
                TBL(["Year", "Activity", "Deadline"], [
                    ["Year 1", "Full conformity assessment, Report of Conformity issued", "Assessment start"],
                    ["Year 2", "Self-attestation by the OSA", "First anniversary of assessment start"],
                    ["Year 3", "Self-attestation by the OSA", "Second anniversary of assessment start"],
                    ["End of Year 3", "Certification expires", "End of the third year"],
                ], caption="The three-year certification lifecycle"),
                P("The self-attestations in years two and three are not free passes: they are signed statements "
                  "by the OSA that the control environment has not materially degraded since the last assessment. "
                  "A material change in the environment during the cycle is what triggers an out-of-cycle "
                  "re-assessment."),
            ],
            "terms": [
                ("Self-attestation", "A signed statement by the OSA that the control environment has not materially degraded."),
                ("Out-of-cycle re-assessment", "A re-assessment triggered by a material change during the cycle."),
            ],
        },
        {
            "id": "9.6",
            "title": "Your Capstone",
            "minutes": 60,
            "blocks": [
                P("The capstone is the graded instrument for this course. It has two deliverables, weighted "
                  "equally, plus a defense presentation and peer review."),
                TBL(["Deliverable", "Format", "Weight"], [
                    ["Assessment Report", "Document", "50%"],
                    ["Control Matrix", "Code / spreadsheet", "50%"],
                ], caption="Capstone deliverables"),
                UL([
                    "**Defense presentation**: 15 minutes to a panel of three assessors.",
                    "**Peer review**: minimum of two reviewers per submission.",
                    "**Rubric**: a single criterion, Accuracy, scored on four levels - Errors, Partial, Good, "
                    "Excellent - at 100% weight.",
                    "**Mastery threshold**: 70%.",
                ]),
                P("The capstone is assessed at the course level, not per module. It is the instrument that "
                  "turns the seven modules of theory into a demonstrated capability, and it is what the "
                  "certification record attaches to."),
                NOTE("Evaluation framework reminder",
                     "The course evaluation framework weights three components: Formative 30% (threshold 60), "
                     "Summative 40% (threshold 70), Capstone 30% (threshold 70). Retakes are allowed, with a "
                     "maximum of three attempts."),
            ],
            "terms": [
                ("Capstone", "The graded end-of-course project: Assessment Report + Control Matrix + defense."),
                ("Peer review", "Review by a minimum of two peers, required for capstone submission."),
            ],
        },
    ],
    "questions": [
        Q("m9q1", "single",
          "A control has three applicable Assessment Objectives: one Satisfactory, one Compensating Control, "
          "and one Deficient. What is the control-level designation?",
          [("Wrong", "Satisfactory"),
           ("Wrong", "Compensating Control"),
           ("Correct", "Deficient"),
           ("Wrong", "Not Applicable")],
          explain="A control is Satisfactory only if every applicable AO is Satisfactory, Compensating Control "
                  "or N/A. A single Deficient AO makes the whole control Deficient.",
          competency="documents"),
        Q("m9q2", "single",
          "An assessment finds that 78% of assessed controls meet the conformity criteria. What is the "
          "conformity designation?",
          [("Wrong", "Strictly Conforms"),
           ("Wrong", "Conforms"),
           ("Correct", "Significant Deficiency"),
           ("Wrong", "Material Weakness")],
          explain="Significant Deficiency covers at least 70% but less than 80%. 78% falls in that band.",
          competency="documents"),
        Q("m9q3", "multi",
          "Which statements about a compensating control are correct?",
          [("Correct", "It must be validated as applicable, reasonable, and implemented and operating properly"),
           ("Correct", "It cannot itself be a deficient control"),
           ("Correct", "It provides equivalent or comparable protection to the deficient control"),
           ("Wrong", "It removes the requirement to test the underlying control's AOs"),
           ("Wrong", "It must be a control from a different SCF domain")],
          explain="The three validation conditions and the equivalent-or-comparable protection test come from "
                  "the BoK. A deficient control cannot compensate, and there is no cross-domain requirement.",
          competency="documents"),
        Q("m9q4", "single",
          "Which assessment method is characterized by continuous evaluation with recurring human review "
          "validating automated results?",
          [("Wrong", "MPIT"),
           ("Wrong", "APIT"),
           ("Correct", "AEHR"),
           ("Wrong", "CICA")],
          explain="AEHR - Automated Evidence with Human Review - is the continuous method and pairs with "
                  "Comprehensive rigor. CICA is the incremental cadence built on automated evidence, not a method.",
          competency="documents"),
        Q("m9q5", "single",
          "What is the deadline for re-evaluating a control designated Deficient with additional evidence?",
          [("Wrong", "Any time before the ROC is published"),
           ("Wrong", "Within 30 business days of the assessment"),
           ("Correct", "During the assessment and for up to ten business days after the active assessment period"),
           ("Wrong", "There is no re-evaluation window")],
          explain="The window is during the assessment and up to ten business days after - and only while the "
                  "ROC has not yet been delivered to the OSA.",
          competency="documents"),
        Q("m9q6", "multi",
          "Which are the capstone's deliverables and requirements?",
          [("Correct", "An Assessment Report worth 50%"),
           ("Correct", "A Control Matrix worth 50%"),
           ("Correct", "A 15-minute defense presentation to a panel of three"),
           ("Correct", "Peer review by a minimum of two reviewers"),
           ("Wrong", "A published tool conforming to the SCF's CC BY-ND 4.0 restriction"),
           ("Wrong", "A 40-page written examination")],
          explain="The two deliverables carry 50% each, and the defense and peer review are both required. The "
                  "CC BY-ND restriction is a licence constraint on SCF content, not a grading instrument.",
          competency="documents"),
    ],
}


MODULE_10 = {
    "id": 10,
    "slug": "audit-evidence-capstone",
    "title": "Audit, Evidence & Capstone Execution",
    "hours": 4,
    "competencies": ["documents", "sheets"],
    "objectives": [
        "Explain the eight-phase SCF lifecycle from focal documents to capstone mastery.",
        "Map an evidence request (ERL) to its assessment objectives and controls.",
        "Apply the audit observation tagging convention to a finding.",
        "Describe the conformity assessment execution and reporting process.",
        "Complete the capstone deliverables to the published rubric.",
    ],
    "lessons": [
        {
            "id": "10.1",
            "title": "The Eight-Phase SCF Lifecycle",
            "minutes": 40,
            "blocks": [
                P("The SCF lifecycle runs from source frameworks to certified mastery. Eight phases, each with "
                  "its own artifacts, identifiers and audit checkpoints."),
                TBL(["Phase", "Name", "Key artifacts", "Audit tag"], [
                    ["0", "Source frameworks", "Focal Documents (270), STRM crosswalks", "[FD-<FDI>]"],
                    ["1", "Control catalog", "1,591 controls, 34 domains, SCR-CMM L0-L5", "[CTL-<ID>]"],
                    ["2", "Tailoring", "Living Control Set (MCR/DSR), compensating controls", "[LCS], [TAILOR]"],
                    ["3", "Scoping", "USG zones 1-10, assessment boundary", "[ZONE-<n>]"],
                    ["4", "Assessment objectives", "6,446 AOs, SDP, PPTDF, rigor", "[AO-<ID>]"],
                    ["5", "Evidence", "422 ERLs, 30 areas of focus, collection methods", "[ERL-<n>]"],
                    ["6", "Risk & threat", "65 risks, 14 groupings, 45 threats", "[RISK-<id>], [THR-<id>]"],
                    ["7", "Assessment execution", "Control/conformity designations, ROC, certification", "[CTL-DESIG], [CONF-DESIG]"],
                    ["8", "Capstone & mastery", "Assessment Report, Control Matrix, defense, peer review", "[CAP-REPORT], [CAP-MATRIX]"],
                ], caption="The eight-phase SCF lifecycle"),
            ],
            "terms": [
                ("Lifecycle phase", "One of eight phases from source frameworks to certified mastery."),
                ("Audit tag", "Standardized tag for tagging evidence and observations."),
            ],
        },
        {
            "id": "10.2",
            "title": "Audit Observation Tagging Convention",
            "minutes": 45,
            "blocks": [
                P("Every audit finding is tagged with a standard structure so findings are traceable, "
                  "comparable and reportable. The convention covers the full lifecycle."),
                CODE("text", """[AUDIT-OBSERVATION]
  Evidence ID:      ERL-<n> / AO-<id> / CTL-<id>
  Phase:            0-8
  Status:           Provided | Missing | Partial | N/A
  Observation:      <finding text>
  Risk ref:         [RISK-<id>] [RG-<name>]
  Threat ref:       [THR-<id>] [NT/MT-<n>]
  Designation:      [CTL-DESIG] / [CONF-DESIG]
  Gap/Remediation:  <action required>"""),
                P("Example: a governance policy reviewed only in 2025 would be tagged as a Deficient control "
                  "with a remediation to complete the annual review before ROC delivery."),
                NOTE("Disposition codes",
                     "P = Pass (Satisfactory), F = Fail (Deficient), CC = Compensating Control, "
                     "NA = Not Applicable, PND = Pending evidence."),
            ],
            "terms": [
                ("Disposition", "P (Pass), F (Fail), CC (Compensating Control), NA (Not Applicable), PND (Pending)."),
                ("ROC", "Report of Conformity - the deliverable of a conformity assessment."),
            ],
        },
        {
            "id": "10.3",
            "title": "Conformity Assessment Execution",
            "minutes": 50,
            "blocks": [
                P("The SCR CAP assessment runs in a fixed sequence. Each step produces a deliverable that "
                  "feeds the next."),
                OL([
                    "**Scoping** - define the assessment boundary using the USG (zones 1-10).",
                    "**Control selection** - identify in-scope controls from the tailored Living Control Set.",
                    "**AO review** - pull AOs for each in-scope control; note the SDP minimums.",
                    "**Evidence collection** - request artifacts per the ERL; record collection method.",
                    "**Testing** - MPIT/APIT/AEHR at Standard/Enhanced/Comprehensive rigor.",
                    "**Control designation** - Satisfactory / Deficient / Compensating / N/A per control.",
                    "**Conformity designation** - Strictly Conforms / Conforms / Significant Deficiency / Material Weakness.",
                    "**ROC delivery** - Report of Conformity issued to the OSA.",
                    "**Certification** - three-year cycle: Year 1 full, Year 2 self-attest, Year 3 self-attest.",
                ]),
                TBL(["Step", "Output", "Disposition if failed"], [
                    ["Scoping", "Assessment boundary document", "Re-scope and re-submit"],
                    ["Control selection", "In-scope control list", "Re-tailor the LCS"],
                    ["AO review", "AO test plan", "Re-scope AOs"],
                    ["Evidence collection", "Evidence package", "Request missing evidence"],
                    ["Testing", "Test results", "Re-test or re-designate"],
                    ["Control designation", "Control-level designations", "Re-designate"],
                    ["Conformity designation", "Conformity-level designation", "Remediate and re-assess"],
                    ["ROC delivery", "Report of Conformity", "Re-issue after remediation"],
                    ["Certification", "Certificate issued", "Re-assess in full"],
                ], caption="Assessment execution sequence"),
            ],
            "terms": [
                ("OSA", "Organization Seeking Assessment."),
                ("CAB", "Conformity Assessment Body - the accredited assessor organization."),
            ],
        },
        {
            "id": "10.4",
            "title": "Capstone: Assessment Report & Control Matrix",
            "minutes": 60,
            "blocks": [
                P("The capstone has two deliverables weighted equally, plus a defense and peer review. It is "
                  "the graded instrument that turns theory into demonstrated capability."),
                TBL(["Deliverable", "Format", "Weight", "Key content"], [
                    ["Assessment Report", "Document", "50%", "Scope, methodology, findings, designations, recommendations"],
                    ["Control Matrix", "Spreadsheet/code", "50%", "Control-to-evidence mapping, AO results, dispositions"],
                ], caption="Capstone deliverables"),
                UL([
                    "**Defense presentation**: 15 minutes to a panel of three assessors.",
                    "**Peer review**: minimum of two reviewers per submission.",
                    "**Rubric**: Accuracy, scored on four levels - Errors, Partial, Good, Excellent (100% weight).",
                    "**Mastery threshold**: 70%.",
                ]),
                NOTE("Evaluation framework",
                     "Formative 30% (threshold 60), Summative 40% (threshold 70), Capstone 30% (threshold 70). "
                     "Retakes allowed, max 3 attempts."),
            ],
            "terms": [
                ("Capstone", "The graded end-of-course project."),
                ("Peer review", "Review by minimum two peers, required for submission."),
            ],
        },
    ],
    "questions": [
        Q("m10q1", "single",
          "How many phases does the SCF lifecycle have, from source frameworks to capstone mastery?",
          [("Wrong", "5"),
           ("Wrong", "7"),
           ("Correct", "9 (phases 0-8)"),
           ("Wrong", "12")],
          explain="Eight phases numbered 0-8: source frameworks, control catalog, tailoring, scoping, "
                  "assessment objectives, evidence, risk/threat, assessment execution, capstone/mastery.",
          competency="documents"),
        Q("m10q2", "single",
          "Which disposition code indicates a compensating control was accepted?",
          [("Wrong", "P"),
           ("Wrong", "F"),
           ("Correct", "CC"),
           ("Wrong", "NA")],
          explain="P = Pass, F = Fail, CC = Compensating Control accepted, NA = Not Applicable, PND = Pending.",
          competency="documents"),
        Q("m10q3", "multi",
          "Which are the capstone deliverables and requirements?",
          [("Correct", "Assessment Report worth 50%"),
           ("Correct", "Control Matrix worth 50%"),
           ("Correct", "15-minute defense to a panel of three"),
           ("Correct", "Peer review by minimum two reviewers"),
           ("Wrong", "A published tool conforming to CC BY-ND 4.0"),
           ("Wrong", "A 40-page written examination")],
          explain="Two deliverables at 50% each, plus defense and peer review. CC BY-ND is a licence constraint, "
                  "not a grading instrument.",
          competency="documents"),
        Q("m10q4", "single",
          "In which order does the conformity assessment execution proceed?",
          [("Wrong", "Evidence collection -> scoping -> testing -> ROC"),
           ("Correct", "Scoping -> control selection -> AO review -> evidence collection -> testing -> designation -> ROC -> certification"),
           ("Wrong", "Testing -> scoping -> evidence -> designation"),
           ("Wrong", "Certification -> ROC -> testing -> scoping")],
          explain="Scoping comes first (USG zones), then control selection, AO review, evidence collection, "
                  "testing, designation, ROC delivery, and finally certification.",
          competency="documents"),
        Q("m10q5", "single",
          "What is the conformity designation for an assessment where 75% of controls meet the criteria?",
          [("Wrong", "Conforms"),
           ("Correct", "Significant Deficiency"),
           ("Wrong", "Material Weakness"),
           ("Wrong", "Strictly Conforms")],
          explain="Significant Deficiency = at least 70% but less than 80%. 75% falls in that band.",
          competency="documents"),
        Q("m10q6", "single",
          "What is the re-evaluation window for a Deficient control?",
          [("Wrong", "Any time before the ROC is published"),
           ("Wrong", "Within 30 business days"),
           ("Correct", "During the assessment and up to 10 business days after the active assessment period"),
           ("Wrong", "There is no re-evaluation window")],
          explain="The window closes when the ROC is delivered to the OSA.",
          competency="documents"),
    ],
}

MODULES = [MODULE_10]

MODULES = [MODULE_8, MODULE_9, MODULE_10]
