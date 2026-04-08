---
module: nephrology-ckd-staging
topic: 慢性腎臟病分期與風險分層
difficulty: mixed
bloom_level: mixed
wiki_source:
  - ../wiki/wiki_nephrology_ckd_part1.md
author: "Codex (GPT-5.4)"
date: 2026-04-08
question_count: 10
---

# CKD 分期與風險分層

對應 wiki： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)

本模組聚焦在 CKD definition、CGA staging、GFR category、albuminuria category、KDIGO heat map、eGFR equation 與 progression risk。題目依 TSN 題感配置為 `4 題 recall + 4 題 application + 2 題 analysis`。

## 題目 1

Type: Part A  
Difficulty: recall  
Bloom: recall

題幹：

下列哪一個情境最符合 CKD 的定義門檻，而且已滿足「慢性」條件？

A. eGFR 68 mL/min/1.73 m²、UACR 20 mg/g，持續 6 個月  
B. eGFR 58 mL/min/1.73 m²、UACR 10 mg/g，持續 4 個月  
C. eGFR 92 mL/min/1.73 m²、UACR 25 mg/g，持續 5 個月  
D. eGFR 75 mL/min/1.73 m²、UACR 12 mg/g，急性腸胃炎後 2 週  
E. eGFR 61 mL/min/1.73 m²、UACR 28 mg/g，持續 1 年

### 答案

正確答案：B

### 解析

CKD 的核心門檻是腎功能或腎損傷指標異常且具慢性持續性。以 staging 角度，`GFR <60` 或 `ACR >30` 是重要 threshold；若異常已持續超過 3 個月，就符合 CKD 的 chronicity 概念。B 選項的 eGFR 58 已低於 60，且持續 4 個月，因此最符合 CKD 定義。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：eGFR 仍大於等於 60，UACR 也未超過 30 mg/g，沒有達到 wiki 提示的 CKD threshold。
- C：eGFR 正常，UACR 25 mg/g 也未達 A2 門檻，因此不能用 albuminuria 定義 CKD。
- D：雖然是腎臟相關情境，但只有 2 週，較像 acute change，沒有滿足 CKD 的時間條件。
- E：eGFR 61 與 UACR 28 都在門檻上方或下方邊緣，但未跨過 `GFR <60` 或 `ACR >30` 的 cutpoint。

## 題目 2

Type: Part A  
Difficulty: recall  
Bloom: recall

題幹：

尿中白蛋白/肌酸酐比（UACR）120 mg/g，最適合歸類為下列何者？

A. A1  
B. A2  
C. A3  
D. G2  
E. G3a

### 答案

正確答案：B

### 解析

KDIGO 的 CGA staging 不只看 GFR，也要看 albuminuria category。UACR 120 mg/g 落在 `30-300 mg/g`，因此屬於 `A2`。這類題目是 TSN Part A 常見的基礎分類題。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：A1 是正常到輕度增加的白蛋白尿，通常是 UACR <30 mg/g，不符合 120 mg/g。
- C：A3 代表嚴重增加的白蛋白尿，通常是 UACR >300 mg/g，120 mg/g 還不到這個範圍。
- D：G2 是 GFR category，不是 albuminuria category，分類軸錯了。
- E：G3a 同樣是 GFR category，不是拿來描述 UACR 的分類。

## 題目 3

Type: Part A  
Difficulty: recall  
Bloom: recall

題幹：

某考生看到病人的 eGFR 為 22 mL/min/1.73 m²。依 CKD 的 GFR category，最適合分類為：

A. G2  
B. G3a  
C. G3b  
D. G4  
E. G5

### 答案

正確答案：D

### 解析

GFR category 的基本切點必須熟記。eGFR 22 mL/min/1.73 m² 落在 `15-29`，因此屬於 `G4`。在考題中，先正確放入 G category，才能進一步結合 A category 做 heat map risk stratification。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：G2 是 eGFR 60-89，不符合 22。
- B：G3a 是 eGFR 45-59，不符合 22。
- C：G3b 是 eGFR 30-44，不符合 22。
- E：G5 是 eGFR <15；22 尚未低到 G5。

