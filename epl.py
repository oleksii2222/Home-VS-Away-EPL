import pandas as pd
import numpy as np

# -------------EPL columns-----------
# Index(['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG',
#    'HTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
#    'HY', 'AY', 'HR', 'AR'],

# -------------EPL seasons datasets------------

epl24_25 = pd.read_csv('EPL 24-25.csv')
epl23_24 = pd.read_csv('season-2324.csv')
epl22_23 = pd.read_csv('season-2223.csv')
epl21_22 = pd.read_csv('season-2122.csv')
epl20_21 = pd.read_csv('season-2021.csv')

# !!!! These datasets are already cleaned and taken from https://github.com/datasets/football-datasets


# -----------Merged dataset (Feature Engineering)----------

# Add column season because in merged dataset we will don't see whach year match is it
epl24_25['season'] = '24-25'
epl23_24['season'] = '23-24'
epl22_23['season'] = '22-23'
epl21_22['season'] = '21-22'
epl20_21['season'] = '20-21'

# Merge all in 1 table
EPL = pd.concat([epl20_21, epl21_22, epl22_23, epl23_24, epl24_25])

# Total goals per match
EPL['Total_goals'] = EPL['FTHG'] + EPL['FTAG']


# We got 1900 rows (matches) and 24 columns
EPL.shape

final_dataset = EPL.to_csv('EPL.csv')
