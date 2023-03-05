
import requests


class API_USER :

    URL = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/"
    API_KEY = str()
    HOST = "cricbuzz-cricket.p.rapidapi.com"

    def __init__(self, key) :
        
        self.API_KEY = key

        self.header = {
            "X-RapidAPI-Key": self.API_KEY,
            "X-RapidAPI-Host": self.HOST
        }

    def __scoreCardUrl(self, matchID) :
        return self.URL + str(matchID) + "/scard"


    def __commentatoryURL(self, matchID) :
        return self.URL + str(matchID) + "/comm"


    def getScorecard(self, id) :

        response = requests.request("GET", 
                                    self.__scoreCardUrl(matchID=id), 
                                    headers=self.header)

        return response.text

    def getCommentatory(self, id) :

        response = requests.request("GET", 
                                    self.__commentatoryURL(matchID=id), 
                                    headers=self.header)

        return response.text
        

if __name__ == "__main__":

    user = API_USER("f6bfae9f81mshffe4d7e59696e55p194f70jsn129166b51d44")
    
    print(user.getCommentatory(40381))


    