# Zacharias Frankel, *Darkhe ha-Mishnah*: Hebrew and English

Site: <https://openseforim.org/frankel-darkhe/>

Zacharias Frankel (1801–1875), first head of the Jewish Theological Seminary at Breslau, published *Darkhe ha-Mishnah*
(Leipzig 1859; Latin title *Hodegetica in Mischnam*), the first critical history of the Mishnah and its sages. Its
historical account of the Oral Law set off one of the great controversies of nineteenth-century Judaism. It has never
been translated into English. This repository holds a Hebrew text checked against the scan, an English translation
paragraph by paragraph, and the scripts that build the reader.

## Status

| Part | Pages | Status |
|---|---|---|
| 1. The author's preface | VII–X (files p018–p021) | 24-Nov-2026. Hebrew checked against the scan line by line; 12 rows translated; 1 uncertain rendering. |
| 2– | the introduction to the Mishnah | OCR only (`data/he_raw/`), not checked or translated |

## Sources

- **Base text:** the first edition, Leipzig 1859, Harvard copy at HathiTrust
  ([hvd.hwmg1g](https://babel.hathitrust.org/cgi/pt?id=hvd.hwmg1g), public domain). Page files `pNNN` are the pages of
  the HathiTrust PDF; its first page is HathiTrust's notice, so file `pNNN` is image `seq=NNN-1` in the viewer
  (not yet checked in the viewer). The supplement, *Tosafot u-mafteaḥ* (Leipzig 1867), is not included yet.
- **Translations that exist:** none in English; studies only (for example D. Mackler, *Jewish Studies Quarterly* 28, 2021).

## Method

- **OCR:** [Kraken](https://kraken.re/) with the PP-OCRv6 medium model, line by line, on Kaggle GPUs (24-Nov-2026),
  1-bit pages at half size. Raw output for the whole book: `data/he_raw/` (not checked). The front matter came out
  empty and is still to be done.
- **Checking:** every line compared with the scan by eye; spelling and abbreviations as printed, except where the print
  confuses look-alike letters (ה and ח, ס and מ), which Frankel himself warns of in the preface: there the word is
  given in its intended form.
- **English:** close to the Hebrew; the rhymed prose of the preface is rendered for sense, with biblical phrases
  identified in [gray brackets]. The translation is by Claude (Anthropic), directed and reviewed by Ezra Brand.

## Files

- `data/he/pNNN.txt`: checked Hebrew, one file per page (`@ N` printed page; `#` heading; blank line = paragraph break;
  `---` then the page's notes).
- `data/en/part-NN.en.txt`, `part-NN.fn.en.txt`, `part-NN.notes.json`: English rows, notes, uncertain renderings.
- `scripts/config.py`: the work's settings; `scripts/build_site.py` builds `docs/`; `scripts/make_scans.py` makes the
  page images for the scan panel.

## Licence

Text and translation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The Hebrew original is in the
public domain.
