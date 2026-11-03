---
name: molecular-epi-amr
description: 分子流行病學（NGS／全基因體定序）與抗藥性（AMR）研究的寫作與審稿疊加層，搭配 academic-writing-skills 或 paper-review 使用。Use for manuscripts on bacterial or viral genomic epidemiology, WGS-based typing (MLST, cgMLST, SNP distance), phylogenetics and transmission inference, outbreak investigation, antimicrobial susceptibility testing (MIC, CLSI/EUCAST breakpoints), resistance genes and plasmids (ESBL, carbapenemase, mcr), genotype–phenotype concordance, AMR surveillance, or risk-factor and outcome studies of resistant infections. Triggers include 抗藥性、抗生素抗藥、分子流病、全基因體定序、次世代定序、菌株分型、群聚感染、院內感染、AMR, WGS, NGS, CRE, CRAB, MRSA, ESBL.
---

# 分子流行病學與抗藥性研究疊加層

## 定位

本 skill 是**疊加層**，不是獨立的寫作流程。寫作、修改時以 `academic-writing-skills`（繁中版 `academic-writing-skills-zh-tw`）為基礎；審稿時以 `paper-review`（繁中版 `paper-review-zh-tw`）為基礎。基礎 skill 的誠信關卡、處理範圍、嚴重度（S0–S4）與功能完整性回顧一律保留，本疊加層只補充領域檢查。

套用前先讀基礎 skill 的 `overlay-contract.md`。本疊加層中的每條規則都已標示類別：

- **〔設計〕**：由研究設計推導出的要求
- **〔領域〕**：本領域的慣例、術語或常見證據形式
- **〔規範〕**：特定報告指引或期刊要求，只在作者採用該指引或投稿該期刊時才是要求

〔領域〕與〔規範〕不得升格為通用科學要求。清單項目是「需要稿件證據回答的問題」，不是自動判定錯誤的依據；稿件沒寫，先判斷是「未報告」還是「沒做」，不要替作者推定。

## 適用與排除

**適用：**病原體基因體流行病學、群聚或院內傳播調查、抗藥性監測、抗藥基因與質體研究、基因型–表現型一致性研究、抗藥性感染的危險因子或預後研究、宿主基因與感染相關研究中的病原體部分。

**排除或交給其他工具：**

- 系統性回顧與統合分析的檢索、篩選、GRADE：交給 `pubmed-to-meta` skill；本疊加層只檢查寫作與推論界線。
- 定序資料的實際分析、pipeline 執行：交給 `bio-research` plugin 的相關 skill；本疊加層不執行分析，也不產生數值。
- 純宿主基因體、腫瘤基因體、非感染性疾病：不適用。
- 只做文法或用字修改：只套用 [terminology-and-style.md](references/terminology-and-style.md)，不要展開全套檢查。

## 依任務載入參考檔

只載入與稿件實際內容相符的檔案，混合型研究可同時載入多個：

| 稿件內容 | 載入 |
|---|---|
| 選擇或核對報告指引 | [reporting-guidelines.md](references/reporting-guidelines.md) |
| 定序、組裝、分型、SNP 距離、親緣樹、傳播推論、群聚調查 | [genomic-epidemiology.md](references/genomic-epidemiology.md) |
| 藥敏試驗、MIC、判讀標準、抗藥基因、質體、基因型–表現型一致性 | [amr-phenotype-genotype.md](references/amr-phenotype-genotype.md) |
| 抗藥性盛行率、監測資料、危險因子、臨床預後 | [amr-clinical-epidemiology.md](references/amr-clinical-epidemiology.md) |
| 物種、基因、蛋白、抗藥表型的寫法與中英用語 | [terminology-and-style.md](references/terminology-and-style.md) |

## 高優先檢查（任何實質章節都要先確認）

1. **推論單位一致〔設計〕：**分母是分離株、病人、住院事件還是樣本？摘要、結果、表格是否用同一個單位？同一病人重複分離株是否去重？
2. **基因型不等於表現型〔領域〕：**偵測到抗藥基因時，文字是否寫成「帶有 *bla*<sub>KPC-2</sub>」而非「具抗藥性」，除非有表現型藥敏結果支持？
3. **基因相關不等於直接傳播〔領域〕：**SNP 距離小或同一 cluster，只能支持「基因上相近、與傳播相符」；直接傳播需要流行病學連結（時間、地點、接觸）佐證。
4. **判讀標準與版本〔規範〕：**藥敏結果是否寫明 CLSI 或 EUCAST、年份與版本？跨年度資料是否用同一版本重新判讀，或說明版本差異？
5. **抽樣與確認偏誤〔設計〕：**分離株是全部收集、隨機抽樣、還是只送抗藥株或參考實驗室株？推論範圍是否與抽樣方式相符（例如不能用送驗株估計族群盛行率）？
6. **重現性與資料可取得性〔規範〕：**原始 reads 的 BioProject／accession、工具與資料庫版本、參考基因體、主要參數是否都已提供？

## 寫作時

- 先用基礎 skill 的段落寫作契約，再把上面相關的檢查放進「證據」與「推論界線」欄位。
- 機制解釋（例如「因為 efflux pump 過度表現導致抗藥」）只有在稿件有表現量、突變或功能實驗證據時才能寫成結論；否則寫成假說，並標示需要的證據。
- 不得補上稿件或來源中沒有的 accession、版本號、判讀標準、SNP 門檻、序列型別或統計數值；缺少時列為待作者提供。

## 審稿時

在 `paper-review` 的審稿備忘錄表頭 `MODULES:` 欄位寫明：`molecular-epi-amr` 以及實際載入的參考檔與原因。每個問題沿用基礎 skill 的嚴重度與證據狀態，另外標出規則類別（〔設計〕／〔領域〕／〔規範〕）。

報告指引的缺漏項目，若不影響推論效度，通常屬於報告完整性問題，不要與效度問題混為同一嚴重度。

## 回報

在基礎 skill 的回報格式之外，加註：

- 採用了哪一份報告指引，或為何沒有採用
- 哪些領域檢查因資料未提供而列為「無法核實」
- 是否有任何文字把基因型寫成表現型、把基因相近寫成直接傳播、或把相關寫成因果
