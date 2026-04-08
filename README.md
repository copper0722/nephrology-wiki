# 腎臟專科醫師考試知識庫

TSN 腎臟專科醫師甄審筆試 + 口試準備資源。以多個 LLM（Claude · Codex · Gemma）共同維護的 EBM 知識庫。

> **有腎臟考試相關的 paywall 文章？歡迎 DM 寄給我，我會加入知識庫。**
> 你手邊有跟考試相關的文獻（尤其 Review），歡迎私訊提供，我會整理進 wiki 讓大家都能用。

## 考試範圍（官方推薦書籍）

### 115年 (2026)
| 教科書 | 版次 |
|---|---|
| **Brenner & Rector's The Kidney** | 11e (2020) |
| **Principles and Practice of Dialysis** (Henrich) | 5e (2017) |
| **Pediatric Nephrology** (Avner) | 7e (2016) |

### 116年 (2027)
| 教科書 | 版次 |
|---|---|
| **Brenner & Rector's The Kidney** | 11e (2020) |
| **Handbook of Dialysis Therapy** (Nissenson & Fine) | 6e (2023) |
| **Pediatric Nephrology** (Emma) | 8e (2022) |

### 期刊來源（兩年皆適用）

一年內已發表之 Review：KI, AJKD, JASN, CJASN, Pediatric Nephrology, 台灣腎臟醫學雜誌

## 考試題型

- **Part A**：傳統考題（基礎）100 題
- **Part B**：臨床考題 50 題（部分含子題）
- **Part 2**：口試

## Wiki 內容

每個 .md 都是 EBM 格式：evidence grading (GRADE)、quantitative (HR/CI/NNT)、PMID citation。

### 腎臟科核心
| Topic | File |
|---|---|
| CKD 分期/流行病學/進展 | wiki_nephrology_ckd_part1.md |
| CKD 管理/保守治療/移植 | wiki_nephrology_ckd_part2.md |
| CKD 共病/心血管/骨代謝 | wiki_nephrology_ckd_part3.md |
| CKD 最新試驗/指引/生物標記 | wiki_nephrology_ckd_part4.md |
| 血液透析 | wiki_nephrology_dialysis_hd.md |
| 腹膜透析 | wiki_nephrology_dialysis_pd.md |
| AKI | wiki_nephrology_aki.md |
| 腎性貧血 | wiki_nephrology_anemia.md |
| 電解質與 CKD-MBD | wiki_nephrology_electrolytes.md |
| 高血壓與 CKD | wiki_nephrology_hypertension.md |
| CKD 減重 | wiki_ckd_obesity_weight_management.md |
| 考試範圍/缺口分析 | wiki_tsn_board_exam.md |

### 跨科 & 方法學
| Topic | File |
|---|---|
| EBM 研究方法 | wiki_research_methods_ebm.md |
| 營養與代謝 | wiki_nutrition_metabolism.md |
| 感染科 | wiki_infectious_disease.md |
| 心臟科 | wiki_cardiology_atherosclerosis.md |
| 內分泌 | wiki_endocrinology_diabetes.md |
| 藥理 | wiki_pharmacology_clinical.md |

## 使用方式

1. 直接閱讀 `.md` 檔案（GitHub 可預覽 Markdown）
2. **Clone 到本地，搭配你的 LLM 使用**（Claude/GPT/Gemini）— 推薦方式
3. 搜尋關鍵字：每個 claim 有 PMID/DOI，可直接查 PubMed
4. 有 paywall 文章？歡迎 DM 提供，我會加入知識庫

## 已知缺口（建置中）

| Topic | 考題比重 | 狀態 |
|---|---|---|
| 腎小管/TMA/妊娠/兒腎/遺傳 | ~37 題 (23%) | 🔴 缺 |
| 腎絲球疾病 | ~20 題 (13%) | 🔴 缺 |
| 移植 | ~16 題 (10%) | 🔴 缺 |
| AKI/毒物/CRRT | ~11 題 (7%) | 🟡 薄弱 |

## 作者

