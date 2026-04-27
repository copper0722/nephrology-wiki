# nephro-cme — 腎專考試複習專區 (Nephro Board Exam Review Center)

GitHub: `copper0722/nephro-cme` (public)

## Purpose

TSN 腎臟專科甄試考試導向的複習專區。Vault canonical wiki 的**考試特化投影**。

## Strategic Direction (Copper directive 2026-04-26)

**Pivot 1 — Interactive Q&A focused, Q-as-entity (Copper refinement 2026-04-26).** 此 repo 的核心 deliverable 是「互動式考題」(interactive question bank)。原先 4-zone（note / slides / cme / wiki）裡 **`cme/` 升格為 primary product**；note/slides/wiki 為 supporting source layer 而非並列。**Question = primary entity, NOT note**: 每題 = 1 stem + 4 options + 4 option-level wiki blocks（每個選項配一段教科書錨定的解釋——為何這選項對 / 錯）。Wiki content 從 textbook-derived 而非自由聯想。出口讓考生互動作答 + 即時看到選項層級的 textbook explanation + wiki cross-link。

**Pivot 2 — Continuous OA CME ingestion capability.** Agent 必須持續搜集 open access nephrology CME — NephSAP / ASN Kidney Self-Assessment / KDIGO board review / AJKD Core Curriculum / CJASN ASN-IN-Review 等。建立 cron pipeline：source discovery → license check → wikify → MCQ extraction → question bank append。**不再是一次性人工 wikify**。

**Pivot 3 — TSN exam = 4-選項 (A-D), single best answer.** 2026-04-26 verified from raw 學長姐 recall 2020/2021/2023/2024（Kuo LiYuan FB DM 觸發 + raw content 證實）。**所有 cme/ 模組（含 4 既存）+ `cme/_template.md` + `cme/CLAUDE.md` + `cme/README.md` + `nephro-cme/README.md` 必須 5→4 重作**。具體 line edits 見 `_upgrade-plan-codex-2026-04-26.md` §TSN Fix Scope。

**Pivot 4 — NephSAP 為 Q-bank 主軸.** Vault 已有 **10 卷 NephSAP raw** at `medwiki-raw/clinical_medicine/internal_medicine/nephrology/NephSAP_*.md` (Vol23 No3-5 + Vol24 No1-5 + 兩本特刊, 共 4,900 行)。這是 ASN 官方 self-assessment, **大量 case-based MCQ + rationale**, license 容許學術轉譯（去識別 + paraphrase）。**第一波應在此完成 ≥100 題互動化**, 不要重新 wikify-from-scratch。

**Pivot 5 — Latest-edition-wins, topic-based Q ref (Copper directive 2026-04-26).** 醫學知識半衰期短，專科考試以最新版本為主。**Current latest = Brenner 12e (2026)**, 已 3 章 full note (Ch19/55/63) at `~/repos/note/textbook/brenner-12e/`。13e 將來出版時自動接管 default — pipeline 設計就以多版本切換為前提。Source layer (`medwiki-raw/` + `medwiki/`) edition-pinned 並存（11e/12e/13e 共存不刪舊）；Q-bank 用 **topic slug** 而非 chapter number 對應 textbook，由 `brenner_topic_index` PG table resolver 自動指向最新版。同 policy 適用 Nissenson 6e→7e、Daugirdas 6e→7e、Emma 8e→9e、KDIGO 2024→2026、NephSAP Vol N→N+1。詳見 `_textbook-ingest-pipeline.md` §Versioning policy + `cme/_template-v2.md`。

**Source for raw 學長姐 recall (private)**: `note/tsn-exam-recall/tsn-recall-{2020-lin,2020-pdf,2021-anon,2021-wang,2023,2024}.md`. 2022 缺漏 (Kuo DM 標註).

## Repo 2-Zone Structure (2026-04-27 — pivot finalized)

**Scope finalized per Copper directive 2026-04-27**: nephro-cme = exam questions + wiki answers ONLY. `/note/` and `/slides/` archived (see `_archive/2026-04-27-pre-pivot/`) — they violated the new scope (notes belong in `~/repos/note/`, slides belong on BoAn website per opt-in publish).

