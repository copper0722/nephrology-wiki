# nephro-cme Interactive Q-Bank Upgrade Plan — 2026-04-26

## Status Audit

Current repo root is `/Users/copper/repos/nephro-cme` on branch `main`. Observed public repo structure is still the old parallel model: `note/`, `slides/`, `cme/`, `nephrology-cme-wiki/`, `docs/`, `scripts/`, `.github/workflows/marp-build.yml`. `README.md:L5-L12` says "three blocks" but lists four rows and still describes `/cme/` as "TSN 5-option question bank + rationale". `CLAUDE.md:L21-L28` also still documents the old 4-zone structure and `CLAUDE.md:L27` says `cme/` is TSN 5-option. The fresh pivot directive exists at `CLAUDE.md:L9-L19`, so the card is internally inconsistent.

`cme/` currently contains only protocol/readme/template plus 4 module files. There is no `cme/bank/`, no schema, no generated manifest, no interactive app. Existing module count is 17 questions: `nephrology-ckd-staging.md` has 10, `nephrology-pd-adequacy-rkf.md` has 2, `nephrology-pd-mechanical-complications.md` has 2, `nephrology-pd-peritonitis-management.md` has 3. All 4 modules use 5 visible options where each question has an `E` distractor. No existing module has `Correct answer: E`, so mechanical 5->4 conversion can usually drop/rewrite `E` without changing answer keys, but each explanation must be re-read.

`cme/_template.md` is 67 lines and explicitly uses `E` at `L39`, `Correct answer: <<A-E>>` at `L43`, distractor `E` at `L58`, and "5 options only (`A-E`)" at `L62`. `cme/CLAUDE.md` is 171 lines and still says 5-option at `L52`, `L58`, and `L68`. `cme/README.md:L27` says every question is A-E five options and `L48` says the repo does not track score, which conflicts with the new interactive target.

`docs/index.html` and `.github/workflows/marp-build.yml` already prove GH Pages-style static delivery exists, but it is slide-first. The workflow currently triggers only on `slides/**/*.md` and regenerates a slide landing page into `docs/index.html`; it does not build CME assets.

`scripts/` contains only `scripts/wiki_worker.py`. It is stale for this repo: constants point to `/Users/copper/dropbox/Vault/repos/nephrology-wiki`, `cme/bank/raw`, and `repos/nephrology-wiki`, while current repo is `/Users/copper/repos/nephro-cme`. `sync_canonical_updates()` and `generate_mcqs()` are `pass`, so no live CME generation pipeline exists.

Private recall sources are present under `/Users/copper/repos/note/tsn-exam-recall/`: `tsn-recall-2020-lin.md` 46L, `tsn-recall-2020-pdf.md` 85L, `tsn-recall-2021-anon.md` 100L, `tsn-recall-2021-wang.md` 172L, `tsn-recall-2023.md` 367L, `tsn-recall-2024.md` 317L. `CLAUDE.md:L20-L29` confirms 2022 missing. Binary originals also exist at `/Users/copper/repos/note/_binary/tsn-exam-recall/`; `unzip -l` verifies 17 media files in 2023 docx and 8 in 2024 docx.

NephSAP raw sources exist at `/Users/copper/repos/medwiki-raw/clinical_medicine/internal_medicine/nephrology/NephSAP_*.md`: 10 files, 4,900 total lines. However, current `.md` content does not contain extractable question stems/options/rationales. It contains issue content and a `# Self-Assessment Questions` pointer plus `# Self-Assessment Examination`; sample `NephSAP_Nephsap202408Vol23No3.md:L52` states the exam has thirty single-best-answer questions, and `L261-L362` points to the online exam, but the actual MCQ text is absent. No `_sidecar` directory or `source.pdf` was found under `/Users/copper/repos/medwiki-raw` or `/Users/copper/repos`. Therefore NephSAP Q extraction is still feasible, but Stage 0 must re-fetch authenticated exam/PDF material from `nephsap.org` or restore missing sidecars before parsing.

Existing git worktree was dirty before this plan: `CLAUDE.md` modified and multiple old `note/Ch*.md` deletions staged/unstaged by prior work. This plan does not depend on those changes and should not revert them.

## Pivot Rationale

Primary product should become `cme/` because candidate value is not "read more notes"; it is repeated answer selection, immediate explanation, and wrong-topic repair. Current notes/slides/wiki are supply layers. The public user should land on questions, not on agent-oriented M2M wiki. The repo already has candidate-facing `cme/README.md`, 17 working question examples, and GH Pages infrastructure in `docs/`; the lowest-risk pivot is to make a static interactive Q-bank that consumes markdown question files and writes no server-side state.

