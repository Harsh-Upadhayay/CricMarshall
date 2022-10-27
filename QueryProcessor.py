import pandas as pd
from timefhuman import timefhuman as th
from datetime import datetime

class QueryProcessor() :

    id_df = pd.DataFrame()

    def __init__(self): 
        self.id_df = pd.read_csv("dataset/all/match_id.csv")

    def matchByDateN2Teams(self, dt, tm1, tm2):
        return (self.id_df[(self.id_df['date'].str.contains(dt) & self.id_df['teams'].str.contains(tm1) & self.id_df['teams'].str.contains(tm2))] )

    def filterByGender(self, df, gen) :
        return df[df['type'] == gen]
    

if __name__ == "__main__":
    qp = QueryProcessor()
    print((qp.filterByGender(qp.matchByDateN2Teams('2010-', 'India', 'Sri Lanka'), 'male')))