| Zone | 路徑 | 語言 | 目標讀者 | 內容 |
|---|---|---|---|---|
| **1. cme** | `/cme/` | zh-TW | 考生 | TSN 4-option (A-D) interactive Q-bank、answer reveal、per-option why、local score tracking。**Primary product.** |
| **2. nephrology-cme-wiki** | `/nephrology-cme-wiki/` | M2M English | CC agents | Q-rationale source layer。每選項 (A-D) 配一段 textbook-anchored 解釋。Wiki content 從 vault `medwiki/` + private `~/repos/note/textbook/` 衍生（不手改本 repo 內 wiki 條目）。|

**Archived zones** (do not delete; per Law §1.3):
- `_archive/2026-04-27-pre-pivot/note/` — 5 .md (3 superseded brenner12e chapters + README); future Copper-readable notes go to `~/repos/note/textbook/{book}/` (private vault)
- `_archive/2026-04-27-pre-pivot/slides/` — 50 .md (Daugirdas slides); future slide-deck publish goes to BoAn website via `~/repos/boan-website/scripts/boan-web-publish.py` (opt-in per article, not auto-sync)

**Source of truth for nephrology textbook content**: `~/repos/note/textbook/{book}/` (private vault) + `~/repos/medwiki-raw/clinical_medicine/internal_medicine/nephrology/_textbooks/{book}/` (raw). NOT in this repo.

Cross-refs: `textbook-notes` repo (non-nephro slides) being archived 2026-04-27 → BoAn website becomes sole share target for textbook slides.

## Content Scope (Inflow Sources)

1. **指定教科書章節** → `/note/` — 每 chapter 一個 note
   - Brenner & Rector's Kidney 12e（vault canonical，TSN list 寫 11e 但 12e 可）
   - Nissenson & Fine, Handbook of Dialysis Therapy 6e (2023) — 116 年指定
   - Daugirdas 6e — Copper 主動加，雖非 TSN 指定但考試常出
   - Pediatric Nephrology (Emma 8e 2022) — 小兒科
   - （Henrich Dialysis 5e 2017，115 年指定，可選）

2. **指定期刊 review articles** → `/note/` — 每篇 review 一個 note
   - Kidney International, AJKD, JASN, CJASN, Pediatric Nephrology, Acta Nephrologica
   - Rolling 1-year window (116 年: 2026-07-01 to 2027-06-30)
   - 掃 PubMed `publication_type=Review` filter + journal filter
   - OA 自動抓+ wikify；非 OA → Zotero metadata-only + Copper 手動下載 PDF

3. **考古題 recall / 考試邏輯** → `/cme/`
   - 每題 **TSN 4-選項 (A-D) 格式** + rationale (5-選項 deprecated 2026-04-26)
   - 來源：考古題 recall (private at `note/tsn-exam-recall/`)、NephSAP、AJKD Core Curriculum、章末題、自製

4. **Wiki synthesis** → `/nephrology-cme-wiki/` (strict rule, 2026-04-19)
   - 由 `/note/` 中 `publish: true + publish_to: nephro-cme` 的 notes，按 `wiki_topic:` aggregate，script overwrite-style 產出
   - 非 independent write、non-editable；要改 wiki → 改 source note
   - Deferred 至 `/note/` ≥30 才啟動 synthesizer
   - 2026-04-19 前內容已 archive 至 `_archive/nephrology-wiki-pre-strict-rule-2026-04-19.zip` (vault-side)

5. **Teaching slides** → `/slides/{book}/` (2026-04-19 new zone, migrated from textbook-notes)
   - 由 `/note/` 中 `publish: true + publish_to: nephro-cme` 的 notes，抽取 `## TEACHING SLIDES` section → Marp .md + GH Actions render .html
   - 2026-04-19 初始遷入 39 個 Daugirdas 6e 章節 slides

## Source Hierarchy — Textbook First (Law, 2026-04-12)

| 面向 | Vault wiki (canonical) | This repo (考試) |
|---|---|---|
| 目的 | Copper 的私人 Wikipedia | TSN 專科考試準備，公開 |
| 讀者 | CC agent + Copper | 考生 + Copper |
| 格式 | M2M compressed English | 考試導向，key facts + 考題邏輯 |
| 範疇 | 全面（基礎→臨床→政策→運動） | 聚焦考題範圍（教科書章節對應） |
| EBM | 完整 GRADE/causal (/med-read) | 精簡：正確答案的邏輯 |
| 更新 | 持續（all sources） | 考前密集（教科書+考古題+一年內 review） |

## Knowledge Flow

