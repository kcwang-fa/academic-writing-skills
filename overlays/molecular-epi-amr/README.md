# molecular-epi-amr 疊加層

分子流行病學（NGS／WGS）與抗藥性研究用的寫作與審稿疊加層。它不會取代 `academic-writing-skills` 與 `paper-review`，而是在它們的流程上補充領域檢查。

本資料夾放在 `skills/` 之外，所以不屬於上游 plugin 的內容，也不影響上游的版本號檢查與翻譯 hash。

## 內容

| 檔案 | 用途 |
|---|---|
| `SKILL.md` | 適用範圍、載入規則、六項高優先檢查、寫作與審稿時的使用方式 |
| `references/reporting-guidelines.md` | STROME-ID、STROBE、RECORD、STROBE-AMS、ORION 等報告指引對照 |
| `references/genomic-epidemiology.md` | 定序品質、變異呼叫、分型、SNP 距離、親緣樹、分子時鐘、傳播推論、質體 |
| `references/amr-phenotype-genotype.md` | 藥敏方法、CLSI／EUCAST 判讀與版本、MDR／XDR 定義、抗藥基因偵測、VME／ME |
| `references/amr-clinical-epidemiology.md` | 監測分母、感染與移生、危險因子對照組、預後研究偏誤、抗生素用量 |
| `references/terminology-and-style.md` | 物種、基因、蛋白寫法與中英用語對照 |
| `evals/routing_cases.json` | 路由與界線測試案例 |

每條規則都標有類別：〔設計〕、〔領域〕或〔規範〕，沿用上游 `overlay-contract.md` 的分類，避免把領域慣例當成通用要求。

## 在 Claude Code 安裝

1. 安裝上游的基礎 skill：

```bash
claude plugin marketplace add WenyuChiou/ai-research-skills
```

```bash
claude plugin install academic-writing-skills@ai-research-skills --scope user
```

2. 把這個疊加層複製到個人 skill 資料夾：

```bash
git clone -b claude/laughing-bell-ck3wev https://github.com/kcwang-fa/academic-writing-skills.git
```

```bash
mkdir -p ~/.claude/skills && cp -r academic-writing-skills/overlays/molecular-epi-amr ~/.claude/skills/
```

只想在某個論文專案使用時，改複製到該專案的 `.claude/skills/`。

## 使用範例

```text
用 academic-writing-skills-zh-tw 搭配 molecular-epi-amr，修改這段 Methods 的 WGS 與 cgMLST 描述。
```

```text
用 paper-review-zh-tw 搭配 molecular-epi-amr 審查這篇 CRKP 群突發稿件，只審查不修改。
```

## 限制

- 參考檔中的指引版本、文獻與門檻為 2026 年整理時的認知，引用前請以原始文獻與 EQUATOR Network 最新版核對。
- 靜態測試只確認檔案結構、路由與界線文字存在，不能證明實際寫作或審稿品質；實際效果需要用真實稿件試用後調整。
- 中英用語對照是建議，不是官方標準。
