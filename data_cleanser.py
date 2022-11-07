
import os
import pandas as pd
from QueryProcessor import QueryProcessor 
qp = QueryProcessor()
 
directory = r'C:\Users\Harsh Upadhayay\Documents\CricMarshall\database\csv_dataset'

playerTeams = dict()

allteams = qp.getAllTeams()
playerTeams = pd.DataFrame(columns = allteams)
for filename in os.scandir(directory):
    if filename.is_file() and '_scorecard' in filename.name:
        df = pd.read_csv(filename.path, index_col=0)
        for idx, row in df.iterrows():
            try:
                playerTeams.loc[row['name']][row['team']] += 1
            except:
                playerTeams.loc[row['name']] = [0] * len(allteams)
                playerTeams.loc[row['name']][row['team']] = 1
                
playerTeams.to_csv('t.csv')