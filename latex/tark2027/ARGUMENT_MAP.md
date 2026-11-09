# Argument map: arXiv version → TARK

Draft by Claude, 2026-11-09, from a full read of body, appendix and supplementary (transcripts skimmed). **Not validated by the authors.**

## Current shape (EPTCS build)
| § | Title | Pages | Words (text) | Floats | Footnotes |
|---|---|---|---|---|---|
| — | Title + abstract | 1–1.5 | 212 | | |
| 1 | Introduction | 1–4 | 1704 | | 1 (informal impossibility proof, ~250 w) |
| 2 | The curse of shared knowledge (related work) | 4–7 | 1559 | | 1 |
| 3 | Experimental design | 7–9 | 1542 | | |
| 4 | Game strategies | 9–11 | 1253 | | 1 (proof: no safe cut-off) |
| 5 | Results | 11–17 | 1317 | Table 1, Figs 1–5 | |
| 6 | Discussion | 17–20 | 1600 | Fig 6 (knowledge diagram + logit), Fig 7 (post-game Qs) | |
| 7 | Conclusion | 20–22 | 745 | | |
| | **Main text** | **22.2** | **~9.9k + captions** | **8** | |

10 pages leaves roughly **4.5–5k words of text + 3–4 floats**. About half the text has to leave the main body.

## Claims
| ID | Claim | Evidence / location | Essential for TARK? |
|---|---|---|---|
| C0 | **Thesis.** People act as if they have common knowledge when they only have shallow $n$th-order shared knowledge ("curse of shared knowledge"), in a game where common knowledge is unattainable and acting on it is costly. | Whole paper | — |
| C1 | In the canteen dilemma, arriving at $8{:}50 − 0{:}10n$ gives exactly $n$th-order shared knowledge that both arrived before 9:00, and never common knowledge. Same structure as coordinated attack / e-mail game. | §1 trekking example; §6 ¶2 + Fig 6 | **yes, the core of the logic** |
| C2 | All-office is the only safe strategy (§4 footnote proof). Only all-office or canteen-before-9 can be Pareto optimal, for any payoffs $u_c > u_o > u_m$ (App C Theorem). With our payoffs all-office is optimal (§4, App B). | §4, App B, App C | **yes, theorem statement in main text** |
| C3 | Canteen choices stay robust up to 8:40, are about 50% at 8:50, and switch to office at 9:00 or later. The 50% point is about 8:50 in every experiment. | Table 1, Fig 1, Fig 6 (combined logit), App A.1 | yes |
| C4 | Certainty is high early and drops towards 8:50. | Fig 2 | supporting |
| C5 | Miscoordination is about 50% at 8:40/8:50 and 8:50/9:00. Payoffs are far below the guaranteed \$9.80. | Table 1, Fig 3, §5 ¶1 | yes |
| C6 | No convergence over rounds, even after miscoordination. | Fig 4, App A.1, App F.2 | supporting (one sentence) |
| C7 | The pattern is robust to an abstract framing (DIS cards and stones) and to the rules being common knowledge (rules read aloud in class). | §3 DIS, Fig 5 | supporting (one paragraph) |
| C8 | Post-game: about 75% name a "safe" cut-off between 8:30 and 8:50; under 4% say "no such time"; 89% say there is common knowledge at 8:10. DIS interviews agree. | Fig 7, §6 | **yes, the most direct evidence for C0** |
| C9 | Interpretation: players tell private and shared knowledge apart (8:50 vs 8:40) but not higher shared knowledge from common knowledge. Alternatives considered: cognitive overload; lack of common knowledge of rationality (beauty contest); a mixed 50% strategy. | §6 | yes, condensed |
| C10 | Positioning: prior experiments (Thomas et al., De Freitas et al.) state knowledge levels explicitly, whereas here they must be deduced. Rubinstein's e-mail game is analysed theoretically only, and this is experimental. Bounded rationality usually makes agents conclude *less*; here they conclude *more*. | §2 ¶4–6, §7 | **yes, the "novelty" criterion** |

## Dependencies
- C1 is needed by C0, C2, C9 and C10. It is now introduced twice: the trekking example (§1, about 1.2k words) and the in-game analysis (§6 ¶2 + Fig 6). **One of the two can go.**
- C2 (theorem) is needed to call behaviour suboptimal. The main text gives only the informal argument; the proof can stay in App C.
- §2 ¶1–3 (Theory of Mind / cog-sci background, about 900 words) feeds nothing in C1–C10 except general motivation. It is the cleanest candidate to move or cut for a logic audience.
- §3 holds ethics, recruitment and payoff details that the CFP doesn't need in the main text. All of it already has a home in App A, B and D.

## TARK fit (Claude's read)
- Fig 6 is effectively a Kripke model of the game, and TARK readers will read it that way. It probably deserves to move up to where the game is introduced.
- Comparators TARK reviewers will expect and which the paper doesn't cite: (a) Halpern & Moses on coordinated attack (the paper cites Fagin et al. 1995 instead); (b) Monderer & Samet (1989) on common $p$-belief / "approximate common knowledge". Reviewers may ask whether players' behaviour is rational under common $p$-belief. **Both need verification by an author before they can be cited (rule 3).** Experimental studies of the e-mail game probably exist: Claude doesn't know them reliably, so this needs a human literature check.

## Two options for restructuring (decision for the authors)
**A: Keep the order, trim every section.** Least invasive. The trekking example stays shortened, §2 shrinks to about ⅓, and Figs 2, 4 and 5 go to the appendix.

**B: Re-sequence for a logic audience.** The text is reused as far as possible; mostly blocks are moved:
| New § | Content (sources) | Target pp. |
|---|---|---|
| — | Title, abstract | 0.6 |
| 1 | Introduction: trekking example condensed to one paragraph, questions A/B, contribution (§1, §2 ¶4–6) | 1.4 |
| 2 | The Canteen Dilemma: rules, knowledge structure with Fig 6 diagram, strategies, theorem statement (§3 story, §6 ¶2, §4, App C statement) | 2.0 |
| 3 | Experiments: MTurk, DTU, DIS in brief (§3) | 1.0 |
| 4 | Results: Table 1, Fig 1 (or Fig 6 logit), Fig 3, Fig 7 (§5, §6 post-game) | 2.6 |
| 5 | Discussion: interpretation and alternatives (§6) | 1.4 |
| 6 | Related work and conclusion (§2 ¶4–6 remainder, §7) | 1.0 |
| | **Total** | **10.0** |

Claude's recommendation: **B**. It puts the epistemic-logic content (C1, C2) up front, where TARK reviewers will look first. That uses the venue shift rather than fighting it, and it still removes the most text by moving rather than deleting.
