# nephrology-wiki — TSN 腎臟專科考試知識庫

GitHub: `copper0722/nephrology-wiki` (public)

## Purpose

考試導向的腎臟科知識庫。Vault canonical wiki 的**考試特化投影**。

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
  ↓ /med-read
Vault canonical wiki (wiki/)
  ↓ filter: exam-relevant topics only
  ↓ reformat: key facts + 考題邏輯 (not full EBM appraisal)
This repo (repos/nephrology-wiki/wiki/)
  ↓ git push
GitHub (public, 考生使用)
```

**Vault → repo, NOT repo → vault.** Canonical wiki 是 upstream。This repo 是 downstream export。

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

This folder is an **open git repo pushed to public GitHub**. Symlinked at `wiki/nephrology-wiki/`.

**NEVER put inside this folder:**
- Patient data, clinic info, personal notes
- Copper's private annotations or opinions
- Paywall PDF originals
- Anything not intended for public viewing

**Only:** wiki .md (knowledge), README, CLAUDE.md (card), scripts.

All agents MUST check: am I writing to `nephrology-wiki/`? If yes → public-safe content only.

## Management

- **Managed in vault** (`repos/nephrology-wiki/`), not on GitHub directly
- Symlink: `wiki/nephrology-wiki/` → `repos/nephrology-wiki/`
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
1. All three read from same source: vault `ref/` raw.md + `wiki/` canonical wiki
2. Each writes to `repos/nephrology-wiki/wiki/` — same files, merge on conflict
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
3. 整理成標準 CME format（_template.md）
4. Cross-link to wiki topic
5. Opus editorial review
6. Publish to `cme/` (public) — **去除任何可辨識考題來源的資訊**（改寫 vignette，不直接用原題）

## Agent Work Cycle

每次 agent spawn 進 nephrology-wiki：

```
1. python3 repos/vault-scripts/wiki-orphan-scan.py
   → _data/wiki_orphans.tsv (vault-wide orphan list)

2. Filter: only nephrology-relevant orphans
   (KDIGO, Daugirdas, NolphGokal, nephrology articles)

3. For each nephro orphan:
   → read raw.md → /med-read → vault wiki .md (canonical)
   → export to repos/nephrology-wiki/wiki/ (exam format)

4. Scan vault wiki for updates since last run:
   → git log --since="last run" -- wiki/wiki_nephrology_*.md
   → re-export updated topics to repo

5. CME question generation:
   → new wiki content → auto-generate MCQ → cme/ folder

6. git add -A && commit && push (auto-push cron handles this)
```

## TODO
- [ ] 考古題 gap analysis: 115年考題 vs 現有 wiki coverage — dd:auto (2026-04-08)
- [ ] Brenner 11e 章節 mapping → wiki topics — plan:auto (2026-04-08)
- [ ] Nissenson 6e wikify (116年考試) — dd:auto (2026-04-08)
- [ ] Export script: vault wiki → repo wiki (filtered + reformatted) — plan:auto (2026-04-08)
- [ ] Taiwan case reports → CME questions: batch convert downloaded OA cases to MCQ format — dd:auto (2026-04-08)
- [ ] CME section setup (Codex designing) — plan:auto (2026-04-08)

## Changelog

| date | summary |
|---|---|
| 2026-04-08 | Card created. Cloned to vault `repos/nephrology-wiki/`. Defined vault→repo flow + exam protocol. |
| 2026-04-07 | README updated: corrected book list to TSN official, added paywall article welcome. |