## 題目 4

Type: Part A  
Difficulty: recall  
Bloom: recall

題幹：

關於 CKD 的 eGFR 估算方式，下列何者最符合對應 wiki 的敘述？

A. CKD-EPI 2021 仍以 race coefficient 為必要組成  
B. eGFRcr-cys 的準確度通常低於 eGFRcr  
C. eGFRcr 可作為初始估算，若需要確認可用 eGFRcys 或 eGFRcr-cys  
D. cystatin C 不應用於 CKD staging  
E. Cockcroft-Gault 是所有病人的首選 confirmatory equation

### 答案

正確答案：C

### 解析

對應 wiki 清楚寫到：`eGFRcr initial, eGFRcys/eGFRcr-cys for confirmation`，而 2021 新版 GFR equations 也強調移除 race coefficient，並指出 `eGFRcr-cys` 整體上最準。C 完整對應這個邏輯。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉；〈GFR Estimation Without Race—NKF-ASN Task Force (2021)〉；〈New GFR Equations Without Race (2021)〉

### 錯誤選項解析

- A：2021 版重點就是拿掉 race coefficient，不是保留。
- B：wiki 指出 creatinine-cystatin C combined equation 更準，不是更差。
- D：cystatin C 正是 confirmatory approach 的重要工具，不能說完全不應使用。
- E：Cockcroft-Gault 在部分藥物劑量情境仍可見，但不是 wiki 這裡主張的首選 confirmatory equation。

## 題目 5

Type: Part B  
Difficulty: application  
Bloom: application

題幹：

63 歲男性，糖尿病與高血壓病史，最近 6 個月追蹤兩次，eGFR 都約 52 mL/min/1.73 m²，UACR 約 420 mg/g。依 CGA staging 與 KDIGO heat map，最適合的判讀是下列何者？

A. CKD G2A1，低風險  
B. CKD G3aA2，高風險  
C. CKD G3aA3，非常高風險  
D. CKD G3bA3，非常高風險  
E. CKD G4A3，已等同腎衰竭需立即透析

### 答案

正確答案：C

### 解析

eGFR 52 屬於 `G3a`，UACR 420 mg/g 屬於 `A3`。KDIGO heat map 下，`G3aA3` 屬於 very high risk。對應 wiki 強調 `CGA staging replaces GFR-only classification`，而且 `GFR and albuminuria are independent CVD predictors`，所以不能只看 eGFR。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：eGFR 52 不是 G2，UACR 420 也遠高於 A1。
- B：eGFR 分類對，但 UACR 420 已進入 A3，不是 A2。
- D：UACR 分類對，但 eGFR 52 是 G3a，不是 G3b。
- E：G4 需要 eGFR 15-29；而且「需要立即透析」不能只靠分期決定，wiki 也提醒透析時機不能只靠 eGFR cutoff。

## 題目 6

Type: Part B  
Difficulty: application  
Bloom: application

題幹：

29 歲女性，IgA nephropathy，4 個月內兩次 UACR 分別為 165 與 180 mg/g，eGFR 穩定在 96 mL/min/1.73 m²。下列哪一個分類最正確？

A. 不算 CKD，因為 eGFR 正常  
B. CKD G1A1  
C. CKD G1A2  
D. CKD G2A2  
E. 只能算 AKI，不能算 CKD

### 答案

正確答案：C

### 解析

這題的關鍵是不能把「正常 eGFR」誤認為「沒有 CKD」。對應 wiki 指出 `GFR <60 or ACR >30 defines CKD/AKD threshold`，所以 albuminuria 本身就能界定腎損傷。此病人的 eGFR 96 屬於 `G1`，UACR 180 mg/g 屬於 `A2`，且已持續超過 3 個月，因此是 `CKD G1A2`。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：正常 eGFR 不等於沒有 CKD；持續性白蛋白尿本身就是 CKD marker。
- B：G1 正確，但 UACR 180 屬於 A2，不是 A1。
- D：A2 正確，但 eGFR 96 應分在 G1，不是 G2。
- E：AKI 重點是急性變化；這題是持續 4 個月，符合 chronicity。

