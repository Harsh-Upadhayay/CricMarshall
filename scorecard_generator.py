from math import ceil
import pandas as pd

class scorecard_generator:

    scard_entries = ["name", "team","runs_scored", "balls_played", "fours", "sixes", "strike_rate",
                     "overs_deliverd", "runs_given", "wickets", "no_balls", "wides", "economy"]
    
    scorecard = pd.DataFrame()

    def __init__(self, match_id="64917"):

        df = pd.read_csv("database/csv_dataset/" + match_id + ".csv")

        players = self.__get_players(match_id)
        self.scorecard = pd.DataFrame(columns=self.scard_entries, index=players)
        
        for player in players :       
            for entry in self.scard_entries :
                self.scorecard.loc[player][entry] = self.__get_entry(df, player, entry)

        self.save_scorecard(match_id)
        
    def __get_entry(self, df, player, entry) :
        if entry == "name":
            return player

        elif entry ==  "team":
            return self.countries[player]
        
        elif entry == "runs_scored":
            return df[df['striker'] == player]['runs_off_bat'].agg('sum')
        
        elif entry ==  "balls_played":
            return df[(df['striker'] == player) & (df['wides'] != 1)]['runs_off_bat'].agg('count')
        
        elif entry ==  "fours":
            return (df[(df['striker'] == player) & (df['runs_off_bat'] == 4)]['runs_off_bat'].agg('count'))
        
        elif entry ==  "sixes":
            return (df[(df['striker'] == player) & (df['runs_off_bat'] == 6)]['runs_off_bat'].agg('count'))
        
        elif entry ==  "strike_rate":
            if df[df['striker'] == player]['runs_off_bat'].agg('count') == 0 :
                return 0
            else :
                return ((df[(df['striker'] == player)]['runs_off_bat'].agg('sum')) /
                         df[(df['striker'] == player) & (df['wides'] != 1)]['runs_off_bat'].agg('count')) * 100
        
        elif entry ==  "overs_deliverd":
            return ceil((df[(df['bowler'] == player) & (df['extras'] == 0)]['runs_off_bat'].agg('count')) / 6.0)
        
        elif entry ==  "runs_given":
            return (
              df[(df['bowler'] == player)]['runs_off_bat'].agg('sum') 
            + df[(df['bowler'] == player)]['extras'].agg('sum')
            - df[(df['bowler'] == player)]['byes'].agg('sum') 
            - df[(df['bowler'] == player)]['legbyes'].agg('sum'))
        
        elif entry ==  "wickets":
            return df[((df['bowler'] == player) & (df['wicket_type'] != None))]['wicket_type'].agg('count')
        
        elif entry ==  "no_balls":
            return df[(df['bowler'] == player)]['noballs'].agg('count')
        
        elif entry ==  "wides":
            return df[(df['bowler'] == player)]['wides'].agg('count')
        
        elif entry ==  "economy":
            if ceil((df[(df['bowler'] == player) & (df['extras'] == 0)]['runs_off_bat'].agg('count')) / 6.0)  == 0:
                return 0
            else :
                return (
                df[(df['bowler'] == player)]['runs_off_bat'].agg('sum') 
                + df[(df['bowler'] == player)]['extras'].agg('sum')
                - df[(df['bowler'] == player)]['byes'].agg('sum') 
                - df[(df['bowler'] == player)]['legbyes'].agg('sum')) / ceil((df[(df['bowler'] == player) & (df['extras'] == 0)]['runs_off_bat'].agg('count')) / 6.0)

        
        else:
            return None
         
    def __get_players(self, match_id) :

        col_names = ["1", "2", "3", "4", "5", "6"]
        df = pd.read_csv("database/csv_dataset/" + match_id + "_info.csv", names=col_names)
        
        ndf = pd.DataFrame((df[df['2'] == 'player'][['4', '3']]))
        
        self.countries = pd.Series(ndf['3'].values,index=ndf['4']).to_dict()
        return self.countries.keys()
            
    def save_scorecard(self, match_id) :

        self.scorecard.to_csv("database/csv_dataset/" + match_id + "_scorecard.csv")


if __name__ == "__main__":
    sg = scorecard_generator()