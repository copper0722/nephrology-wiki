---
summary: EBM methodology reference — study design hierarchy, bias taxonomy, statistical measures, SR/MA methods, reporting guidelines. CC agents reference this page for evidence quality in all wiki articles.
sources: 1
updated: 2026-04-06
tags: [EBM, research-methods, biostatistics, systematic-review, study-design]
---

# Evidence-Based Medicine & Health Research Methods

Core EBM methodology reference for CC agents. All clinical claims in wiki pages must meet evidence standards defined here.

## 1. Study Design Hierarchy

Evidence strength ranked by design. Higher = stronger causal inference.

| rank | design | key feature | primary measure | causal inference |
|---|---|---|---|---|
| 1 | SR/MA | pooled estimate from multiple studies | pooled OR/RR/HR, I^2 | strongest (synthesis) |
| 2 | RCT | random assignment to intervention/control | efficacy, NNT, ARR | strong (experimental) |
| 3 | cohort (prospective) | follow exposed/unexposed forward in time | incidence rate ratio (RR) | moderate-strong |
| 4 | cohort (retrospective) | historic baseline + follow-up from records | RR | moderate |
| 5 | case-control | compare exposure history: cases vs controls | odds ratio (OR) | moderate (analytic) |
| 6 | cross-sectional | snapshot of prevalence at one time point | prevalence, prevalence ratio | weak (no temporality) |
| 7 | case series/report | describe group with same condition | descriptive stats, CFR | weakest (no comparison) |
| 8 | expert opinion | unsystematic clinical experience | — | lowest |

### Design Selection Logic

- **Causality required** → RCT (or quasi-experimental if randomization unethical)
- **Rare disease** → case-control (cases oversampled)
- **Rare exposure** → prospective cohort (recruit by exposure status)
- **Descriptive/prevalence** → cross-sectional
- **Synthesis of existing literature** → systematic review +/- meta-analysis

### Primary vs Secondary vs Tertiary

| level | definition | examples |
|---|---|---|
| primary | collects new data from individuals | RCT, cohort, case-control, cross-sectional, qualitative |
| secondary | analyzes existing data | chart review, claims data, publicly available datasets |
| tertiary | reviews/synthesizes published literature | narrative review, systematic review, meta-analysis |

## 2. Study Design Details

### 2.1 Case Series

- Describes group of individuals with same disease/procedure
- No comparison group → no measure of association
- Uses: identify new syndromes, describe atypical presentations, generate hypotheses
- Key measures: counts, percentages, CFR (case fatality rate)
- CFR = deaths from disease / total cases of disease
- Limitation: no generalizability, no causal inference

### 2.2 Cross-Sectional Study

- Prevalence study — snapshot of exposure + disease at one time point
- Representative sample required (key validity threat: non-representativeness)
- Key measure: prevalence (point or period), prevalence ratio (PR)
- KAP survey = knowledge, attitudes, practices — common instrument
- Repeated cross-sectional = resample same source population over time (different individuals each wave)
- **Cannot assess causality** — no temporal sequence between exposure and disease
- Most popular primary design (fast, cheap, one data collection point)

### 2.3 Case-Control Study

- Cases (disease+) vs controls (disease-) → compare exposure histories
- Best for rare diseases
- Key measure: **odds ratio (OR) = ad/bc** from 2x2 table
- OR=1: no association; OR>1: exposure risky; OR<1: exposure protective
- 95% CI interpretation: entire CI >1 → significant risk; entire CI <1 → significant protection; CI crosses 1 → not significant
- Matching: none, frequency (group), matched-pairs (individual)
- **Cannot calculate disease rates** — cases oversampled, study population not representative
- Correct phrasing: "cases had greater/lesser odds of exposure than controls"
- Key bias: **recall bias** (cases search memories differently than controls)
- Other bias: misclassification bias (incorrect case/control assignment)

### 2.4 Cohort Study

- Follow participants forward in time → measure incident (new) disease
- Prospective: recruit by exposure status, follow into future
- Retrospective (historic): use past records for baseline, follow to present
- Longitudinal: representative sample followed forward, multiple exposures/outcomes
- Key measure: **incidence rate ratio (RR) = [a/(a+b)] / [c/(c+d)]**
- RR=1: no difference; RR>1: risky; RR<1: protective
- 95% CI: same interpretation as OR
- Additional measures:
  - Attributable risk (AR) = rate_exposed - rate_unexposed (excess risk)
  - AR% = AR / rate_exposed (etiologic fraction in exposed)
  - Population attributable risk (PAR) = rate attributable to exposure in total population
