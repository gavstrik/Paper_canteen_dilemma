# Status of the TARK 2027 cut-down (2026-11-09)

Snapshot for co-authors. The PDF snapshot is `tark2027.pdf`; text changed in the TARK version is shown in red (`\modified{}`).
Details: every edit is in `AI_LEDGER.md`, everything that left the main text is in `CUTS.md`, and the errata are in `ERRATA.md`.

**Where it stands:** the main text ends on **p.12** (about 11.8 pages; the arXiv version ran to 23). The limit is 10 pages excluding references, so **about 1.8 pages still have to go**. Every build passes with no undefined references.

## A. Errata (commit 53e42a9)
Fixed in the TARK copy, each marked `\modified{}` and logged in the ledger:
- **1:** arrival times start at **8:00**, not 8:10 (game-story quote; App. C range), matching the instructions and the data.
- **6:** DIS cards run **2 to 10**, not 2 to 9.
- **9:** App. C, proof of Lemma 3: $s(t+0{:}10)=c$ → $s'(t+0{:}10)=c$.
- **10:** App. C: one added sentence noting that "Pareto dominates" ($EU(s')>EU(s)$) coincides with the standard notion, because the game is common-payoff.
- **11:** typos in the body, appendix and supplementary. The "the the" in a DIS interview transcript is left as it is (verbatim speech).
- **17:** a white stone corresponds to **canteen** (the text said office).

Already fixed in earlier steps: 5 (participant count), 7 (Table 1 caption), 8 ("weighted least squares").
Still open: **2** ("12 pairs, probability 1/6"). An author needs to check the oTree arrival-time generator first.

## B. Re-sequencing and condensing (Option B)
New structure: §1 Introduction → §2 The Canteen Dilemma → §3 Experiments → §4 Results → §5 Discussion → §6 Related work and conclusion.
- **§2** collects the game: the story, outcomes, payoffs, the knowledge structure with the Kripke-style diagram (old Fig 6, now Fig 1), the strategy argument, the footnote proof that no cut-off is safe, and an unnumbered restatement of the App. C theorem (all-office or canteen-before-9 are the only Pareto-optimal candidates).
  - Deviation from the plan: the payoff-tiers paragraph went into §2, not §3, because the strategy argument needs the payoff order.
- **§1**: the trekking example is down to two paragraphs. The informal impossibility proof moved verbatim to a new appendix subsection. There is one contribution paragraph.
- **§3**: participants, the rules shown and read aloud (so the rules were common knowledge in all three experiments), and a five-sentence summary of the DIS rules. The full DIS rules stay in the appendix.
- **§4**: the choice curves, miscoordination, the post-game questions (safe cut-off; common knowledge at 8:10) and the DIS interviews.
- **§5**: interpretation and the alternatives considered (cognitive overload; beauty contest / no common knowledge of rationality; the mixed 50% strategy).
- **§6**: Thomas / De Freitas et al. and Rubinstein, then the conclusion.
- **Cut (as in the approved plan):** the Theory-of-Mind background (old §2 ¶1–3), the "implications for multiple disciplines" paragraph, and the Agnes/Bertram intuition paragraph in the old §4. All of it remains in the arXiv version.
- **Moved to App. B verbatim:** the canteen-before-9 arithmetic and the justification for logarithmic scoring.
- **No claim or number has changed.** The authors' hedges are kept, including that real-life penalties are probably lower, that this is a "plausible conjecture", and "at least not in our game".
- There were two passes: six planned iterations, then a second condensing pass over every section, because the first pass stayed too close to verbatim.

## What we need to check
1. **Every red passage.** These are condensed or rewritten sentences. Do they keep the authors' voice and the original meaning?
2. **The conclusion still says, as the arXiv version does:** "our findings suggest that they cannot distinguish the two … at least not in our game". This is stronger than the core claim ("behave as if", not "cannot distinguish"). Keep it or soften it?
3. **The restated theorem in §2**, including the phrase "disregarding certainty estimates", checked against App. C.
4. **Erratum 2:** the 1/6 and the 12 pairs, once the oTree generator has been checked.
5. **The appendix is still MTurk-heavy** (App. A, App. B, the walkthrough). App. B now has the moved DTU paragraph sitting under the old MTurk bonus text. This will be fixed when MTurk comes out of the appendix (a step already planned for later).

## Options for the last ~1.8 pages
None of these is in the approved plan, so each one needs approval. All of them move material rather than delete it.

| Option | Saves (approx.) |
|---|---|
| Figs 2 and 3 side by side in one float | ~0.35 pp |
| Move the no-cut-off footnote proof to App. C (the CFP allows proofs in the appendix) | ~0.3 pp |
| Move the mixed-strategy argument (§5) to the appendix, keeping one sentence | ~0.25 pp |
| Move the DIS interview details to the appendix, keeping one sentence plus "the rules were common knowledge" | ~0.2 pp |
| Shorten the abstract and the acknowledgments | ~0.2 pp |
| Narrow Figs 6 and 7 slightly | ~0.15 pp |

All six together come to about 1.5 pages. The remaining few tenths would need either one more condensing pass or a further move: for example, the DIS paragraph in §4 could shrink to its numbers, or Rubinstein could be reduced to two sentences.
