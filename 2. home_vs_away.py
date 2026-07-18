# ---Home VS Away matches, is it real important for more chances for win?

from epl import EPL
import pandas as pd
import numpy as np

# -------------EPL columns-----------
# Index(['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG',
#    'HTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
#    'HY', 'AY', 'HR', 'AR', 'Total_goals', 'season'],


# General analysis of home and away wins

home_away = EPL.groupby('FTR', as_index=False).agg(
    wins=('FTR', 'count'), goals_home_team=('FTHG', 'sum'), goals_away_team=('FTAG', 'sum'))
# #  FTR  wins  goals_home_team  goals_away_team
# 0   A   646              378             1583
# 1   D   433              485              485
# 2   H   821             2106              503

ha_wins_absdiff = home_away.iloc[2, 1] - home_away.iloc[0, 1]
ha_wins_diff = (home_away.iloc[2, 1] /
                home_away.iloc[0, 1] * 100 - 100).round(2)
ha_goals_absdiff = home_away.iloc[2, 2] - home_away.iloc[0, 3]
ha_goals_diff = (home_away.iloc[2, 2] /
                 home_away.iloc[0, 3] * 100 - 100).round(2)

h_avg_goals = home_away.iloc[2, 2] / home_away.iloc[2, 1]
a_avg_goals = home_away.iloc[0, 3] / home_away.iloc[0, 1]
avg_goals_diff = (h_avg_goals - a_avg_goals).round(4)
# Home team have more on 175 - 27,09% wins than away team
# Home teams winners score more goals compare with away team winners (523 goals - 33)
# Home teams winner score average 2,57 goals per match,
# away teams winner score less on 0,1147 goals per match (2,45)


# ------------------Home_away_teams---------------
# !!!!
# We will check most succes teams at home compare away, and away compare with home
# Absolute variables don't show truth, because we have
# strong teams which have more wins in count compare with other teams. Therefore we check % of succes home vs aways matches
# !!!!
# -----------------------------------------------


ha_teams = EPL[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']].copy()
mapping_home = {'H': 'Win', 'A': 'Defeat', 'D': 'Draw'}
mapping_away = {'H': 'Defeat', 'A': 'Win', 'D': 'Draw'}

ha_teams['FTR_home'] = ha_teams['FTR'].map(mapping_home)
ha_teams['FTR_away'] = ha_teams['FTR'].map(mapping_away)

# --Check most succes teams at home and away
home_teams = ha_teams.groupby('HomeTeam', as_index=False).agg(
    wins_home=('FTR_home', lambda x: (x == 'Win').sum()),
    defeat_home=('FTR_home', lambda x: (x == 'Defeat').sum()),
    draw_home=('FTR_home', lambda x: (x == 'Draw').sum()))

# ---------------
away_teams = ha_teams.groupby('AwayTeam', as_index=False).agg(
    wins_away=('FTR_away', lambda x: (x == 'Win').sum()),
    defeat_away=('FTR_away', lambda x: (x == 'Defeat').sum()),
    draw_away=('FTR_away', lambda x: (x == 'Draw').sum()))

ha_final = pd.merge(home_teams, away_teams, how='left',
                    left_on='HomeTeam', right_on='AwayTeam').rename(columns={'HomeTeam': 'Team'}).drop(columns='AwayTeam')

# ----Remove the team that have to less wins overall
ha_final = ha_final[(ha_final['wins_home'] >= 10) |
                    (ha_final['wins_away'] >= 10)]

# ----Create of final dataset of H/A statystics
ha_final['wins_h/a_rate'] = (ha_final['wins_home'] /
                             ha_final['wins_away']).round(2)
ha_final['defeat_h/a_rate'] = (ha_final['defeat_home'] /
                               ha_final['defeat_away']).round(2)
ha_final['draw_h/a_rate'] = (ha_final['draw_home'] /
                             ha_final['draw_away']).round(2)
home_away = ha_final.to_excel('home_away_rate.xlsx', index=False)
home_away
print(ha_final[['Team', 'wins_h/a_rate', 'defeat_h/a_rate', 'draw_h/a_rate']])
print(ha_final.shape)