**王介立 醫師** — 腎臟專科，柏安透析中心
- FB: [王介立醫師](https://www.facebook.com/drchiehliwang)
- GitHub: [@copper0722](https://github.com/copper0722)

## 授權

CC BY-NC-SA 4.0｜非醫療建議，僅供教育與研究用途。

## 💡 關於我們的 AI 方法學 (Our Multi-Agent Methodology)

這個 Repo 並非由單一人類或單一 AI 獨立撰寫，而是透過 **Multi-Author Agent Model (多模型協作架構)** 在本地端自動巡檢、對抗與生成的結果。我們公開這個方法學，希望不僅幫助考生閱讀知識，也能讓有興趣的醫師或開發者了解現代醫學知識庫是如何透過自動化管道大規模建立的。

### 協作團隊與職責

本知識庫的背後有三位獨立的 LLM (Large Language Model) 進行非同步協作：

1. **Gemma 4 (The Builder / Bulk Processor)**
   - **職責**：知識鋪磚與缺口填補。
   - **排程**：每 2 小時自動巡檢。
   - **工作邏輯**：她會自動追蹤考題缺口 (Gap analysis)，讀取並濃縮海量的教科書與文獻原始檔（Raw .md），並將其結構化為適合考試閱讀的筆記格式，大量擴充知識庫基礎。

2. **Claude 3.5 Sonnet / Opus (The Workhorse & Editor-in-Chief)**
   - **職責**：EBM (實證醫學) 方法學把關、主力寫手與每週統籌。
   - **排程**：持續執行文獻讀取 (`/med-read` pipeline) 與每週發布審查。
   - **工作邏輯**：Wiki 的核心檔案主要由 Opus 透過 CC CLI (包含 Local 與 Cloud 端) 生成。兩者的分工為： 
     - **Local AI**：專注於處理具有版權或 Paywall 的敏感資訊（如原版教科書、付費期刊），確保考題基礎的本地化處理。
     - **Cloud CC**：主動訂閱與接收 RSS 最新醫學資訊，取得 Open Access (OA) 的文章並進行大規模的線上解析與 Wiki 寫入。
   - 確保每一條納入的醫學 Guideline 與 Paper 符合 EBM 框架（如 GRADE、NNT 等），並且過濾掉有方法學瑕疵的結論。

3. **OpenAI Codex / GPT-5.4 (The Adversarial Reviewer)**
   - **職責**：獨立的「對抗性審閱者 (Adversarial Reviewer)」。
   - **排程**：每天自動啟動一次 (Daily execution)。
   - **工作邏輯**：他被設定為「**挑錯者**」。他會自動檢查 Gemma 與 Claude 寫好的檔案，從不同的醫學邏輯維度去挑戰、抓錯。如果有爭議或考題常見的 Distractor，他會直接在文件中補上 `Codex:` 的批註，協助考生釐清盲點。

### 醫學實證與流行病學把關 (Editorial Methodology)

在審查每一篇文獻或每一個考點時，作為總編的 Claude (Opus) 嚴格遵循兩大流行病學教科書的審核框架：
1. **Causal Inference (Miguel Hernán):** 
   - 我們不會輕易將觀察性研究 (Observational claims) 合成為因果關係。在將資訊列入知識庫前，皆會經過其五大因果推論檢核：反事實 (Counterfactual) 是否明確定義？交擾因素 (Confounding) 是否被阻斷？是否有對撞偏差 (Collider bias) 或存活者偏差 (Immortal time bias) 的陷阱？
2. **Users' Guides to the Medical Literature (Gordon Guyatt 等):**
   - 所有的臨床建議皆需經過三個守門員：**Validity (效度) → Importance (重要性) → Applicability (適用性)**。
   - 包含對 RCT 所要求的 ITT 及盲測檢查；若是觀察型研究則著重比較組與劑量反應；我們且致力於量化指標 (ARR, RRR, NNT) 的萃取，而非只留下含糊的「顯著或不顯著」。

### 資料流 (Pipeline) 的運作方式
- **Ingestion**：PDF/文獻進入 Vault → 轉換成 M2M (Machine-to-Machine) 可讀的 Raw.md。
- **Evaluation**：各模型讀取 Raw.md，並將臨床珍珠、試驗數據與證據等級 (GRADE) 抽取出來。
- **Consolidation**：最後依據考題邏輯（而非純學術邏輯）重新將知識點安置於各個 Markdown 檔案中。
- **Push**：所有過程皆在本地伺服器內自動完成，確認無隱私病人數據後，透過 git 腳本自動推送到這個公開的 GitHub 專案。
