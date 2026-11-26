"""Settings of the Darkhe ha-Mishnah reader, used by build_site.py and make_scans.py."""

SHORT = "Frankel, Darkhe ha-Mishnah"
TITLE_HE = "דרכי המשנה"
TITLE_HTML = "Zacharias Frankel, <i>Darkhe ha-Mishnah</i>"
SUBTITLE = "The ways of the Mishnah, with an English translation paragraph by paragraph"
EDITION = "Leipzig 1859"
SCAN_NAME = "the HathiTrust scan"
NOTES_HEAD = "Frankel's notes"
REST = "The introduction to the Mishnah: the Oral Law, the tannaim, the redaction"

# page files are the pages of the HathiTrust PDF of hvd.hwmg1g (file pNNN = PDF page NNN). The PDF's first page is
# HathiTrust's notice, so file pNNN is image seq NNN-1 in the HathiTrust viewer (checked by the owner in the viewer, 24-Nov-2026).
PAGES_DIR = "data/pages"


def scan_url(stem):
    return f"https://babel.hathitrust.org/cgi/pt?id=hvd.hwmg1g&seq={int(stem[1:]) - 1}"


PARTS = {
    1: ("The author's preface",
        "Why the Mishnah, the gate to the Oral Law, needs an introduction; Maimonides' introduction; the Breslau "
        "seminary and the plan of the book",
        ["p018", "p019", "p020", "p021"]),
}

ABOUT = """Zacharias Frankel (1801–1875), chief rabbi of Dresden and from 1854 the first head of the Jewish Theological
Seminary at Breslau, published <i>Darkhe ha-Mishnah</i> (Leipzig 1859; Latin title <i>Hodegetica in Mischnam</i>) as the
first critical history of the Mishnah and its sages. Its historical account of the Oral Law set off one of the great
controversies of nineteenth-century Judaism. It has never been translated into English."""

BACKGROUND_BLURB = "Frankel, the Breslau seminary, and the controversy over the book."

INDEX_BODY = """<h2>The Hebrew text</h2>
<ul>
<li><b>Base text:</b> the first edition, Leipzig 1859. Scan: Harvard copy at HathiTrust,
<a href="https://babel.hathitrust.org/cgi/pt?id=hvd.hwmg1g">hvd.hwmg1g</a> (public domain). The supplement
(<i>Tosafot u-mafteaḥ</i>, 1867) is not included yet.</li>
<li><b>OCR:</b> Kraken with the PP-OCRv6 model, line by line, then checked against the scan by eye. The print confuses
similar letters (Frankel himself warns of ה and ח), so some words are read by sense; these are noted.</li>
</ul>

<h2>Method</h2>
<ul>
<li><b>Rows.</b> One row is one heading or one paragraph of the print.</li>
<li><b>English.</b> Close to the Hebrew; Frankel's rhymed prose in the preface is translated for sense, with biblical
phrases identified in gray brackets.</li>
<li><b>Uncertain renderings</b> have the mark ⚠ and a note at the end of the page.</li>
<li><b>Translator.</b> The translation is by Claude (Anthropic), directed and reviewed by Ezra Brand.</li>
</ul>

<h2>Translations that exist</h2>
<ul><li>None in English is known.</li></ul>"""

WORK = {"schema": 1, "slug": "frankel-darkhe", "order": 37, "kind": "translation",
        "title": "Zacharias Frankel, *Darkhe ha-Mishnah*", "short_title": "*Darkhe ha-Mishnah*", "title_he": TITLE_HE,
        "author": "Zacharias Frankel (1801–1875)",
        "status_label": "In progress · preface (pilot)",
        "start": "part-01.html", "start_label": "The author's preface",
        "summary": "The first critical history of the Mishnah and its sages, with an English translation paragraph by paragraph.",
        "base_edition": {"label": "Leipzig 1859; HathiTrust scan", "scan_url": "https://babel.hathitrust.org/cgi/pt?id=hvd.hwmg1g"},
        "method": "Paragraph-aligned Hebrew and English; Hebrew from Kraken OCR checked against the scan.",
        "cite": "Zacharias Frankel, *Darkhe ha-Mishnah*, Hebrew text with English translation, ed. Ezra Brand. Open Seforim",
        "url": "https://openseforim.org/frankel-darkhe/", "repo": "https://github.com/openseforim/frankel-darkhe", "doi": "10.5281/zenodo.24559624",
        "licence": {"name": "CC BY-SA 4.0", "url": "https://creativecommons.org/licenses/by-sa/4.0/"}}
