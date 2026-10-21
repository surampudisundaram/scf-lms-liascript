# -*- coding: utf-8 -*-
"""Shared renderers for the SCF-2026.3 LMS projection.

One content source (course_content.py) -> three targets:
  * LiAScript markdown  (artifacts/liascript/course.lia.md)
  * SCORM 2004 4th Ed   (artifacts/scorm/sco/*.html)
  * LearnHouse TipTap  (artifacts/learnhouse/*, pushed to the LearnHouse API)

Every fact rendered here originates from the OKF bundle at
D:\\Secure Controls Framework\\scf_lms_bundle_v2. No content is invented here.
"""
import html
import re

# --------------------------------------------------------------------- inline
_TOKEN = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`")


def md_to_html(text):
    """Convert the limited inline markdown used in course_content to HTML."""
    s = html.escape(text, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def md_to_tiptap(text):
    """Convert the limited inline markdown used in course_content to TipTap text nodes."""
    out = []
    pos = 0
    for m in _TOKEN.finditer(text):
        if m.start() > pos:
            out.append({"type": "text", "text": text[pos:m.start()]})
        if m.group(1) is not None:
            out.append({"type": "text", "marks": [{"type": "bold"}], "text": m.group(1)})
        elif m.group(2) is not None:
            out.append({"type": "text", "marks": [{"type": "italic"}], "text": m.group(2)})
        else:
            out.append({"type": "text", "marks": [{"type": "code"}], "text": m.group(3)})
        pos = m.end()
    if pos < len(text):
        out.append({"type": "text", "text": text[pos:]})
    return out


def plain(text):
    """Strip inline markup - used where the target renderer has no markdown support."""
    return re.sub(r"\*\*(.+?)\*\*", r"\1", re.sub(r"\*([^*]+)\*", r"\1", text.replace("`", "")))


def _cell(text):
    return " ".join(str(text).split()).replace("|", "\\|")


# ------------------------------------------------------------------- markdown
def blocks_to_md(blocks, level=3):
    """Render content blocks to LiAScript-flavoured markdown."""
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            out.append("#" * level + " " + b[1])
        elif kind == "p":
            out.append(b[1])
        elif kind == "ul":
            out.append("\n".join("- " + i for i in b[1]))
        elif kind == "ol":
            out.append("\n".join("%d. %s" % (n + 1, t) for n, t in enumerate(b[1])))
        elif kind == "table":
            head, rows, cap = b[1]["head"], b[1]["rows"], b[1]["caption"]
            lines = []
            if cap:
                lines.append("**%s**" % cap)
                lines.append("")
            lines.append("| " + " | ".join(_cell(h) for h in head) + " |")
            lines.append("|" + "|".join(["---"] * len(head)) + "|")
            for r in rows:
                lines.append("| " + " | ".join(_cell(c) for c in r) + " |")
            out.append("\n".join(lines))
        elif kind == "note":
            out.append("> **%s**\n>\n> %s" % (b[1]["title"], b[1]["text"]))
        elif kind == "code":
            out.append("```%s\n%s\n```" % (b[1]["lang"], b[1]["code"]))
        else:
            raise ValueError("unknown block %r" % (kind,))
    return "\n\n".join(out)


def terms_to_md(terms):
    if not terms:
        return ""
    return "\n".join("- **%s** - %s" % (t, d) for t, d in terms)


