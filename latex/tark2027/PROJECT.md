# TARK 2027 cut-down — project brief

Read this first in every session. Then `CFP.md`, `CUTS.md`, `AI_LEDGER.md`.

## Goal
Cut "The Curse of Shared Knowledge" (Bolander, Engelhardt, Nicolet) from the arXiv/PLOS ONE version
(~22 EPTCS pages main text, ~12k words) to **≤ 10 EPTCS pages excluding references** for TARK 2027
(submission 19 March 2027). Venue shift: cog-sci → logic/rationality audience.

Spirit: **be gentle with the paper.** It must survive as itself and fit TARK. No co-author constraints.

## Source of truth
- Original: `../Arxiv Oct 2025 (PLOS ONE version)/` on branch `main`. **Never edit it. Never touch `main`.**
- Working version: `latex/tark2027/` on branch `tark2027`. PR to `main` when ready.
- `cd.bib` here is a fork of `latex/cd.bib` (submission dir must be self-contained).

## Files
| File | Role |
|---|---|
| `main.tex` | EPTCS wrapper; `\label{mainend}` marks end of counted text |
| `abstract.tex`, `body.tex` | counted main text |
| `appendix.tex`, `supplementary.tex` | uncounted; reviewers need not read |
| `build.sh` | compile + budget check. **Run after every edit.** |
| `CUTS.md` | what left the main text, where it went |
| `AI_LEDGER.md` | every AI action; source for TARK AI disclosure |

## Rules for editing
1. **Delete or move before rewriting.** Moving to appendix is preferred over deleting.
2. **Keep the authors' voice and match the paper's tone** (measured, hedged, plain academic prose, first-person plural). When condensing, reuse the authors' own sentences and words. No new framing, no AI-flavoured prose ("delve", "crucially", "notably", "underscores", tricolons, em-dash chains).
2b. **Mark changed or added text with `\modified{...}`** (macro in `main.tex`; `\showmodifiedtrue` renders it red, `\showmodifiedfalse` renders it plain for submission). Pure moves and deletions are not marked; `CUTS.md` covers those. Be pragmatic: wrap whole changed sentences, not single words. Some text will unavoidably be AI-written. That's accepted, as long as it's marked and logged.
3. **No new citations** unless a human author verifies the source exists and says what it is claimed to say.
4. **No change to claims, numbers, statistics, or formal results.** Condensing must not strengthen or weaken a claim.
5. **One section per iteration.** Build, check page count, check refs, commit.
6. **Every edit → one `AI_LEDGER.md` row + (if text left main) one `CUTS.md` row.** Same commit.
7. After any cut: check dangling `\ref`s, notation defined only in removed text, forward references, and promises in intro/abstract.
8. Commented-out text (`%`) is not content. It may be removed in the TARK copy, logged as `fix`.
9. Engine is tectonic (XeTeX). Before submission, cross-check page count with pdflatex (Overleaf or TeX Live): line breaks can differ.

## Workflow
0. ✅ Port to EPTCS, zero content change. Baseline: main text ends p.23 (22.2 pp).
1. ✅ Inputs from authors: direction, structure, DTU rules, core claim (2026-11-09).
2. ✅ Argument map + Option B budget approved (2026-11-09). ✅ Figures regenerated on DTU1+DTU2 (+DIS), `plots/tark_*` via `scripts/make_figures.py`. Next: authors pick the figure set (ARGUMENT_MAP.md), then cut.
3. ◐ Cut section by section. 3.1–3.4 done; 3.5 re-sequence + condense done in 12 iterations (main text ends p.12, ~1.8 pp over). Errata fixed (except 2). Status and options for the last pages: `STATUS.md`.
4. ☐ Retarget for TARK: related work toward epistemic logic / game theory; literature since 2019 (human-verified).
5. ☐ AI disclosure paragraph (from ledger), final consistency pass, pdflatex cross-check, send to co-authors.

## Goal clarification (TSN, 2026-11-09)
Other versions may exist in parallel (co-author drafts, other models). We need **one good cut**, and this branch can be it.

