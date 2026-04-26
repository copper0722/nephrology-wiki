---
type: pipeline-spec
topic: continuous textbook feeding for Q-bank wiki retrieval
generated: 2026-04-26
agent: claude-opus-4-7
status: draft
---

# Continuous textbook ingestion — pipeline spec

Triggered by Copper directive 2026-04-26: nephro-cme requires per-option textbook-anchored explanation; Brenner 12e is the largest gap (currently 3 of ~70 chapters wikified). This spec covers the inflow side: PDF → raw → wiki, ready for Q-option lookup.

## Versioning policy (Copper directive 2026-04-26)

**Latest-edition-wins, edition-pinned in source layer.**

- 醫學知識半衰期短；專科考試以最新版本為主。**Current latest Brenner = 12e (2026)**；13e 將來出版時自動接管 default。
- **Source layer (`medwiki-raw/` + `medwiki/`)**：edition-pinned，**不刪舊版**。`BrennerRector11e_Ch19_*` 和 `BrennerRector12e_Ch19_*` 並存（13e 出版後再加 `BrennerRector13e_*`）。舊版保留為歷史 / cross-edition comparison 用。
- **Q-bank reference**：**topic-based, not chapter-number-based**. Chapter numbers shift between editions; topic concepts persist. Q frontmatter 用 `brenner_topic: "ckd-risk-prediction"` (slug)；resolver 查 topic→latest-edition chapter 動態解析。
- **Resolver rule**：`SELECT path FROM brenner_topic_index WHERE topic_slug = ? ORDER BY edition DESC LIMIT 1`. 預設用最新版；UI 可加 toggle 看舊版做 cross-edition diff。
- **Edition transition trigger**：當下一版（如 13e）開始入庫時，agent run 一次 `brenner_topic_index` 重建 — for each topic_slug，找最高 edition wiki 設為 canonical，舊版設 `superseded_by: 13e_chXX`。Q-bank 自動指向新版不需手動改。
- **Stale audit**：每月 cron 比對 PG 中 `cme_question_wiki_refs.wiki_path` vs `brenner_topic_index.canonical_path`；不一致 → 自動 update ref（無語意變更）或 flag opus review（topic 已合併/分裂等結構變動）。
- **Same policy applies to**：Nissenson (6e→7e), Daugirdas (6e→7e), Emma Pediatric (8e→9e), KDIGO guidelines (2024→2026), NephSAP (Vol N → Vol N+1).

## Scope (T0 = 2026-04-26)

| textbook | edition | status | gap |
|---|---|---|---|
| Brenner & Rector's The Kidney | 12e (2026) | 3/~70 chapters wikified | ~67 chapters |
| Nissenson & Fine Handbook of Dialysis Therapy | 6e (2023) | 0 wikified | full book (116 年指定) |
| Daugirdas Handbook of Dialysis | 6e | 39 slides synced (note/textbook-notes/), 0 wiki | full wiki layer |
| Emma Pediatric Nephrology | 8e (2022) | 0 wikified | full book (兒科) |
| Harrison Internal Med (nephro chapters) | 22e (2025) | 9 chapter raws + wiki at `clinical_medicine/internal_medicine/nephrology/Harrison22e_Ch*.md` | partial coverage |

## Source PDF inventory (verified 2026-04-26)

- **Brenner 12e**: 304MB 2-volume PDF at `~/Library/CloudStorage/Dropbox/VaultBinary_Backup/proj/medical-note/_archive/Brenner & Rector's The Kidney 2-volume set...pdf` (Jan 2025 mtime). Single mega-PDF; needs per-chapter split.
- **Brenner 11e**: archived zip at `~/Library/CloudStorage/Dropbox/VaultBinary_Backup/raw/books/_archive/2020_BrennerKidney_11e.zip`.
- **Nissenson 6e / Daugirdas 6e / Emma 8e**: PDF location TBD (Copper to provide; not located in vault search 2026-04-26).

## Ingestion modes

### Mode A — interactive `_inbox` drop (Copper-paced)

```
Copper drops PDF → ~/Library/CloudStorage/Dropbox/_Inbox/{anything}.pdf
                       ↓
   [hourly cron OR /wiki skill on demand]
                       ↓
   identify(textbook, edition, chapter) by:
     - filename heuristic (e.g. "BrennerCh19_*.pdf")
     - first-page extraction (chapter num + title)
     - manual chapter-num input via _inbox sidecar .json
                       ↓
   citationKey = {Series}{Edition}_Ch{NN}_{TitleSlug}
                       ↓
   dedup vs medwiki-raw/.../{citationKey}.md AND vs textbook chapters_raw table (PG)
                       ↓
   if new: stage to ~/VaultBinary/_sidecar/{citationKey}/source.pdf
                       ↓
   MinerU on hm4: mineru -p {pdf} -o /tmp/mineru_out/{key} -m auto -l en
                       ↓
   raw .md: medwiki-raw/clinical_medicine/internal_medicine/nephrology/{citationKey}.md
                       ↓
   _Inbox cleanup (rm dropped PDF after byte-OK verification per handover #612)
                       ↓
   trigger /wiki synthesis (Pattern B → wiki/{topic}/{citationKey}.md)
                       ↓
   trigger Q-option backlink: any Q in cme/bank/ with brenner_chapter==NN gets wiki refs auto-attached
```

### Mode B — bulk Brenner 12e split (one-shot)

For the existing 304MB 2-volume PDF that holds ~70 chapters:

1. Extract TOC via `mutool show {pdf} outline > brenner-toc.txt` → parse chapter page ranges.
2. For each chapter, `mutool extract {pdf} {start}-{end} -o ~/VaultBinary/_sidecar/BrennerRector12e_Ch{NN}_{TitleSlug}/source.pdf`.
3. Mineru batch (sequential).
4. Place raws.

