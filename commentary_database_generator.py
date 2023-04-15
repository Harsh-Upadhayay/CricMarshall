from LiveScoreAPI import API_USER, dataExtracter, log
from api_keys import api_keys
import pandas as pd

if __name__ == "__main__":
    
    user = API_USER("2165b51fa1msh36b5c699287ecc8p1990a4jsnf24efe6b66ae")
    api_calls = 0
    20200403
    for date in pd.date_range(start='03/04/2020', end='1/03/2023').strftime('%Y%m%d').tolist():
        # try : 
        print(date)
        EidDump = user.reqEidByDate(date)
        print(EidDump)
        api_calls += 1
        extr = dataExtracter(EidDump)
        matchList = extr.extEid()
        extr.saveEid()

        # except Exception as E :
        #     log(date, E)

        for match in matchList :

            try : 
                print(match)
                dump = user.reqCommentary(match['Eid'])
                if len(dump) == 0:
                    continue
                api_calls += 1
                
                extr = dataExtracter(dump)
                extr.saveComm()

            except Exception as E :
                
                log(match['Eid'], E)
            

            if api_calls > 3000:

                log(date, "stopped_here")
                exit()
