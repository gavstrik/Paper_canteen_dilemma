"""Regenerate Table 1 and the main-text figures for the TARK 2027 version.

Data: DTU1 + DTU2 only (MTurk is cut from the TARK version), plus DIS where relevant.
Each function is a port of the notebook that made the published figure; the source is
named in the docstring. Deviations from the original code are marked `DEVIATION:`.

Usage (from latex/tark2027/):
    python scripts/make_figures.py              # write TARK figures to plots/tark_*
    python scripts/make_figures.py --reproduce  # run the ports on the ORIGINAL data
                                                # selection (MTurk+DTU1+DTU2) and check
                                                # them against the published numbers;
                                                # writes nothing to plots/

Originals in plots/ are never overwritten: every output file starts with `tark_`.
"""
import argparse
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

HERE = os.path.dirname(os.path.abspath(__file__))
TARK = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(TARK))
DATA = os.path.join(REPO, "Data")
OUT = os.path.join(TARK, "plots")

SEED = 1          # DEVIATION: originals set no seed for seaborn's bootstrap
N_BOOT = 10000    # as in the originals ("Set n_boot to 10000 for the final plot")
COL = {"DTU1": "#ff7f00", "DTU2": "#4daf4a", "MTurk": "#377eb8", "DIS": "#984ea3"}
TIMES = ["8:00", "8:10", "8:20", "8:30", "8:40", "8:50", "9:00", "9:10"]

sns.set_style("white")
sns.set_context("notebook")
plt.rcParams["font.family"] = "sans-serif"


# ----------------------------------------------------------------------------- data
def load(exps):
    """Raw per-choice data. CSV and XLSX copies were checked identical (AI_LEDGER #15)."""
    frames = []
    for e in exps:
        d = pd.read_csv(os.path.join(DATA, f"{e}_anonymous.csv"), index_col=0)
        d["exp"] = e
        frames.append(d)
    return pd.concat(frames, ignore_index=True)


def load_dis(drop_table7=False):
    """DIS long-format block (table, r, player, card, choice; choice 1 = white).
    Table 7 is the one marked "Robins table" in python/DIS_data_overview.ipynb."""
    d = pd.read_excel(os.path.join(DATA, "DIS.xlsx"))[["table", "r", "player", "card", "choice"]]
    if drop_table7:
        d = d[d.table != 7]
    return d.reset_index(drop=True)


def minutes(arrival):
    """python/fig1.ipynb: 9.0 -> 8.6, 9.1 -> 8.7, then minutes after 8:00 (0..70)."""
    return (arrival.replace({9.0: 8.6, 9.1: 8.7}) - 8) * 100


def save(fig_or_none, name, outdir, **kw):
    for ext in ("pdf", "png"):
        plt.savefig(os.path.join(outdir, f"{name}.{ext}"), dpi=300, transparent=True, **kw)
    plt.close("all")


# --------------------------------------------------------------------------- Table 1
def table1(df, exps, max_rounds):
    """Port of python/table.ipynb (Robin Engelhardt). Returns a DataFrame."""
    rows = []
    for e in exps:
        x = df[df.exp == e]
        players = x.code.unique()
        pay = [x[x.code == p]["payoff"].unique().item() for p in players]
        rows.append({
            "Treatment": e,
            "N": len(players),
            "MaxRounds": max_rounds[e],
            "avg. rounds": round(len(x) / len(players), 2),
            "n": len(x),
            "Ruin": round(100 * sum(1 for p in pay if p == 0) / len(players), 2),
            "payoff": round(100 * np.mean(pay) / max_rounds[e], 2),
            "Avg penalty": round(x.bonus.mean(), 2),
        })
    return pd.DataFrame(rows)


