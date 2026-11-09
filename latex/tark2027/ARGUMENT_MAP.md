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

## Update 2026-11-09: direction set, MTurk is cut
Reason: length, and common knowledge of the rules can't be assumed on MTurk. Evidence must come from settings where the rules are common knowledge.

**Does the effect survive without MTurk?** Recomputed from `Data/DTU{1,2}_anonymous.csv` (choice 1 = canteen; post-game `cutoff` 7.0 = "There is no such time"; `simple` 1.0 = "Yes, common knowledge"):

| | MTurk | DTU1+2 |
|---|---|---|
| Canteen at 8:00–8:30 | ~92% | ~99% |
| Canteen at 8:40 / 8:50 | 90% / 47% | 89% / 50% |
| Canteen at ≥ 9:00 (forbidden) | 15% | ~3% |
| Miscoordination, early pairs (8:00–8:30) | 10–15% | 1–2% |
| Miscoordination, 8:40/8:50 and 8:50/9:00 | 50% / 45% | 41% / 46% |
| Post-game: safe cut-off 8:30–8:50 | 76% | 73% |
| Post-game: "There is no such time" | 2.4% | 10.9% (DTU1 15.4%, DTU2 2.4%) |
| Post-game: common knowledge at 8:10 = yes | 89% | 87% |

Reading: the effect survives and is **cleaner** without MTurk. MTurk carries noise (forbidden choices, early miscoordination) that is consistent with the rules not being common knowledge. In DTU the miscoordination sits only at the critical pairs. DTU1 students (AI and Multi-Agent Systems course) answer "no such time" more often, possibly from prior exposure, which is worth stating.

**Consequences for the cut:**
- §3: the MTurk design, recruitment, ethics and payout paragraphs leave the main text. The logarithmic scoring rule (payoffs) stays because it applies to DTU too.
- Table 1, Figs 1–4 and 6 (logit) and Fig 7 have to be **regenerated from DTU data only** (the analysis code is in `python/`). Fig 5 (DIS) is unchanged.
- The argument that the rules are common knowledge (C7) becomes central. DIS is documented (projector, read aloud). **DTU presentation is unknown; ask the authors.**
- The abstract's participant counts change: DTU1 80 + DTU2 42 + DIS 12 = 134.
- Errata #3 (46 pairs) and #4 (MTurk payout) become moot.

## Decision 2026-11-09
- **Option B approved** (TSN). The overall point C0 stays.
- DTU rules were shown on a common screen and read aloud (TSN), so C7 (rules are common knowledge) now holds for **every** remaining experiment. That answers the objection that led to cutting MTurk, and it should be stated explicitly in the new §3.

## Update 2026-11-09: figures regenerated on DTU1+DTU2 (+ DIS)
Script: `scripts/make_figures.py`, a port of the notebooks that made the published figures. `--reproduce` runs the ports on the original MTurk+DTU selection and matches every stored notebook output and every paper number (Table 1, Fig 3 counts, Fig 4 tables, post-game %). Outputs: `plots/tark_*` (originals untouched). All numbers: `plots/tark_stats.txt`.

### Float sizes in EPTCS (image height at the given width; text page = 623 pt ≈ 46 lines)
| Float | Content | Claim | Width | Image | + caption ≈ | Share of a page |
|---|---|---|---|---|---|---|
| Table 1 | 2 rows (DTU1, DTU2) | C5 | — | ~80 pt | ~40 pt | 0.2 |
| Fig 1 | choice curves DTU1, DTU2 | C3 | 0.6 | 179 pt | 40 pt | 0.37 |
| Fig 1 + DIS (variant) | the same plus DIS on a shared axis (card c ↦ 9:00 + 0:10(c−9)) | C3, C7 | 0.6 | 179 pt | 55 pt | 0.40 |
| Fig 2 | certainty violins, DTU1 vs DTU2 | C4 | 0.8 | 208 pt | 80 pt | 0.46 |
| Fig 3 | coordination by arrival pair | C5 | 0.6 | 161 pt | 55 pt | 0.37 |
| Fig 4 | canteen frequency by round | C6 | 0.8 | 225 pt | 55 pt | 0.46 |
| Fig 5 | DIS logit | C7 | 0.6 | 179 pt | 40 pt | 0.35 |
| Fig 6 | knowledge diagram + DTU logit | C1, C3 | 1.0 | ~200 pt | 55 pt (caption condensed from 9 lines to ~4) | 0.42 |
| Fig 7 | post-game answers | C8 | 0.8 | 180 pt | 55 pt | 0.38 |

### Proposal: 4 floats, about 1.6 pp (approved by TSN, 2026-11-09)
1. **Fig 6 (diagram + logit) moves up to new §2.** It is the Kripke model of the game (C1) and carries the pooled choice curve (C3) on the same picture. This is the TARK figure.
2. **Fig 1 + DIS (merged) in §4.** One float replaces Figs 1 and 5. It shows both DTU classes and the card version on one axis, which is the robustness claim C7 in a single image. Caveat: DIS has a different payoff (lose everything), and card 2 maps to 7:50, outside the canteen range. The caption must say so.
3. **Fig 3 in §4.** The miscoordination at the critical pairs (C5) is the cost of the curse, and it isn't visible anywhere else.
4. **Fig 7 in §4.** The most direct evidence for C0 (C8).
- **To the appendix:** Table 1 (one sentence on payoffs and ruin rates in the text), Fig 2 (one sentence: median "very certain" up to 8:30, "somewhat certain" at 8:50), Fig 4 (one sentence: WLS slopes |b| ≤ 0.002 per round at 8:40/8:50/9:00, no convergence), Fig 5 (absorbed into the merged Fig 1).
- **Cheaper fallback:** drop Fig 1 too (the Fig 6 inset already shows the curve) and put Figs 3 and 7 side by side, which leaves ~1.1 pp. Not recommended: DIS would then have no figure.

