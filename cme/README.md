# CME 題庫區

這個資料夾是互動 Q-bank 的 Markdown source。題庫入口在 [`../docs/qbank/`](../docs/qbank/)，目的是把知識點轉成可反覆作答的 TSN 4-option (A-D) 單選題，練習「分期、判讀、風險分層、臨床推論」。

所有題目都以本 repo 的 wiki 為基礎重新編寫，內容公開、安全、原創，不放病人個資，也不直接轉貼考古題或付費題庫。

## 怎麼使用

1. 先讀對應的 wiki 主題，建立基本架構。
2. 再做 CME 模組，先自行作答，不要先看答案。
3. 對答案時，回看每題後面的 `Source` 與 wiki 連結，把錯題回到原文整理。
4. 第二輪練習時，優先重做自己錯過的題目與同主題模組。

建議起手式：

- 先讀 [CKD Part 1](../wiki/wiki_nephrology_ckd_part1.md)
- 再做 [CKD 分期模組](nephrology-ckd-staging.md)

## 題型設計

- `Part A｜基礎題`
  - 對應甄審筆試的基礎題型。
  - 常見內容是定義、切點、分期、公式、關鍵數字。
- `Part B｜臨床題`
  - 對應臨床情境題。
  - 常見內容是病例分期、風險判讀、檢驗解讀、下一步判斷。
- 每題固定為單選題，`A-D` 四個選項。
- 每題都有完整解析，且會說明其他選項為什麼錯。

## 難度分級

- `recall`
  - 純記憶與基本理解，例如 CKD 定義、GFR category、albuminuria category。
- `application`
  - 把知識套用到病例，例如依 eGFR + UACR 做 CGA staging 或 heat map 判讀。
- `analysis`
  - 比較多組資料、解釋矛盾資訊、判斷哪個風險訊號更重要。

## CME 與 Wiki 的導航方式

- 每個模組前言都會標示對應 wiki 來源。
- 每題答案區都會放 `Source`，直接連回原始 wiki 檔案。
- 如果你是先從 wiki 讀起，可以沿著模組連結做題。
- 如果你是先從題目開始，也可以用答案區的連結回去補概念。

## 進度追蹤

互動版會在瀏覽器 `localStorage` 記錄本機正答/錯答與弱點 topic；資料不會上傳。若需要長期筆記，也可在自己的 fork、本地 markdown 複本，或筆記軟體中追蹤。

可用的最簡單格式：

- [ ] [CKD 分期與風險分層（10 題）](nephrology-ckd-staging.md)

每做完一個模組，至少記三件事：

- 完成日期
- 正答數 / 總題數
- 需要回讀的 wiki 主題

## 目前模組

| 模組 | 對應 wiki | 題數 | 重點 |
|---|---|---:|---|
| [CKD 分期與風險分層](nephrology-ckd-staging.md) | [wiki_nephrology_ckd_part1.md](../wiki/wiki_nephrology_ckd_part1.md) | 10 | CKD 定義、CGA staging、KDIGO heat map、eGFR equation、進展風險 |
