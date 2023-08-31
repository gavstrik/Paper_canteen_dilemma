import pandas as pd

"""
combining all three datasets into one
"""

datafile_AMT = '../data/MTurk_anonymous.xlsx'
datafile_DTU1 = '../data/DTU1_anonymous.xlsx'
datafile_DTU2 = '../data/DTU2_anonymous.xlsx'

# main code
df_AMT = pd.DataFrame(pd.read_excel(datafile_AMT))
df_DTU1 = pd.DataFrame(pd.read_excel(datafile_DTU1))
df_DTU2 = pd.DataFrame(pd.read_excel(datafile_DTU2))

df_AMT['exp'] = "AMT"