### Text claims the DTU-only data changes (fix during the cut; numbers need an author's sign-off, rule 4)
| Where | arXiv text | DTU1+DTU2 | Status |
|---|---|---|---|
| §6, post-game | "there is no such time" chosen by "less than 4%" | **10.9%** (DTU1 15.4%, DTU2 2.4%) | **changes.** The claim still holds (a small minority), but the number triples. |
| §6, post-game | 8:30–8:50 "approximately 75%" | 73.1% | still holds |
| §6, CK question | "yes" 89% | 88.0% | still holds |
| §5, Fig 1 caption | MTurk vs DTU slope/intercept differ, $p<.0001$ | moot. DTU1 vs DTU2: neither the intercept nor the slope difference is significant on its own (p = .78, .28); the joint LR test p < .001 ignores pair clustering | drop the claim |
| §5 | 50% point "close to 8:50 in all experiments" | DTU1 8:48, DTU2 8:52, DIS card 7.5 (≈ 8:45) | still holds |
| §5, Fig 3 | canteen > 86% if both arrive before 8:50; miscoordination ≈ 50% at 8:40/8:50 and 8:50/9:00 | ≥ 91.0%; 41.1% / 45.8% | still holds |
| §5, Fig 4 | 8:40 around 90%, 8:50 around 50%, no change over rounds | WLS 0.90→0.89 and 0.49→0.51 over 30 rounds | still holds |
| §5, Fig 2 | ≤ 8:30 very high confidence; lower at 8:50 | median 0.99 up to 8:30, 0.75 at 8:50 | still holds |
| §5, Fig 2 | DTU1 steepest profile, "most aware of the danger" | DTU1 mean certainty 0.73 at 8:50 vs DTU2 0.79; canteen at 8:50 is 43% vs 64% | still holds (DTU1 vs DTU2 only) |
| Fig 6 caption | n = 7432, all three experiments | n = 3172, DTU1+DTU2 (and see ERRATA 12) | caption changes |
| §5, MTurk paragraphs and Table 1 AMT row | — | — | leave with MTurk |

## Step 3 status (2026-11-09, end of session)
Done: MTurk out of main text (abstract, §3, §4 payoffs restated for DTU, §5, §6); approved floats in place (merged Fig 1, Fig 3, Fig 6 with DTU inset, Fig 7); Table 1 and Figs 2, 4, 5 in new App. D. Main text ends **p.19** (from 23). Fig 6 is still in §6; it moves to the new §2 during re-sequencing.

### Step 3.5 plan: re-sequence and condense (Option B), needs about −9 pp (≈ 4k words)
| New § | Source | Action | Claim touched |
|---|---|---|---|
| 1 Intro | §1 ¶1–2 | keep | — |
| | §1 trekking ¶3–5 (setup, depth conventions, message-by-message depths) | condense to one ¶; the depth-convention text already lives in App. `A:definitions` | **C1** (informal intro) |
| | §1 footnote (informal impossibility proof, ~250 w) | move to appendix | **C1** |
| | §1 questions A/B ¶ | keep | C0 |
| | §1 ¶ "We have designed a coordination game…" + "Humans generally find…" + §2 ¶6 last part | condense to one contribution ¶ | C0, C10 |
| 2 Canteen Dilemma | §3 game story quote + outcomes ¶ | move here | — |
| | §6 ¶1–2 (knowledge structure) + Fig 6 | move here; condense the Fig 6 caption from 9 to about 4 lines | **C1** |
| | §4 ¶1–3 (strategies, all-office only safe, no-cut-off footnote proof) | move here; condense ¶1–2; keep the footnote proof | **C2** |
| | §4 ¶4 ("counter-intuitive… Agnes/Bertram") | cut → arxiv (overlaps the knowledge-structure ¶) | C2 (intuition only) |
| | §4 ¶5–6 (canteen-before-9 arithmetic, theorem pointer) | condense; state Theorem (App. C) in the main text | **C2** |
| 3 Experiments | §3 overview, payoffs ¶, DIS ¶ | condense; DIS rules quote → 2-sentence summary + App. `app:dis-rules-full` | C7 |
| 4 Results | current §5 + post-game part of §6 (Fig 7, both questions, DIS interviews) | move together; light condense | C3–C8 |
| 5 Discussion | §6 ¶3–5 (private vs shared; overload; beauty contest / mixed strategy) and the ¶ "Participants might of course not…" | condense | **C9** |
| 6 Related work & conclusion | §2 ¶4–6 (Thomas, De Freitas; Rubinstein) + §7 | condense into ~1 pp | **C10** |
| — | §2 ¶1–3 (ToM / cog-sci background, ~900 w) | cut → arxiv | none (motivation only) |
| — | §7 "implications for multiple disciplines" ¶ | cut → arxiv | none |

### Open items for authors (not blocking 3.5)
- Errata needing sign-off before the text is fixed: 1 (8:10 → 8:00), 2 (12 pairs, 1/6: check the oTree generator), 6 (cards 2–9 → 2–10), 17 (white ↔ office slip).
- The appendix is still MTurk-heavy: App. A (design, \$4.17 payout, mixed-effects regression fitted on MTurk+DTU), App. B (\$2 fee, \$10 bonus), supplementary walkthrough titled MTurk, Table A1. Proposal: strip MTurk from the appendix (→ arxiv), retitle the walkthrough as the oTree interface used at DTU, and drop or refit the mixed-effects analysis on DTU only.
- Decision (TSN, 2026-11-09): strip MTurk from the appendix **later**, not now.
