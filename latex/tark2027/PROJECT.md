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
2. ✅ Argument map + Option B budget approved (2026-11-09). Next: regenerate figures on DTU+DIS data, then re-check the budget.
3. ☐ Cut section by section (several internal iterations before co-authors see it).
4. ☐ Retarget for TARK: related work toward epistemic logic / game theory; literature since 2019 (human-verified).
5. ☐ AI disclosure paragraph (from ledger), final consistency pass, pdflatex cross-check, send to co-authors.

## Open inputs
- [x] Editorial direction (2026-11-09): **cut the MTurk experiment.** Reasons: length, and common knowledge of the rules can't be assumed on MTurk (anonymous co-player, rules read individually). The paper's evidence must rest on settings where the rules are demonstrably common knowledge.
- [x] DTU1/DTU2 rules (TSN, 2026-11-09): **shown on a common screen and read aloud to the students**, as at DIS. So the rules were common knowledge in all remaining experiments. **The arXiv text doesn't say this for DTU.** The TARK version must state it, sourced from the authors (ledger category `new`, validated by TSN).
- [x] Structure (TSN, 2026-11-09): **Option B**, re-sequenced for a logic audience (see `ARGUMENT_MAP.md`). Keep the overall point (C0) unchanged. Don't fight the venue.
- [x] Core claim (TSN, 2026-11-09). **This is the yardstick for every cut.**
  > Prior work (Thomas, De Freitas, Pinker et al.) shows that people treat common knowledge as a distinct category and act on it, but only when the experiment tells them which knowledge state they are in. In the Canteen Dilemma, and in its card-game twin from the logic literature, the knowledge state has to be deduced, and common knowledge is provably unattainable. Players **behave as if they had common knowledge** already at shallow depths of shared knowledge (around 1–3; the boundary is a step, not a sharp line), in their choices and in their stated certainty, and most claim a safe cut-off exists. Coordination guaranteed by common knowledge is a theorem; that this matters for people outside the lab is a conjecture.
  - **Never strengthen to "cannot distinguish".** It's behaviour, not belief (an author decision, 2026-11-09, consistent with the arXiv version).
  - The data shows a step at the private/shared boundary (8:50 → 8:40), then a plateau. Keep depth language blurry ("shallow", "1–3"), not exact.
- Private process notes (not in repo): `~/dev/canteen-dilemma/notes/PRIVATE.md` on TSN's machine.
- Prior reviews (Cognitive Science, PLOS ONE) exist in `../../reviewing/` but are **deliberately out of scope**: different audience. Don't use unless asked.