Recommended delivery surface: GH Pages static SPA reading generated JSON from markdown frontmatter/body. It wins on hosting cost (zero), agent automation (markdown in git remains source of truth), candidate UX (radio selection, reveal, score, filters, local resume), and public-safety (no backend, no accounts, no private raw). Jupyter/notebook is weaker for ordinary candidates and harder on mobile. Anki `.apkg` should be an export target after v0.1, not primary, because it hides source review and complicates attribution.

Question canonicality should be split. Private structured audit metadata belongs in PG `vault_main` per Law, e.g. `cme_question_sources`, `cme_publication_audit`, `license_class`, `review_state`. Public repo canonical artifact should be `.md` question files plus generated JSON. No SQLite/CSV as canonical. The public `.md` must be sufficient to rebuild the website, while PG stores non-public source fingerprints, license decisions, reviewer state, and ingestion logs.

## Architecture

Keep existing paths stable for v0.1, then add bank/app layers. Do not move the 4 existing modules until links are repaired.

Proposed repo shape:

```text
/Users/copper/repos/nephro-cme/
  README.md                         # candidate-first, points to docs/qbank/
  CLAUDE.md                         # card, cme-centric rules
  cme/
    README.md                       # author + candidate guide, 4-option only
    CLAUDE.md                       # protocol card, 4-option only
    _template.md                    # single-question/module template
    _schema/question.schema.json    # to create; validates frontmatter/body
    nephrology-*.md                 # current 4 modules, converted in place
    bank/                           # to create; primary public question bank
      nephsap/<issue>/qNNN.md       # paraphrased NephSAP-derived items
      recall/<year>/qNNN.md         # public-safe rewritten recall vignettes
      oa/<source-key>/qNNN.md       # OA CME-derived items
    index.json                      # generated, not hand-edited
  docs/
    index.html                      # qbank landing replaces slide-only landing
    qbank/                          # static SPA assets
  scripts/
    build_cme_index.py              # to create
    extract_nephsap.py              # to create
    oa_ingest.py                    # to create
    recall_rewrite_queue.py         # to create
    validate_cme.py                 # to create
```

Question file frontmatter should be per-question, not per-module only. Module markdown can remain curated review sets, but the interactive engine needs stable IDs. Required fields: `id`, `source_kind`, `source_path`, `license_class`, `public_safety`, `topic`, `tags`, `difficulty`, `bloom_level`, `brenner_chapter`, `guideline_refs`, `answer`, `review_state`, `author`, `date`. Body standard: stem, options A-D, answer explanation, distractor analysis A-D, source links. `scripts/build_cme_index.py` parses all `cme/**/*.md`, rejects any A-E item, and writes `cme/index.json` plus `docs/qbank/questions.json`.

## Pipeline Designs

NephSAP extraction. Source inventory is the 10 verified files in `medwiki-raw/.../nephrology/NephSAP_*.md`. Stage 0 is mandatory because current `.md` files only expose issue article text and online exam metadata, not MCQs. Authenticated fetch should use Copper's logged-in browser/session or exported source PDFs and store raw private captures under medwiki-raw sidecar paths, not `nephro-cme`. Parser input target: restored `source.pdf`/HTML per citation key. Parser output target: public-safe paraphrases in `cme/bank/nephsap/{vol23-no3|vol23-no4|...}/qNNN.md`. Validation gates: exactly four options A-D, one answer key, rationale present, no verbatim ASN wording, no copied figure, source citation only to issue/topic. Realistic first pass: if each full issue exposes 30 online exam questions as stated in raw files, four issues can supply >=100 candidates; 10 issues imply about 240-300 candidates, but current repo cannot reach that until authenticated exam capture is restored.

OA CME collection. Existing local root is `/Users/copper/repos/medwiki-raw/clinical_medicine/internal_medicine/nephrology/` with 164 `.md` files and several KDIGO files verified (`KDIGO2026AKI.md`, `CKD/blood_pressure/KDIGO2021BPCKD.md`, `glomerular/iga/KDIGO2025IgANephropathy.md`, etc.). AJKD Core Curriculum, CJASN ASN-IN-Review, ASN Kidney News, and NKF SCM are not yet visible as dedicated local source queues from the audit; crawler should create entries under the same medwiki-raw nephrology tree after license classification. Discovery methods: PubMed query for review/core curriculum, Crossref/Unpaywall license lookup, society page RSS/sitemap where available, and NephSAP authenticated inventory. Cadence: weekly off-peak Tue 03:00-09:00 TST for heavy crawling; daily lightweight metadata check allowed via non-CC workers. License classes: `oa_full_reuse`, `oa_derivative_ok`, `fair_use_citation_only`, `private_only`, `blocked_unknown`. Only `oa_full_reuse`/`oa_derivative_ok` may feed public paraphrased CME automatically; `fair_use_citation_only` needs short citation plus original question generation from concepts; `private_only` remains PG/raw only.

