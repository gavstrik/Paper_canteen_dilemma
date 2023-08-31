import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

datafiles = [
             '../RawData/MTurk/canteen_dilemma_data_(set 1 of 3).csv',
             '../RawData/MTurk/canteen_dilemma_data_(set 2 of 3).csv',
             '../RawData/MTurk/canteen_dilemma_data_(set 3 of 3).csv',
            ]


def make_dataframe(df):
    # take only the relevant columns in data sheet
    df = df[[
    'session.code',
    'participant.code',
    'participant.mturk_worker_id',
    'canteen_dilemma_lsr.1.group.id_in_subsession',
    'canteen_dilemma_lsr.2.group.id_in_subsession',
    'canteen_dilemma_lsr.3.group.id_in_subsession',
    'canteen_dilemma_lsr.4.group.id_in_subsession',
    'canteen_dilemma_lsr.5.group.id_in_subsession',
    'canteen_dilemma_lsr.6.group.id_in_subsession',
    'canteen_dilemma_lsr.7.group.id_in_subsession',
    'canteen_dilemma_lsr.8.group.id_in_subsession',
    'canteen_dilemma_lsr.9.group.id_in_subsession',
    'canteen_dilemma_lsr.10.group.id_in_subsession',
    'canteen_dilemma_lsr.1.player.id_in_group',
    'canteen_dilemma_lsr.2.player.id_in_group',
    'canteen_dilemma_lsr.3.player.id_in_group',
    'canteen_dilemma_lsr.4.player.id_in_group',
    'canteen_dilemma_lsr.5.player.id_in_group',
    'canteen_dilemma_lsr.6.player.id_in_group',
    'canteen_dilemma_lsr.7.player.id_in_group',
    'canteen_dilemma_lsr.8.player.id_in_group',
    'canteen_dilemma_lsr.9.player.id_in_group',
    'canteen_dilemma_lsr.10.player.id_in_group',
    'canteen_dilemma_lsr.1.player.arrival_time',
    'canteen_dilemma_lsr.2.player.arrival_time',
    'canteen_dilemma_lsr.3.player.arrival_time',
    'canteen_dilemma_lsr.4.player.arrival_time',
    'canteen_dilemma_lsr.5.player.arrival_time',
    'canteen_dilemma_lsr.6.player.arrival_time',
    'canteen_dilemma_lsr.7.player.arrival_time',
    'canteen_dilemma_lsr.8.player.arrival_time',
    'canteen_dilemma_lsr.9.player.arrival_time',
    'canteen_dilemma_lsr.10.player.arrival_time',
    'canteen_dilemma_lsr.1.player.choice',
    'canteen_dilemma_lsr.2.player.choice',
    'canteen_dilemma_lsr.3.player.choice',
    'canteen_dilemma_lsr.4.player.choice',
    'canteen_dilemma_lsr.5.player.choice',
    'canteen_dilemma_lsr.6.player.choice',
    'canteen_dilemma_lsr.7.player.choice',
    'canteen_dilemma_lsr.8.player.choice',
    'canteen_dilemma_lsr.9.player.choice',
    'canteen_dilemma_lsr.10.player.choice',
    'canteen_dilemma_lsr.1.player.certainty',
    'canteen_dilemma_lsr.2.player.certainty',
    'canteen_dilemma_lsr.3.player.certainty',
    'canteen_dilemma_lsr.4.player.certainty',
    'canteen_dilemma_lsr.5.player.certainty',
    'canteen_dilemma_lsr.6.player.certainty',
    'canteen_dilemma_lsr.7.player.certainty',
    'canteen_dilemma_lsr.8.player.certainty',
    'canteen_dilemma_lsr.9.player.certainty',
    'canteen_dilemma_lsr.10.player.certainty',
    'canteen_dilemma_lsr.1.player.payoff',
    'canteen_dilemma_lsr.2.player.payoff',
    'canteen_dilemma_lsr.3.player.payoff',
    'canteen_dilemma_lsr.4.player.payoff',
    'canteen_dilemma_lsr.5.player.payoff',
    'canteen_dilemma_lsr.6.player.payoff',
    'canteen_dilemma_lsr.7.player.payoff',
    'canteen_dilemma_lsr.8.player.payoff',
    'canteen_dilemma_lsr.9.player.payoff',
    'canteen_dilemma_lsr.10.player.payoff',
    'canteen_dilemma_lsr.1.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.2.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.3.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.4.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.5.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.6.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.7.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.8.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.9.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.10.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.1.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.2.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.3.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.4.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.5.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.6.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.7.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.8.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.9.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.10.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.1.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.2.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.3.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.4.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.5.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.6.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.7.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.8.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.9.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.10.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.1.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.2.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.3.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.4.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.5.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.6.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.7.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.8.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.9.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.10.player.fault_canteen_dilemma',
    'participant.payoff',
    ]]

    # rename columns
    df.columns = [
        'session',
        'code',
        'turker',
        'group1','group2','group3','group4','group5','group6','group7','group8','group9','group10',
        'id_in_group1','id_in_group2','id_in_group3','id_in_group4','id_in_group5','id_in_group6','id_in_group7','id_in_group8','id_in_group9','id_in_group10',
        'arrival1','arrival2','arrival3','arrival4','arrival5','arrival6','arrival7','arrival8','arrival9','arrival10',
        'choice1','choice2','choice3','choice4','choice5','choice6','choice7','choice8','choice9','choice10',
        'certainty1','certainty2','certainty3','certainty4','certainty5','certainty6','certainty7','certainty8','certainty9','certainty10',
        'bonus1','bonus2','bonus3','bonus4','bonus5','bonus6','bonus7','bonus8','bonus9','bonus10',
        'strategy1','strategy2','strategy3','strategy4','strategy5','strategy6','strategy7','strategy8','strategy9','strategy10',
        'simple1','simple2','simple3','simple4','simple5','simple6','simple7','simple8','simple9','simple10',
        'cutoff1','cutoff2','cutoff3','cutoff4','cutoff5','cutoff6','cutoff7','cutoff8','cutoff9','cutoff10',
        'fault1','fault2','fault3','fault4','fault5','fault6','fault7','fault8','fault9','fault10',
        'payoff',
    ]

    df.reset_index(inplace=True)
    df["id"] = df.index
    df = pd.wide_to_long(df, stubnames=[
                                        'group',
                                        'id_in_group',
                                        'arrival',
                                        'choice',
                                        'certainty',
                                        'bonus',
                                        'strategy',
                                        'simple',
                                        'cutoff',
                                        'fault',
                                       ],
                          i='id', j='round').reset_index()

    # remove all entries where bonus = 0:
    df = df[df['bonus'] != 0]

    # keep only relevant columns:
    df = df[['session', 'code', 'turker', 'group', 'id_in_group', 'round', 'arrival',
             'choice', 'certainty', 'bonus', 'strategy', 'simple',
             'cutoff', 'fault', 'payoff']]

    # sort and reset index
    df = df.sort_values(['session', 'group', 'round', 'id_in_group'])
    df.reset_index(inplace=True, drop=True)
    print('number of players:', len(df.code.unique()))

    # hack here to populate the payoff column with the true payoffs
    players = df.code.unique()
    for player in players:
        if df[df.code == player]['payoff'].unique().item() != -2:
            pay = df[df.code == player]['bonus'].sum()
            if pay < -10:
                pay = -10
            idxs = df.index[df.code == player].tolist()
            for idx in idxs:
                df.loc[idx, 'payoff'] = 10 + pay

    # and subsequently find the -2 player and her colleague and remove them:
    quitters = []
    for player in players:
        if df[df.code == player]['payoff'].unique().item() == -2:
            # find the colleague who's payoff also needs to be removed
            player_id_in_group = df[df.code == player]['id_in_group'].unique().item()
            player_session = df[df.code == player]['session'].unique().item()
            player_group = df[df.code == player]['group'].unique().item()
            if player_id_in_group == 1:
                colleague = df[(df.session == player_session) & (df.group == player_group) & (df.id_in_group == 2)]['code'].unique().item()
            if player_id_in_group == 2:
                colleague = df[(df.session == player_session) & (df.group == player_group) & (df.id_in_group == 1)]['code'].unique().item()

            quitters.append(player)
            quitters.append(colleague)

    # and finaly remove the players:
    print('removing', len(set(quitters)), 'quitters')
    for r in quitters:
        df = df[df.code != r]
    print('players left =', len(df.code.unique()))

    return df


# load datafiles
df_all = pd.DataFrame()
for datafile in datafiles:
    df = pd.DataFrame(pd.read_csv(datafile, low_memory=False))
    df_all = df_all.append(df, sort=True)
df_all = df_all[df_all['session.is_demo'] == 0]

df = make_dataframe(df_all)
print(df.head())
print(df.keys())
print('number of participants:', len(df.turker.unique()))
print('total number of rounds played:', len(df), 'average =', len(df)/len(df.turker.unique()))

# save
# df.to_csv('../data/MTurk.csv')
# df.to_excel('../data/MTurk.xlsx')
df = df.drop(['turker'], 1) # make anonymous
df.to_csv('../data/MTurk_anonymous.csv')
df.to_excel('../data/MTurk_anonymous.xlsx')
