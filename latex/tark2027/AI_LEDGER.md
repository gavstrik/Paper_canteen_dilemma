# AI Ledger

Every action taken by an AI assistant (Claude Code, model Claude Opus 5.5) on the TARK 2027 version of this paper.
Purpose: (1) transparency to co-authors, (2) source for the mandatory TARK AI-use disclosure paragraph.

Categories: `infra` (build, files, tooling — no text change) · `move` (text relocated verbatim) · `cut` (text deleted) · `condense` (text shortened/rephrased) · `new` (new text written) · `fix` (typo, ref, formatting).
Validation column: who checked it and how. `pending` until a human author has reviewed.

| # | Date | Category | What | Files | Validation |
|---|---|---|---|---|---|
| 1 | 2026-11-09 | infra | Created branch `tark2027`; new dir `latex/tark2027/` with EPTCS style files (`eptcs.cls` v1.7, `eptcs.bst` from eptcs.org). | — | TSN approved approach |
| 2 | 2026-11-09 | infra | Copied verbatim from `latex/Arxiv Oct 2025 (PLOS ONE version)/`: `body.tex`, `supplementary.tex`, `images/`, `plots/`; and `latex/cd.bib`. No edits. | body.tex, supplementary.tex, cd.bib | `cmp` |
| 3 | 2026-11-09 | infra | Split `body.tex` at `\appendix` into `body.tex` (main text, l.1–483) and `appendix.tex` (l.484–726). Lossless. | body.tex, appendix.tex | `cat body appendix \| cmp` with original: identical |
| 4 | 2026-11-09 | infra | Extracted abstract verbatim (incl. comments) from arXiv `main.tex` l.196–245 into `abstract.tex`. | abstract.tex | sed line range |
| 5 | 2026-11-09 | infra | New `main.tex` in EPTCS format: ported packages/macros used by body; dropped PLOS layout hacks (margins, `\figurename{Fig}`, caption style, `\DisableLigatures` — pdflatex-only); authors via `\institute`; bibliography style `plain` → `eptcs`; order now main → acks → refs → appendix → supplementary; `\label{mainend}` marks end of counted text. Acknowledgments text verbatim. | main.tex | Compiles; main-text word count 12,098 vs 11,854 in arXiv PDF (diff = acks + running heads) |
| 6 | 2026-11-09 | infra | `build.sh`: tectonic compile, reports page on which main text ends, fails on >10 pages, live author comments (`\tobo` etc. rendering), undefined refs/cites. | build.sh | Run; baseline main text ends p.23 |
