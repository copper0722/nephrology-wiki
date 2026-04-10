---
type: review
created: 2026-04-10
topic: gemma4 8B vs 31B wiki quality comparison
source: Aitken2020 (AVF patency RCT)
---

# Gemma 4 Quality Comparison: 8B vs 31B

## Test Article
Aitken et al. (2020) — Regional vs Local Anesthesia for AVF Creation. N=126 RCT.

## Metrics

| metric | 8B (Q4_K_M) | 31B (Q4_K_M) |
|---|---|---|
| **Generation time** | 41s | 189s (4.6x slower) |
| **Output size** | 3.7KB (57 lines) | 2.8KB (39 lines) |
| **Structure compliance** | 4 sections + summary table | 4 sections + summary table |
| **Data accuracy** | ✅ N=126, patency numbers correct | ✅ N=126, patency numbers correct, added p-values (p=0.02, p=0.008) |
| **LaTeX ban** | ❌ used `$\rightarrow$` (lines 27-28) | ❌ used `$\rightarrow$` (lines 17, 23, 38) — worse |
| **Textbook refs** | ❌ vague (no chapter numbers) | ❌ vague (section names but no chapter numbers) |
| **Exam logic depth** | Moderate: 3 distractors listed | Better: mechanism→clinical→distractor flow, pitfall explicit |
| **Clinical nuance** | Mentioned cost-effectiveness | Added TDC avoidance as cost driver, RCF/BCF distinction |
| **Conciseness** | Verbose, some filler | Tighter, more M2M-style |

## Verdict

**31B is meaningfully better:**
1. **P-values included** — 8B omitted statistical significance
2. **Distractor reasoning** — 31B explains WHY each distractor is wrong, 8B just lists them
3. **Clinical specificity** — 31B mentions TDC avoidance, AVF subtypes (RCF/BCF)
4. **More concise** — less padding, more information density

**Both fail on:**
1. LaTeX ban — `$\rightarrow$` appears in both (31B worse: 3 instances vs 2)
2. Textbook chapter numbers — neither gives specific chapters
3. No KDOQI/NKF guideline citation

## Recommendation

- **Use 31B for production.** 4.6x slower but substantially better clinical reasoning.
- **Prompt needs hardening:** add explicit `$` ban with examples, require chapter numbers not just book names.
- **Post-processing:** sed `$\rightarrow$` → `→` as safety net.