## Literature to check in the later lit pass (an author verifies each)
- Pinker, *When Everyone Knows That Everyone Knows* (book, 2025). It cites our preprint and is directly relevant, since our core claim positions us against Thomas, De Freitas, Pinker et al.
- Halpern & Moses (coordinated attack); Monderer & Samet 1989 (common $p$-belief); experimental studies of the e-mail game.

## Open inputs
- [x] Editorial direction (2026-11-09): **cut the MTurk experiment.** Reasons: length, and common knowledge of the rules can't be assumed on MTurk (anonymous co-player, rules read individually). The paper's evidence must rest on settings where the rules are demonstrably common knowledge.
- [x] DTU1/DTU2 rules (TSN, 2026-11-09): **shown on a common screen and read aloud to the students**, as at DIS. So the rules were common knowledge in all remaining experiments. **The arXiv text doesn't say this for DTU.** The TARK version must state it, sourced from the authors (ledger category `new`, validated by TSN).
- [x] Structure (TSN, 2026-11-09): **Option B**, re-sequenced for a logic audience (see `ARGUMENT_MAP.md`). Keep the overall point (C0) unchanged. Don't fight the venue.
- [x] Core claim (TSN, 2026-11-09). **This is the yardstick for every cut.**
  > Prior work (Thomas, De Freitas, Pinker et al.) shows that people treat common knowledge as a distinct category and act on it, but only when the experiment tells them which knowledge state they are in. In the Canteen Dilemma, and in its card-game twin from the logic literature, the knowledge state has to be deduced, and common knowledge is provably unattainable. Players **behave as if they had common knowledge** already at shallow depths of shared knowledge (around 1–3; the boundary is a step, not a sharp line), in their choices and in their stated certainty, and most claim a safe cut-off exists. Coordination guaranteed by common knowledge is a theorem; that this matters for people outside the lab is a conjecture.
  - **Never strengthen to "cannot distinguish".** It's behaviour, not belief (an author decision, 2026-11-09, consistent with the arXiv version).
  - The data shows a step at the private/shared boundary (8:50 → 8:40), then a plateau. Keep depth language blurry ("shallow", "1–3"), not exact.
- [x] Figures (TSN, 2026-11-09): **main text = Fig 6 (diagram + DTU curve, moved to §2), Fig 1 merged with DIS, Fig 3, Fig 7.** Table 1 and Figs 2, 4 and 5 go to the appendix (see `ARGUMENT_MAP.md`). TSN delegates the figure choice to Claude.
- [x] DIS (TSN, 2026-11-09): table 7 ("Robins table") was played by an author, so it is excluded. DIS = 12 students, n = 180.
- [x] Number change approved (TSN, 2026-11-09): "There is no such time" goes from "less than 4%" to 10.9% on DTU data (DTU1 15.4%, DTU2 2.4%). The other changed claims in `ARGUMENT_MAP.md` (Fig 6 n, the dropped MTurk-vs-DTU test) follow from cutting MTurk.
- Sharing: TSN emails co-authors about progress. `figures_comparison.pdf` (built by `scripts/comparison/build.sh`) shows the arXiv vs TARK figures. Goal: a TARK PDF that everyone can read.
- Private process notes (not in repo): `~/dev/canteen-dilemma/notes/PRIVATE.md` on TSN's machine.
- Prior reviews (Cognitive Science, PLOS ONE) exist in `../../reviewing/` but are **deliberately out of scope**: different audience. Don't use unless asked.

## Next session (handoff, 2026-11-09)
Start with `STATUS.md`. Open: author answers on the "What we need to check" list and on the options for the last ~1.8 pp (none approved yet). After every cut, run `build.sh` and `scripts/check_lost_sentences.py HEAD`; every listed sentence needs a CUTS row. Lesson from step 3.5: check words per section against the plan's budget (≈600 words/page) *before* writing; the first pass stayed too verbatim and needed a second pass.
