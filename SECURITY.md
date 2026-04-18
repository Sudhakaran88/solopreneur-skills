# Security Policy

## Scope

This repository contains marketing and growth skill definitions (Markdown files) and a small Python validator script. It ships no runtime code to end users. The realistic security surface is:

- The validator script and its CI workflow in `.github/`
- Markdown content that may be loaded into an AI agent's context
- The skills' recommendations themselves (e.g. advice that could harm deliverability, compliance, or legal posture if followed blindly)

## Supported Versions

The `main` branch is the only supported version. Releases tagged on `main` receive fixes.

## Reporting a Vulnerability

Please do **not** open a public issue for security problems.

Report privately via one of:

1. GitHub's [private vulnerability reporting](https://github.com/Sudhakaran88/solopreneur-skills/security/advisories/new) (preferred).
2. A direct message to the maintainer on [LinkedIn](https://www.linkedin.com/in/sudhakaran88/).

Please include:

- A description of the issue and its impact
- Steps to reproduce (for CI/tooling issues) or the skill path + line numbers (for content issues)
- Your assessment of severity

You can expect an initial acknowledgement within 7 days. Fixes for valid reports are typically merged within 30 days, with credit to the reporter in the changelog unless you request otherwise.

## What qualifies as a security issue

- Vulnerabilities in the validator script or GitHub Actions workflow
- Supply-chain concerns (dependency pinning, action SHAs, token permissions)
- Skill content that instructs users to perform actions violating law, platform ToS (Gmail bulk sender rules, CAN-SPAM, GDPR, Google scaled-content-abuse policy), or that enables harmful behavior (dark patterns, deceptive pricing)
- Leaked credentials or secrets in git history

## What does not qualify

- Disagreement with a marketing tactic on effectiveness grounds — open a normal issue or PR instead
- Typos, broken links, or missing sources — open a normal issue or PR
