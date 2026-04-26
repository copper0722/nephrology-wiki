-- nephro-cme Week 1 schema bootstrap
-- DDL only. Do not execute from this file during Codex Week 1.

CREATE TABLE IF NOT EXISTS brenner_topic_index (
  topic_slug TEXT PRIMARY KEY,
  canonical_path TEXT NOT NULL,
  edition TEXT NOT NULL,
  chapter TEXT,
  title TEXT NOT NULL,
  superseded_by TEXT,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS cme_question_wiki_refs (
  q_id TEXT NOT NULL,
  option_letter CHAR(1) NOT NULL CHECK (option_letter IN ('A', 'B', 'C', 'D')),
  wiki_path TEXT NOT NULL,
  section_anchor TEXT,
  score REAL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (q_id, option_letter)
);