- Person-time analysis: accounts for variable follow-up duration (person-years denominator)
- Censoring: participants lost to follow-up stop contributing person-time
- Key bias: loss to follow-up, information bias (differential examination of exposed vs unexposed)
- Can also calculate OR for cohort: ad/bc — but OR ≠ RR when disease is common

### 2.5 Experimental Study (RCT)

- **Gold standard for causality** — researcher assigns exposure
- Components: intervention, control, randomization, blinding, outcome definition
- Trial types: superiority (new > comparison), noninferiority (new ≥ comparison), equivalence (new = comparison)
- Control types: placebo, active comparison/standard of care, dose-response, no intervention, self (crossover)

**Randomization methods:**

| method | description |
|---|---|
| simple | coin toss / random number generator per participant |
| stratified | divide into subgroups first, randomize within each |
| block | randomize groups (e.g., schools, clinics) not individuals |

**Blinding:**

| level | who is blinded |
|---|---|
| single-blind | participant does not know group assignment |
| double-blind | participant AND outcome assessor blinded |
| open-label | neither blinded |

**Key measures:**
- Efficacy = (rate_unfavorable_control - rate_unfavorable_intervention) / rate_unfavorable_control
- Efficacy = ideal conditions; Effectiveness = real-world conditions
- **NNT** (number needed to treat) = 1 / ARR = 1 / (rate_control - rate_intervention)
  - Small NNT = more effective. NNT=5 means treat 5 to prevent 1 event.
- **NNH** (number needed to harm) = 1 / ARI
  - Large NNH = safer intervention.
- **ARR** (absolute risk reduction) = rate_control - rate_intervention
- Analysis approaches: intention-to-treat (all randomized, regardless of compliance) vs per-protocol (compliant only)

**Ethical requirements:**
- Equipoise: genuine uncertainty about which treatment is better
- Distributive justice: source population appropriate, not exploitative
- Monitoring adverse events; conditions for early termination defined a priori
- Belmont Report principles: respect for persons, beneficence, distributive justice

### 2.6 Screening/Diagnostic Test Evaluation

| metric | definition | formula |
|---|---|---|
| sensitivity | true positive rate | TP / (TP + FN) |
| specificity | true negative rate | TN / (TN + FP) |
| PPV | positive predictive value | TP / (TP + FP) |
| NPV | negative predictive value | TN / (TN + FN) |
| LR+ | positive likelihood ratio | sensitivity / (1 - specificity) |
| LR- | negative likelihood ratio | (1 - sensitivity) / specificity |
| AUC | area under ROC curve | 0-1, higher = better discrimination |

- Sensitivity-specificity tradeoff: lowering threshold → ↑sensitivity, ↓specificity
- LR+ >10 and LR- <0.1 = good test
- ROC curve: plots sensitivity (y) vs 1-specificity (x) across cutpoints

## 3. Bias Taxonomy

### 3.1 Selection Bias

| bias | definition | vulnerable designs |
|---|---|---|
| allocation bias | nonrandom assignment to treatment groups | RCT (if randomization fails) |
| overmatching | too many matching criteria → cannot evaluate matched variables | case-control |
| loss to follow-up | differential dropout between groups | cohort, RCT |
| volunteer bias | participants differ systematically from non-participants | all primary studies |

### 3.2 Information Bias

| bias | definition | vulnerable designs |
|---|---|---|
| recall bias | cases remember exposures differently than controls | case-control |
| reporting bias | systematic under/over-reporting by one group | all |
| detection/surveillance bias | screened population appears to have higher disease rate | cohort |
| observer bias | assessor evaluates groups differently based on expectations | all (minimized by blinding) |
| misclassification bias | incorrect assignment of exposure or disease status | case-control, cohort |
| Hawthorne effect | behavior changes because participants know they are observed | RCT, quasi-experimental |
| lead-time bias | early detection falsely appears to prolong survival | screening studies |

### 3.3 Confounding and Effect Modification

- **Confounder**: associated with both exposure AND outcome, not on causal pathway. Distorts true association.
  - Detection: compare crude vs stratum-specific ORs. If stratum-specific are similar to each other but different from crude → confounding.
  - Solution: report adjusted measure (Mantel-Haenszel, regression).