def table1_tex(t):
    """Same tabular layout as body.tex (Table 1), rows only changed."""
    lines = [r"\begin{tabular}{l|ccccccc}", r"\hline",
             r"\small Treatment   & \small   N &   \small MaxRounds &  \small  avg. rounds &  "
             r"\small  n &  \small Ruin & \small   payoff & \small   Avg penalty \\", r"\hline"]
    for _, r in t.iterrows():
        lines.append(f"\\small {r.Treatment:<8} & {r.N:>3} & {r.MaxRounds:>3} & {r['avg. rounds']:>5g} & "
                     f"{r.n:>4} & {r.Ruin:>5.2f} & {r.payoff:>5.2f} & {r['Avg penalty']:>5.2f} \\\\")
    lines += [r"\hline", r"\end{tabular}"]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- Fig 1
def fig1(df, exps, name, outdir, dis=None):
    """Port of python/fig1.ipynb (published fig1.png): logistic regression per experiment,
    bootstrapped 95% CI bands, dots = mean choice per arrival time with bootstrapped CI.
    If `dis` is given (variant only), DIS is overlaid with card c mapped to
    9:00 + 0:10 (c - 9), i.e. card 2 -> 7:50 (x = -10)."""
    d = df[df.exp.isin(exps)][["arrival", "choice", "exp"]].copy()
    d["arrival"] = minutes(d["arrival"])
    labels = {e: f"{e}  (n={int((d.exp == e).sum())})" for e in exps}
    if dis is not None:
        # card 8 -> 8:50 = 50; card 9 -> 9:00 = 60; card 10 -> 9:10 = 70; card 2 -> 7:50 = -10
        x = pd.DataFrame({"arrival": 50 + (dis.card - 8) * 10.0, "choice": dis.choice, "exp": "DIS"})
        d = pd.concat([d, x], ignore_index=True)
        labels["DIS"] = f"DIS, white stone (n={len(dis)})"
    order = list(labels)
    g = sns.lmplot(x="arrival", y="choice", hue="exp", hue_order=order, data=d,
                   palette={k: COL[k] for k in order}, logistic=True, ci=95, n_boot=N_BOOT,
                   x_estimator=np.mean, x_ci="ci", y_jitter=.2, legend=False, height=4,
                   aspect=1.5, seed=SEED)
    lo = -12 if dis is not None else -2
    g.set(xlim=(lo, 72))
    g.set(ylabel="frequency of canteen choice" if dis is None else "frequency of canteen / white",
          xlabel="arrival" if dis is None else "arrival (DIS card)")
    xt = ([-10] if dis is not None else []) + [0, 10, 20, 30, 40, 50, 60, 70]
    g.set(xticks=xt, yticks=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
    g.set(xticklabels=(["7:50\n(2)"] if dis is not None else []) +
          (TIMES if dis is None else [f"{t}\n({c})" for t, c in zip(TIMES, range(3, 11))]))
    # DEVIATION: legend patches use the plotted colours (original used named
    # 'blue'/'orange'/'green', slightly different from the '#377eb8'-style palette).
    plt.legend(handles=[patch.Patch(color=COL[k], label=labels[k]) for k in order], loc="lower left")
    plt.grid()
    plt.tight_layout()
    save(None, name, outdir, bbox_inches="tight")


# --------------------------------------------------------------------------- Fig 2
def fig2(df, split, name, outdir):
    """Port of software/python/fig2_certainties.ipynb: split violins of certainty by arrival.
    Original split MTurk (blue) vs DTU1+DTU2 (orange). `split` maps exp -> hue label."""
    d = df[df.exp.isin(split)][["arrival", "certainty", "exp"]].copy()
    d["hue"] = d.exp.map(split)
    hues = list(dict.fromkeys(split.values()))
    fig, ax = plt.subplots(figsize=(7, 4))
    # DEVIATION: seaborn 0.13 draws the inner box of split violins unsplit and overlapping;
    # we draw no inner box and mark each half's median with a white dot (the original
    # caption: "The white dots correspond to the median certainty estimate").
    ax = sns.violinplot(x="arrival", y="certainty", hue="hue", hue_order=hues,
                        palette=[COL.get(h, h) for h in hues], split=True, inner=None,
                        density_norm="area", data=d, ax=ax)
    med = d.groupby(["arrival", "hue"]).certainty.median()
    for i, a in enumerate(sorted(d.arrival.unique())):
        for j, h in enumerate(hues):
            ax.scatter(i + (-0.08 if j == 0 else 0.08), med[(a, h)], color="white",
                       edgecolor="k", linewidth=.6, s=22, zorder=3)
    ax.yaxis.tick_right()
    plt.ylabel("certainty of coordination", fontsize=18)
    plt.xlabel("arrival", fontsize=18)
    ax.set_xticks(range(8))
    ax.set_xticklabels(TIMES, fontsize=14)
    plt.yticks([.5, .625, .75, .875, .99], ["'very uncertain'", "'slightly certain'",
               "'somewhat certain'", "'quite certain'", "'very certain'"], fontsize=16)
    # DEVIATION: original removed the legend (colours explained in the caption only).
    # With DTU1/DTU2 split we keep a small legend so the figure stands alone.
    ax.legend(title=None, fontsize=11, loc="lower left")
    plt.tight_layout()
    save(None, name, outdir)


# --------------------------------------------------------------------------- Fig 3
PAIRS = ["8:00/8:10", "8:10/8:20", "8:20/8:30", "8:30/8:40", "8:40/8:50", "8:50/9:00", "9:00/9:10"]


def coord_counts(df, exps):
    """software/python/fig3_miscoordinations.ipynb cells 3 and 5: pair mean of arrival and
    choice; choice mean 0 = office, 0.5 = miscoordination, 1 = canteen."""
    d = df[df.exp.isin(exps)]
    p = d.groupby(["exp", "session", "group", "round"], as_index=False)[["arrival", "choice"]].mean()
    office, mis, canteen = [], [], []
    for a in sorted(p.arrival.unique()):
        c = p[p.arrival == a].choice.values
        office.append(int((c == 0.).sum())); mis.append(int((c == 0.5).sum())); canteen.append(int((c == 1.).sum()))
    assert len(office) == 7, "expected 7 consecutive arrival pairs"
    return office, mis, canteen


def fig3(df, exps, name, outdir):
    """Port of software/python/fig3_miscoordinations.ipynb (stacked % bars)."""
    office, mis, canteen = coord_counts(df, exps)
    plt.figure(figsize=(10, 6))
    x = np.arange(7)
    y1, y2, y3 = np.array(office), np.array(mis), np.array(canteen)
    snum = y1 + y2 + y3
    y1, y2, y3 = y1 / snum * 100., y2 / snum * 100., y3 / snum * 100.
    plt.bar(x, y3, bottom=y1 + y2, color="#2d7f5e", edgecolor="white", width=.85, label="canteen")
    plt.bar(x, y2, bottom=y1, color="#de2d26", edgecolor="white", width=.85, label="miscoordination")
    plt.bar(x, y1, color="#6a51a3", edgecolor="white", width=.85, label="office")
    # DEVIATION: segments below 3% are not labelled (labels overlapped; values are in tark_stats.txt).
    for xs, ys, vs in [(x, y1 / 2, y1), (x, y1 + y2 / 2, y2), (x, y1 + y2 + y3 / 2, y3)]:
        for xpos, ypos, yval in zip(xs, ys, vs):
            if yval >= 3:
                plt.text(xpos, ypos, "%.1f" % yval, ha="center", va="center", fontsize=12)
    for xpos, ypos, yval in zip(x, y1 + y2 + y3, snum):
        plt.text(xpos, ypos, "N=%d" % yval, ha="center", va="bottom", fontsize=12)
    plt.ylim(0, 110)
    plt.legend(bbox_to_anchor=(1.01, 0.5), loc="center left", fontsize=12)
    plt.xticks(x, PAIRS, fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.xlabel("arrival time", fontsize=14)
    plt.ylabel("percentage", fontsize=14)
    plt.tight_layout()
    save(None, name, outdir, bbox_inches="tight", pad_inches=0.02)
    return office, mis, canteen


# --------------------------------------------------------------------------- Fig 4
def timeseries(df, exps):
    d = df[df.exp.isin(exps)][["round", "arrival", "choice"]]
    tot = d.groupby(["arrival", "round"])["choice"].size().unstack(level=0).fillna(0)
    can = d[d.choice == 1].groupby(["arrival", "round"]).size().unstack(level=0)
    can = can.reindex(index=tot.index, columns=tot.columns).fillna(0)
    return tot, can / tot


def wls(freq, tot, a):
    """np.polyfit(round, freq, 1, w=sqrt(n)) as in python/fig4.ipynb.
    DEVIATION: rounds with no observation at this arrival time (n = 0, freq NaN) are dropped;
    with 30-round DTU data some late rounds are empty, which would make polyfit fail."""
    ok = tot[a].values > 0
    r = freq.index.values.astype(float)[ok]
    return r, np.polyfit(r, freq[a].values[ok], 1, w=np.sqrt(tot[a].values[ok]))


def fig4(df, exps, name, outdir):
    """Port of python/fig4.ipynb (published fig4.png)."""
    tot, freq = timeseries(df, exps)
    colors = ["#377eb8", "#ff7f00", "#4daf4a", "#f781bf", "#a65628", "#984ea3", "#999999", "#e41a1c"]
    arr = [8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 9.0, 9.1]
    fig, ax = plt.subplots(figsize=(8, 5))
    rounds = freq.index.values.astype(float)
    # DEVIATION: original plotted dots at x = 0..R-1 and the WLS lines at x+1 = 1..R,
    # i.e. dots one round to the left of their lines. Here both use the actual round number.
    for a, c, t in zip(arr, colors, TIMES):
        ax.scatter(rounds, freq[a], s=tot[a].values, marker="o", color=c, label=t)
    fits = {}
    for a in (8.5, 8.4, 9.0):
        r, coef = wls(freq, tot, a)
        fits[a] = coef
        ax.plot(rounds, np.poly1d(coef)(rounds), color=colors[arr.index(a)])
    plt.ylabel("frequency of canteen choice", fontsize=18)
    plt.xlabel("round", fontsize=18)
    plt.xticks(fontsize=16); plt.yticks(fontsize=16)
    handles, _ = ax.get_legend_handles_labels()
    lgd = ax.legend(handles, TIMES, title="arrival time", prop={"size": 14}, bbox_to_anchor=(1, 1))
    plt.grid()
    plt.tight_layout()
    save(None, name, outdir, bbox_extra_artists=(lgd,), bbox_inches="tight")
    return tot, freq, fits


# --------------------------------------------------------------------------- Fig 5 (DIS)
def fig5_dis(dis, name, outdir):
    """Port of python/fig5_DIS.ipynb (published fig5_DIS.png)."""
    g = sns.lmplot(x="card", y="choice", data=dis, logistic=True, ci=95, n_boot=N_BOOT,
                   x_estimator=np.mean, x_ci="ci", y_jitter=.2, legend=False, height=4,
                   aspect=1.5, seed=SEED, line_kws={"color": "#377eb8"}, scatter_kws={"color": "#377eb8"})
    g.set(xlim=(2, 11))
    g.set(ylabel="frequency of white")
    g.set(xticks=[2, 3, 4, 5, 6, 7, 8, 9, 10], yticks=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
    plt.legend(handles=[patch.Patch(color="#377eb8", label=f"DIS (n={len(dis)})")], loc="lower left")
    plt.grid()
    plt.tight_layout()
    save(None, name, outdir, bbox_inches="tight")


# --------------------------------------------------------------------------- Fig 6 inset
def fig6_inset(df, exps, name, outdir):
    """Port of software/python/fig5_logit_all.ipynb: the logistic curve placed inside the
    knowledge diagram (body.tex, fig:indistinguish). Same size, limits and savefig call,
    so it drops into the TikZ picture at the same position.
    NOTE: the original concatenated all three files into `df_all` but then fitted `df`,
    which at that point held only the last file read (DTU2). See ERRATA."""
    d = df[df.exp.isin(exps)][["arrival", "choice"]].copy()
    d["arrival"] = d["arrival"].replace({9.0: 8.6, 9.1: 8.7})
    fig, ax = plt.subplots()
    fig.set_size_inches(6.7, 1.2)
    r = sns.regplot(x="arrival", y="choice", data=d, scatter_kws={"color": "white"},
                    ci=95, n_boot=N_BOOT, logistic=True, ax=ax, seed=SEED)
    plt.setp(r.collections[1], alpha=1)
    r.set(xlim=(8.2, 8.7))
    r.axis("off")
    for ext in ("pdf", "png"):   # original: pdf without bbox_inches (that is the one used)
        kw = {"bbox_inches": "tight"} if ext == "png" else {}
        plt.savefig(os.path.join(outdir, f"{name}.{ext}"), transparent=True, dpi=300, **kw)
    plt.close("all")
    return len(d)


# --------------------------------------------------------------------------- Fig 7
CUTOFF = {6.0: "I don't know", 7.0: "There is no\nsuch time", 8.0: "8:00", 8.1: "8:10",
          8.2: "8:20", 8.3: "8:30", 8.4: "8:40", 8.5: "8:50", 9.0: "9:00", 9.1: "9:10"}
SIMPLE = {1.0: "Yes", 2.0: "No", 3.0: "Don't\nknow"}


def postgame(df, exps):
    d = df[df.exp.isin(exps)]
    c = d.cutoff.dropna().value_counts().reindex(list(CUTOFF), fill_value=0)
    s = d.simple.dropna().value_counts().reindex(list(SIMPLE), fill_value=0)
    return c, s


def fig7(df, exps, name, outdir):
    """Port of software/python/fig6_cutoff.py (published fig6_cutoff.pdf).
    DEVIATION: categories are mapped explicitly (codes 6.0 = "I don't know", 7.0 = "There is no
    such time", 8.0..9.1 = times; simple 1/2/3 = Yes/No/Don't know, as in the original label
    order). The original labelled np.unique() output positionally, which mislabels or fails
    when a category has no answers; in DTU1+DTU2 nobody answered 8:10."""
    c, s = postgame(df, exps)
    fig, axes = plt.subplots(nrows=1, ncols=2, gridspec_kw={"width_ratios": [3.5, 1]}, figsize=(8, 4))
    axes[0].bar(list(CUTOFF.values()), c.values / c.sum(), width=.7, align="center", label=f"N={c.sum()}")
    axes[0].set_xticks(np.arange(len(CUTOFF)))
    axes[0].set_xticklabels(list(CUTOFF.values()), rotation=60, ha="center")
    axes[0].tick_params(axis="x", labelsize=12); axes[0].tick_params(axis="y", labelsize=12)
    axes[0].set_ylabel("Fraction of participants", fontsize=13)
    axes[0].legend()
    axes[0].set_title("A: Cutoff point", loc="left", fontsize=14)
    axes[1].bar(list(SIMPLE.values()), s.values / s.sum(), width=.7, align="center", label=f"N={s.sum()}")
    axes[1].set_ylabel("Fraction of participants", fontsize=13)
    axes[1].set_title("B: Common\n    Knowledge", loc="left", fontsize=14)
    axes[1].tick_params(axis="x", labelsize=12); axes[1].tick_params(axis="y", labelsize=12)
    plt.tight_layout()
    save(None, name, outdir, bbox_inches="tight")
    return c, s


# --------------------------------------------------------------------------- statistics
def logit_fit(x, y):
    m = sm.GLM(y, sm.add_constant(x), family=sm.families.Binomial()).fit()
    b0, b1 = m.params.iloc[0], m.params.iloc[1]
    return m, b0, b1, -b0 / b1


def fmt_min(m):
    """minutes after 8:00 on the equidistant scale (60 = 9:00) -> h:mm string."""
    h, mm = divmod(m, 60)
    return f"{8 + int(h)}:{mm:04.1f}"


def stats_report(df, exps, dis):
    L = []
    p = L.append
    p(f"# Verification statistics, data = {'+'.join(exps)}" + (" + DIS" if dis is not None else ""))
    d = df[df.exp.isin(exps)].copy()
    d["m"] = minutes(d.arrival)
    p("\n## Canteen choice by arrival time (% canteen, n)")
    for e in exps + ["pooled"]:
        x = d if e == "pooled" else d[d.exp == e]
        t = x.groupby("arrival").choice.agg(["mean", "size"])
        p(f"{e:7s} " + "  ".join(f"{TIMES[i]} {100*r['mean']:5.1f}% ({int(r['size'])})" for i, (_, r) in enumerate(t.iterrows())))
    p("\n## Logistic fit choice ~ minutes (0..70, 9:00 = 60); 50% point = -b0/b1")
    for e in exps + ["pooled"]:
        x = d if e == "pooled" else d[d.exp == e]
        _, b0, b1, x50 = logit_fit(x.m, x.choice)
        p(f"{e:7s} b0={b0:7.3f} b1={b1:8.4f}  50% at {x50:5.2f} min = {fmt_min(x50)}")
    if dis is not None:
        _, b0, b1, x50 = logit_fit(dis.card, dis.choice)
        p(f"DIS     card scale: b0={b0:7.3f} b1={b1:8.4f}  50% at card {x50:4.2f}"
          f" (= {fmt_min(50 + (x50 - 8) * 10)} on the canteen scale)")
        t = dis.groupby("card").choice.agg(["mean", "size"])
        p("DIS white by card: " + "  ".join(f"{c}: {100*r['mean']:.1f}% ({int(r['size'])})" for c, r in t.iterrows()))
    if len(exps) == 2:
        x = d.copy()
        m1 = smf.glm("choice ~ m * C(exp)", data=x, family=sm.families.Binomial()).fit()
        m0 = smf.glm("choice ~ m", data=x, family=sm.families.Binomial()).fit()
        lr = 2 * (m1.llf - m0.llf)
        from scipy.stats import chi2
        p(f"\nDTU1 vs DTU2, GLM choice ~ m*exp: LR test vs pooled model chi2(2)={lr:.2f}, p={chi2.sf(lr, 2):.4g}")
        p("  coefficients: " + ", ".join(f"{k}={v:.4f} (p={m1.pvalues[k]:.3g})" for k, v in m1.params.items()))
        p("  (pair-level clustering ignored, as in the original analysis)")
    p("\n## Coordination by arrival pair (office / miscoordination / canteen, % of pair-rounds)")
    o, mi, c = coord_counts(df, exps)
    for k, (a, b, cc) in enumerate(zip(o, mi, c)):
        n = a + b + cc
        p(f"{PAIRS[k]:10s} N={n:4d}  office {100*a/n:5.1f}  mis {100*b/n:5.1f}  canteen {100*cc/n:5.1f}")
    p("\n## Certainty: median and mean by arrival time")
    for e in exps + ["pooled"]:
        x = d if e == "pooled" else d[d.exp == e]
        t = x.groupby("arrival").certainty.agg(["median", "mean"])
        p(f"{e:7s} " + "  ".join(f"{TIMES[i]} {r['median']:.3f}/{r['mean']:.3f}" for i, (_, r) in enumerate(t.iterrows())))
    p("\n## Fig 4 WLS lines (freq ~ round, weights sqrt(n)): slope per round, value at round 1 and last round")
    tot, freq = timeseries(df, exps)
    for a, lab in ((8.4, "8:40"), (8.5, "8:50"), (9.0, "9:00")):
        r, coef = wls(freq, tot, a)
        f = np.poly1d(coef)
        p(f"{lab}  slope {coef[0]:+.4f}/round  fit r1 {f(1):.3f}  fit r{int(r.max())} {f(r.max()):.3f}  (rounds with data: {len(r)})")
    p("\n## Post-game answers")
    for e in exps + ["pooled"]:
        ee = exps if e == "pooled" else [e]
        cc, s = postgame(df, ee)
        N, S = cc.sum(), s.sum()
        safe = cc[[8.3, 8.4, 8.5]].sum()
        p(f"{e:7s} cutoff N={N}: " + ", ".join(f"{CUTOFF[k].replace(chr(10), ' ')}={v}" for k, v in cc.items()))
        p(f"        safe cut-off 8:30-8:50: {safe}/{N} = {100*safe/N:.1f}%;  'no such time': {cc[7.0]}/{N} = {100*cc[7.0]/N:.1f}%")
        p(f"        CK at 8:10 N={S}: yes {s[1.0]} ({100*s[1.0]/S:.1f}%), no {s[2.0]} ({100*s[2.0]/S:.1f}%), don't know {s[3.0]} ({100*s[3.0]/S:.1f}%)")
    p("\n## Arrival-pair frequencies (unordered pairs, % of pair-rounds)")
    pr = d.groupby(["exp", "session", "group", "round"]).arrival.mean().round(3)
    for e in exps:
        v = pr.loc[e].value_counts(normalize=True).sort_index()
        p(f"{e:7s} " + "  ".join(f"{PAIRS[i]} {100*x:.1f}%" for i, x in enumerate(v.values)))
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- reproduce
def reproduce():
    """Run the ports on MTurk+DTU1+DTU2 and compare with numbers stored in the original
    notebooks / printed in the paper. Writes figures to a temp dir only."""
    import tempfile
    tmp = tempfile.mkdtemp(prefix="tark_repro_")
    df = load(["MTurk", "DTU1", "DTU2"])
    df.loc[df.exp == "MTurk", "exp"] = "AMT"
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"[{'OK ' if good else 'BAD'}] {label}: got {got}, want {want}")

    t = table1(df, ["AMT", "DTU1", "DTU2"], {"AMT": 10, "DTU1": 30, "DTU2": 30})
    # python/table.ipynb stored output
    want = [["AMT", 680, 10, 6.26, 4260, 52.79, 23.59, -1.59],
            ["DTU1", 80, 30, 27.0, 2160, 17.5, 27.03, -0.83],
            ["DTU2", 42, 30, 24.1, 1012, 30.95, 24.11, -0.98]]
    check("Table 1 (python/table.ipynb output)", t.values.tolist(), want)
    o, m, c = coord_counts(df, ["AMT", "DTU1", "DTU2"])
    check("Fig 3 counts (fig3_miscoordinations.ipynb output)", [o, m, c],
          [[3, 6, 9, 8, 41, 280, 362], [44, 31, 36, 62, 259, 257, 89], [403, 516, 547, 454, 266, 30, 13]])
    tot, freq = timeseries(df, ["AMT", "DTU1", "DTU2"])
    check("Fig 4 n, round 1 (fig4.ipynb output)", tot.loc[1].astype(int).tolist(), [50, 112, 121, 119, 113, 114, 117, 56])
    check("Fig 4 freq 8:50, rounds 1-5", [round(v, 6) for v in freq[8.5].iloc[:5]],
          [0.596491, 0.478992, 0.566372, 0.468354, 0.45])
    cc, s = postgame(df, ["AMT", "DTU1", "DTU2"])
    check("Fig 7 all categories present (original positional labels valid)", int((cc > 0).sum()), 10)
    check("Fig 7 'no such time' < 4% (paper)", bool(cc[7.0] / cc.sum() < .04), True)
    check("Fig 7 CK yes = 89% (paper)", round(100 * s[1.0] / s.sum()), 89)
    safe = cc[[8.3, 8.4, 8.5]].sum() / cc.sum()
    check("Fig 7 8:30-8:50 'approximately 75%' (paper)", round(100 * safe), 76)
    check("Fig 1 n per experiment (legend)", [int((df.exp == e).sum()) for e in ["AMT", "DTU1", "DTU2"]], [4260, 2160, 1012])
    check("Fig 5 DIS n (legend)", len(load_dis()), 210)
    # Fig 6 inset: refit exactly as the original code did (df = last file = DTU2) and as the
    # caption says (all three). Both written to tmp for visual comparison with plots/fig5_logit_all.pdf
    n_bug = fig6_inset(df, ["DTU2"], "inset_as_coded_DTU2", tmp)
    n_cap = fig6_inset(df, ["AMT", "DTU1", "DTU2"], "inset_as_captioned_all", tmp)
    print(f"[info] Fig 6 inset: as coded n={n_bug}, as captioned n={n_cap} (caption says n=7432). PNGs in {tmp}")
    print("REPRODUCTION", "PASSED" if ok else "FAILED")
    return ok, tmp


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reproduce", action="store_true")
    a = ap.parse_args()
    if a.reproduce:
        ok, _ = reproduce()
        sys.exit(0 if ok else 1)

    exps = ["DTU1", "DTU2"]
    df = load(exps)
    # Author decision (TSN, 2026-11-09): table 7 was played by an author (RE); excluded.
    # This matches the arXiv text (12 students, n = 180); the arXiv figure wrongly used n = 210.
    dis = load_dis(drop_table7=True)
    os.makedirs(OUT, exist_ok=True)

    t = table1(df, exps, {"DTU1": 30, "DTU2": 30})
    with open(os.path.join(OUT, "tark_table1.tex"), "w") as f:
        f.write("% Generated by scripts/make_figures.py (DTU1+DTU2 only). Rows only; caption lives in body.tex.\n")
        f.write(table1_tex(t))
    fig1(df, exps, "tark_fig1_choices", OUT)
    fig1(df, exps, "tark_fig1_choices_with_DIS", OUT, dis=dis)
    fig2(df, {"DTU1": "DTU1", "DTU2": "DTU2"}, "tark_fig2_certainties", OUT)
    fig3(df, exps, "tark_fig3_miscoordinations", OUT)
    fig4(df, exps, "tark_fig4_timeseries", OUT)
    fig5_dis(dis, "tark_fig5_DIS", OUT)
    fig6_inset(df, exps, "tark_fig6_logit_inset", OUT)
    fig7(df, exps, "tark_fig7_postgame", OUT)
    rep = stats_report(df, exps, dis)
    d6 = load_dis(drop_table7=False)
    _, b0, b1, x50 = logit_fit(d6.card, d6.choice)
    t6 = d6.groupby("card").choice.agg(["mean", "size"])
    rep += (f"\n## For reference: DIS incl. table 7 (author-played; used in the arXiv figure), n={len(d6)}\n"
            f"DIS7    b0={b0:7.3f} b1={b1:8.4f}  50% at card {x50:4.2f}\n"
            "DIS7 white by card: " + "  ".join(f"{c}: {100*r['mean']:.1f}% ({int(r['size'])})" for c, r in t6.iterrows()) + "\n")
    rep += "\n## Table 1\n" + t.to_string(index=False) + "\n"
    with open(os.path.join(OUT, "tark_stats.txt"), "w") as f:
        f.write(rep)
    print(rep)


if __name__ == "__main__":
    main()
