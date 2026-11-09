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
2. **Keep the authors' voice.** When condensing, reuse the authors' own sentences and words. No new framing, no AI-flavoured prose ("delve", "crucially", "notably", "underscores", tricolons, em-dash chains).
3. **No new citations** unless a human author verifies the source exists and says what it is claimed to say.
4. **No change to claims, numbers, statistics, or formal results.** Condensing must not strengthen or weaken a claim.
5. **One section per iteration.** Build, check page count, check refs, commit.
6. **Every edit → one `AI_LEDGER.md` row + (if text left main) one `CUTS.md` row.** Same commit.
7. After any cut: check dangling `\ref`s, notation defined only in removed text, forward references, and promises in intro/abstract.
8. Commented-out text (`%`) is not content. It may be removed in the TARK copy, logged as `fix`.
9. Engine is tectonic (XeTeX). Before submission, cross-check page count with pdflatex (Overleaf or TeX Live): line breaks can differ.

## Workflow
0. ✅ Port to EPTCS, zero content change. Baseline: main text ends p.23 (22.2 pp).
1. ☐ Inputs from authors: editorial direction, core claim in 3–5 sentences.
2. ☐ Argument map: claims → sections → dependencies. Page budget per section. **Human approves.**
3. ☐ Cut section by section (several internal iterations before co-authors see it).
4. ☐ Retarget for TARK: related work toward epistemic logic / game theory; literature since 2019 (human-verified).
5. ☐ AI disclosure paragraph (from ledger), final consistency pass, pdflatex cross-check, send to co-authors.

## Open inputs
- [ ] Editorial direction for the cut-down.
- [ ] Core claim, 3–5 sentences.
- Private process notes (not in repo): `~/dev/canteen-dilemma/notes/PRIVATE.md` on TSN's machine.
- Prior reviews (Cognitive Science, PLOS ONE) exist in `../../reviewing/` but are **deliberately out of scope**: different audience. Don't use unless asked.
