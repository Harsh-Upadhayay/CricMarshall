import pandas as pd
from timefhuman import timefhuman as th
from datetime import datetime
from ErrorCodes import ErrorCodes as EC

class QueryProcessor() :

    id_df = pd.DataFrame()

    def __init__(self): 
        self.id_df = pd.read_csv("database/match_id.csv")
        self.teams_df = pd.read_csv("database/playerTeams.csv")
        
    def matchByDateN2Teams(self, dt, tm1, tm2):
        return (self.id_df[(self.id_df['date'].str.contains(dt) & self.id_df['teams'].str.contains(tm1) & self.id_df['teams'].str.contains(tm2))] )

    def filterByGender(self, df, gen) :
        return df[df['type'] == gen]
    
    def getAllTeams(self) :
        teams = set()
        tmp = self.id_df['teams'].to_list()
        for x in tmp :
            a, b = x.split(' vs ')
            teams.add(a)
            teams.add(b)
        return list(teams)

    def runWicketByPlayer(self, matchID, player, req):
        df = pd.read_csv("database/csv_dataset/" + str(matchID) + "_scorecard.csv", index_col=0)
        try :
            return df.loc[player][req]
        except:
            return EC.PLAYER_DIDNT_PLAYED

    def teamByPlayerNoppTeam(self, player, oppTeam):
        pass

if __name__ == "__main__":
    qp = QueryProcessor()
    # print((qp.filterByGender(qp.matchByDateN2Teams('2010-', 'India', 'Sri Lanka'), 'male')))