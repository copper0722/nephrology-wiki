#!/usr/bin/env python3
"""Validate nephro-cme question Markdown against the public v2 gates."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised in fresh envs
    print("ERROR: PyYAML is required. Run: python3 -m pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(2) from exc


ROOT = Path(__file__).resolve().parents[1]
CME_DIR = ROOT / "cme"

ANSWER_RE = re.compile(r"^(?:Correct answer|正確答案|answer)\s*[:：]\s*([A-E])\b", re.I)
QUESTION_HEADING_RE = re.compile(r"^##\s+(?:Q(?P<qnum>\d+)|題目\s*(?P<cnum>\d+))\b", re.I)
OPTION_E_RE = re.compile(r"^\s*(?:###\s*)?E[.)．、:：]\s+")
DISTRACTOR_E_RE = re.compile(r"^\s*[-*]\s*E\s*[:：]\s+")


@dataclass
class Message:
    level: str
    line: int
    text: str


@dataclass
class QuestionBlock:
    qid: str
    start: int
    text: str


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, 1
    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break
    if end_index is None:
        return {}, text, 1
    raw = "\n".join(lines[1:end_index])
    meta = yaml.safe_load(raw) or {}
    if not isinstance(meta, dict):
        meta = {}
    body = "\n".join(lines[end_index + 1 :])
    return meta, body, end_index + 2


def default_files() -> list[Path]:
    excluded_names = {"README.md", "CLAUDE.md"}
    files: list[Path] = []
    for path in sorted(CME_DIR.rglob("*.md")):
        if path.name in excluded_names:
            continue
        if path.name.startswith("_template"):
            continue
        files.append(path)
    return files


def question_blocks(path: Path, meta: dict[str, Any], text: str) -> list[QuestionBlock]:
    lines = text.splitlines()
    headings: list[tuple[int, str]] = []
    module = str(meta.get("module") or meta.get("id") or path.stem)
    for lineno, line in enumerate(lines, start=1):
        match = QUESTION_HEADING_RE.match(line)
        if match:
            num = match.group("qnum") or match.group("cnum") or str(len(headings) + 1)
            headings.append((lineno, f"{module}-q{int(num):02d}"))

    if not headings:
        qid = str(meta.get("id") or module)
        return [QuestionBlock(qid=qid, start=1, text=text)]

    blocks: list[QuestionBlock] = []
    for idx, (start, qid) in enumerate(headings):
        end = headings[idx + 1][0] - 1 if idx + 1 < len(headings) else len(lines)
        blocks.append(QuestionBlock(qid=qid, start=start, text="\n".join(lines[start - 1 : end])))
    return blocks


def answer_for(block: QuestionBlock, meta: dict[str, Any], single_block: bool) -> str | None:
    if single_block and meta.get("answer") is not None:
        return str(meta["answer"]).strip().upper()
    for line in block.text.splitlines():
        match = ANSWER_RE.match(line.strip())
        if match:
            return match.group(1).upper()
    return None


def validate_file(path: Path, seen: dict[str, Path]) -> tuple[list[Message], list[Message]]:
    text = path.read_text(encoding="utf-8")
    meta, _body, _body_start = split_frontmatter(text)
    errors: list[Message] = []
    warnings: list[Message] = []

    for lineno, line in enumerate(text.splitlines(), start=1):
        if OPTION_E_RE.match(line) or DISTRACTOR_E_RE.match(line):
            errors.append(Message("ERROR", lineno, "option/distractor E is present; v2 requires A-D only"))

    for field in ("license_class", "public_safety"):
        if not meta.get(field):
            errors.append(Message("ERROR", 1, f"missing required frontmatter field: {field}"))

    if not meta.get("brenner_topic"):
        warnings.append(Message("WARN", 1, "missing brenner_topic; warn-only until topic index is populated"))

    blocks = question_blocks(path, meta, text)
    for block in blocks:
        if block.qid in seen:
            errors.append(Message("ERROR", block.start, f"duplicate question id: {block.qid} also in {rel(seen[block.qid])}"))
        else:
            seen[block.qid] = path

        answer = answer_for(block, meta, single_block=len(blocks) == 1)
        if not answer:
            errors.append(Message("ERROR", block.start, f"{block.qid}: missing answer key"))
        elif answer not in {"A", "B", "C", "D"}:
            errors.append(Message("ERROR", block.start, f"{block.qid}: answer must be A-D, got {answer}"))

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CME Markdown files against v2 gates.")
    parser.add_argument("files", nargs="*", type=Path, help="Specific files to validate. Defaults to cme/**/*.md modules.")
    args = parser.parse_args()

    files = args.files or default_files()
    seen: dict[str, Path] = {}
    failed = False

    for path in files:
        full_path = path if path.is_absolute() else ROOT / path
        errors, warnings = validate_file(full_path, seen)
        status = "FAIL" if errors else "PASS"
        print(f"{status} {rel(full_path)}")
        for msg in [*errors, *warnings]:
            print(f"  {msg.level} line {msg.line}: {msg.text}")
        failed = failed or bool(errors)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
