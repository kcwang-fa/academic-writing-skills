"""Static integrity checks for the molecular epidemiology / AMR overlay skill."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OVERLAY = ROOT / "overlays" / "molecular-epi-amr"
SKILL = OVERLAY / "SKILL.md"
REFERENCES = OVERLAY / "references"
EVALS = OVERLAY / "evals" / "routing_cases.json"
TAG = re.compile(r"〔(設計|領域|規範)〕")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def all_text() -> str:
    return "\n".join(read(p) for p in [SKILL, *sorted(REFERENCES.glob("*.md"))])


def test_frontmatter_names_the_overlay_and_its_base_skills():
    text = read(SKILL)
    match = re.match(r"---\nname: (?P<name>[^\n]+)\ndescription: (?P<desc>[^\n]+)\n---\n", text)
    assert match, "SKILL.md needs name and description frontmatter"
    assert match["name"] == "molecular-epi-amr"
    for base in ("academic-writing-skills", "paper-review"):
        assert base in match["desc"]


def test_every_reference_is_routed_and_every_route_exists():
    text = read(SKILL)
    linked = set(re.findall(r"\]\(references/([^)#]+\.md)\)", text))
    present = {p.name for p in REFERENCES.glob("*.md")}
    assert linked == present


def test_rules_carry_an_overlay_category():
    for path in REFERENCES.glob("*.md"):
        if path.name == "terminology-and-style.md":
            continue  # declared as domain convention as a whole
        text = read(path)
        assert TAG.search(text), f"{path.name} has no tagged rules"
        for line in (line for line in text.splitlines() if line.startswith("- 〔")):
            assert TAG.match(line[2:]), f"{path.name}: unknown category in {line[:40]}"


def test_overlay_states_its_integrity_boundaries():
    text = " ".join(all_text().split())
    for boundary in (
        "不是獨立的寫作流程",
        "不得升格為通用科學要求",
        "不得補上稿件或來源中沒有的",
        "不得替作者編造 accession",
        "基因型不等於表現型",
        "EQUATOR Network",
        "不要把本表的版本當作已核實事實",
    ):
        assert boundary in text, boundary


def test_routing_cases_point_at_real_references_and_stated_boundaries():
    data = json.loads(read(EVALS))
    present = {p.name for p in REFERENCES.glob("*.md")}
    text = " ".join(all_text().split())
    ids = [case["id"] for case in data["cases"]]
    assert len(ids) == len(set(ids))
    assert any(not case["expected_references"] for case in data["cases"]), "need an out-of-scope case"
    for case in data["cases"]:
        assert set(case["expected_references"]) <= present, case["id"]
        for boundary in case["required_boundaries"]:
            assert boundary in text, f"{case['id']}: {boundary}"
