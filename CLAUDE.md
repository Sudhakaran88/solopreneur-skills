# CLAUDE.md

Instructions for Claude Code instances working in this repo. For the full authoring spec see [`AGENTS.md`](./AGENTS.md); for contribution flow see [`CONTRIBUTING.md`](./CONTRIBUTING.md). If this file disagrees with either, `AGENTS.md` wins.

## Repository purpose

Open-source Claude skills for solopreneur marketing — SEO, CRO, copywriting, email, pricing, growth, and analytics. Each skill packages opinionated, research-backed guidance a founder can run without hiring a specialist.

## Skill structure

Every skill lives at `skills/<skill-name>/SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: One sentence on when to use this skill, with trigger phrases. 50–1024 characters.
metadata:
  version: 1.0.0
  author: Your Name
  license: MIT
---
```

The filename is always `SKILL.md` (uppercase). The folder name is kebab-case and matches the `name` field.

## When adding skills

1. Read `CONTRIBUTING.md` end-to-end before writing.
2. Check existing skills in `skills/` for overlap — prefer extending a sibling skill over creating a near-duplicate.
3. Research before writing: Reddit threads, practitioner blogs, primary frameworks. Every non-obvious claim should be traceable to a source.
4. Draft the skill, then run the validator.

## When editing skills

- Preserve the `metadata.version` field in frontmatter.
- Bump version on meaningful content changes (not typos): patch for fixes, minor for added sections, major for reorganization.
- Log the change in `VERSIONS.md`.
- Run the validator before committing.

## Style rules

- Target under 500 lines per `SKILL.md`. If you are over, you are padding.
- Plain markdown. Minimal emoji — none in body copy, sparingly in section headers only if the skill already uses them.
- Banned phrases (single source of truth — enforced by the validator as warnings): `delve`, `leverage`, `unlock`, `supercharge`, `game-changer`, `in today's landscape`, `ever-evolving`, `navigate the complexities`, `robust`, `seamless`, `at the end of the day`.
- Cite sources inline with the year: `(Baymard, 2024)`, `(Nielsen Norman, 2023)`.
- Every skill must include these three sections: `Common Mistakes`, `Contrarian Takes`, `Related Skills`.
- Every skill must end with the footer: `*Generated using the <skill-name> skill from Solopreneur Skills*`.

## Testing a skill

```bash
python .github/scripts/validate_skills.py
```

The validator checks frontmatter (name, description length, `metadata.{version,author,license}`), required sections, footer line, line count, and banned phrases.

## Commit style

Conventional commits:

- `feat: add churn-prevention skill`
- `fix: correct frontmatter version in cold-email`
- `docs: expand installation guide`
- `chore: update validator script`

Keep the subject under 72 characters. Body optional but welcome for non-trivial changes.