Recall vignette rewrite. Private source is `/Users/copper/repos/note/tsn-exam-recall/`; public output is `cme/bank/recall/{2021|2023|2024}/`. 2020-lin and 2020-pdf are topic recalls only, so they should generate gap-analysis TODOs and wiki coverage checks, not direct MCQs. 2021-anon has 9 traditional + 6 clinical A-D MCQs; 2021-wang has 18 clinical A-D MCQs; 2023 has chapter recall + ~20 A-D MCQs plus 17 images; 2024 has 43 topic items + multiple A-D MCQs plus 8 images. Rewrite protocol: change age/sex/comorbidity/lab values, preserve medical logic, replace exact answer wording, remove source attribution/year labels, cite only general topic source. Image-dependent items: extract private media from binary docx to private sidecar for analysis, then publish either text-only equivalent, stylized original SVG/diagram, or skip if the image is essential and likely copyrighted.

## Interactive Mechanism Spec

Build a static SPA under `docs/qbank/`. Data source is generated `questions.json`; source of truth remains markdown. Core UI: topic/sidebar filter, random mode, sequential mode, one-question screen, A-D radio buttons, submit, immediate correct/incorrect state, reveal explanation, distractor analysis, source links, next question. Store only local progress in `localStorage`: answered IDs, selected option, correctness, timestamps, topic weakness counts, current streak, reset button. No login, no server, no analytics.

Markdown fallback should use `<details><summary>Reveal answer</summary>` or generated answer sections so GitHub readers can still use files without JS. The SPA should hide answers until submit/reveal; this is UX only, not security. Build validation must fail if any item has option E, missing answer, duplicate ID, `source_kind=recall` without `public_safety: rewritten`, or `license_class` absent.

Initial UI should not be a marketing landing page. `docs/index.html` should become the qbank first screen with a secondary link to slides. Existing slide build can stay under `docs/slides/`.

## TSN Fix Scope

Exact stale files and lines observed:

- `/Users/copper/repos/nephro-cme/CLAUDE.md:L27`: old `TSN 5-選項格式題庫` -> `TSN 4-option (A-D) interactive question bank`. `L15` also says "line 314" must change, but actual `L314` is not a TSN-format line; update that directive note to point at `L27` or remove the stale line-number claim.
- `/Users/copper/repos/nephro-cme/README.md:L12`: old `TSN 5-選項題庫 + rationale` -> `TSN 4-option interactive Q-bank + answer reveal + score`.
- `/Users/copper/repos/nephro-cme/cme/README.md:L27`: old `A-E 五個選項` -> `A-D 四個選項`; `L48` should change from "repo does not track score" to "browser localStorage tracks score locally".
- `/Users/copper/repos/nephro-cme/cme/CLAUDE.md:L52`: old `Still use 5 options (A-E)` -> `Use 4 options (A-D)`. `L58`: old `5 options (A-E)` -> `4 options (A-D)`. `L68`: old `Five options (A-E)` -> `Four options (A-D)`.
- `/Users/copper/repos/nephro-cme/cme/_template.md:L39`: remove `E. <<OPTION E>>`; `L43` `<<A-E>>` -> `<<A-D>>`; `L58` remove E distractor row; `L62` `5 options only (A-E)` -> `4 options only (A-D)`.
- `/Users/copper/repos/nephro-cme/cme/nephrology-ckd-staging.md`: remove/rewrite E option + E distractor analysis at `L33/L50`, `L66/L83`, `L99/L116`, `L132/L149`, `L165/L182`, `L198/L215`, `L231/L248`, `L264/L281`, `L301/L318`, `L334/L351`.
- `/Users/copper/repos/nephro-cme/cme/nephrology-pd-adequacy-rkf.md`: `L11` says TSN 5-option; change to 4-option. Remove/rewrite E at `L39/L58` and `L76/L95`.
- `/Users/copper/repos/nephro-cme/cme/nephrology-pd-mechanical-complications.md`: `L11` says TSN 5-option; change to 4-option. Remove/rewrite E at `L39/L58` and `L76/L95`.
- `/Users/copper/repos/nephro-cme/cme/nephrology-pd-peritonitis-management.md`: `L11` says TSN 5-option; change to 4-option. Remove/rewrite E at `L39/L58`, `L76/L95`, `L113/L137`.