```
Sources (textbooks, reviews, guidelines)
  ↓ /med-read (now part of /wiki)
Vault canonical wiki (wiki/)
  ↓ filter: exam-relevant topics only
  ↓ reformat: key facts + 考題邏輯 (not full EBM appraisal)
This repo (repos/nephro-cme/nephrology-cme-wiki/ + note/ + slides/ + cme/)
  ↓ textbook-share-sync.py (launchd) + repos-auto-push.sh (cron 10min)
  ↓ git push
GitHub (public, 考生使用)
```

**Vault → repo, NOT repo → vault.** Canonical wiki 是 upstream。This repo 是 downstream export。

## TSN Board Exam — Official Designated Materials (2026-04-13)

Source: TSN 腎臟專科醫師甄審規則 第三、四、五條 + 推薦書籍清單。

### Designated Journals (Review articles only, **1-year window**)

| Journal | Abbrev | OA | PubMed indexed |
|---|---|---|---|
| Kidney International | Kidney Int | hybrid | ✓ |
| American Journal of Kidney Diseases | Am J Kidney Dis | hybrid | ✓ |
| Journal of the American Society of Nephrology | J Am Soc Nephrol | subscription | ✓ |
| Clinical Journal of the American Society of Nephrology | Clin J Am Soc Nephrol | subscription | ✓ |
| Pediatric Nephrology | Pediatr Nephrol | hybrid | ✓ |
| 台灣腎臟醫學會雜誌 (Acta Nephrologica) | Acta Nephrol | likely full_oa | partial (TSN-published) |

**Article-type filter**: review articles only. Not original research, case reports, editorials.
**Date window**: rolling 1 year before exam date.
- 115 年甄試 window: 2025-07-01 to 2026-06-30
- 116 年甄試 window: 2026-07-01 to 2027-06-30
- 117 年 / 118 年 etc.: shift +1 year each.

### Designated Textbooks

**115 年 甄試** (TSN 推薦清單):
1. **Brenner & Rector's The Kidney, 11e (2020)**
2. **Principles and Practice of Dialysis** (Henrich), 5e 2017
3. **Pediatric Nephrology** (Avner / Harmon / Niaudet), 7e 2016 [小兒科]

**116 年 甄試** (TSN 推薦清單):
1. **Brenner & Rector's The Kidney, 11e (2020)** (TSN list 仍寫 11e，但實務以最新版讀)
2. **Handbook of Dialysis Therapy** (Nissenson / Fine), 6e 2023 ← Henrich Dialysis dropped, replaced
3. **Pediatric Nephrology** (Emma / Goldstein / Bagga / Bates), 8e 2022 [小兒科]

**Brenner edition policy (2026-04-13)**: vault canonical = **12e (2026)**. 雖然 TSN 推薦清單寫 11e，**讀最新版於專科醫師考試沒有問題**（內容延伸、不會少考），不需 un-archive 11e。Wiki 與 note pipeline 全以 12e 為 anchor。

### Exam Structure

- Part A: 傳統考題 (textbook + classic concepts)
- Part B: 臨床考題 (case-based)
- 口試 (oral)
- 筆試通過、口試未過 → 筆試 3 年保留，下次只考口試

### Eligibility (摘要)

- 內/兒科專科醫師 + 腎臟訓練 ≥ 2 年
- 腎臟繼續教育積分 ≥ 150 單位（A 類 ≥ 125）
- ≥ 1 篇第一作者腎臟論文（台腎雜誌 / SCI / 學會討論會）
- 若海外腎專（美/日/歐/加/南非/澳/紐/星/港）→ 免訓練要求

### Application to wiki coverage

- Wiki 涵蓋 8 sections（見下方 Scope）— 對應 Brenner 11e 章節 + Nissenson Ch / Henrich Ch
- 每月掃 6 本指定 journal review articles → wikify within window
- 1-year rolling window 重要：超過窗口的 review 雖然可參考但不會出題

## Source Hierarchy — Textbook First

**All textbooks are highly trusted sources for wiki.** For nephro-wiki specifically, nephrology textbooks are the primary source.