- **Effect modifier**: defines biologically different subgroups with different responses to exposure.
  - Detection: stratum-specific measures differ from each other AND from crude (Breslow-Day test).
  - Solution: report stratum-specific measures. Do NOT pool.
- **Interaction**: effect of one predictor depends on another. Synergistic (↑risk beyond expected) or antagonistic.
- **Ecological fallacy**: assuming individual-level associations from population-level (aggregate) data.

### 3.4 Publication Bias

- Studies with significant results more likely to be published than null results
- Threatens validity of systematic reviews/meta-analyses
- Detection: funnel plot asymmetry (missing studies in null-result region)
- Mitigation: comprehensive search (grey literature, multiple databases, no language restriction)

## 4. Statistical Methods

### 4.1 Descriptive Statistics

| variable type | central tendency | spread | display |
|---|---|---|---|
| ratio/interval (normal) | mean | standard deviation (SD) | histogram |
| ratio/interval (skewed) | median | interquartile range (IQR) | boxplot |
| ordinal/ranked | median | IQR | boxplot |
| nominal/categorical | mode | — | bar chart, pie chart |

- SD: 68% within ±1 SD, 95% within ±2 SD, 99% within ±3 SD of mean
- z-score = (value - mean) / SD → how many SDs from mean

### 4.2 Confidence Intervals

- 95% CI = range in which true population parameter falls with 95% confidence
- Width determined by: sample size (larger → narrower), variability, confidence level
- CI corresponds to significance level: 95% CI ↔ α=0.05
- For OR/RR: 95% CI crossing 1.0 → not significant; entirely >1 or <1 → significant
- 99% CI = wider, harder to reach significance; 90% CI = narrower, easier to reach significance

### 4.3 p-Value Interpretation

- p-value = probability of observing result as extreme as or more extreme than observed, assuming null hypothesis is true
- p < 0.05 → reject null hypothesis (at α=0.05 level)
- p-value does NOT measure: (a) probability hypothesis is true, (b) clinical importance, (c) effect size
- Type I error (α): false positive — reject null when it's true. Set at 5% by convention.
- Type II error (β): false negative — fail to reject null when alternative is true.
- **Multiple comparisons**: running many tests inflates Type I error. Not acceptable to test many outcomes hoping for one significant result.

### 4.4 Measures of Association

| measure | study design | formula | null value |
|---|---|---|---|
| OR (odds ratio) | case-control, logistic regression | ad/bc | 1.0 |
| RR (rate ratio / relative risk) | cohort | incidence_exposed / incidence_unexposed | 1.0 |
| HR (hazard ratio) | survival analysis (Cox regression) | hazard_exposed / hazard_unexposed | 1.0 |
| ARR (absolute risk reduction) | RCT | rate_control - rate_intervention | 0 |
| NNT | RCT | 1/ARR | ∞ |
| PR (prevalence ratio) | cross-sectional | prevalence_A / prevalence_B | 1.0 |
| r (correlation coefficient) | correlational | Pearson or Spearman | 0 |

**Reporting standard**: always report point estimate + 95% CI + p-value. Never report "significant" without numbers.

### 4.5 Regression Analysis

**Linear regression** (outcome = continuous):
- Simple: one predictor. Multiple: ≥2 predictors.
- β coefficient = change in outcome per 1-unit change in predictor (holding other predictors constant)
- r² = proportion of variance explained (0-1)
- Assumptions: linearity, normal residuals, homoscedasticity, no multicollinearity (VIF <10)

**Logistic regression** (outcome = binary):
- Coefficients (β) → OR = exp(β)
- 95% CI for OR: exp(β ± 1.96 × SE)
- Adjusted OR: controls for confounders in the model
- Goodness-of-fit: Hosmer-Lemeshow test, likelihood ratio tests

**Survival analysis:**
- Kaplan-Meier plot: cumulative survival over time
- Log-rank test: compare survival curves between groups
- Cox proportional hazards: estimates hazard ratio (HR), adjusts for covariates
- HR interpretation: same as RR (HR=1 no difference, HR>1 higher hazard, HR<1 lower hazard)

### 4.6 Sample Size and Power

