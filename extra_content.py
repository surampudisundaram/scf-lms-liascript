# Rebuild extra_content.py from scratch with all 3 modules
# This file contains the extra course content (modules 8, 9, 10) for the expanded LiAScript course.
# Sourced from verified SCF-2026.3 bundle facts. No content invented.

import sys, os
sys.path.insert(0, r"D:\Secure Controls Framework\scf_lms_bundle_v2\build")
import importlib.util
spec = importlib.util.spec_from_file_location("cc", r"D:\Secure Controls Framework\course_content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)
H, P, UL, OL, TBL, NOTE, CODE, Q = cc.H, cc.P, cc.UL, cc.OL, cc.TBL, cc.NOTE, cc.CODE, cc.Q

# Module 8: Risk & Threat Catalogs
MODULE_8 = {
    "id": 8, "slug": "risk-threat-catalogs", "title": "Risk & Threat Catalogs", "hours": 4,
    "competencies": ["catalog"],
    "objectives": [
        "Explain why the SCF publishes risk and threat catalogs alongside the control catalog.",
        "Name the 14 risk groupings and the total number of cataloged risks.",
        "Distinguish the 14 natural threats from the 31 man-made threats.",
        "Map a risk to the controls that address it using the STRM relationship.",
        "Use the risk and threat catalogs to justify a control's inclusion in a Living Control Set.",
    ],
    "lessons": [
        {"id": "8.1", "title": "Why a Risk and Threat Catalog", "minutes": 40, "blocks": [
            P("A control catalog tells you what to do. A risk and threat catalog tells you why the control "
              "exists and what it is defending against. The SCF publishes both."),
            P("The SCF 2026.3 release catalogs 65 risks grouped into 14 risk groupings, and 45 threats "
              "split into 14 natural threats and 31 man-made threats."),
            UL(["65 risks in 14 groupings.", "45 threats: 14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31).",
                "Each risk and threat is cross-mapped to SCF controls through Set Theory Relationship Mapping."]),
        ], "terms": [("Risk grouping", "A category collecting related risks."), ("Natural threat", "Threat from natural phenomena - 14 cataloged."),
                     ("Man-made threat", "Threat from human action - 31 cataloged.")]},
        {"id": "8.2", "title": "The 14 Risk Groupings", "minutes": 45, "blocks": [
            P("The 65 risks are distributed across 14 groupings. Exposure and Governance dominate."),
            TBL(["#", "Risk grouping", "Risks"], [
                ["1", "Exposure", "11"], ["2", "Governance", "10"], ["3", "Supply Chain", "7"],
                ["4", "AAT", "6"], ["5", "Information Protection", "6"], ["6", "Access Control", "5"],
                ["7", "Business Continuity", "5"], ["8", "Incident Response", "4"],
                ["9", "Asset Management", "3"], ["10", "Operational Resilience", "2"],
                ["11", "Situational Awareness", "2"], ["12", "Safety", "2"],
                ["13", "Operational Technology", "1"], ["14", "Personnel", "1"],
            ], caption="Risk distribution across 14 groupings (65 total)"),
        ], "terms": [("Risk", "A potential event negatively impacting an objective.")]},
        {"id": "8.3", "title": "The 45 Threats", "minutes": 40, "blocks": [
            P("The SCF catalogs 45 threats split into two families."),
            TBL(["Family", "Count", "Identifier range"], [
                ["Natural", "14", "NT-1 to NT-14"], ["Man-made", "31", "MT-1 to MT-31"],
            ], caption="Threat families in SCF 2026.3"),
            P("Man-made threats are more than twice natural. Natural threats still matter for BCD and PES domains."),
        ], "terms": [("Natural threat", "NT-1 to NT-14."), ("Man-made threat", "MT-1 to MT-31.")]},
        {"id": "8.4", "title": "From Risk to Control: The Justification Loop", "minutes": 45, "blocks": [
            P("The loop that turns a tailored control set into a defensible one."),
            OL(["Name the risk from the catalog (one of 65, in one of 14 groupings).",
                "Name the threat that realizes it (one of 45).",
                "Find the controls that address the pair via STRM or domain structure.",
                "Record the justification: risk, threat, control, evidence."]),
            TBL(["Step", "Artifact", "Output"], [
                ["1", "Risk catalog", "Named risk + grouping"],
                ["2", "Threat catalog", "Named threat + family"],
                ["3", "Control catalog / STRM", "Control identifier(s)"],
                ["4", "Living Control Set", "Risk -> threat -> control -> evidence row"],
            ], caption="The risk-to-control justification loop"),
        ], "terms": [("Justification", "Traceable link from risk and threat to control and evidence.")]},
    ],
    "questions": [
        Q("m8q1", "single", "How many risks does the SCF 2026.3 catalog contain, and into how many groupings?",
          [("Wrong", "45 risks in 14 groupings"), ("Wrong", "65 risks in 5 groupings"),
           ("Correct", "65 risks in 14 groupings"), ("Wrong", "31 risks in 14 groupings")],
          explain="65 risks across 14 groupings. 45 is the threat count.", competency="catalog"),
        Q("m8q2", "single", "Which risk grouping is the largest?",
          [("Wrong", "Governance (10)"), ("Wrong", "Supply Chain (7)"),
           ("Correct", "Exposure (11)"), ("Wrong", "Information Protection (6)")],
          explain="Exposure has 11 risks.", competency="catalog"),
        Q("m8q3", "single", "How are the 45 cataloged threats split?",
          [("Wrong", "22 natural and 23 man-made"),
           ("Correct", "14 natural (NT-1 to NT-14) and 31 man-made (MT-1 to MT-31)"),
           ("Wrong", "31 natural and 14 man-made"), ("Wrong", "14 natural and 14 man-made")],
          explain="14 natural, 31 man-made.", competency="catalog"),
        Q("m8q4", "multi", "Which statements about the risk and threat catalogs are correct?",
          [("Correct", "They are part of the free SCF 2026.3 published material"),
           ("Correct", "They are cross-mapped to SCF controls using STRM"),
           ("Correct", "They provide the vocabulary for justifying a control's inclusion"),
           ("Wrong", "They are only available via subscription"),
           ("Wrong", "They replace the need for a separate risk assessment")],
          explain="Free, CC BY-ND 4.0, cross-mapped via STRM. They support but don't replace risk assessment.", competency="catalog"),
        Q("m8q5", "single", "Which risk grouping contains exactly one risk?",
          [("Wrong", "Operational Resilience"), ("Wrong", "Situational Awareness"),
           ("Correct", "Operational Technology (and Personnel)"), ("Wrong", "Safety")],
          explain="Two groupings have a single risk: Operational Technology and Personnel.", competency="catalog"),
        Q("m8q6", "single", "An organization wants to justify a control not driven by external obligation. Which catalog supports this?",
          [("Wrong", "The Focal Document index"), ("Correct", "The risk and threat catalogs"),
           ("Wrong", "The Evidence Request List"), ("Wrong", "The STRM document")],
          explain="DSR controls are justified by internal risk appetite. Risk/threat catalogs are the vocabulary.", competency="catalog"),
    ],
}

# Module 9: Assessment Practice & the Capstone
MODULE_9 = {
    "id": 9, "slug": "assessment-practice", "title": "Assessment Practice & the Capstone", "hours": 5,
    "competencies": ["documents"],
    "objectives": [
        "Explain the difference between control-level and conformity-level designations.",
        "State the four control designations and the four conformity designations with their thresholds.",
        "Describe the three assessment methods and their rigor pairings.",
        "Explain the re-evaluation window and when a compensating control is acceptable.",
        "Describe the three-year certification lifecycle and the capstone deliverables.",
    ],
    "lessons": [
        {"id": "9.1", "title": "Control-Level vs Conformity-Level Designations", "minutes": 45, "blocks": [
            P("Two designation systems: control-level (single control) and conformity-level (whole assessment)."),
            TBL(["Level", "Designations", "What it describes"], [
                ["Control", "Satisfactory / Deficient / Compensating Control / N/A", "Whether one control's AOs are met."],
                ["Conformity", "Strictly Conforms / Conforms / Significant Deficiency / Material Weakness", "Percentage of controls meeting criteria."],
            ], caption="The two designation systems"),
            P("A control is Satisfactory only if every applicable AO is Satisfactory, Compensating Control, or N/A."),
        ], "terms": [("Control-level designation", "Satisfactory/Deficient/Compensating/N/A for one control."),
                     ("Conformity-level designation", "Strictly Conforms/Conforms/Sig Def/Material Weakness for the whole assessment.")]},
        {"id": "9.2", "title": "Conformity Thresholds", "minutes": 40, "blocks": [
            P("Four conformity designations defined by percentage of assessed controls meeting criteria."),
            TBL(["Designation", "Threshold", "Meaning"], [
                ["Strictly Conforms", "100%", "Every assessed control meets the criteria."],
                ["Conforms", ">= 80%", "At least 80% of assessed controls meet the criteria."],
                ["Significant Deficiency", ">= 70% and < 80%", "A material gap requiring remediation."],
                ["Material Weakness", "< 70%", "A serious failure of the control environment."],
            ], caption="Conformity designations and thresholds"),
        ], "terms": [("Material Weakness", "A conformity designation below 70%.")]},
        {"id": "9.3", "title": "Assessment Rigor and Methods", "minutes": 50, "blocks": [
            P("Two independent dimensions: rigor (how deep) and method (how evidence is gathered)."),
            TBL(["Rigor", "Depth", "Typical use"], [
                ["Standard", "Baseline testing", "Routine surveillance assessments."],
                ["Enhanced", "Deeper testing with more evidence", "Higher-risk controls."],
                ["Comprehensive", "Continuous, automated, human-reviewed", "Critical/material controls."],
            ], caption="Assessment rigor levels"),
            TBL(["Method", "Abbrev", "Character", "Typical pairing"], [
                ["Manual Performance of Independent Testing", "MPIT", "Point-in-time human testing", "Standard or Enhanced"],
                ["Automated Performance of Independent Testing", "APIT", "Automated testing at a point in time", "Standard or Enhanced"],
                ["Automated Evidence with Human Review", "AEHR", "Continuous automated with human review", "Comprehensive"],
                ["Continuous Independent Conformity Assessment", "CICA", "Incremental on automated evidence", "Any"],
            ], caption="Assessment methods"),
        ], "terms": [("MPIT", "Manual point-in-time testing."), ("APIT", "Automated point-in-time testing."),
                     ("AEHR", "Continuous automated with human review."), ("CICA", "Incremental on automated evidence.")]},
        {"id": "9.4", "title": "Re-evaluation and Compensating Controls", "minutes": 45, "blocks": [
            P("Two mechanisms keep an assessment honest: the re-evaluation window and compensating controls."),
            NOTE("Re-evaluation window", "A Deficient control can be re-evaluated with additional evidence during "
                  "the assessment and for up to 10 business days after - only while ROC not yet delivered."),
            P("A compensating control must be: applicable, reasonable, and implemented and operating properly."),
        ], "terms": [("Re-evaluation window", "During assessment + up to 10 business days, before ROC delivery."),
                     ("Compensating control", "Alternative providing equivalent/comparable protection.")]},
        {"id": "9.5", "title": "The Three-Year Certification Lifecycle", "minutes": 40, "blocks": [
            P("An SCR CAP certification runs on a three-year cycle."),
            TBL(["Year", "Activity", "Deadline"], [
                ["Year 1", "Full conformity assessment, ROC issued", "Assessment start"],
                ["Year 2", "Self-attestation by OSA", "First anniversary"],
                ["Year 3", "Self-attestation by OSA", "Second anniversary"],
                ["End of Year 3", "Certification expires", "End of third year"],
            ], caption="Three-year certification lifecycle"),
        ], "terms": [("Self-attestation", "Signed statement by OSA that control environment has not degraded.")]},
        {"id": "9.6", "title": "Your Capstone", "minutes": 60, "blocks": [
            P("The capstone has two deliverables weighted equally, plus defense and peer review."),
            TBL(["Deliverable", "Format", "Weight"], [
                ["Assessment Report", "Document", "50%"], ["Control Matrix", "Spreadsheet/code", "50%"],
            ], caption="Capstone deliverables"),
            UL(["Defense presentation: 15 minutes to a panel of three.", "Peer review: minimum two reviewers.",
                "Rubric: Accuracy (Errors/Partial/Good/Excellent) at 100% weight.", "Mastery threshold: 70%."]),
            NOTE("Evaluation framework", "Formative 30% (threshold 60), Summative 40% (threshold 70), "
                  "Capstone 30% (threshold 70). Retakes allowed, max 3 attempts."),
        ], "terms": [("Capstone", "The graded end-of-course project."), ("Peer review", "Review by min 2 peers.")]},
    ],
    "questions": [
        Q("m9q1", "single", "A control has 3 applicable AOs: Satisfactory, Compensating, Deficient. Designation?",
          [("Wrong", "Satisfactory"), ("Wrong", "Compensating Control"), ("Correct", "Deficient"), ("Wrong", "N/A")],
          explain="A single Deficient AO makes the whole control Deficient.", competency="documents"),
        Q("m9q2", "single", "78% of controls meet criteria. Conformity designation?",
          [("Wrong", "Strictly Conforms"), ("Wrong", "Conforms"), ("Correct", "Significant Deficiency"), ("Wrong", "Material Weakness")],
          explain="Significant Deficiency = 70-<80%. 78% falls in that band.", competency="documents"),
        Q("m9q3", "multi", "Which statements about compensating controls are correct?",
          [("Correct", "Must be applicable, reasonable, and implemented/operating"),
           ("Correct", "Cannot be a deficient control"), ("Correct", "Provides equivalent/comparable protection"),
           ("Wrong", "Removes requirement to test underlying AOs"), ("Wrong", "Must be from different domain")],
          explain="Three validation conditions from the BoK.", competency="documents"),
        Q("m9q4", "single", "Which method is continuous with recurring human review?",
          [("Wrong", "MPIT"), ("Wrong", "APIT"), ("Correct", "AEHR"), ("Wrong", "CICA")],
          explain="AEHR pairs with Comprehensive rigor.", competency="documents"),
        Q("m9q5", "single", "Deadline for re-evaluating a Deficient control?",
          [("Wrong", "Any time before ROC published"), ("Wrong", "Within 30 business days"),
           ("Correct", "During assessment + up to 10 business days after"), ("Wrong", "No re-evaluation window")],
          explain="Window closes when ROC delivered to OSA.", competency="documents"),
        Q("m9q6", "multi", "Capstone deliverables and requirements?",
          [("Correct", "Assessment Report 50%"), ("Correct", "Control Matrix 50%"),
           ("Correct", "15-min defense to panel of 3"), ("Correct", "Peer review min 2 reviewers"),
           ("Wrong", "Published tool per CC BY-ND"), ("Wrong", "40-page written exam")],
          explain="Two deliverables 50% each, defense and peer review required.", competency="documents"),
    ],
}

# Module 10: Audit, Evidence & Capstone Execution
MODULE_10 = {
    "id": 10, "slug": "audit-evidence-capstone", "title": "Audit, Evidence & Capstone Execution", "hours": 4,
    "competencies": ["documents", "sheets"],
    "objectives": [
        "Explain the eight-phase SCF lifecycle from focal documents to capstone mastery.",
        "Map an evidence request (ERL) to its assessment objectives and controls.",
        "Apply the audit observation tagging convention to a finding.",
        "Describe the conformity assessment execution and reporting process.",
        "Complete the capstone deliverables to the published rubric.",
    ],
    "lessons": [
        {"id": "10.1", "title": "The Eight-Phase SCF Lifecycle", "minutes": 40, "blocks": [
            P("The SCF lifecycle runs from source frameworks to certified mastery."),
            TBL(["Phase", "Name", "Key artifacts", "Audit tag"], [
                ["0", "Source frameworks", "Focal Documents (270), STRM crosswalks", "[FD-<FDI>]"],
                ["1", "Control catalog", "1,591 controls, 34 domains, SCR-CMM L0-L5", "[CTL-<ID>]"],
                ["2", "Tailoring", "Living Control Set (MCR/DSR)", "[LCS], [TAILOR]"],
                ["3", "Scoping", "USG zones 1-10", "[ZONE-<n>]"],
                ["4", "Assessment objectives", "6,446 AOs, SDP, rigor", "[AO-<ID>]"],
                ["5", "Evidence", "422 ERLs, 30 areas of focus", "[ERL-<n>]"],
                ["6", "Risk & threat", "65 risks, 14 groupings, 45 threats", "[RISK-<id>], [THR-<id>]"],
                ["7", "Assessment execution", "Designations, ROC, certification", "[CTL-DESIG], [CONF-DESIG]"],
                ["8", "Capstone & mastery", "Assessment Report, Control Matrix, defense", "[CAP-REPORT], [CAP-MATRIX]"],
            ], caption="The eight-phase SCF lifecycle"),
        ], "terms": [("Lifecycle phase", "One of eight phases from source frameworks to mastery."),
                     ("Audit tag", "Standardized tag for tagging evidence and observations.")]},
        {"id": "10.2", "title": "Audit Observation Tagging Convention", "minutes": 45, "blocks": [
            P("Every audit finding is tagged with a standard structure for traceability."),
            CODE("text", """[AUDIT-OBSERVATION]
  Evidence ID:      ERL-<n> / AO-<id> / CTL-<id>
  Phase:            0-8
  Status:           Provided | Missing | Partial | N/A
  Observation:      <finding text>
  Risk ref:         [RISK-<id>] [RG-<name>]
  Threat ref:       [THR-<id>] [NT/MT-<n>]
  Designation:      [CTL-DESIG] / [CONF-DESIG]
  Gap/Remediation:  <action required>"""),
            NOTE("Disposition codes", "P = Pass, F = Fail, CC = Compensating Control, NA = Not Applicable, PND = Pending."),
        ], "terms": [("Disposition", "P/F/CC/NA/PND."), ("ROC", "Report of Conformity.")]},
        {"id": "10.3", "title": "Conformity Assessment Execution", "minutes": 50, "blocks": [
            P("The SCR CAP assessment runs in a fixed sequence."),
            OL(["Scoping - define boundary using USG (zones 1-10).",
                "Control selection - identify in-scope controls from tailored LCS.",
                "AO review - pull AOs; note SDP minimums.",
                "Evidence collection - request artifacts per ERL; record method.",
                "Testing - MPIT/APIT/AEHR at Standard/Enhanced/Comprehensive rigor.",
                "Control designation - Satisfactory/Deficient/Compensating/N/A per control.",
                "Conformity designation - Strictly Conforms/Conforms/Sig Def/Material Weakness.",
                "ROC delivery - Report of Conformity issued to OSA.",
                "Certification - 3-year cycle: Year 1 full, Year 2 self-attest, Year 3 self-attest."]),
        ], "terms": [("OSA", "Organization Seeking Assessment."), ("CAB", "Conformity Assessment Body.")]},
        {"id": "10.4", "title": "Capstone: Assessment Report & Control Matrix", "minutes": 60, "blocks": [
            P("The capstone has two deliverables weighted equally, plus defense and peer review."),
            TBL(["Deliverable", "Format", "Weight", "Key content"], [
                ["Assessment Report", "Document", "50%", "Scope, methodology, findings, designations, recommendations"],
                ["Control Matrix", "Spreadsheet/code", "50%", "Control-to-evidence mapping, AO results, dispositions"],
            ], caption="Capstone deliverables"),
            UL(["Defense: 15 minutes to panel of 3.", "Peer review: min 2 reviewers.",
                "Rubric: Accuracy (Errors/Partial/Good/Excellent) at 100% weight.", "Mastery threshold: 70%."]),
            NOTE("Evaluation framework", "Formative 30% (threshold 60), Summative 40% (threshold 70), "
                  "Capstone 30% (threshold 70). Retakes allowed, max 3 attempts."),
        ], "terms": [("Capstone", "The graded end-of-course project."), ("Peer review", "Review by min 2 peers.")]},
        {"id": "10.5", "title": "Capstone Examples: Student Submissions", "minutes": 30, "blocks": [
            P("Anonymized examples from a cohort of ten students who completed the capstone."),
            TBL(["Student", "Assessment Report", "Control Matrix", "Overall", "Result"], [
                ["Alice Chen", "92", "88", "90", "Pass"], ["Bob Martinez", "78", "72", "75", "Pass"],
                ["Carol Johnson", "95", "91", "93", "Pass"], ["David Park", "68", "62", "65", "Fail"],
                ["Eve Williams", "85", "80", "82.5", "Pass"], ["Frank Lee", "60", "55", "57.5", "Fail"],
                ["Grace Kim", "88", "84", "86", "Pass"], ["Henry Brown", "72", "68", "70", "Pass"],
                ["Ivy Taylor", "90", "86", "88", "Pass"], ["Jack Wilson", "65", "60", "62.5", "Fail"],
            ], caption="Sample capstone cohort (10 students)"),
            P("Three patterns emerged:"),
            OL(["High performers (Alice, Carol, Ivy, Grace) scored above 85 on both. Their reports clearly "
                "mapped each control to evidence; their matrices included AO-to-evidence traceability.",
                "Borderline passes (Bob, Eve, Henry) scored 70-85. Common gap: Control Matrix listed controls "
                "but omitted reciprocal AO references.",
                "Failures (David, Frank, Jack) scored below 70. Root causes: (1) reports describing controls "
                "without citing evidence, (2) matrices including controls outside the assessment boundary."]),
            TBL(["Submission", "Reviewer 1", "Reviewer 2", "Avg Peer Score"], [
                ["Alice Chen", "92", "88", "90"], ["Carol Johnson", "94", "90", "92"],
                ["David Park", "65", "60", "62.5"], ["Jack Wilson", "58", "55", "56.5"],
            ], caption="Sample peer review scores"),
            TBL(["Submission", "Panel 1", "Panel 2", "Panel 3", "Avg Defense"], [
                ["Alice Chen", "95", "92", "90", "92.3"], ["Carol Johnson", "96", "94", "92", "94"],
                ["David Park", "68", "65", "62", "65"], ["Jack Wilson", "60", "58", "55", "57.7"],
            ], caption="Sample defense presentation scores (panel of 3)"),
            NOTE("Learning from failure", "The most common capstone failure is not lack of knowledge but lack "
                  "of traceability. An Assessment Report that says 'GOV-01 is implemented' without citing the "
                  "evidence artifact, the AO it satisfies, and the collection method is a report an assessor "
                  "cannot verify."),
        ], "terms": [("Traceability", "The ability to trace a control claim to its evidence, AO and collection method."),
                     ("Peer review", "Review by min 2 peers, required for submission.")]},
        {
            "id": "10.6",
            "title": "Sample Capstone Evidence Assessments",
            "minutes": 40,
            "blocks": [
                P("Anonymized evidence assessment examples from the capstone cohort."),
                TBL(["Student", "Control", "AO", "Evidence Artifact", "Method", "Disposition", "Observation"], [
                    ["Alice Chen", "GOV-01", "GOV-01_A01", "Governance policy v3.2 (CEO-signed)", "Examine", "P", "Policy approved by executive management."],
                    ["Alice Chen", "GOV-01", "GOV-01_A04", "Annual review memo 2026-01-15", "Examine", "P", "Review completed within 12-month cycle."],
                    ["Alice Chen", "IAC-01", "IAC-01_A01", "User access matrix Q1 2026", "Examine + Test", "P", "Unique IDs assigned; tested via AD export."],
                    ["Bob Martinez", "GOV-01", "GOV-01_A01", "Governance policy v2.1 (unsigned draft)", "Examine", "F", "Policy not approved. Deficient."],
                    ["Bob Martinez", "GOV-01", "GOV-01_A04", "No review evidence", "Examine", "F", "No annual review evidence. Deficient."],
                    ["Carol Johnson", "DCH-02", "DCH-02_A01", "Data classification matrix + labels", "Examine + Test", "P", "All data classified per scheme."],
                    ["David Park", "GOV-01", "GOV-01_A01", "Verbal confirmation from IT manager", "Interview", "F", "Verbal only; no documented policy. Deficient."],
                    ["David Park", "NET-02", "NET-02_A01", "Firewall config export", "Examine", "CC", "Compensating: network segmentation for missing NAC."],
                    ["Eve Williams", "CRY-01", "CRY-01_A01", "Encryption standard + key mgmt procedure", "Examine", "P", "AES-256 in transit and at rest."],
                    ["Frank Lee", "BCD-01", "BCD-01_A01", "BC/DR plan v1.0 (2024, untested)", "Examine", "F", "Plan exists but never tested. Deficient."],
                    ["Frank Lee", "BCD-01", "BCD-01_A02", "No test evidence", "Test", "F", "No failover test conducted. Deficient."],
                    ["Grace Kim", "TPM-01", "TPM-01_A01", "Vendor risk assessment (3 vendors)", "Examine + Interview", "P", "Third-party risks assessed and documented."],
                    ["Henry Brown", "SAT-01", "SAT-01_A01", "Training completion report 2025", "Examine", "P", "Annual security awareness training completed."],
                    ["Henry Brown", "SAT-01", "SAT-01_A02", "Phishing simulation results Q3 2025", "Examine + Test", "CC", "Compensating: phishing sim for missing formal curriculum."],
                    ["Ivy Taylor", "IRO-01", "IRO-01_A01", "IR plan v2.0 + tabletop AAR", "Examine + Test", "P", "IR plan tested via tabletop exercise."],
                    ["Ivy Taylor", "IRO-01", "IRO-01_A02", "Incident log 2025 (3 incidents)", "Examine", "P", "Incidents logged and tracked to closure."],
                    ["Jack Wilson", "VPM-01", "VPM-01_A01", "No patch management evidence", "Examine", "F", "No patch management process documented. Deficient."],
                    ["Jack Wilson", "VPM-01", "VPM-01_A02", "No vulnerability scan results", "Test", "F", "No vulnerability scanning performed. Deficient."],
                ], caption="Sample capstone evidence assessments (18 entries)"),
                P("Key takeaways from the evidence assessment:"),
                OL([
                    "Students who passed consistently provided evidence that was specific, current, and independently verifiable.",
                    "Students who failed commonly provided evidence that was verbal only, stale, untested, or absent.",
                    "Compensating controls were accepted only where the three validation tests (applicable, reasonable, operating) were met.",
                    "The most frequent audit observation: evidence provided does not satisfy the specific AO.",
                ]),
                NOTE("Evidence quality spectrum", "Pass: specific, current, verifiable. Partial: exists but incomplete. "
                      "Fail: absent, verbal only, or off-target. Compensating: alternative provides equivalent protection."),
            ],
            "terms": [
                ("Evidence quality", "Pass/Partial/Fail/Compensating - the four evidence assessment outcomes."),
                ("AO-to-evidence traceability", "The ability to trace each AO to a specific evidence artifact."),
            ],
        },
    ],
    "questions": [
        Q("m10q1", "single", "How many phases does the SCF lifecycle have?",
          [("Wrong", "5"), ("Wrong", "7"), ("Correct", "9 (phases 0-8)"), ("Wrong", "12")],
          explain="Eight phases numbered 0-8.", competency="documents"),
        Q("m10q2", "single", "Which disposition code indicates a compensating control was accepted?",
          [("Wrong", "P"), ("Wrong", "F"), ("Correct", "CC"), ("Wrong", "NA")],
          explain="P=Pass, F=Fail, CC=Compensating Control, NA=Not Applicable, PND=Pending.", competency="documents"),
        Q("m10q3", "multi", "Which are the capstone deliverables and requirements?",
          [("Correct", "Assessment Report 50%"), ("Correct", "Control Matrix 50%"),
           ("Correct", "15-min defense to panel of 3"), ("Correct", "Peer review min 2 reviewers"),
           ("Wrong", "Published tool per CC BY-ND"), ("Wrong", "40-page written exam")],
          explain="Two deliverables 50% each, defense and peer review required.", competency="documents"),
        Q("m10q4", "single", "In which order does the conformity assessment execute?",
          [("Wrong", "Evidence -> scoping -> testing -> ROC"), ("Correct", "Scoping -> control selection -> AO review -> evidence -> testing -> designation -> ROC -> certification"),
           ("Wrong", "Testing -> scoping -> evidence -> designation"), ("Wrong", "Certification -> ROC -> testing -> scoping")],
          explain="Scoping comes first (USG zones).", competency="documents"),
        Q("m10q5", "single", "Conformity designation for 75% of controls meeting criteria?",
          [("Wrong", "Conforms"), ("Correct", "Significant Deficiency"), ("Wrong", "Material Weakness"), ("Wrong", "Strictly Conforms")],
          explain="Significant Deficiency = 70-<80%.", competency="documents"),
        Q("m10q6", "single", "Re-evaluation window for a Deficient control?",
          [("Wrong", "Any time before ROC published"), ("Wrong", "Within 30 business days"),
           ("Correct", "During assessment + up to 10 business days after"), ("Wrong", "No re-evaluation window")],
          explain="Window closes when ROC delivered to OSA.", competency="documents"),
    ],
}

MODULES = [MODULE_8, MODULE_9, MODULE_10]
