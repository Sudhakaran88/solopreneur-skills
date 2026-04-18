#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md file against repo quality rules."""
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
REQUIRED_META = ["version", "author", "license"]
# Marketing skills should include these for consistency. Audit/build skills
# (website-audit, shopify-audit, etc.) use a different structure (checklists,
# step-by-step flows) so section enforcement is advisory only.
RECOMMENDED_SECTIONS = ["Common Mistakes", "Related Skills"]
MAX_LINES = 500


def validate(skill_md: Path):
    errors: list[str] = []
    parent_name = skill_md.parent.name
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    body = ""

    if len(lines) > MAX_LINES:
        errors.append(f"file is {len(lines)} lines (max {MAX_LINES})")

    if not text.startswith("---"):
        errors.append("missing YAML frontmatter")
        return errors, []

    try:
        _, fm, body = text.split("---", 2)
    except ValueError:
        errors.append("malformed frontmatter (no closing ---)")
        return errors, []

    try:
        data = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        errors.append(f"invalid YAML frontmatter: {e}")
        return errors, []

    if not data.get("name"):
        errors.append("frontmatter missing 'name:'")
    elif data["name"] != parent_name:
        errors.append(f"name '{data['name']}' != directory '{parent_name}'")

    if not data.get("description"):
        errors.append("frontmatter missing 'description:'")

    meta = data.get("metadata") or {}
    if not isinstance(meta, dict):
        errors.append("frontmatter 'metadata:' must be a mapping")
    else:
        for key in REQUIRED_META:
            if not meta.get(key):
                errors.append(f"frontmatter missing 'metadata.{key}:'")

    warnings = []
    for section in RECOMMENDED_SECTIONS:
        if section not in body:
            warnings.append(f"recommended section '{section}' not found")

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