# ------------------------------------------------------------------------ html
def blocks_to_html(blocks, level=3):
    """Render content blocks to HTML for the SCORM SCOs."""
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            out.append("<h%d>%s</h%d>" % (level, md_to_html(b[1]), level))
        elif kind == "p":
            out.append("<p>%s</p>" % md_to_html(b[1]))
        elif kind == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % md_to_html(i) for i in b[1]))
        elif kind == "ol":
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % md_to_html(t) for t in b[1]))
        elif kind == "table":
            head, rows, cap = b[1]["head"], b[1]["rows"], b[1]["caption"]
            parts = ["<table>"]
            if cap:
                parts.append("<caption>%s</caption>" % md_to_html(cap))
            parts.append("<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % md_to_html(h) for h in head))
            parts.append("<tbody>%s</tbody>" % "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % md_to_html(c) for c in r) for r in rows))
            parts.append("</table>")
            out.append("".join(parts))
        elif kind == "note":
            out.append('<div class="note"><p class="note-title">%s</p><p>%s</p></div>'
                       % (md_to_html(b[1]["title"]), md_to_html(b[1]["text"])))
        elif kind == "code":
            out.append('<pre class="code"><code class="language-%s">%s</code></pre>'
                       % (b[1]["lang"], html.escape(b[1]["code"], quote=False)))
        else:
            raise ValueError("unknown block %r" % (kind,))
    return "\n".join(out)


def terms_to_html(terms):
    if not terms:
        return ""
    items = "".join('<li><strong>%s</strong> &mdash; %s</li>' % (md_to_html(t), md_to_html(d))
                    for t, d in terms)
    return '<h3 class="terms-head">Key terms</h3><ul class="terms">%s</ul>' % items


# --------------------------------------------------------------------- tiptap
def blocks_to_tiptap(blocks, level=3):
    """Render content blocks to a list of TipTap nodes."""
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h":
            out.append({"type": "heading", "attrs": {"level": level},
                        "content": md_to_tiptap(b[1])})
        elif kind == "p":
            out.append({"type": "paragraph", "content": md_to_tiptap(b[1])})
        elif kind == "ul":
            out.append({"type": "bulletList", "content": [
                {"type": "listItem", "content": [{"type": "paragraph", "content": md_to_tiptap(i)}]}
                for i in b[1]]})
        elif kind == "ol":
            out.append({"type": "orderedList", "content": [
                {"type": "listItem", "content": [{"type": "paragraph", "content": md_to_tiptap(t)}]}
                for t in b[1]]})
        elif kind == "table":
            head, rows, cap = b[1]["head"], b[1]["rows"], b[1]["caption"]
            nodes = []
            if cap:
                nodes.append({"type": "paragraph", "content": [
                    {"type": "text", "marks": [{"type": "bold"}], "text": cap}]})
            nodes.append({"type": "table", "content": [
                {"type": "tableRow", "content": [
                    {"type": "tableHeader", "content": [{"type": "paragraph", "content": md_to_tiptap(h)}]}
                    for h in head]},
            ] + [
                {"type": "tableRow", "content": [
                    {"type": "tableCell", "content": [{"type": "paragraph", "content": md_to_tiptap(c)}]}
                    for c in r]} for r in rows]})
            out.extend(nodes)
        elif kind == "note":
            out.append({"type": "blockquote", "content": [
                {"type": "paragraph", "content": [
                    {"type": "text", "marks": [{"type": "bold"}], "text": b[1]["title"]}]},
                {"type": "paragraph", "content": md_to_tiptap(b[1]["text"])}]})
        elif kind == "code":
            out.append({"type": "codeBlock", "attrs": {"language": b[1]["lang"]},
                        "content": [{"type": "text", "text": b[1]["code"]}]})
        else:
            raise ValueError("unknown block %r" % (kind,))
    return out


def terms_to_tiptap(terms):
    if not terms:
        return []
    return [
        {"type": "heading", "attrs": {"level": 3}, "content": [{"type": "text", "text": "Key terms"}]},
        {"type": "bulletList", "content": [
            {"type": "listItem", "content": [{"type": "paragraph", "content": [
                {"type": "text", "marks": [{"type": "bold"}], "text": t},
                {"type": "text", "text": " - " + d}]}]} for t, d in terms]},
    ]


def doc(content):
    return {"type": "doc", "content": content}


# ---------------------------------------------------------------------- quizzes
def quiz_to_md(q):
    """LiAScript quiz block.

    Single choice -> [(X)] / [( )]
    Multiple choice -> [[X]] / [[ ]]
    Solution block -> two lines of three or more asterisks.
    """
    lines = [q["prompt"], ""]
    lines.append('<!-- data-randomize data-max-trials="3" -->')
    for marker, text in q["options"]:
        label = plain(text)
        if q["type"] == "single":
            lines.append("[(X)] %s" % label if marker == "Correct" else "[( )] %s" % label)
        else:
            lines.append("[[X]] %s" % label if marker == "Correct" else "[[ ]] %s" % label)
    if q.get("hint"):
        lines.append("[[?]] %s" % plain(q["hint"]))
    if q.get("explanation"):
        lines.append("***")
        lines.append(q["explanation"])
        lines.append("***")
    return "\n".join(lines)


def quiz_to_html(q, index):
    """Interactive SCORM knowledge check item."""
    qid = "q%d" % index
    kind = "radio" if q["type"] == "single" else "checkbox"
    parts = ['<div class="quiz-item" id="%s">' % qid]
    parts.append('<p class="quiz-q"><span class="quiz-id">%s</span> %s</p>'
                 % (qid.upper(), md_to_html(q["prompt"])))
    parts.append('<div class="quiz-options">')
    for n, (marker, text) in enumerate(q["options"]):
        parts.append(
            '<label class="quiz-opt"><input type="%s" name="%s" value="%d" data-correct="%s"> '
            '<span>%s</span></label>'
            % (kind, qid, n, "1" if marker == "Correct" else "0", md_to_html(text)))
    parts.append("</div>")
    if q.get("hint"):
        parts.append('<p class="quiz-hint"><em>Hint:</em> %s</p>' % md_to_html(q["hint"]))
    parts.append('<p class="quiz-feedback" id="%s-fb"></p>' % qid)
    parts.append("</div>")
    return "\n".join(parts)


def quiz_to_tiptap(q):
    """LearnHouse has no quiz node - emit a self-assessment knowledge check."""
    out = [{"type": "heading", "attrs": {"level": 3},
            "content": [{"type": "text", "text": "Question %s" % q["id"].upper()}]}]
    out.append({"type": "paragraph", "content": md_to_tiptap(q["prompt"])})
    opts = []
    for marker, text in q["options"]:
        node = {"type": "listItem", "content": [{"type": "paragraph", "content": []}]}
        inline = []
        if marker == "Correct":
            inline.append({"type": "text", "marks": [{"type": "bold"}], "text": "Correct answer: "})
        inline.extend(md_to_tiptap(text))
        node["content"][0]["content"] = inline
        opts.append(node)
    out.append({"type": "bulletList", "content": opts})
    if q.get("hint"):
        out.append({"type": "paragraph", "content": [
            {"type": "text", "marks": [{"type": "italic"}], "text": "Hint: "}] + md_to_tiptap(q["hint"])})
    if q.get("explanation"):
        out.append({"type": "blockquote", "content": [
            {"type": "paragraph", "content": [
                {"type": "text", "marks": [{"type": "bold"}], "text": "Explanation"}]},
            {"type": "paragraph", "content": md_to_tiptap(q["explanation"])}]})
    return out
