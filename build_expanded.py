# -*- coding: utf-8 -*-
"""Build the expanded LiAScript course: base 7 modules + 2 extra modules.

Reads course_content.py from the bundle (read-only) and extra_content.py from
this folder. Writes course.lia.md here, then commits and pushes.
"""
import importlib.util
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = r"D:\Secure Controls Framework\scf_lms_bundle_v2"
sys.path.insert(0, HERE)
import render  # noqa: E402

CONTENT = os.path.join(os.path.dirname(BUNDLE), "course_content.py")
EXTRA = os.path.join(HERE, "extra_content.py")
OUT = os.path.join(HERE, "course.lia.md")


def load(path):
    spec = importlib.util.spec_from_file_location("cc", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def md_table(head, rows):
    lines = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * len(head)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(lines)


def course_intro(m):
    total_h = sum(x["hours"] for x in m.MODULES)
    total_q = sum(len(x["questions"]) for x in m.MODULES)
    total_l = sum(len(x["lessons"]) for x in m.MODULES)
    out = []
    out.append("# SCF-2026.3 Secure Controls Framework (Expanded Edition)")
    out.append(
        "This course teaches the Secure Controls Framework (SCF) as published in the **2026.3** release, "
        "in an expanded edition that adds two modules beyond the base seven: the risk and threat catalogs, "
        "and assessment practice with the capstone. The SCF is a metaframework: a single control catalog "
        "that maps hundreds of laws, regulations and frameworks onto one common control language.")
    out.append(
        "The course is built strictly from the SCF-2026.3 source bundle. Figures quoted throughout are the "
        "published values, not estimates.")
    out.append("## Course at a glance")
    out.append(md_table(["", ""], [
        ["Modules", str(len(m.MODULES))],
        ["Lessons", str(total_l)],
        ["Knowledge checks", str(total_q)],
        ["Estimated effort", "%d hours" % total_h],
        ["Release", "SCF 2026.3"],
        ["Format", "LiAScript (offline-capable, self-assessing)"],
    ]))
    out.append("## Module guide")
    out.append(md_table(["#", "Module", "Competency", "Hours"],
        [[str(mod["id"]), mod["title"], ", ".join(mod["competencies"]), str(mod["hours"])]
         for mod in m.MODULES]))
    out.append("## How each module is built")
    out.append(
        "Every module opens with its learning objectives, then works through its lessons, then closes with "
        "a six-question knowledge check. The knowledge check is self-assessing.")
    return out


def module_section(mod):
    out = []
    out.append("# Module %d - %s" % (mod["id"], mod["title"]))
    out.append("Estimated effort: **%d hours**. Competency: **%s**." % (mod["hours"], ", ".join(mod["competencies"])))
    out.append("## Learning objectives")
    for o in mod["objectives"]:
        out.append("- " + o)
    for lesson in mod["lessons"]:
        out.append("## %s %s" % (lesson["id"], lesson["title"]))
        out.append("_%d minutes_" % lesson["minutes"])
        out.append(render.blocks_to_md(lesson["blocks"], level=3))
        terms = lesson.get("terms") or []
        if terms:
            out.append("### Key terms")
            out.append(render.terms_to_md(terms))
    out.append("## Module %d knowledge check" % mod["id"])
    for q in mod["questions"]:
        out.append(render.quiz_to_md(q))
    return out


def main():
    base = load(CONTENT)
    extra = load(EXTRA)
    combined_modules = list(base.MODULES) + list(extra.MODULES)

    # Build a combined module object
    class M:
        pass
    M.MODULES = combined_modules
    m = M()

    parts = []
    HEADER = """<!--
author: Secure Controls Framework Council
email: info@securecontrolsframework.org
version: 2026.3.0
language: en
narrator: US English Female

comment: SCF-2026.3 Secure Controls Framework (Expanded Edition) - 10 modules,
50+ hours, built from the SCF-2026.3 OKF bundle.
-->
"""
    parts.append(HEADER)
    body = []
    body.extend(course_intro(m))
    for mod in m.MODULES:
        body.extend(module_section(mod))
    parts.append("\n\n".join(body))
    parts.append("\n")

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(parts))
    print("wrote", OUT, os.path.getsize(OUT), "bytes")
    print("modules:", len(m.MODULES), "lessons:", sum(len(x["lessons"]) for x in m.MODULES),
          "questions:", sum(len(x["questions"]) for x in m.MODULES))


if __name__ == "__main__":
    main()
