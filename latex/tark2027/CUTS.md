# Cut Ledger

What left the 10-page main text, why, and where it went. Nothing is lost: the full version remains on arXiv and on `main`.

Destinations: `appendix` (moved to appendix of this submission) · `arxiv` (only in full version; cite arXiv) · `deleted` (redundant / no longer needed) · `condensed` (kept, shorter).

## Page budget
| Section | arXiv baseline (EPTCS pp.) | Target pp. | Current pp. |
|---|---|---|---|
| _to be set in planning step_ | | | |
| **Total main text** | **22.2** | **≤ 10.0** | **ends p.19** (after step 3.1–3.4) |

## Cuts
| # | Section | What (first words / label) | Size | Destination | Why |
|---|---|---|---|---|---|
| 1 | §3 | "For the main experiment, we recruited a total of 680 participants from Amazon Mechanical Turk…" (MTurk recruitment, ethics approval, dates, HIT, consent, waiting room) | 1 ¶, ~8 lines | appendix (same content already in App. `app:mturk-walkthrough`); arxiv once the appendix drops MTurk | MTurk cut (editorial direction) |
| 2 | §3 | "The two DTU classroom experiments differed slightly from the MTurk experiment…" (\$30 vs \$10, 30 vs 10 rounds); "A fixed participation fee of \$2 is given to all MTurk players"; "\$10 (MTurk)" | 3 clauses | arxiv (MTurk details still in App. A, B for now) | MTurk cut; DTU half kept, reworded |
| 3 | §3 DIS ¶ | "Second, when doing experiments on MTurk, the players in principle cannot be guaranteed…"; "By reading up the rules and showing them on the projector in class solves the issue…" | 3 sentences | condensed into the new §3 sentence that the rules were public in all three experiments | the objection no longer applies to any remaining experiment |
| 4 | §5 | "despite doing the experiment with more than 800 people"; "The average bonus paid to our MTurk participants was a mere \$2.36… only 46 out of 340 MTurk pairs…"; "Comparing the MTurk experiment with the DTU experiments…" | 2 ¶ | arxiv (MTurk); DTU numbers condensed into one ¶ | MTurk cut |
| 5 | §5 | Table 1 | float | appendix (App. D, DTU rows only; AMT row → arxiv) | approved float set |
| 6 | §5 | Fig 1 (MTurk+DTU choice curves), its p < .0001 MTurk-vs-DTU claim, "MTurk participants in blue…", pointer to the mixed-effects appendix | float + 2 sentences | replaced by merged Fig 1 (DTU1, DTU2, DIS); p-value deleted (moot, approved); mixed-effects analysis stays in App. A (still MTurk-based) | approved float set |
| 7 | §5 | Fig 2 (certainty violins) and its paragraph ("The violin plots… The subtle differences… MTurk…") | float + 1 ¶ | appendix (App. D, DTU1 vs DTU2); one sentence left in main | approved float set |
| 8 | §5 | Fig 4 (canteen frequency by round) and its paragraph; "MTurk participants do choose the canteen a little less often after a miscoordination…" | float + 1 ¶ | appendix (App. D); MTurk sentence → arxiv; one sentence left in main | approved float set |
| 9 | §5 | Fig 5 (DIS logit) | float | appendix (App. D); absorbed into merged Fig 1 | approved float set |
| 10 | §5 DIS ¶ | "and with a slope that is most similar to the DTU experiments (which makes sense, as here the participants are also students in computer science and AI)" | ½ sentence | deleted | comparison was relative to MTurk |
| 11 | §5 | "The differences between the three experiments are however still relatively minor. In the following we will combine data from all three experiments." | 2 sentences | first kept in App. D (reworded); second deleted | MTurk cut |
| 12 | §4 (step 3.5, it. 1) | "The fact that the all-office strategy is the only safe one is counter-intuitive to most people…" (Agnes/Bertram ¶, incl. "A major point of our experiments is to test whether this kind of recursive perspective-taking is utilized…") | 1 ¶, ~190 w | arxiv | approved 3.5 plan: overlaps the knowledge-structure ¶ now in §2 |
| 13 | §4 ¶1–2 → §2 | "In other words, depending on the arrival time of your colleague… So which one to choose?"; "What if you then instead arrive at 8:40? In this case… However, we just concluded… So," | ~100 w | condensed (bridging sentence `\modified`) | the iterated argument is kept in full |
| 14 | §3 → §2 | "We call the game the `Canteen Dilemma'." | 1 sentence | deleted | the name is now the section title and first sentence |
| 15 | Fig 6 caption (now Fig 1) | worked example "since these are the two arrival times for player 2 that player 1 will consider possible…", "e.g. when arriving at 8:40, there is shared knowledge to depth 1…" | ~4 lines | condensed | approved 3.5 plan (9 → ~6 lines) |
| 16 | §4 last ¶ → §2 | "A strategy to always go to the canteen if arriving before some cut-off… (see Appendix C for more details)" | 1 ¶ | condensed into the theorem ¶ | cut-off strategy now defined right before the restated theorem |
| 17 | §1 trekking ¶3–5 (step 3.5, it. 2) | "The most dangerous situation is if one of them goes to the base…"; "In this situation, we would say that Agnes and Bertram both have private knowledge…", "More generally, a fact is private knowledge…", "Some consider the case where everybody knows a fact to still only be private knowledge…"; the depth-three walk-through ("To have shared knowledge to depth three… A) … B) … Thus we have asymmetry… If he also asks her to confirm…"); "At first it might seem that it is sufficient… Even shared knowledge to depth two is not sufficient." | ~600 w | condensed (definitions of depth one/two, the convention and the pointer to App. `A:definitions` kept in one `\modified` passage; conventions in full in App. `A:definitions`) | approved 3.5 plan |
| 18 | §1 footnote | informal impossibility proof ("To derive a contradiction, suppose $n$th-order shared knowledge for some $n$ is sufficient…") | ~250 w | appendix (new App. `app:trekking-proof`, verbatim, one `\modified` lead-in sentence) | approved 3.5 plan |
| 19 | §1 contribution ¶s | "…corresponding to the situation in the trekking example where one of the trekkers would leave the other at the top…"; "i.e., for sufficiently high levels of shared knowledge… explicitly distinguished the common knowledge situation from the $n$th-order shared knowledge situation" (→ one `\modified` clause); ", hence helping to understand the notion of common knowledge better…" | ~110 w | condensed | approved 3.5 plan |
| 20 | §2 ¶6 (curse of shared knowledge) → §1 | "The electronic mail game and the mountain trekking example are complicated…"; "In this paper, we devise a novel game in which the higher orders of shared knowledge are not achieved dynamically…" (duplicates the §1 game sentence); "Letting humans play our game, we have been able to address the previous questions in more detail."; "So people behave as if having common knowledge, despite…" (duplicates the §1 sentence on B) | ~90 w | deleted (duplicates); the rest of ¶6 and the conjecture/"curse" sentences moved into the §1 contribution ¶ | approved 3.5 plan |
