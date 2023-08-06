import pandas as pd

df_premier22 = pd.read_csv('https://football-data.co.uk/mmz4281/2223/E0.csv')

print('==================before ==========>')
print(df_premier22)

df_premier22.rename(columns={'FTHG':'home_goals',
                             'FTAG':'away_goals',
                             'AvgCAHA':'average_something'}, inplace=True)

print('=================after renaming=======>')
print(df_premier22)