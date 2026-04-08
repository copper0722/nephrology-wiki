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
Vault canonical wiki (proj/wiki/)
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

## Content Rules

- Language: M2M English (same as vault wiki — 考生也是醫師，能讀 M2M)
- 不需要 PICO/GRADE/bias full appraisal — 考試要的是正確知識
- 但保留 key evidence（landmark trial names, NNT, GRADE recommendations from guidelines）
- 結構：topic-based（不是 per-article），按教科書章節組織

## ⚠️ PUBLIC FOLDER — No Personal Data

This folder is an **open git repo pushed to public GitHub**. Symlinked at `proj/wiki/nephrology-wiki/`.

**NEVER put inside this folder:**
- Patient data, clinic info, personal notes
- Copper's private annotations or opinions
- Paywall PDF originals
- Anything not intended for public viewing

**Only:** wiki .md (knowledge), README, CLAUDE.md (card), scripts.

All agents MUST check: am I writing to `nephrology-wiki/`? If yes → public-safe content only.

## Management

- **Managed in vault** (`repos/nephrology-wiki/`), not on GitHub directly
- Symlink: `proj/wiki/nephrology-wiki/` → `repos/nephrology-wiki/`
- One place to manage, vault = source of truth
- `git push` → GitHub public mirror

## Multi-Author Model

Three independent LLM authors contribute to this wiki. Each reads vault raw literature and updates wiki autonomously.

| author | model | access | role | schedule |
|---|---|---|---|---|
| **Claude Sonnet** | Sonnet 4.6 | vault local + cloud | workhorse author, /med-read pipeline, bulk wikify | continuous |
| **Codex** | GPT-5.4 | vault via CC plugin | independent contributor, adversarial perspective, gap fill | on dispatch or weekly |
| **Gemma 4** | Gemma 4 | vault raw .md (read-only) | independent contributor, alternative perspective, bulk processing | on dispatch |
| **Claude Opus** | Opus 4.6 | vault local | **Editor-in-Chief**: periodic audit, methodology compliance (Guyatt/Hernán), quality gate | weekly editorial review |

**Protocol:**
1. All three read from same source: vault `ref/` raw.md + `proj/wiki/` canonical wiki
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

**Editorial Review (Opus, weekly):**
1. Read all wiki .md modified since last review (`git log --since="7 days"`)
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

## TODO
- [ ] 考古題 gap analysis: 115年考題 vs 現有 wiki coverage — dd:auto (2026-04-08)
- [ ] Brenner 11e 章節 mapping → wiki topics — plan:auto (2026-04-08)
- [ ] Nissenson 6e wikify (116年考試) — dd:auto (2026-04-08)
- [ ] Export script: vault wiki → repo wiki (filtered + reformatted) — plan:auto (2026-04-08)

## Changelog

| date | summary |
|---|---|
| 2026-04-08 | Card created. Cloned to vault `repos/nephrology-wiki/`. Defined vault→repo flow + exam protocol. |
| 2026-04-07 | README updated: corrected book list to TSN official, added paywall article welcome. |