- **Power** = 1 - β = probability of detecting true effect. Standard: ≥80%.
- α typically set at 0.05 (95% confidence level).
- Factors increasing required sample size: smaller expected effect size, lower exposure prevalence, higher desired power, lower α.
- Underpowered study → cannot detect true associations → Type II error.
- Power calculation should be done a priori (during study design), not post hoc.
- Sample size estimation requires: expected effect size, α level, desired power, variability estimates.

## 5. Systematic Review and Meta-Analysis Methodology

### 5.1 Systematic Review Process

1. Define focused research question (PICO/PICOT)
2. Develop comprehensive search strategy (Boolean operators, MeSH terms)
3. Search multiple databases (PubMed/MEDLINE, Embase, CINAHL, Cochrane, etc.)
4. Supplement: snowball sampling, grey literature, hand searching
5. Screen titles/abstracts → screen full text → apply eligibility criteria
6. Independent dual review recommended
7. Extract data into standardized table
8. Quality assessment of included studies
9. Synthesize findings (narrative or quantitative)
10. Report per PRISMA checklist

### 5.2 Search Strategy

- Boolean operators: AND (narrows), OR (expands), NOT (excludes)
- MeSH terms: controlled vocabulary for MEDLINE; broader/narrower/related terms available
- Validate search: confirm known-relevant articles are captured
- Limiters (year, language, database) must be justified; unjustified restriction = bias
- Built-in database filters (e.g., PubMed "Clinical Trial" filter) often miss unindexed articles → use with caution

### 5.3 Quality Assessment

- Assess internal validity: measurement precision, bias risk, methodological rigor
- Tools vary by study design (Cochrane Risk of Bias for RCTs, Newcastle-Ottawa for observational)
- Body of evidence quality: many high-quality RCTs = strong; few small case series = weak
- Both significant and null results must be reported and interpreted

### 5.4 Meta-Analysis

**When to pool:**
- Studies must have similar: population, exposure/intervention, outcome definition, design
- Heterogeneity assessment required before pooling

**Heterogeneity measures:**

| statistic | interpretation |
|---|---|
| Cochran's Q | weighted sum of squared differences between individual and pooled effects; large Q = high heterogeneity |
| I² | 0% = all variability from chance; 25% = low; 50% = moderate; 75% = high heterogeneity |

**Models:**

| model | when to use | CI width |
|---|---|---|
| fixed effects | low heterogeneity (similar studies) | narrower |
| random effects | significant heterogeneity | wider (adjusts for between-study variance) |

**Effect size**: magnitude of difference — OR, RR, HR, difference in means, correlation coefficient. Cohen's d evaluates clinical meaningfulness of mean differences.

**Visualization:**
- **Forest plot**: horizontal axis = effect size; vertical line at null; square = point estimate (size ∝ weight); horizontal line = 95% CI; diamond = pooled estimate
- **Funnel plot**: x-axis = effect size; y-axis = sample size. Symmetric triangle = no publication bias. Missing corner = publication bias likely.

### 5.5 Reporting Quality: GRADE System

GRADE (Grading of Recommendations, Assessment, Development and Evaluation) rates quality of evidence body:

| level | definition | typical source |
|---|---|---|
| High (A) | very unlikely further research will change confidence | well-conducted RCTs |
| Moderate (B) | further research likely to have important impact | RCTs with limitations, strong observational |
| Low (C) | further research very likely to change confidence | observational studies |
| Very Low (D) | any estimate very uncertain | case series, expert opinion |

**Factors that lower GRADE:**
- Risk of bias, inconsistency, indirectness, imprecision, publication bias

**Factors that raise GRADE (for observational studies):**
- Large effect size, dose-response gradient, all plausible confounders would reduce effect

**Recommendation strength:**
- Strong (1): benefits clearly outweigh risks, or vice versa
- Weak/conditional (2): balance of benefits/risks is close or uncertain

Standard citation format: `KDIGO 2024 recommends SGLT2i for CKD G2-G4 with albuminuria (1B)` = strong recommendation, moderate-quality evidence.

## 6. Reporting Guidelines

