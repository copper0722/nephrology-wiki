# Deprecated CME Template

This legacy module template is deprecated as of 2026-04-26.

Use [`_template-v2.md`](./_template-v2.md) for all new CME work.

Current schema rule:

- one question = one Markdown file under `cme/bank/{source}/{id}.md`
- 4 options only (`A-D`)
- single best answer
- required frontmatter: `schema_version`, `id`, `source_kind`, `license_class`, `public_safety`, `review_state`, `topic_tags`, `brenner_topic`, `difficulty`, `bloom`, `answer`
- each option carries its own textbook-anchored `Why` and `Sources` block

Do not create new questions from this file.