## 題目 7

Type: Part B  
Difficulty: application  
Bloom: application

題幹：

78 歲女性，明顯肌少症，血清肌酸酐偏低。creatinine-based eGFR 為 61 mL/min/1.73 m²，UACR 40 mg/g。若你想確認她的 CKD staging，下列哪一個下一步最符合對應 wiki？

A. 補回 race coefficient 後重新計算 eGFR  
B. 使用 cystatin C 或 creatinine-cystatin C combined equation 做確認  
C. 因為 eGFR 大於 60，所以直接排除 CKD  
D. 只看 UACR，不需再評估 GFR  
E. 直接依 Cockcroft-Gault 決定是否開始透析

### 答案

正確答案：B

### 解析

wiki 對 CKD 的 GFR estimation 很明確：`eGFRcr initial, eGFRcys/eGFRcr-cys for confirmation`。在肌少症病人，單靠 creatinine 容易高估 true GFR，因此用 cystatin C 或 combined equation 做 confirmatory staging 特別合理。這題同時提醒：UACR 40 mg/g 已是 A2，不能因 eGFR 邊界值就忽略腎損傷證據。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉；〈New GFR Equations Without Race (2021)〉

### 錯誤選項解析

- A：2021 方向是移除 race coefficient，不是補回去。
- C：UACR 已超過 30 mg/g，仍要考慮 CKD；而且 borderline creatinine eGFR 還需要 confirmatory testing。
- D：albuminuria 很重要，但 staging 是 CGA，不是只看 A 不看 G。
- E：透析決策不能靠這種單一步驟公式直接判定，和本題的 confirmatory staging 問題也不相符。

## 題目 8

Type: Part B  
Difficulty: application  
Bloom: application

題幹：

67 歲男性，已知 CKD，eGFR 38 mL/min/1.73 m²，UACR 650 mg/g，serum bicarbonate 20 mmol/L。兩個月前因高血鉀停用 ACE inhibitor。根據對應 wiki，以下哪一項最能指出他腎功能惡化的風險訊號？

A. 低 bicarbonate 加上重度白蛋白尿，都支持較高 progression risk  
B. 停用 RAAS inhibitor 後，ESRD 風險通常會下降  
C. 一旦 eGFR <45，albuminuria 就不再有預後價值  
D. 只有 serum creatinine 對預後有用，酸中毒與白蛋白尿都不重要  
E. bicarbonate 20 mmol/L 表示 CKD 分期一定是 G5

### 答案

正確答案：A

### 解析

這題把 staging 與 progression risk 結合。對應 wiki 指出 `GFR and albuminuria are independent CVD predictors`；另有 UBI study summary 提到 metabolic acidosis 與 `eGFR decline >30%` 有關；RAAS inhibitor discontinuation 的 section 也指出停藥與 mortality、CV events、ESRD 增加相關。綜合來看，重度 albuminuria、低 bicarbonate、以及中斷 RAAS blockade 都是惡化訊號。A 最完整。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉；〈Sodium Bicarbonate for Metabolic Acidosis—UBI Study (2019)〉；〈RAAS Inhibitor Discontinuation & CKD Outcomes (2022)〉

### 錯誤選項解析

- B：對應 wiki 恰好相反，停用 RAAS inhibitor 與較差 outcome 有關，不是保護。
- C：albuminuria 是 independent predictor，不會因 GFR 降到某一點就失去意義。
- D：wiki 反覆強調不能只看 creatinine/eGFR，albuminuria 與 acid-base status 都和 prognosis 有關。
- E：bicarbonate 20 是酸中毒風險訊號，不是 G category 的定義條件，更不能單獨推到 G5。

## 題目 9

Type: Part B  
Difficulty: analysis  
Bloom: analysis

