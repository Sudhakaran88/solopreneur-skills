#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md file against repo quality rules.

Hard failures (exit 1):
  - Missing/malformed frontmatter
  - `name` missing or mismatched with directory
  - `description` missing
  - `metadata.{version,author,license}` missing or wrong shape
  - Over MAX_LINES lines
  - Banned phrases anywhere in the body (excluding code spans / fences)

Advisory warnings (do not fail CI; printed for author attention):
  - Missing recommended sections (Common Mistakes, Contrarian Takes, Related Skills)
  - Missing or mismatched footer line
  - `description` outside 50–1024 characters
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"

REQUIRED_META = ["version", "author", "license"]
RECOMMENDED_SECTIONS = ["Common Mistakes", "Contrarian Takes", "Related Skills"]
MAX_LINES = 500
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 1024
FOOTER_TEMPLATE = "*Generated using the {name} skill from Solopreneur Skills*"

# Single source of truth for banned phrases. Match as whole words,
# case-insensitive. Multi-word phrases allow any run of whitespace.
BANNED_PHRASES = [
    "delve",
    "leverage",
    "unlock",
    "supercharge",
    "game-changer",
    "in today's landscape",
    "ever-evolving",
    "navigate the complexities",
    "robust",
    "seamless",
    "at the end of the day",
]


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    # Word-boundary wrap single words; collapse whitespace runs in multi-word phrases.
    tokens = phrase.split()
    escaped = r"\s+".join(re.escape(t) for t in tokens)
    return re.compile(rf"(?<![\w-]){escaped}(?![\w-])", re.IGNORECASE)


BANNED_PATTERNS = [(p, _phrase_pattern(p)) for p in BANNED_PHRASES]

# Strip fenced code blocks (```...```) and inline code (`...`) before scanning
# for banned phrases. Authors can quote the words verbatim in code spans when
# discussing them as terms (e.g. in copy-editing.md) without tripping the rule.
_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def _strip_code(body: str) -> str:
    body = _FENCED_CODE_RE.sub("", body)
    body = _INLINE_CODE_RE.sub("", body)
    return body


def validate(skill_md: Path):
    errors: list[str] = []
    warnings: list[str] = []
    parent_name = skill_md.parent.name
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    body = ""

    if len(lines) > MAX_LINES:
        errors.append(f"file is {len(lines)} lines (max {MAX_LINES})")

    if not text.startswith("---"):
        errors.append("missing YAML frontmatter")
        return errors, warnings

    try:
        _, fm, body = text.split("---", 2)
    except ValueError:
        errors.append("malformed frontmatter (no closing ---)")
        return errors, warnings

    try:
        data = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        errors.append(f"invalid YAML frontmatter: {e}")
        return errors, warnings

    name = data.get("name")
    if not name:
        errors.append("frontmatter missing 'name:'")
    elif name != parent_name:
        errors.append(f"name '{name}' != directory '{parent_name}'")

    description = data.get("description")
    if not description:
        errors.append("frontmatter missing 'description:'")
    else:
        dlen = len(description)
        if dlen < DESCRIPTION_MIN or dlen > DESCRIPTION_MAX:
            warnings.append(
                f"description is {dlen} chars (target {DESCRIPTION_MIN}–{DESCRIPTION_MAX})"
            )

    meta = data.get("metadata") or {}
    if not isinstance(meta, dict):
        errors.append("frontmatter 'metadata:' must be a mapping")
    else:
        for key in REQUIRED_META:
            if not meta.get(key):
                errors.append(f"frontmatter missing 'metadata.{key}:'")

    for section in RECOMMENDED_SECTIONS:
        if section not in body:
            warnings.append(f"recommended section '{section}' not found")

    if name:
        expected_footer = FOOTER_TEMPLATE.format(name=name)
        if expected_footer not in body:
            warnings.append(f"footer line missing or incorrect (expected: {expected_footer!r})")

    scan_body = _strip_code(body)
    for phrase, pattern in BANNED_PATTERNS:
        hits = pattern.findall(scan_body)
        if hits:
            errors.append(f"banned phrase {phrase!r} appears {len(hits)}x — rewrite")

    return errors, warnings


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: {SKILLS_DIR} does not exist")
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print(f"ERROR: no SKILL.md files found in {SKILLS_DIR}")
        return 1

    failed = 0
    warned = 0
    for skill_md in skill_files:
        rel = skill_md.relative_to(ROOT)
        errors, warnings = validate(skill_md)
        if errors:
            failed += 1
            print(f"FAIL: {rel}")
            for err in errors:
                print(f"  - {err}")
            for w in warnings:
                print(f"  ~ {w}")
        elif warnings:
            warned += 1
            print(f"OK:   {rel}")
            for w in warnings:
                print(f"  ~ {w}")
        else:
            print(f"OK:   {rel}")

    print()
    print(f"{len(skill_files) - failed}/{len(skill_files)} skills passed")
    if warned:
        print(f"{warned} skill(s) with advisory warnings (not blocking)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
