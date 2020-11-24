import numpy as np
import pandas as pd
from tabulate import tabulate

"""
Pretty printing the most important stats.
Usage: copy output into latex file.

Table 1: Exp. = experiment; N = number of subjects; R = maximum number of rounds;
r_mean = average number of rounds played; Ruin = percentage of participants loosing all their
bonus before (or in) the last round; ToEnd = percentage of participants having a bonus
left after last round; AvgBonus = average bonus earned (percentages relate to the to the
initial bonus given); s_mean = average penality per player per round. Please note that `Ruin'
and `ToEnd' not add up to unity because those players who were paired with ruined players
were stopped prematurely but still received what was left of their bonus.
"""

datafile_AMT = '../data/MTurk_anonymous.xlsx'
datafile_DTU1 = '../data/DTU1_anonymous.xlsx'
datafile_DTU2 = '../data/DTU2_anonymous.xlsx'
# transactiondata = '../RawData/transactiondata.xlsx'

def tabulated_stats(experiments):
    table = pd.DataFrame()
    participants = []
    max_rounds = [10,30,30]
    avg_rounds = []
    avg_penalty = []
    ruined = []
    payout_a = []
    for idx, experiment in enumerate(experiments):
        participants.append(len(experiment.code.unique()))  # total number of participants
        players = experiment.code.unique()
        ruin = 0
        money_left = 0
        pay_a = []
        for player in players:
            pay_a.append(experiment[experiment.code == player]['payoff'].unique().item())    # summing all payoffs
            if experiment[experiment.code == player]['payoff'].unique().item() == 0:
                ruin += 1
            else:
                money_left += 1

        avg_rounds.append(len(experiment)/len(experiment.code.unique()))
        ruined.append(100*ruin/len(experiment.code.unique()))
        payout_a.append(sum(pay_a)/len(pay_a))
        avg_penalty.append(experiment.bonus.mean())


    table['Treatment'] = ['AMT', 'DTU1', 'DTU2']
    table['N'] = participants
    table['MaxRounds'] = max_rounds
    table['avg. rounds'] = np.around(avg_rounds,2)
    table['Ruin'] = np.around(ruined,2)
    table['payoff'] = np.around(100*np.array(payout_a)/np.array(max_rounds),2)
    table['Avg penalty'] = np.around(avg_penalty,2)

    return table


# main code
df_AMT = pd.DataFrame(pd.read_excel(datafile_AMT))
df_DTU1 = pd.DataFrame(pd.read_excel(datafile_DTU1))
df_DTU2 = pd.DataFrame(pd.read_excel(datafile_DTU2))
df_all = df_AMT
df_all = df_all.append(df_DTU1)
df_all = df_all.append(df_DTU2)

table = tabulated_stats([df_AMT, df_DTU1, df_DTU2])
print(tabulate(table, tablefmt="latex_raw", headers="keys", showindex=False))

# df = pd.DataFrame(pd.read_excel(transactiondata))
# print(df['Transaction Type'].unique())
# df = df[(df['Transaction Type'] != 'Prepayment') & (df['Transaction Type'] != 'FeePayment')]
# print('total paid to players =', sum(df['Amount']))
# print('number of players:', len(df['Recipient ID'].unique()))
# print('avg =', sum(df['Amount'])/len(df['Recipient ID'].unique()))