| tier | source | trust level | use |
|---|---|---|---|
| **T1 — Nephrology textbooks** | Brenner & Rector 12e, Daugirdas 6e, Nissenson 6e, Harrison nephrology chapters | highest | **primary source for every wiki topic** |
| T2 | KDIGO/KDOQI/ISPD guidelines (latest version) | very high | superseded by newer version |
| T3 | Landmark RCTs + systematic reviews (NEJM/JAMA/Lancet/KI/JASN) | high | cite for specific evidence |
| T4 | Society statements (TSN/ASN) | moderate-high | Taiwan-specific context |
| T5 | Cohort studies, case series, review articles (non-landmark) | moderate | supplementary |

**Rule:** every wiki entry MUST have textbook reference as primary anchor. Add secondary refs (RCTs/guidelines) on top. A wiki built only from journal articles without textbook backing = incomplete.

**Textbook update rule:** always use latest edition. Older editions only for historical comparison. Brenner 11e (2020) archived; Brenner 12e (2026) canonical.

## Exam-Specific Protocol

1. **考古題 mapping**: 考題 → 對應教科書章節 → gap analysis → vault wiki 有就 export，沒有就先 vault wikify 再 export
2. **正確答案邏輯**: 每個 wiki entry 不只列 facts，要解釋「為什麼這是正確答案」「哪些選項是 distractor」
3. **教科書對應**: 每個 topic 標註來源教科書+章節（Brenner Ch.X, Nissenson Ch.Y）
4. **一年內 review**: 考前掃 PubMed — KI/AJKD/JASN/CJASN/PedNephrol review articles within exam window
5. **Gap fill priority**: 考古題出現但 wiki 沒有 → 最高優先 wikify

## Scope — TSN Exam Topics ONLY

Based on 2025 exam recall (~160 questions), this repo covers ONLY these 8 sections:

| # | topic | examples |
|---|---|---|
| 01 | Electrolytes & acid-base | Na, K, Bartter, Gitelman, RTA, DI |
| 02 | CKD-MBD & stones | Ca, Mg, P, FGF23, phosphate binders, renal osteodystrophy |
| 03 | CKD & ESKD management | GFR, RRT, anemia, dermatology, geriatrics, palliative |
| 04 | Transplant | rejection, immunosuppression, BKV, donor eval |
| 05 | Hypertension | renovascular, aldosterone, ANP |
| 06 | Glomerular diseases | FSGS, MN, MPGN, lupus nephritis, ANCA, IgAN, Alport |
| 07 | AKI & toxicology | contrast, rhabdomyolysis, CRRT, urine studies |
| 08 | Tubular/TMA/Pregnancy/Peds/Genetics | Fanconi, HUS/TTP, ADPKD, Fabry, pediatric NS |

**EXCLUDED** (not part of TSN exam, belongs in vault canonical wiki only):
- Standalone cardiology (arrhythmia, atherosclerosis) — unless cardiorenal
- Standalone hematology (malignant/nonmalignant) — unless renal anemia
- Standalone infectious disease — unless UTI/pyelonephritis/BKV
- Standalone endocrinology — unless diabetic nephropathy/CKD-MBD
- General medicine, nutrition, public health, EBM methods, dementia
- Any topic not testable on TSN 腎臟專科甄試

**Rule**: if a topic's renal intersection is already covered in a nephrology wiki entry (e.g., renal anemia in CKD wiki), do NOT create a standalone non-nephro file. Renal-adjacent content belongs INSIDE the nephrology topic file.

Source: `wiki/wiki_tsn_board_exam.md` — 2025 考古題 recall analysis.

## Content Rules

- Language: M2M English (same as vault wiki — 考生也是醫師，能讀 M2M)
- **NO LaTeX**: Use Unicode characters for ions (e.g., K⁺, Ca²⁺) and symbols (→, ↑, Δ). GitHub renderer does NOT support LaTeX.
- **YAML Frontmatter Required**: Every entry MUST start with:
  ```yaml
  ---
  type: wiki
  generated: YYYY-MM-DD
  source: path/to/raw.md
  tags: [nephrology, ...]
  author: gemma4
  ---
  ```
- **Topic-based Naming**: H1 must be a topic (e.g., `# Hyperkalemia in Dialysis Patients`), NOT an article title.
- **Exam-Specific Structure**: Every entry MUST include:
  - **Exam Logic**: why this is the correct answer, common distractors.
  - **Textbook ref**: Brenner Ch.X, Nissenson Ch.Y, Daugirdas Ch.Z.
  - **Key trials**: author, year, N, bottom line.
