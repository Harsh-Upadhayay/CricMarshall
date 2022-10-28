from scorecard_generator import scorecard_generator 
import pandas as pd
from datetime import datetime

logfile = open("log.csv", 'a')

def log(id, msg) :

    cur_time = datetime.now().strftime("%H:%M:%S")
    logline = cur_time + "," + id + "," + msg + "\n" 
    logfile.write(logline)
    

start = datetime.now()

match_ids = pd.read_csv("match_id.csv")['id'].to_list()

for id in match_ids:
    try :
        sg = scorecard_generator(id)
    except Exception as e:
        log(id, str(e))

    print (id)

print ("Execution Time : " , ((datetime.now() - start).__str__()))
logfile.write("Execution Time : "  + ((datetime.now() - start).__str__()))