Risk: TOC may not be machine-readable; PDF may be a screenshot OCR (per existing Brenner card mentioning VitalSource → Adobe OCR pipeline). If so, OCR-quality text extraction may fail; manual chapter splitting may be needed.

**Recommend Mode A first** (Copper-paced, low coupling). Mode B = TODO if Copper wants to backfill.

## Script: `scripts/textbook_ingest.py` (to create)

```python
# Pseudocode
import pathlib
INBOX = pathlib.Path("~/Library/CloudStorage/Dropbox/_Inbox").expanduser()
SIDE = pathlib.Path("~/VaultBinary/_sidecar").expanduser()
RAW = pathlib.Path("~/repos/medwiki-raw/clinical_medicine/internal_medicine/nephrology").expanduser()

def identify_textbook(pdf):
    # 1. filename heuristic
    # 2. fallback: pdftotext first 2 pages, regex chapter+series
    # 3. fallback: ask Copper via stdin (interactive) or sidecar .json drop
    return citation_key, series, chapter, title

def dedup(citation_key):
    # check medwiki-raw/.../{key}.md and PG textbooks.chapters_raw
    return is_new

def mineru(pdf, key):
    out = f"/tmp/mineru_out/{key}"
    subprocess.run(["mineru", "-p", str(pdf), "-o", out, "-m", "auto", "-l", "en"])

def place(key):
    # move /tmp/mineru_out/{key}/auto/*.md → medwiki-raw/.../{key}.md (with frontmatter)
    # move /tmp/mineru_out/{key}/auto/images/ → ~/VaultBinary/_sidecar/{key}/images/
    pass

def synth_wiki(key):
    # invoke /wiki skill or wiki-agent on the new raw
    pass

def synth_note(key, series, edition, ch, title):
    # invoke /note-writer skill (Opus mandatory per Law §0)
    # output: note/textbook/{series}-{edition}/{key}.md
    # NEVER flat to note/ root (Copper directive 2026-04-26 — hierarchy required)
    target_dir = NOTE_ROOT / "textbook" / f"{series}-{edition}"
    target_dir.mkdir(parents=True, exist_ok=True)
    out = target_dir / f"{key}.md"
    pass

def update_registry(key, doi=None, isbn=None, series=None, edition=None, ch=None, title=None):
    # INSERT/UPDATE article_registry.db (or migrate to PG vault_main.articles)
    # status: 'raw' after MinerU; 'wikified' after wiki synth; 'noted' after note-writer
    pass

def main():
    for pdf in INBOX.glob("*.pdf"):
        key, series, ch, title = identify_textbook(pdf)
        if dedup(key):
            stage = SIDE / key / "source.pdf"
            stage.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(pdf, stage)
            mineru(stage, key)
            place(key)
            synth_wiki(key)
            verify_byte_match(pdf, stage) and pdf.unlink()  # cleanup _Inbox per handover #612
```

## Cron schedule

- Hourly: `textbook_ingest.py --mode interactive` checks _Inbox, processes any new PDFs (off-peak only; peak window 21:00-02:00 TST skipped per Law §peak-hours).
- Tue 03:00 (burn window): `textbook_ingest.py --mode review` — verify all wikified chapters have option-level Q backlinks; flag orphan wikis (chapter wikified but no Q references it yet → write `dispatch:opus` TODO to generate Qs).

## Q-option backlink mechanism

When a new wiki entry lands at `medwiki/.../brenner12e_ch{NN}_{topic}.md`:

1. Index its sections (H2/H3 headers, KEY TAKEAWAYS, key tables, key figures).
2. For each existing Q with `brenner_chapter == NN`, scan its option-level `## Sources` block; if missing wiki ref, append `medwiki/.../brenner12e_ch{NN}_{topic}.md §{best-matching section}`.
3. Store mapping in PG `cme_question_wiki_refs (q_id, option_letter, wiki_path, section_anchor, score, created_at)`.
4. SPA reads this table at build to render per-option "為何這選項對/錯" with deep link to wiki.

## Multi-author ownership

- **Opus local**: identify_textbook (judgment-heavy), wiki synthesis quality.
- **Codex**: textbook_ingest.py implementation, MinerU error handling, Q-option backlink algorithm.
- **Gemma local**: cron worker (off-peak), bulk MinerU dispatch, byte-match verification.
- **Copper**: drop PDFs into _Inbox, approve identify_textbook fallback prompts.

## Definition of done — pipeline v0.1

- [ ] `scripts/textbook_ingest.py` exists, handles ≥1 PDF end-to-end (PDF→raw→wiki).
- [ ] Hourly cron entry registered in PG `schedule_registry`.
- [ ] First Brenner chapter dropped via _Inbox processed automatically.
- [ ] Q-option backlink populates `cme_question_wiki_refs` for that chapter.
- [ ] _Inbox cleanup gate enforced (post-byte-match rm).

## TODO

- [ ] Build `scripts/textbook_ingest.py` per pseudocode above — dispatch:codex:auto (2026-04-26)
- [ ] Build `cme_question_wiki_refs` table in PG vault_main — dispatch:codex:auto (2026-04-26)
- [ ] Decide Brenner 12e bulk-split vs Copper-paced mode — manual (2026-04-26)
- [ ] Source PDFs for Nissenson 6e / Daugirdas 6e / Emma 8e — manual (2026-04-26)
- [ ] Test pipeline E2E with one real Brenner chapter (Ch01 or Ch03) — dispatch:opus:manual (2026-04-26)
- [ ] Register cron in PG schedule_registry, off-peak only — plan:auto (2026-04-26)