Conversion rule: do not blindly delete all E text if it is the best distractor. For each item, keep the best 3 distractors among A-E, ensure the keyed answer remains A-D, then rewrite distractor analysis to A-D only. Existing answer keys are not E, so no re-keying is expected.

## Multi-Author Collaboration

New ownership model:

- Opus local = Editor-in-Chief. Owns medical correctness, public-safety review, recall rewrite approval, final v0.1 release gate.
- Opus cloud = OA discovery and source acquisition when legally public/OA. Runs off-peak or low-intensity metadata jobs; no peak heavy CC work.
- Codex = architecture, validators, extractor scripts, CI/GH Pages app, adversarial audit, line-number migration checks.
- Gemma local/cloud = bulk draft worker for topic tagging, paraphrase candidates, distractor generation from approved sources. No final publish without Opus/Codex validation.
- Copper = manual decisions: NephSAP login/session access, 2022 recall request, copyright risk tolerance, public launch approval.

Git conventions: feature branches by lane (`feat/qbank-spa`, `data/nephsap-batch-001`, `fix/tsn-four-option`, `ingest/oa-cme`). Commit prefixes: `fix:`, `feat:`, `data:`, `review:`, `docs:`. No author deletes another author's content wholesale; replacement batches should add generated diff summaries. Public raw from recall/NephSAP is forbidden. Heavy ingestion scheduled outside 21:00-02:00 TST; non-CC workers may do parsing/tagging during peak if no CC quota is consumed.

## Two-Week Sprint Plan

Week 1:

1. Fix TSN 4-option surfaces: template, cme card, parent card, README/cme README, 4 modules. Add validator that fails on option E.
2. Add per-question schema and `scripts/build_cme_index.py`; generate first `cme/index.json`.
3. Build `docs/qbank/` static SPA with answer reveal and localStorage score. Repoint `docs/index.html` to qbank while preserving slides link.
4. Restore NephSAP Stage 0 input: authenticated capture or source PDFs for at least 4 issues. Prove parser on one issue and produce 20 paraphrased draft questions in private review state.
5. Start recall conversion: 2021-anon and 2021-wang into rewritten public-safe drafts; 2020 files into gap-analysis queue.

Week 2:

1. Scale NephSAP extraction to >=100 reviewed public-safe questions across at least 4 issues.
2. Convert selected 2023/2024 recall questions, excluding unresolved image-dependent items until diagrams are rebuilt.
3. Add OA source registry + license classifier; seed with verified local KDIGO files and external discovery targets for AJKD/CJASN/Kidney News/NKF.
4. Add CI/GH Action validation for schema, A-D only, duplicate IDs, broken links, and public-safety flags.
5. Opus editorial review + Codex adversarial audit, then launch v0.1 on GH Pages.

v0.1 DoD:

- >=100 public-safe A-D questions.
- All existing 17 questions converted to A-D.
- `docs/qbank/` live with answer reveal, scoring, reset, topic filters.
- Every question has source_kind, license_class, topic tags, answer, explanation, distractor analysis.
- No verbatim exam recall, no NephSAP copied stems, no private attribution, no paywall excerpts.
- Build validator passes locally and in GitHub Actions.
- README first viewport points candidates to interactive qbank.

## Recommendation Summary

Default decision: build a GH Pages static SPA and keep markdown as the public source of truth. Do not make Jupyter or Anki primary. Treat NephSAP as first high-volume source, but do not assume current `medwiki-raw` files contain MCQs; restore authenticated exam/PDF capture first. Treat recall files as private raw only; publish rewritten vignettes, never source-like stems. Fix A-D format before generating new volume, otherwise every downstream validator and UI will encode the wrong exam shape. Open Copper decisions: NephSAP auth handoff, 2022 recall request, and whether ASN-derived paraphrases are acceptable for public educational release or should remain private until reviewed.

## Refinement Appendix (Copper directives 2026-04-26 mid-session)

**R1 — Q-as-entity (not note-as-entity).** Question is the primary record. Each option (A-D) carries its own textbook-anchored "Why" block (right or wrong, sourced from textbook). Notes/wiki are retrieval targets for option blocks, not standalone deliverables. Implementation: `cme/_template-v2.md` written with per-option `## Why` + `## Sources` blocks. Old aggregated module files (cme/nephrology-{topic}.md) deprecated; one Q = one .md under `cme/bank/{source}/{id}.md`; module = view filter on the bank.

