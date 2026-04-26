---
schema_version: 2
id: <citationKey>          # e.g. tsn2024-q03 / nephsap-vol22-no1-q12 / brenner12e-ch19-q4
source_kind: <recall|nephsap|brenner|nissenson|harrison|daugirdas|self|other>
source_path: <vault path of authoritative source>
source_year: <YYYY>
license_class: <oa_full_reuse|oa_derivative_ok|fair_use_citation_only|private_only|blocked_unknown>
public_safety: <verbatim|paraphrased|rewritten>   # public-publishable iff in {paraphrased, rewritten} AND license allows
review_state: <draft|opus_review|copper_approved|published>
topic_tags: [<_s/im/nephrology/...>, ...]
brenner_topic: <slug>      # topic-slug, e.g. ckd-risk-prediction. Resolver picks latest-edition wiki via brenner_topic_index. Chapter numbers shift across editions; topic persists.
brenner_topic_secondary: [<slug>, ...]    # other Brenner topics touching same Q (optional)
guideline_refs: [KDIGO-CKD-2024, KDOQI-..., ...]    # optional
difficulty: <recall|application|analysis>
bloom: <remember|understand|apply|analyze|evaluate>
answer: <A|B|C|D>
date: <YYYY-MM-DD>
author: <opus|codex|gemma|copper>
---

# <Q-title in zh-TW>

## Stem

> <Stem prose, zh-TW. No source attribution, no exam-year markers, vignette fictionalized.>

## Options

### A. <Option A text>

**Status**: ✅ Correct  /  ❌ Incorrect

**Why** (textbook-anchored, ≤6 lines):
> <Explain by citing Brenner 12e Ch{NN} §{section title}, page/figure/table ref. State the medical reason this option is right or wrong. Keep evidence-tight; no speculation.>

**Sources**:
- Brenner 12e Ch{NN} (`medwiki/.../brenner12e_chNN_<topic>.md` §{section})
- KDIGO 2024 CKD §{recommendation number} (if applicable)
- Other landmark trials only if pivotal (NEJM/JAMA/Lancet/KI/JASN with author + year + N)

### B. <Option B text>

**Status**: ✅ Correct  /  ❌ Incorrect

**Why**:
> <Same structure as A.>

**Sources**:
- ...

### C. <Option C text>

**Status**: ✅ Correct  /  ❌ Incorrect

**Why**:
> <Same.>

**Sources**:
- ...

### D. <Option D text>

**Status**: ✅ Correct  /  ❌ Incorrect

**Why**:
> <Same.>

**Sources**:
- ...

## Distractor logic

<Concise 2-3 lines: why each wrong option is plausibly chosen but wrong. Test-taker training perspective. Optional if option-level Why blocks already cover this.>

## Cross-links

- Wiki topic: `medwiki/clinical_medicine/internal_medicine/nephrology/<topic>/...`
- Related Q: `cme/bank/<source>/<id>.md` (id-only, not full path)
- Source raw: `medwiki-raw/clinical_medicine/internal_medicine/nephrology/<key>.md` (private if license restricts)

---

## Build rules (delete this whole `## Build rules` section before publishing)

1. **Format invariant**: 4 選項 (A-D) only. Single best answer. Stem in zh-TW; technical tokens inline English.
2. **Q-as-entity**: every option carries its own textbook-anchored Why block. Wiki content is option-level, not topic-monolithic.
3. **Public-safety**: NO verbatim NephSAP / Brenner / 學長姐 stems. Vignettes rewritten (age/sex/lab values changed; medical logic preserved). No exam-year attribution. No author (林家宏/匿名/etc.).
4. **Source citation**: every Why block must point at a wiki section that itself points back to verbatim raw.md. Three-hop traceability.
5. **Brenner ref required (topic-based)**: every Q must declare a primary `brenner_topic` slug. Resolver auto-picks latest-edition chapter via `brenner_topic_index` PG table — survives 12e→13e transition without per-Q rewrite. If no Brenner topic applies, escalate to Copper before publish (Q tests outside Brenner scope — likely Nissenson/Daugirdas/Emma/guideline-only).
6. **License gate**: `license_class` controls publish path. `private_only` → never publish; stay in private layer. `fair_use_citation_only` → paraphrase + cite, no verbatim quotes >2 sentences. `oa_*` → reuse OK with attribution.
7. **One Q = one .md file** under `cme/bank/{source}/{id}.md`. Aggregated module files (`cme/nephrology-{topic}.md`) deprecated; module = view filter on the bank, not a file.
8. **No copied figure**: image-dependent Qs must rebuild diagrams as Mermaid/SVG, OR cite the figure ref in Brenner without embedding the original image.
9. **CR/LF**: LF only. UTF-8 no BOM.
10. **Indexing**: `scripts/build_cme_index.py` reads frontmatter and writes `cme/index.json` for the SPA.
