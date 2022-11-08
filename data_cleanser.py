
import os
import pandas as pd
from QueryProcessor import QueryProcessor 
import pickle as pk
import ast



# Emmission matrix 
# df = pd.read_csv("database/playerTeams.csv", index_col=0)
# df['Total Matches'] = df.sum(axis=1)
# print(df.loc['V Kohli']['Total Matches'])
# df = df.div(df['Total Matches'], axis=0)
# print(df.loc['V Kohli']['Royal Challengers Bangalore'])
# df.to_csv("EmmissionMatrix.csv", index=False)

# dl = pk.load(file)# print(dl)

# create playerTeams.csv 

# directory = r'C:\Users\Harsh Upadhayay\Documents\CricMarshall\database\csv_dataset'

# playerTeams = dict()

# allteams = qp.getAllTeams()
# playerTeams = pd.DataFrame(columns = allteams)
# for filename in os.scandir(directory):
#     if filename.is_file() and '_scorecard' in filename.name:
#         df = pd.read_csv(filename.path, index_col=0)
#         for idx, row in df.iterrows():
#             try:
#                 playerTeams.loc[row['name']][row['team']] += 1
#             except:
#                 playerTeams.loc[row['name']] = [0] * len(allteams)
#                 playerTeams.loc[row['name']][row['team']] = 1

# playerTeams.to_csv('t.csv')


# Vectorizing emmission matrix of players 
# players = self.teams_df.index
# teams = self.teams_df.columns

# for team in teams:
#     for player in players:
#         if self.teams_df.loc[player][team] != 0:
#             if player in self.playerTeams:
#                 self.playerTeams[player].append(team)
#             else:
#                 self.playerTeams[player] = [team]

