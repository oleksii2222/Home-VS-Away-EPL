# -------DESCRIPTIVE ANALYSIS OF EPL FOR 5 seasons---------
from epl import EPL
import pandas as pd
import numpy as np
# -------------EPL columns-----------
# Index(['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG',
#    'HTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC',
#    'HY', 'AY', 'HR', 'AR', 'Total_goals', 'season'],


# --------Average variables per match in EPL----------
avg_goals = EPL['Total_goals'].mean().round(2)
avg_goals = pd.DataFrame([{'season': 'total', 'avg_goals': avg_goals}])
avg_goals_seasons = EPL.groupby('season', as_index=False).agg(
    avg_goals=('Total_goals', 'mean')).round(2)

avg_goals = pd.concat([avg_goals_seasons, avg_goals])

print(avg_goals)