題幹：

你在門診看到兩位病人：  
甲病人：eGFR 88 mL/min/1.73 m²，UACR 720 mg/g。  
乙病人：eGFR 32 mL/min/1.73 m²，UACR 8 mg/g。  

下列哪一個解讀最符合 CGA staging 的精神？

A. 甲病人 eGFR 正常，所以一定是低風險  
B. 只有乙病人算 CKD，因為甲病人 eGFR 仍正常  
C. 兩人都符合 CKD，但不能只靠 GFR 判斷風險，因為 albuminuria 是獨立預後指標  
D. 甲病人只能看 A category，乙病人只能看 G category，CGA 不適用  
E. 兩人既然都算 CKD，風險就必然相同

### 答案

正確答案：C

### 解析

這題測的是「為什麼 CGA staging 取代 GFR-only classification」。對應 wiki 直接寫到 `CGA staging replaces GFR-only classification`，而且 `GFR and albuminuria are independent CVD predictors`。甲病人雖然 eGFR 尚可，但 A3 白蛋白尿代表顯著風險；乙病人則因 G3b 已有腎功能下降。兩人都屬 CKD，也都不是只看單一軸就能充分描述。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉

### 錯誤選項解析

- A：正常 eGFR 不能把重度白蛋白尿洗掉；A3 本身就代表高風險訊號。
- B：甲病人 UACR 720 mg/g，已遠超過 CKD 的 albuminuria threshold。
- D：CGA 的目的就是整合 Cause、GFR、Albuminuria，不是把不同病人拆成只看單一欄位。
- E：同樣是 CKD 不代表風險相同；heat map 的存在就是為了區分不同組合的風險層級。

## 題目 10

Type: Part B  
Difficulty: analysis  
Bloom: analysis

題幹：

70 歲女性，糖尿病史，因截肢與肌肉量偏低，creatinine-based eGFR 為 64 mL/min/1.73 m²；cystatin C-based eGFR 為 48 mL/min/1.73 m²；UACR 120 mg/g，已持續 5 個月。下列哪一個判讀最符合對應 wiki？

A. 不算 CKD，因為 creatinine-based eGFR 仍高於 60  
B. 可合理視為 CKD G3aA2，且應重視 cystatin C / combined equation 的 confirmatory role  
C. 應分為 CKD G1A3，因為 cystatin C 在糖尿病人都會低估 GFR  
D. 只能算 AKD，因為白蛋白尿尚未超過 300 mg/g  
E. 只要 cystatin C eGFR <50，就應立即開始透析

### 答案

正確答案：B

### 解析

這題要整合 chronicity、albuminuria、以及 discordant eGFR estimates。她的 UACR 120 mg/g 已是 `A2`，而且持續 5 個月，已符合 CKD 的 chronic albuminuria 條件。又因為病人肌肉量偏低，creatinine-based eGFR 可能高估 true kidney function，此時依 wiki 應以 `eGFRcys` 或 `eGFRcr-cys` 做 confirmatory assessment。若以 cystatin C 48 作為較可信的 staging 依據，則最合理是 `CKD G3aA2`。  

Source： [../wiki/wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md)〈Uses of GFR and Albuminuria Level in Acute and Chronic Kidney Disease (2022)〉；〈GFR Estimation Without Race—NKF-ASN Task Force (2021)〉；〈New GFR Equations Without Race (2021)〉

### 錯誤選項解析

- A：錯在只看 creatinine eGFR。wiki 已提醒 creatinine 是 initial estimate，不是所有情況下的 final truth。
- C：UACR 120 是 A2 不是 A3；而且 wiki 並未支持「糖尿病病人 cystatin C 一律低估 GFR」這種絕對說法。
- D：albuminuria >30 mg/g 就已足以支持 CKD marker，不需要等到 >300 mg/g 才算 CKD。
- E：透析起始不能只用單一 eGFR cutpoint 決定，對應 wiki 的 IDEAL 與 guideline sections 都反對這種過度簡化。