**R2 — Continuous textbook feeding (Brenner gap).** Brenner 12e is the largest gap: 3/~70 chapters wikified. 304MB 2-volume PDF exists at `~/Library/CloudStorage/Dropbox/VaultBinary_Backup/proj/medical-note/_archive/Brenner & Rector's The Kidney 2-volume set...pdf`. Ingestion pipeline spec at `nephro-cme/_textbook-ingest-pipeline.md`. Mode A (Copper-paced _Inbox drop, hourly cron) recommended over Mode B (bulk PDF split — risky if scanned/OCR). Q-option backlink stored in PG `cme_question_wiki_refs` table.

**Reconciled architecture under R1 + R2:**

```
PDF (Brenner ch / NephSAP issue / OA review) ─→ MinerU ─→ medwiki-raw/.../{key}.md
                                                              │
                                                              ↓ /wiki synth
                                                  medwiki/.../{topic}/{key}.md
                                                              │
                                                              ↓ Q-option backlink
                                              PG cme_question_wiki_refs
                                                              │
                                                              ↓
       cme/bank/{source}/{id}.md (Q-as-entity, 4-D, per-option Why+Sources)
                                                              │
                                                              ↓ build_cme_index.py
                                              cme/index.json + docs/qbank/questions.json
                                                              │
                                                              ↓
                                              GH Pages SPA (interactive, localStorage)
```

**Schema delta vs Codex original**:
- Original: per-question frontmatter at module level
- Refined: per-question .md file + per-option Why blocks + brenner_chapter required + license_class controls publish gate
- Aggregated module files retired; module = filter view, not file artifact

## TODO

- [ ] Pivot README and CLAUDE cards so `cme/` is the primary product and note/slides/wiki are support layers — plan:auto (2026-04-26), codex-upgrade-plan
- [ ] Convert `cme/_template.md`, `cme/CLAUDE.md`, `cme/README.md`, parent `CLAUDE.md`, and all 4 modules from A-E to A-D — bug:auto (2026-04-26), codex-upgrade-plan
- [ ] Add `scripts/validate_cme.py` to reject option E, missing answer, duplicate ID, and missing license/public-safety fields — dispatch:auto (2026-04-26), codex-upgrade-plan
- [ ] Create per-question markdown schema and generated `cme/index.json` manifest — dispatch:auto (2026-04-26), codex-upgrade-plan
- [ ] Build GH Pages static qbank app with answer reveal, localStorage score, filters, and reset — dispatch:auto (2026-04-26), codex-upgrade-plan
- [ ] Repoint `docs/index.html` from slide-only landing to qbank-first landing with slides as secondary navigation — plan:auto (2026-04-26), codex-upgrade-plan
- [ ] Restore NephSAP Stage 0 source capture because current 10 raw `.md` files lack actual MCQ stems/options/rationales — blocked:manual (2026-04-26), codex-upgrade-plan
- [ ] Implement authenticated NephSAP extractor and parser for 4-option question, answer, rationale, topic, and figure refs — dispatch:auto (2026-04-26), codex-upgrade-plan
- [ ] Produce >=100 public-safe paraphrased NephSAP-derived questions under `cme/bank/nephsap/` — dispatch:manual (2026-04-26), codex-upgrade-plan
- [ ] Build OA CME source registry and license classifier for AJKD Core Curriculum, CJASN/ASN review, KDIGO, Kidney News, and NKF SCM — plan:auto (2026-04-26), codex-upgrade-plan
- [ ] Seed OA pipeline from verified local KDIGO files in `medwiki-raw/.../nephrology/` — dispatch:auto (2026-04-26), codex-upgrade-plan
- [ ] Convert 2020 recall files into wiki/CME gap-analysis queue, not direct MCQ — plan:auto (2026-04-26), codex-upgrade-plan
- [ ] Rewrite 2021-anon and 2021-wang recall MCQs into public-safe A-D vignettes — dispatch:manual (2026-04-26), codex-upgrade-plan
- [ ] Extract 2023 and 2024 recall images privately and rebuild only original/stylized public diagrams where needed — dispatch:manual (2026-04-26), codex-upgrade-plan
- [ ] Ask Kuo LiYuan or other peers for missing 2022 recall source — manual:manual (2026-04-26), codex-upgrade-plan
- [ ] Add PG audit metadata design for private source fingerprints, license decisions, and review state — plan:manual (2026-04-26), codex-upgrade-plan
- [ ] Define branch/commit conventions and release review gate for Opus/Codex/Gemma collaboration — plan:manual (2026-04-26), codex-upgrade-plan
- [ ] Launch v0.1 only after >=100 questions, A-D validation, GH Pages score UI, and public-safety review pass — review:manual (2026-04-26), codex-upgrade-plan
