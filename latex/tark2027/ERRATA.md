# Errata found in the arXiv (Oct 2025) version

Found while reading for the TARK cut-down, 2026-11-09, and checked against `Data/*.csv` and `images/screenshot_instructions.png`.
**None of these are fixed yet.** Corrections to numbers or claims need an author's sign-off (PROJECT.md rule 4).

Severity: **A** = factual error in a number or claim · **B** = internal inconsistency · **C** = typo or cosmetic.

| # | Sev | Where | Issue | Evidence | Proposed fix | Status |
|---|---|---|---|---|---|---|
| 1 | A | body §3 game story; §4; App C ("$8{:}10 \leq t_i \leq 9{:}10$") | The paper says arrival times run **8:10–9:10**. Participants were told **8:00–9:10**, and the data has 8 arrival times, 8:00 to 9:10. The appendix (A) and the Fig. 3 caption do say 8:00. | Instructions screenshot: "between 8:00 am and 9:10 am". `arrival` values in all three CSVs: {8.0, 8.1, …, 8.5, 9.0, 9.1}. | Change the quote to 8:00. In App C, use $8{:}00 \leq t_i$. | open |
| 2 | A | body §4 (canteen-before-9 paragraph) | Follows from #1. "There are 12 pairs of arrival times… probability of miscoordination is 1/6" should be **14 pairs, 1/7**. Expected single-round payoff of canteen-before-9 should be $10 − (2·9.21 + 2·0.02 + 10·0.01)/14 ≈ \$8.67$, not \$8.46. The current formula also leaves out the two 9:00/9:10 office pairs. **Conclusion unchanged**: all-office (\$9.98) is still far better. | Computed from the payoffs in App B. | Recompute in text. | open |
| 3 | A? | body §5 ("only 46 out of 340 MTurk pairs (14%) were able to play 10 rounds and still have any bonus left") | **Cannot reproduce.** From `MTurk_anonymous.csv`: 92 pairs reached round 10. In 73 of them both players had bonus left, and in 85 at least one did. No natural definition gives 46. | Script output in session log 2026-11-09. | Ask whoever ran the original analysis (Robin, TSN) which definition was used. | open |
| 4 | B | App A and App D.3 ("average payout… \$4.17") vs Table A1 (\$4.36) | Mean final bonus over the 680 analysed players is \$2.36 (reproduced), so payout = \$4.36. \$4.17 may be the average over all 714 paid workers, including the excluded colleagues of quitters. | Data reproduces \$2.36. | Clarify or unify. | open |
| 5 | B | Abstract ("three separate experiments involving 802 participants") vs §3 | There are four experiments: MTurk 680, DTU1 80, DTU2 42, DIS 12 (814 in total). 802 leaves out DIS. | §3 text. | Name the four experiments, or explain 802. | open |
| 6 | B | §5 DIS paragraph ("cards with numbers from 2 to 9") | The rules (§3, App D.4) say 2–10. | §3 quote. | "2 to 10". | open |
| 7 | B | Table 1 | `\caption{}` is empty. The legend describes columns (pairs, R, $\bar r$, $\bar s$) that don't match the headers. "AMT" in the table vs "MTurk" everywhere else. | — | Proper caption, consistent labels. | open |
| 8 | C | Fig. 4 caption | "weighted linear squares" → "weighted least squares". | — | — | open |
| 9 | C | App C, Lemma 3 proof | "like $s$ except $s(t+0{:}10) = c$" → $s'(t+0{:}10) = c$. | — | — | open |
| 10 | C | App C | "Pareto dominates" is defined as $EU(s') > EU(s)$. That's fine in a common-payoff game but nonstandard terminology, and TARK reviewers may object. | — | Consider "strictly better" or note the common-payoff equivalence. | open |
| 11 | C | various | Typos: whey, stil, loosing (×2), Betram, specfications, warrents, knowlege, getter, correponds, coffeee, "the the" (×2), "between between", miscoodination (×2), participantion, "theses questions". | — | Fix during cut. | open |

Verified correct against data: all Table 1 values (N, n, average rounds, Ruin %, payoff %, average penalty) for MTurk, DTU1 and DTU2. Payoff arithmetic: \$9.80 all-office over 10 rounds; \$9.90; \$9.21 maximum penalty; ratio 921.
