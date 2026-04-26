#!/usr/bin/env python3
"""Build cme/index.json and docs/qbank/questions.json from CME Markdown."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CME_DIR = ROOT / "cme"
DOCS_QBANK = ROOT / "docs" / "qbank"

ANSWER_RE = re.compile(r"^(?:Correct answer|正確答案|answer)\s*[:：]\s*([A-E])\b", re.I)
QUESTION_HEADING_RE = re.compile(r"^##\s+(?:Q(?P<qnum>\d+)|題目\s*(?P<cnum>\d+))\b", re.I)
OPTION_RE = re.compile(r"^\s*(?:###\s*)?([A-E])[.)．、]\s+(.+?)\s*$")
FIELD_RE = re.compile(r"^(Type|Difficulty|Bloom)\s*:\s*(.+?)\s*$", re.I)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break
    if end_index is None:
        return {}, text
    raw = "\n".join(lines[1:end_index])
    meta = yaml.safe_load(raw) or {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, "\n".join(lines[end_index + 1 :])


def source_files() -> list[Path]:
    excluded_names = {"README.md", "CLAUDE.md"}
    files: list[Path] = []
    for path in sorted(CME_DIR.rglob("*.md")):
        if path.name in excluded_names or path.name.startswith("_template"):
            continue
        files.append(path)
    return files


def slug_anchor(title: str) -> str:
    cleaned = re.sub(r"^#+\s*", "", title.strip()).lower()
    cleaned = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", cleaned).strip("-")
    return f"#{cleaned or 'question'}"


def split_questions(path: Path, meta: dict[str, Any], body: str) -> list[dict[str, Any]]:
    lines = body.splitlines()
    headings: list[tuple[int, str, str]] = []
    module = str(meta.get("module") or meta.get("id") or path.stem)

    for idx, line in enumerate(lines):
        match = QUESTION_HEADING_RE.match(line)
        if not match:
            continue
        num = match.group("qnum") or match.group("cnum") or str(len(headings) + 1)
        qid = f"{module}-q{int(num):02d}"
        headings.append((idx, qid, line))

    if not headings:
        return [{"qid": str(meta.get("id") or module), "heading": "", "anchor": "#", "text": body}]

    blocks: list[dict[str, Any]] = []
    for block_idx, (start, qid, heading) in enumerate(headings):
        end = headings[block_idx + 1][0] if block_idx + 1 < len(headings) else len(lines)
        blocks.append({"qid": qid, "heading": heading, "anchor": slug_anchor(heading), "text": "\n".join(lines[start:end])})
    return blocks


def field_value(block: str, name: str) -> str | None:
    for line in block.splitlines():
        match = FIELD_RE.match(line.strip())
        if match and match.group(1).lower() == name.lower():
            return match.group(2).strip()
    return None


def answer_value(block: str, meta: dict[str, Any], single_block: bool) -> str | None:
    if single_block and meta.get("answer"):
        return str(meta["answer"]).strip().upper()
    for line in block.splitlines():
        match = ANSWER_RE.match(line.strip())
        if match:
            return match.group(1).upper()
    return None


def extract_stem(block: str) -> str:
    lines = block.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip() in {"Stem:", "題幹：", "題幹:"} or line.strip() == "## Stem":
            start = idx + 1
            break
    if start is None:
        return ""
    collected: list[str] = []
    for line in lines[start:]:
        if line.strip() in {"Options:", "### Answer", "### 答案"} or OPTION_RE.match(line):
            break
        cleaned = line.strip().removeprefix(">").strip()
        if cleaned:
            collected.append(cleaned)
    return "\n".join(collected)


def extract_options(block: str) -> dict[str, str]:
    options: dict[str, str] = {}
    for line in block.splitlines():
        match = OPTION_RE.match(line)
        if match and match.group(1) in {"A", "B", "C", "D"}:
            options[match.group(1)] = match.group(2).strip()
    return options


def extract_explanation(block: str) -> str:
    lines = block.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip() in {"### Explanation", "### 解析"}:
            start = idx + 1
            break
    if start is None:
        return ""
    collected: list[str] = []
    for line in lines[start:]:
        if line.startswith("### ") and collected:
            break
        cleaned = line.strip()
        if cleaned and not cleaned.startswith("Source:") and not cleaned.startswith("Source：") and not cleaned.startswith("Section:"):
            collected.append(cleaned)
    return "\n".join(collected)


def extract_option_whys(block: str, explanation: str) -> dict[str, str]:
    whys = {letter: "" for letter in "ABCD"}
    for line in block.splitlines():
        match = re.match(r"^\s*[-*]\s*([A-D])\s*[:：]\s*(.+?)\s*$", line)
        if match:
            whys[match.group(1)] = match.group(2).strip()
    if any(whys.values()):
        return whys

    # v2 files keep Why blocks under each option heading.
    for letter in "ABCD":
        pattern = re.compile(rf"^###\s+{letter}[.)．、]\s+.*?$([\s\S]*?)(?=^###\s+[A-D][.)．、]\s+|^##\s+Distractor|\Z)", re.M)
        match = pattern.search(block)
        if not match:
            continue
        why_match = re.search(r"\*\*Why\*\*.*?:\s*\n([\s\S]*?)(?=\n\*\*Sources\*\*:|\n###|\Z)", match.group(1), re.M)
        if why_match:
            whys[letter] = "\n".join(line.strip().removeprefix(">").strip() for line in why_match.group(1).splitlines() if line.strip())

    if any(whys.values()):
        return whys
    return {letter: explanation for letter in "ABCD"}


def build() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    index: list[dict[str, Any]] = []
    questions: list[dict[str, Any]] = []

    for path in source_files():
        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        blocks = split_questions(path, meta, body)
        for block in blocks:
            qtext = block["text"]
            answer = answer_value(qtext, meta, single_block=len(blocks) == 1)
            difficulty = field_value(qtext, "Difficulty") or meta.get("difficulty")
            bloom = field_value(qtext, "Bloom") or meta.get("bloom") or meta.get("bloom_level")
            topic_tags = meta.get("topic_tags") or meta.get("tags") or [meta.get("topic") or path.stem]
            if isinstance(topic_tags, str):
                topic_tags = [topic_tags]

            entry = {
                "id": block["qid"],
                "source_kind": meta.get("source_kind") or "legacy_module",
                "topic_tags": topic_tags,
                "brenner_topic": meta.get("brenner_topic"),
                "difficulty": difficulty,
                "bloom": bloom,
                "answer": answer,
                "public_safety": meta.get("public_safety"),
                "review_state": meta.get("review_state"),
                "file_path": rel(path),
                "anchor": block["anchor"],
            }
            index.append(entry)

            explanation = extract_explanation(qtext)
            options = extract_options(qtext)
            questions.append(
                {
                    **entry,
                    "module": meta.get("module") or path.stem,
                    "title": meta.get("topic") or path.stem,
                    "stem": extract_stem(qtext),
                    "options": [{"letter": letter, "text": options.get(letter, "")} for letter in "ABCD"],
                    "explanation": explanation,
                    "option_whys": extract_option_whys(qtext, explanation),
                }
            )

    return index, questions


def main() -> int:
    index, questions = build()
    (CME_DIR / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    DOCS_QBANK.mkdir(parents=True, exist_ok=True)
    (DOCS_QBANK / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(index)} entries to {rel(CME_DIR / 'index.json')}")
    print(f"Wrote {len(questions)} questions to {rel(DOCS_QBANK / 'questions.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
