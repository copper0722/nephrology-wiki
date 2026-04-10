---
type: review
created: 2026-04-10
topic: 六模型 wiki 品質盲測比較
source: Aitken2020 (AVF patency RCT, JASN)
---

# 六款 AI 模型寫同一篇腎臟科 Wiki：品質盲測

## 測試設計

同一篇論文（Aitken 2020, JASN — AVF 區域麻醉 vs 局部麻醉 RCT, N=126），餵給六款模型，要求產出「腎臟專科考試導向 wiki」，格式規範相同（禁 LaTeX、需含 Exam Logic / Textbook Ref / Key Trials）。各模型獨立運作，互不參照。

---

## 六模型綜合比較（截圖用）

|                       | Gemma 4 8B | Gemma 4 31B | Codex (GPT-5.4) | Claude Opus 4.6 | Claude Sonnet 4.6 | Claude Haiku 4.5 |
| --------------------- | ---------- | ----------- | --------------- | --------------- | ----------------- | ---------------- |
| **類型**                | 本地 ollama  | 本地 ollama   | ChatGPT Plus    | Anthropic API   | Anthropic API     | Anthropic API    |
| **Token（含 context）**  | 0（免費）      | 0（免費）       | 21K（Plus 額度）    | 33K             | 25K               | 66K†             |
| **生成時間**              | 41s        | 189s        | 253s            | 88s             | 60s               | 32s              |
| **成本**                | $0         | $0          | 月費內             | ~$0.50          | ~$0.10            | ~$0.03           |
| **── 資料 ──**          |            |             |                 |                 |                   |                  |
| P-values / CI         | ❌ 漏        | ✅           | ✅               | ✅               | ✅                 | ✅                |
| Fragility index       | ❌          | ❌           | ✅               | ✅               | ✅                 | ✅                |
| RCF vs BCF 亞組         | ❌          | ❌           | ✅               | ✅               | ✅                 | ✅                |
| 迴歸分析 OR 0.35          | ❌          | ❌           | ❌               | ✅               | ✅                 | ✅                |
| Late maturation       | ❌          | ❌           | ❌               | ✅               | ✅                 | ✅                |
| **── 臨床 ──**          |            |             |                 |                 |                   |                  |
| 機轉深度                  | 基本         | 基本          | 簡潔              | 完整流程圖           | 分步驟               | 詳細               |
| Distractor 分析         | 3 個        | + 為何錯       | 簡要              | 5 題＋表格          | 5 題 Q&A           | 5 個角度            |
| NNT 計算                | ❌          | ❌           | ❌               | ✅ ≈5            | ❌                 | ❌                |
| Causal check (Hernán) | ❌          | ❌           | ❌               | ✅ 四項            | ❌                 | ❌                |
| **── 格式 ──**          |            |             |                 |                 |                   |                  |
| LaTeX ban 合規          | ❌ 2處       | ❌ 3處        | ✅               | ✅               | ✅                 | ✅                |
| 教科書章節號                | ❌          | ❌           | ✅               | ✅               | ✅                 | ✅                |
| Key Trials 數          | 1          | 1           | 1               | 3               | 4                 | 4                |
| **── 總評 ──**          |            |             |                 |                 |                   |                  |
| **排名**                | #6         | #5          | #4              | 🥇              | 🥈                | 🥉               |
| **定位**                | 不推薦        | 免費初稿        | 速查卡             | 最高品質            | 性價比之王             | 最快全面             |

### Token 附註

| | total_tokens | output（從檔案大小估算）| tool calls |
|---|---|---|---|
| **Gemma 4 8B** | 免費 | ~1,400 | — |
| **Gemma 4 31B** | 免費 | ~1,200 | — |
| **Codex (GPT-5.4)** | 21K | ~900 | 1 |
| **Claude Opus 4.6** | 33K | ~2,300 | 5 |
| **Claude Sonnet 4.6** | 25K | ~1,800 | 3 |
| **Claude Haiku 4.5** | 66K | ~2,100 | 1 |

`total_tokens` = input + output 合計，由 agent 框架回報，無 per-call 明細。各模型實際產出僅 1-2K tokens，其餘為 context（vault rules + tool schemas + prompt）。Haiku total 最高的原因不明 — 可能與框架對不同模型的 context 載入策略有關，但無法從單一數字驗證。**勿以 total_tokens 比較模型效率。**

---

## 綜合排名

| 排名 | 模型 | 強項 | 弱項 |
|---|---|---|---|
| 🥇 | **Opus 4.6** | 唯一做到 causal reasoning checklist、NNT、fragility 教學、5 題考題 + distractor 表。臨床推理最深 | 最貴（~$0.50），token 最多 |
| 🥈 | **Sonnet 4.6** | 結構最清晰、Q&A 格式好、clinical pearls 實用、性價比最高 | 無 NNT、無 causal check |
| 🥉 | **Haiku 4.5** | 最快（32s）、全面度接近 Sonnet、含 implementation 段落 | Token 異常高（65K）、教科書版本過舊（Nissenson 4e, Daugirdas 5e） |
| 4 | **Codex (GPT-5.4)** | 最精簡高效、章節號最具體 | 過於壓縮、無機轉圖、無亞組解釋 |
| 5 | **Gemma 4 31B** | 免費、P-values 正確、比 8B 好 | 漏 fragility index、無亞組、LaTeX violation |
| 6 | **Gemma 4 8B** | 免費、最快 | 漏 P-values、漏 CI、LaTeX violation、臨床深度不足 |

---

## 結論

1. **品質天花板 = Opus**：causal reasoning、fragility 解讀、NNT 計算 — 只有 Opus 做到全套。適合高品質 wiki 產出。
2. **性價比冠軍 = Sonnet**：品質接近 Opus 的 80%，成本只有 1/5。適合批量產出。
3. **免費方案 = Gemma 31B**：堪用但需 post-processing（LaTeX 替換、補 fragility、補亞組）。適合初稿 + 人工/AI 審核。
4. **Gemma 8B 不推薦用於醫學 wiki**：遺漏太多關鍵數據。
5. **Codex = 快速精簡摘要**：適合考前速查卡，不適合完整 wiki。
6. **Haiku 需注意教科書版本**：引用了過舊的版本號，可能誤導。

### 最佳工作流建議

```
Gemma 31B (免費批量初稿)
  → Sonnet (審核 + 補齊)
  → Opus (抽樣 editorial review)
```

這個三層流水線兼顧成本與品質，符合 nephrology-wiki 的 multi-author model。
