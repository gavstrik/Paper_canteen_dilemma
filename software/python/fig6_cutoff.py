import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
PLOTS_DIR = '../plots'

"""
Figure 5: A) Frequencies of answers to the question: \Imagine you could have agreed
beforehand with your colleague about a point in time where it is safe to go to the canteen.
What time would that be?" Due to the pragmatics of language, we assume that an answer
like 8:30 entails the belief that all earlier arrival times would also be deemed safe. B)
Frequencies of answers to the question: "Imagine you arrive at 8:10 am. Is it common
knowledge between you and your colleague that it is safe to go to the canteen, that is, you
both arrived before 9:00 am?"
"""

datafiles = [
             '../data/MTurk_anonymous.xlsx',
             '../data/DTU1_anonymous.xlsx',
             '../data/DTU2_anonymous.xlsx',
]


def cutoff_and_common_knowledge(df):
    fig, axes = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3.5, 1]}, figsize=(8,4))

    # first plot showing the cutoff answers:
    df = df[np.isfinite(df['cutoff'])]
    y = df.cutoff.values
    _, counts = np.unique(y, return_counts=True)
    counts0 = counts/np.sum(counts)
    labels0 = ['I don\'t know',  'There is no\nsuch time',  '8:00', '8:10', '8:20', '8:30', '8:40', '8:50', '9:00', '9:10']
    axes[0].bar(labels0, counts0, width=.7, align='center', label='N='+str(len(y)))
    axes[0].set_xticks(np.arange(len(labels0)))
    axes[0].set_xticklabels(labels0, rotation=60, ha="center")
    axes[0].tick_params(axis='x', labelsize=12)
    axes[0].tick_params(axis='y', labelsize=12)
    axes[0].set_ylabel('Fraction of participants', fontsize=13)
    axes[0].legend()
    axes[0].set_title('A: Cutoff point', loc='left', fontsize=14)
    print('frequencies cutoff:', counts0)

    # second plot showing the common knowledge answers:
    df = df[np.isfinite(df['simple'])]
    y = df.simple.values
    _, counts = np.unique(y, return_counts=True)
    counts1 = counts/np.sum(counts)
    labels1 = ['Yes',  'No',  'Don\'t\nknow']
    axes[1].bar(labels1, counts1, width=.7, align='center', label='N='+str(len(y)))
    axes[1].set_ylabel('Fraction of participants', fontsize=13)
    axes[1].set_title('B: Common\n    Knowledge', loc='left', fontsize=14)
    print('frequencies common knowledge:', counts1)
    axes[1].tick_params(axis='x', labelsize=12)
    axes[1].tick_params(axis='y', labelsize=12)
    plt.tight_layout()

    # Remember: save as pdf and transparent=True for Adobe Illustrator
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)

    plt.savefig(os.path.join(PLOTS_DIR, 'fig6_cutoff.png'),
                # bbox_extra_artists=(lgd,),
                bbox_inches='tight', transparent=True, dpi=300)
    plt.savefig(os.path.join(PLOTS_DIR, 'fig6_cutoff.pdf'),
                # bbox_extra_artists=(lgd,),
                bbox_inches='tight', transparent=True, dpi=300)
    plt.show()


# load the data
df_all = pd.DataFrame()
for datafile in datafiles:
    df = pd.DataFrame(pd.read_excel(datafile))
    df_all = df_all.append(df, sort=True)

cutoff_and_common_knowledge(df_all)
