import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

datafiles = [
             '../RawData/DTU1/all_apps_wide_2019-04-09.csv',
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
    'canteen_dilemma_lsr.11.group.id_in_subsession',
    'canteen_dilemma_lsr.12.group.id_in_subsession',
    'canteen_dilemma_lsr.13.group.id_in_subsession',
    'canteen_dilemma_lsr.14.group.id_in_subsession',
    'canteen_dilemma_lsr.15.group.id_in_subsession',
    'canteen_dilemma_lsr.16.group.id_in_subsession',
    'canteen_dilemma_lsr.17.group.id_in_subsession',
    'canteen_dilemma_lsr.18.group.id_in_subsession',
    'canteen_dilemma_lsr.19.group.id_in_subsession',
    'canteen_dilemma_lsr.20.group.id_in_subsession',
    'canteen_dilemma_lsr.21.group.id_in_subsession',
    'canteen_dilemma_lsr.22.group.id_in_subsession',
    'canteen_dilemma_lsr.23.group.id_in_subsession',
    'canteen_dilemma_lsr.24.group.id_in_subsession',
    'canteen_dilemma_lsr.25.group.id_in_subsession',
    'canteen_dilemma_lsr.26.group.id_in_subsession',
    'canteen_dilemma_lsr.27.group.id_in_subsession',
    'canteen_dilemma_lsr.28.group.id_in_subsession',
    'canteen_dilemma_lsr.29.group.id_in_subsession',
    'canteen_dilemma_lsr.30.group.id_in_subsession',
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
    'canteen_dilemma_lsr.11.player.id_in_group',
    'canteen_dilemma_lsr.12.player.id_in_group',
    'canteen_dilemma_lsr.13.player.id_in_group',
    'canteen_dilemma_lsr.14.player.id_in_group',
    'canteen_dilemma_lsr.15.player.id_in_group',
    'canteen_dilemma_lsr.16.player.id_in_group',
    'canteen_dilemma_lsr.17.player.id_in_group',
    'canteen_dilemma_lsr.18.player.id_in_group',
    'canteen_dilemma_lsr.19.player.id_in_group',
    'canteen_dilemma_lsr.20.player.id_in_group',
    'canteen_dilemma_lsr.21.player.id_in_group',
    'canteen_dilemma_lsr.22.player.id_in_group',
    'canteen_dilemma_lsr.23.player.id_in_group',
    'canteen_dilemma_lsr.24.player.id_in_group',
    'canteen_dilemma_lsr.25.player.id_in_group',
    'canteen_dilemma_lsr.26.player.id_in_group',
    'canteen_dilemma_lsr.27.player.id_in_group',
    'canteen_dilemma_lsr.28.player.id_in_group',
    'canteen_dilemma_lsr.29.player.id_in_group',
    'canteen_dilemma_lsr.30.player.id_in_group',
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
    'canteen_dilemma_lsr.11.player.arrival_time',
    'canteen_dilemma_lsr.12.player.arrival_time',
    'canteen_dilemma_lsr.13.player.arrival_time',
    'canteen_dilemma_lsr.14.player.arrival_time',
    'canteen_dilemma_lsr.15.player.arrival_time',
    'canteen_dilemma_lsr.16.player.arrival_time',
    'canteen_dilemma_lsr.17.player.arrival_time',
    'canteen_dilemma_lsr.18.player.arrival_time',
    'canteen_dilemma_lsr.19.player.arrival_time',
    'canteen_dilemma_lsr.20.player.arrival_time',
    'canteen_dilemma_lsr.21.player.arrival_time',
    'canteen_dilemma_lsr.22.player.arrival_time',
    'canteen_dilemma_lsr.23.player.arrival_time',
    'canteen_dilemma_lsr.24.player.arrival_time',
    'canteen_dilemma_lsr.25.player.arrival_time',
    'canteen_dilemma_lsr.26.player.arrival_time',
    'canteen_dilemma_lsr.27.player.arrival_time',
    'canteen_dilemma_lsr.28.player.arrival_time',
    'canteen_dilemma_lsr.29.player.arrival_time',
    'canteen_dilemma_lsr.30.player.arrival_time',
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
    'canteen_dilemma_lsr.11.player.choice',
    'canteen_dilemma_lsr.12.player.choice',
    'canteen_dilemma_lsr.13.player.choice',
    'canteen_dilemma_lsr.14.player.choice',
    'canteen_dilemma_lsr.15.player.choice',
    'canteen_dilemma_lsr.16.player.choice',
    'canteen_dilemma_lsr.17.player.choice',
    'canteen_dilemma_lsr.18.player.choice',
    'canteen_dilemma_lsr.19.player.choice',
    'canteen_dilemma_lsr.20.player.choice',
    'canteen_dilemma_lsr.21.player.choice',
    'canteen_dilemma_lsr.22.player.choice',
    'canteen_dilemma_lsr.23.player.choice',
    'canteen_dilemma_lsr.24.player.choice',
    'canteen_dilemma_lsr.25.player.choice',
    'canteen_dilemma_lsr.26.player.choice',
    'canteen_dilemma_lsr.27.player.choice',
    'canteen_dilemma_lsr.28.player.choice',
    'canteen_dilemma_lsr.29.player.choice',
    'canteen_dilemma_lsr.30.player.choice',
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
    'canteen_dilemma_lsr.11.player.certainty',
    'canteen_dilemma_lsr.12.player.certainty',
    'canteen_dilemma_lsr.13.player.certainty',
    'canteen_dilemma_lsr.14.player.certainty',
    'canteen_dilemma_lsr.15.player.certainty',
    'canteen_dilemma_lsr.16.player.certainty',
    'canteen_dilemma_lsr.17.player.certainty',
    'canteen_dilemma_lsr.18.player.certainty',
    'canteen_dilemma_lsr.19.player.certainty',
    'canteen_dilemma_lsr.20.player.certainty',
    'canteen_dilemma_lsr.21.player.certainty',
    'canteen_dilemma_lsr.22.player.certainty',
    'canteen_dilemma_lsr.23.player.certainty',
    'canteen_dilemma_lsr.24.player.certainty',
    'canteen_dilemma_lsr.25.player.certainty',
    'canteen_dilemma_lsr.26.player.certainty',
    'canteen_dilemma_lsr.27.player.certainty',
    'canteen_dilemma_lsr.28.player.certainty',
    'canteen_dilemma_lsr.29.player.certainty',
    'canteen_dilemma_lsr.30.player.certainty',
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
    'canteen_dilemma_lsr.11.player.payoff',
    'canteen_dilemma_lsr.12.player.payoff',
    'canteen_dilemma_lsr.13.player.payoff',
    'canteen_dilemma_lsr.14.player.payoff',
    'canteen_dilemma_lsr.15.player.payoff',
    'canteen_dilemma_lsr.16.player.payoff',
    'canteen_dilemma_lsr.17.player.payoff',
    'canteen_dilemma_lsr.18.player.payoff',
    'canteen_dilemma_lsr.19.player.payoff',
    'canteen_dilemma_lsr.20.player.payoff',
    'canteen_dilemma_lsr.21.player.payoff',
    'canteen_dilemma_lsr.22.player.payoff',
    'canteen_dilemma_lsr.23.player.payoff',
    'canteen_dilemma_lsr.24.player.payoff',
    'canteen_dilemma_lsr.25.player.payoff',
    'canteen_dilemma_lsr.26.player.payoff',
    'canteen_dilemma_lsr.27.player.payoff',
    'canteen_dilemma_lsr.28.player.payoff',
    'canteen_dilemma_lsr.29.player.payoff',
    'canteen_dilemma_lsr.30.player.payoff',
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
    'canteen_dilemma_lsr.11.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.12.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.13.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.14.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.15.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.16.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.17.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.18.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.19.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.20.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.21.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.22.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.23.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.24.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.25.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.26.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.27.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.28.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.29.player.strategy_canteen_dilemma',
    'canteen_dilemma_lsr.30.player.strategy_canteen_dilemma',
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
    'canteen_dilemma_lsr.11.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.12.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.13.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.14.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.15.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.16.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.17.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.18.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.19.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.20.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.21.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.22.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.23.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.24.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.25.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.26.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.27.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.28.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.29.player.simple_common_knowledge_canteen_dilemma',
    'canteen_dilemma_lsr.30.player.simple_common_knowledge_canteen_dilemma',
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
    'canteen_dilemma_lsr.11.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.12.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.13.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.14.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.15.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.16.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.17.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.18.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.19.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.20.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.21.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.22.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.23.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.24.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.25.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.26.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.27.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.28.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.29.player.cutoff_canteen_dilemma',
    'canteen_dilemma_lsr.30.player.cutoff_canteen_dilemma',
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
    'canteen_dilemma_lsr.11.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.12.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.13.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.14.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.15.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.16.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.17.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.18.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.19.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.20.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.21.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.22.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.23.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.24.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.25.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.26.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.27.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.28.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.29.player.fault_canteen_dilemma',
    'canteen_dilemma_lsr.30.player.fault_canteen_dilemma',
    'participant.payoff',
    ]]

    # rename columns
    df.columns = [
        'session',
        'code',
        'turker',
        'group1','group2','group3','group4','group5','group6','group7','group8','group9','group10',
        'group11','group12','group13','group14','group15','group16','group17','group18','group19','group20',
        'group21','group22','group23','group24','group25','group26','group27','group28','group29','group30',
        'id_in_group1','id_in_group2','id_in_group3','id_in_group4','id_in_group5','id_in_group6','id_in_group7','id_in_group8','id_in_group9','id_in_group10',
        'id_in_group11','id_in_group12','id_in_group13','id_in_group14','id_in_group15','id_in_group16','id_in_group17','id_in_group18','id_in_group19','id_in_group20',
        'id_in_group21','id_in_group22','id_in_group23','id_in_group24','id_in_group25','id_in_group26','id_in_group27','id_in_group28','id_in_group29','id_in_group30',
        'arrival1','arrival2','arrival3','arrival4','arrival5','arrival6','arrival7','arrival8','arrival9','arrival10',
        'arrival11','arrival12','arrival13','arrival14','arrival15','arrival16','arrival17','arrival18','arrival19','arrival20',
        'arrival21','arrival22','arrival23','arrival24','arrival25','arrival26','arrival27','arrival28','arrival29','arrival30',
        'choice1','choice2','choice3','choice4','choice5','choice6','choice7','choice8','choice9','choice10',
        'choice11','choice12','choice13','choice14','choice15','choice16','choice17','choice18','choice19','choice20',
        'choice21','choice22','choice23','choice24','choice25','choice26','choice27','choice28','choice29','choice30',
        'certainty1','certainty2','certainty3','certainty4','certainty5','certainty6','certainty7','certainty8','certainty9','certainty10',
        'certainty11','certainty12','certainty13','certainty14','certainty15','certainty16','certainty17','certainty18','certainty19','certainty20',
        'certainty21','certainty22','certainty23','certainty24','certainty25','certainty26','certainty27','certainty28','certainty29','certainty30',
        'bonus1','bonus2','bonus3','bonus4','bonus5','bonus6','bonus7','bonus8','bonus9','bonus10',
        'bonus11','bonus12','bonus13','bonus14','bonus15','bonus16','bonus17','bonus18','bonus19','bonus20',
        'bonus21','bonus22','bonus23','bonus24','bonus25','bonus26','bonus27','bonus28','bonus29','bonus30',
        'strategy1','strategy2','strategy3','strategy4','strategy5','strategy6','strategy7','strategy8','strategy9','strategy10',
        'strategy11','strategy12','strategy13','strategy14','strategy15','strategy16','strategy17','strategy18','strategy19','strategy20',
        'strategy21','strategy22','strategy23','strategy24','strategy25','strategy26','strategy27','strategy28','strategy29','strategy30',
        'simple1','simple2','simple3','simple4','simple5','simple6','simple7','simple8','simple9','simple10',
        'simple11','simple12','simple13','simple14','simple15','simple16','simple17','simple18','simple19','simple20',
        'simple21','simple22','simple23','simple24','simple25','simple26','simple27','simple28','simple29','simple30',
        'cutoff1','cutoff2','cutoff3','cutoff4','cutoff5','cutoff6','cutoff7','cutoff8','cutoff9','cutoff10',
        'cutoff11','cutoff12','cutoff13','cutoff14','cutoff15','cutoff16','cutoff17','cutoff18','cutoff19','cutoff20',
        'cutoff21','cutoff22','cutoff23','cutoff24','cutoff25','cutoff26','cutoff27','cutoff28','cutoff29','cutoff30',
        'fault1','fault2','fault3','fault4','fault5','fault6','fault7','fault8','fault9','fault10',
        'fault11','fault12','fault13','fault14','fault15','fault16','fault17','fault18','fault19','fault20',
        'fault21','fault22','fault23','fault24','fault25','fault26','fault27','fault28','fault29','fault30',
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

    # retain only the session which actually worked:
    df = df[df.session == 'skcucks5']
    print('removing test sessions')
    print('players left =', len(df.code.unique()))

    # hack here to populate the payoff column with the true payoffs
    players = df.code.unique()
    for player in players:
        if df[df.code == player]['payoff'].unique().item() != -2:
            pay = df[df.code == player]['bonus'].sum()
            if pay < -30:
                pay = -30
            idxs = df.index[df.code == player].tolist()
            for idx in idxs:
                df.loc[idx, 'payoff'] = 30 + pay

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

    print('removing', len(quitters), 'quitters')
    # and finaly remove the players:
    for r in quitters:
        df = df.drop(df[df.code == r].index)
    print('players left =', len(df.code.unique()))

    return df


# load datafiles
df_all = pd.DataFrame()
for datafile in datafiles:
    df = pd.DataFrame(pd.read_csv(datafile, low_memory=False))
    df_all = df_all.append(df, sort=True)

df_all = df_all[df_all['session.is_demo'] == 0]

df = make_dataframe(df_all)
# pd.set_option('display.max_columns', None)

# save
# df.to_csv('../data/DTU_allcd.csv')
# df.to_excel('../data/DTU_allcd.xlsx')
df = df.drop(['turker'], 1)
df.to_csv('../data/DTU1_anonymous.csv')
df.to_excel('../data/DTU1_anonymous.xlsx')