- 不需要 PICO/GRADE/bias full appraisal — 考試要的是正確知識
- 但保留 key evidence（landmark trial names, NNT, GRADE recommendations from guidelines）
- 結構：topic-based（不是 per-article），按教科書章節組織

## ⚠️ PUBLIC FOLDER — No Personal Data

This folder is an **open git repo pushed to public GitHub**. Symlinked at `wiki/nephro-cme/`.

**NEVER put inside this folder:**
- Patient data, clinic info, personal notes
- Copper's private annotations or opinions
- Paywall PDF originals
- Anything not intended for public viewing

**Only:** wiki .md (knowledge), README, CLAUDE.md (card), scripts.

All agents MUST check: am I writing to `nephro-cme/`? If yes → public-safe content only.

## Management

- **Managed in vault** (`repos/nephro-cme/`), not on GitHub directly
- Symlink: `wiki/nephro-cme/` → `repos/nephro-cme/`
- One place to manage, vault = source of truth
- `git push` → GitHub public mirror

## Multi-Author Model

Three independent LLM authors contribute to this wiki. Each reads vault raw literature and updates wiki autonomously.

| author | model | access | role | schedule |
|---|---|---|---|---|
| **Claude Opus** (local) | Opus 4.6 | vault hm4 | primary author + **Editor-in-Chief**: writes wiki, daily editorial audit, methodology compliance (Guyatt/Hernán) | continuous write + daily review |
| **Claude Opus** (cloud) | Opus 4.6 | GitHub clone | primary author: PubMed→OA→/med-read→wiki, q6h scheduled | q6h auto |
| **Codex** | GPT-5.4 | vault via CC plugin | independent contributor, adversarial perspective, gap fill | daily |
| **Gemma 4** | Gemma 4 | vault raw .md (read-only) | independent contributor, alternative perspective, bulk processing | on dispatch |

**Protocol:**
1. All three read from same source: vault `raw/` raw.md + `wiki/` canonical wiki
2. Each writes to `repos/nephro-cme/cc-wiki/` — same files, merge on conflict
3. Claude = final arbiter on methodology (Guyatt/Hernán compliance)
4. Codex = adversarial review: challenges Claude's appraisals, catches errors
5. Gemma = volume: bulk process textbook chapters, fill coverage gaps
6. Git history tracks who wrote what (`Co-Authored-By:` in commits)
7. **No author deletes another's content** — add, revise, flag disagreement in-place

