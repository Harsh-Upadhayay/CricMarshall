
import requests
import pandas as pd
import ast


class API_USER :

    URL = "https://livescore6.p.rapidapi.com/matches/v2/"
    API_KEY = str()
    HOST = "livescore6.p.rapidapi.com"
    queryString = {"Eid":"","Category":"cricket"}
    rootPth = "database/commentary/"

    def __init__(self, key) :
        
        self.API_KEY = key

        self.header = {
            "X-RapidAPI-Key": self.API_KEY,
            "X-RapidAPI-Host": self.HOST
        }

    def __scoreCardUrl(self, matchID) :
        return self.URL + "/scard"

    def __commentaryURL(self, matchID) :
        return self.URL + "get-innings"

    def __eidByDateURL(self) :
        return self.URL + "list-by-date"

    def reqScorecard(self, id) :

        self.queryString["Eid"] = str(id)

        response = requests.request("GET", 
                                    self.__scoreCardUrl(matchID=id), 
                                    headers=self.header,
                                    params=self.queryString)

        return response.text

    def reqCommentary(self, id) :

        self.queryString["Eid"] = str(id)

        try :
            response = ast.literal_eval(open("database/commentary/" + str(id) + ".txt", "r").read())
        except :
            response = requests.request("GET", 
                                    self.__commentaryURL(matchID=id), 
                                    headers=self.header,
                                    params=self.queryString).json()

            open("database/commentary/" + str(id) + ".txt", "w").write(str(response))

        return response

    def reqEidByDate(self, date) :

    
        qryStr = {"Category":"cricket"}
        qryStr.update({"Date" : str(date)})

        response = requests.request("GET", 
                                    self.__eidByDateURL(), 
                                    headers=self.header,
                                    params=self.queryString).json()

        return response


class dataExtracter :

    req = str()
    rootPth = "database/commentary/"

    def __init__(self, req) :

        self.req = req
    
    def extComment(self) :

        self.eid = self.req['Eid'] 
        df = pd.DataFrame(self.req["SDInn"][0]['Com'])
        df.drop(columns=["Aid", "Oid"], inplace=True)
        df.set_index("Ov", inplace=True)
        df.sort_index(ascending=True, inplace=True)

        return ' '.join(df['T'].tolist()), df

    def saveComm(self) :

        comm, commdDF = self.extComment()

        open(self.rootPth + str(self.eid) + '_commentry.txt', 'a').write(comm)
        commdDF.to_csv(self.rootPth + str(self.eid) + '_byballComm.csv')

    def extEid(self) :

        eidList = list()

        for x in ((self.req["Stages"])):
            for y in x['Events']:
                
                eidDict = dict()

                eidDict.update({
                    'Eid' : y['Eid'],
                    'T1' : y['T1'][0]['Nm'],
                    'T2' : y['T2'][0]['Nm']
                })

                eidList.append(eidDict)
                # print (y['Eid'] + ': ' + y['T1'][0]['Nm'] + '  -  ' + y['T2'][0]['Nm'])
    
        return eidList

    def saveEid(self): 

        eidList = self.extEid()

        df = pd.DataFrame(eidList)

        df.to_csv(self.rootPth + 'match_id.csv', mode='a', index=False, header=False)


def log(id, msg) :

    f = open('database/commentary/log.txt', 'a')
    f.write(id + ' : ' + str(msg) + '\n')

    f.close()

if __name__ == "__main__":

    user = API_USER("2165b51fa1msh36b5c699287ecc8p1990a4jsnf24efe6b66ae")
    
    date = "20200304"
    
    x = user.reqEidByDate(20200304)
    print(x)