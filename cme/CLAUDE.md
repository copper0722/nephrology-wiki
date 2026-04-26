# nephrology-wiki/cme — CME question bank card

GitHub repo: `copper0722/nephrology-wiki` (public)

## Purpose

Build a public-safe CME layer on top of `wiki/` for TSN board prep:
- wiki = source knowledge
- cme = retrieval practice + exam-style reasoning
- all items original, no copied exam stems, no patient identifiers, no paywall text

## Folder Layout

| path | role |
|---|---|
| `cme/README.md` | public candidate guide in zh-TW |
| `cme/_template-v2.md` | canonical v2 template for one-Q-per-file bank entries |
| `cme/_template.md` | deprecated legacy redirect to v2 |
| `cme/nephrology-<topic>-<focus>.md` | reusable CME module, one topic per file |
| `cme/CLAUDE.md` | protocol card for all authors |

## Naming Convention

- Lowercase kebab-case only.
- Prefix with specialty domain: `nephrology-`.
- Preferred pattern: `nephrology-<topic>-<focus>.md`.
- One module = one coherent exam unit (for example staging, anemia diagnosis, HD adequacy).

## Required Frontmatter

Each module must start with valid YAML:

```yaml
---
module: nephrology-<topic>-<focus>
topic: <zh-TW module title>
difficulty: <recall|application|analysis|mixed>
bloom_level: <recall|application|analysis|mixed>
wiki_source:
  - ../wiki/<source-file>.md
author: <Claude Opus|Codex|Gemma>
date: YYYY-MM-DD
question_count: <integer>
---
```

## TSN Exam Format

### Part A: 基礎 100 題

- Short stem, concept/definition/threshold/association.
- Use when testing recall of staging cutoffs, definitions, equations, key numbers.
- Use 4 options (`A-D`), single best answer.

### Part B: 臨床 50 題

- Short clinical vignette first, then interpretation/next-step/risk stratification question.
- Use when testing application of wiki facts to CKD staging, prognosis, management logic.
- Single best answer, 4 options (`A-D`).
- No real patient data; fictionalized age/sex/comorbidity only.

## Question Block Standard

Every question must include:
1. `Type` (`Part A` or `Part B`)
2. `Difficulty`
3. `Bloom`
4. Stem in zh-TW
5. Four options (`A-D`)
6. `Correct answer`
7. `Explanation`
8. `Source` citation back to `../wiki/...`
9. Distractor analysis for every wrong option

## Difficulty Map

| difficulty | Bloom | use case |
|---|---|---|
| `recall` | remember / understand | definitions, cutoffs, formula identity, one-step classification |
| `application` | apply | vignette-based staging, choosing confirmatory equation, assigning risk cell |
| `analysis` | analyze | compare cases, resolve discordant data, explain why CGA beats GFR-only thinking |

Rule: modules should usually mix levels. Default target for 10 questions = `4 recall / 4 application / 2 analysis` unless a topic clearly needs another ratio.

## Explanation Standard

Explanation must do three things:
1. State why the keyed answer is best.
2. Cite the exact wiki file with relative path and source section title.
3. Explain why each distractor is wrong, not merely why the correct answer is right.

Preferred citation style:

```md
Source: [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)
Section: "Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)"
```

## Auto-Generation Protocol

Author-agnostic workflow for Claude Opus, Codex, Gemma:

1. Read one source wiki file end-to-end.
2. Extract examable units:
   - definitions
   - thresholds
   - equations / biomarkers
   - risk signals
   - guideline logic
3. Convert units into a balanced Part A + Part B set.
4. Write original stems only. Never paraphrase copyrighted exam-bank wording.
5. Build distractors from nearby-but-wrong concepts:
   - wrong threshold
   - wrong stage
   - wrong equation
   - true fact applied in wrong context
6. Add answer explanations with source citation + distractor analysis.
7. Validate that every claim can be traced back to the linked wiki file.
8. Re-read for public safety and Taiwan terminology.

## Review Process

Same editorial model as `wiki/`:

1. Any of the 3 authors may draft or revise CME modules.
2. Claude Opus performs daily audit on modified `cme/*.md`.
3. Audit checks:
   - methodology consistency with repo standards
   - Guyatt EBM logic preserved where relevant
   - Hernán causal language discipline for prognostic/causal claims
   - answer key accuracy
   - distractor quality
   - public-safety compliance
4. Minor errors: fix directly.
5. Major disagreement: flag inline with `<!-- EDITOR: ... -->` or escalate to Copper.
6. No author deletes another author's work wholesale; revise in place and preserve attribution in git history.

## Progress Tracking

Candidate progress is tracked locally in the browser SPA, not in a hidden server database.

- Each module frontmatter must declare `question_count`.
- `cme/README.md` maintains the public module checklist.
- `docs/qbank/` stores answered IDs, score, and weak topics in `localStorage`.
- Candidates may still keep a personal fork, local markdown copy, or note app for long-form notes.
- Optional module footer: quick self-audit (`done / wrong items / wiki to revisit`).

## Integration With Wiki

- Every module must declare `wiki_source`.
- Every answer explanation must link back to the source wiki file.
- Prefer topic-level cross-links near the top of the module.
- CME is downstream from wiki:
  - wiki explains the knowledge
  - cme tests retrieval + application
- If wiki changes materially, linked CME modules should be regenerated or audited.

## Public-Safety Rules

- No patient identifiers.
- No copied board questions.
- No paywall excerpts.
- No private annotations.
- Original educational content only.

## TODO

- [ ] Build first-pass module map from existing `wiki/` coverage — dispatch:auto (2026-04-08)
- [ ] Add CKD management module from `../wiki/wiki_nephrology_ckd_part2.md` — dispatch:auto (2026-04-08)
- [ ] Define module checklist growth rules in `README.md` as coverage expands — plan:auto (2026-04-08)