**Dispatch format** (in this card's TODO):
```
- [ ] {topic} — dispatch:{author}:{mode} ({date})
```

**Medical Knowledge Half-Life Rule:** Medical knowledge decays. Old data ≠ current truth. Every wiki entry and CME question MUST carry publication year. Opus editorial checks:
- Guideline cited → is it the LATEST version? (e.g., KDIGO 2024 CKD supersedes 2012)
- Trial cited → has it been superseded or contradicted by newer evidence?
- NephSAP 2008-2015 content → flag as NEEDS REVIEW, may be outdated
- Drug recommendations → check current NHI formulary status
- Threshold: content >5 years old without recent validation = stale, must be cross-checked before CME use

**Editorial Review (Opus, daily):**
1. Read all wiki .md modified since last review (`git log --since="1 day"`)
2. Check each entry against /med-read methodology standards:
   - Article entries: PICO present? GRADE rated? Causal claims checked? Nephro bias flagged?
   - Textbook entries: key numbers preserved? No factual errors?
3. Flag issues as inline `<!-- EDITOR: {issue} -->` comments
4. Fix minor errors directly (typos, missing GRADE, wrong NNT calculation)
5. Escalate major issues to Copper (factual disputes, methodology disagreements between authors)
6. Write editorial summary to `_editorial_log.md` (append)
7. **Opus = final word on methodology.** Sonnet/Codex/Gemma write content, Opus ensures quality.

## Current Coverage

19 wiki files, 3,375 lines. Topics: AKI, anemia, CKD (4 parts), HD, PD, electrolytes, HTN, cardiology, endocrinology, infectious disease, hematology, nutrition, public health, EBM methods, general medicine.

## Question Bank Strategy

**Two sources:**

| source | flow | priority |
|---|---|---|
| **Copper-provided** (真實考題) | Copper 提供 → 存入 `cme/bank/` → Opus editorial review → publish | 最高（真題） |
| **Taiwan case reports** | `taiwan-nephro-cases.py` (cron Wed) → /med-read → wiki + CME question generation | 高（出題委員常出自己的 case） |
| **NephSAP** (ASN CME) | 17+ issues in vault (`proj/medical-note/nephsap/`) → /med-read → extract Q&A → reformat | 極高（官方 CME，大量 case-based MCQ） |
| **Auto-generated** | wiki content → LLM generates MCQ → Opus review | 補充 |

**Why Taiwan case reports matter:** TSN 出題委員常出自己投稿的案例。Taiwan-authored nephrology case reports = 高機率考題來源。Pipeline 已在跑（1,676 篇 found, 100 OA downloaded）。

**Copper-provided 真題 protocol:**
1. Copper 提供題目（任何格式：照片、文字、口述）
2. Agent 存入 `cme/bank/raw/` (§1.8 save raw first)
3. 整理成標準 CME format（`cme/_template-v2.md`；legacy `cme/_template.md` is deprecated）
4. Cross-link to wiki topic
5. Opus editorial review
6. Publish to `cme/` (public) — **去除任何可辨識考題來源的資訊**（改寫 vignette，不直接用原題）

## Agent Work Cycle

每次 agent spawn 進 nephro-cme：

```
1. python3 repos/vault-scripts/wiki-orphan-scan.py
   → _data/wiki_orphans.tsv (vault-wide orphan list)

2. Filter: only nephrology-relevant orphans
   (KDIGO, Daugirdas, NolphGokal, nephrology articles)

3. For each nephro orphan:
   → read raw.md → /med-read → vault wiki .md (canonical)
   → export to repos/nephro-cme/cc-wiki/ (exam format)

4. Scan vault wiki for updates since last run:
   → git log --since="last run" -- wiki/wiki_nephrology_*.md
   → re-export updated topics to repo

5. CME question generation:
   → new wiki content → auto-generate MCQ → cme/ folder

6. git add -A && commit && push (auto-push cron handles this)
```

## TODO

### 2026-04-26 directive (4-pivot)

- [ ] **Keyed module 5→4 manual conversion**: existing 17 keyed module questions require Copper/Opus review before dropping E distractors; keep source questions untouched until reviewed — bug:manual (2026-04-26), codex-week1
- [ ] **NephSAP MCQ extraction pipeline**: `medwiki-raw/.../NephSAP_*.md` × 10 → MCQ extractor (案例-題幹-答案-rationale 結構抽取) → `cme/bank/nephsap/` → 互動格式. Target ≥100 題 first pass. — dispatch:opus:manual (2026-04-26)
- [ ] **Interactive Q-bank engine**: design web/CLI interactive answer flow (not just static .md). Options: GH Pages SPA reading `cme/*.md` frontmatter + answer key, OR jupyter-style notebooks, OR static site with hidden answer reveal. Codex to propose. — plan:auto (2026-04-26)
- [ ] **Continuous OA CME ingestion cron**: source-list (NephSAP RSS, AJKD Core Curriculum, KDIGO, CJASN ASN-IN-Review) + license-check + wikify pipeline. Run weekly. — plan:auto (2026-04-26)
- [ ] **學長姐 recall 2020-2024 → CME modules** (4-選項 format): 2021 anon 15Q + 2021 wang 18Q + 2023 ~20Q + 2024 多題, vignette rewrite per protocol §6 (去除 identifiable info). — dispatch:opus:manual (2026-04-26)
- [ ] **2022 recall gap**: 學長姐供應 2020/2021/2023/2024, 2022 缺. 透過 Kuo LiYuan 或其他學長姐補齊. — manual (2026-04-26)
- [ ] **Image extraction for 2023 (17 images) + 2024 (8 images)**: `unzip -j` to sidecar; image-dependent MCQ rebuild. — plan:auto (2026-04-26)

### Carryover (2026-04-08)

- [ ] 考古題 gap analysis: 115年考題 vs 現有 wiki coverage — dd:auto (2026-04-08)
- [ ] Brenner 12e 章節 mapping → wiki topics (TSN 推薦 11e but 讀 12e per Law) — plan:auto (2026-04-08)
- [ ] Nissenson 6e wikify (116年考試指定) — dd:auto (2026-04-08)
- [ ] Export script: vault wiki → repo wiki (filtered + reformatted) — plan:auto (2026-04-08)
- [ ] Taiwan case reports → CME questions: batch convert downloaded OA cases to MCQ format — dd:auto (2026-04-08)