| design | checklist | full name |
|---|---|---|
| case report | CARE | Case Report |
| diagnostic accuracy | STARD | Standards of Reporting of Diagnostic Accuracy |
| cross-sectional | STROBE | Strengthening the Reporting of Observational Studies in Epidemiology |
| case-control | STROBE | (same) |
| cohort | STROBE | (same) |
| RCT | CONSORT | Consolidated Standards of Reporting Trials |
| RCT protocol | SPIRIT | Standard Protocol Items: Recommendations for Intervention Trials |
| quality improvement | SQUIRE | Standards for Quality Improvement Reporting Excellence |
| non-randomized trial | TREND | Transparent Reporting of Evaluations with Nonrandomized Designs |
| economic evaluation | CHEERS | Consolidated Health Economic Evaluation Reporting Standards |
| qualitative | COREQ | Consolidated Criteria for Reporting Qualitative Research |
| qualitative | SRQR | Standards for Reporting Qualitative Research |
| SR/MA (interventions) | PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses |
| MA (observational) | MOOSE | Meta-analysis of Observational Studies in Epidemiology |
| prediction model | TRIPOD | Transparent Reporting of a Multivariable Prediction Model |

## 7. Causality Assessment

### Bradford Hill Criteria

| criterion | question |
|---|---|
| temporality | did exposure precede outcome? (necessary) |
| strength | is the measure of association far from null? |
| dose-response | does higher exposure → higher disease risk? |
| cessation | does removing exposure reduce risk? |
| specificity | are exposure and outcome narrowly defined? |
| biological plausibility | is there a mechanistic explanation? |
| consistency | replicated across studies/populations? |
| coherence | consistent with existing knowledge? |
| experiment | has controlled experiment confirmed? |
| alternate explanations | have confounders/bias been ruled out? |

Not all criteria must be met. More criteria satisfied → stronger causal inference.
**Association ≠ causation.** Statistical significance alone never proves causation.

## 8. Internal vs External Validity

| dimension | definition | threats |
|---|---|---|
| **internal validity** | study measured what it intended in its population | bias (selection, information, confounding), measurement error, protocol violation |
| **external validity** (generalizability) | results applicable to other populations/settings/times | narrow eligibility criteria, single-center, unique population, ideal-world conditions |

- Replicability: same protocol in new population → similar results
- Reproducibility: independent analyst reanalyzes same data → same results

## 9. Clinical vs Statistical Significance

- **Statistically significant**: p < 0.05 (by convention) — result unlikely due to chance alone
- **Clinically significant**: effect size large enough to matter in practice
- A study can be statistically significant but clinically irrelevant: e.g., OR=1.05 (1.01-1.09) with p=0.01 — trivial effect size
- A study can be clinically meaningful but fail to reach statistical significance due to insufficient power
- **Always report effect size** (OR, RR, HR, ARR, NNT) alongside p-value
- NNT contextualizes: NNT=5 over 3 years = meaningful; NNT=500 = questionable clinical value
- Cost-effectiveness considerations: NNT + NNH + treatment cost + disease severity

## 10. Key Formulas Quick Reference

| formula | equation | notes |
|---|---|---|
| OR | ad/bc | from 2x2 table |
| RR | [a/(a+b)] / [c/(c+d)] | from 2x2 table |
| ARR | rate_control - rate_intervention | absolute difference |
| NNT | 1/ARR | lower = more effective |
| NNH | 1/ARI | higher = safer |
| Efficacy | (rate_unfav_control - rate_unfav_intervention) / rate_unfav_control | proportion prevented |
| Sensitivity | TP/(TP+FN) | true positive rate |
| Specificity | TN/(TN+FP) | true negative rate |
| PPV | TP/(TP+FP) | post-test probability if positive |
| NPV | TN/(TN+FN) | post-test probability if negative |
| LR+ | sensitivity/(1-specificity) | >10 = strong positive test |
| LR- | (1-sensitivity)/specificity | <0.1 = strong negative test |
| Power | 1 - β | ≥80% standard |
| CFR | deaths from disease / total cases | case fatality rate |

## Sources

- isbn:2021_HealthResMethods_3e Jacobsen2021 — "Introduction to Health Research Methods: A Practical Guide" 3rd ed. Full textbook extraction covering study designs (Ch 7-15), sampling/power (Ch 19-20), systematic reviews (Ch 26), biostatistics (Ch 29-31), and reporting (Ch 35).

## Changelog

- 2026-04-06: Created from raw.md of Jacobsen 2021 textbook. Comprehensive extraction of study design hierarchy, bias taxonomy, statistical measures (OR/RR/HR/NNT/ARR), SR/MA methodology, GRADE system, reporting guidelines (CONSORT/STROBE/PRISMA), Bradford Hill criteria, confounding/effect modification, sample size/power, clinical vs statistical significance.
