import nltk
from nltk.corpus import stopwords 
from QueryProcessor import QueryProcessor 
import spacy
import calendar
from ErrorCodes import ErrorCodes as EC
nlp = spacy.load('en_core_web_sm')

class InputParser :

    def __init__ (self):
        self.qp = QueryProcessor()
        self.teams = set(self.qp.getAllTeams())

        self.monthMap = ({month: index for index, month in enumerate(calendar.month_name) if month})
        self.monthMap.update({month: index for index, month in enumerate(calendar.month_abbr) if month})
        for x in self.monthMap:
            if len(str(self.monthMap[x])) == 1 :
                self.monthMap[x] = '0' + str(self.monthMap[x])
            else :
                self.monthMap[x] = str(self.monthMap[x])


    def parseDate(self, dt):
        dt = dt[0].split()
        dt.sort()
        dt[1] = self.monthMap[dt[1]]
        return '-'.join(dt)

    def parseRequirement(self, nouns):
                    
        required = set(['runs', 'run', 'wickets', 'wicket'])

        for nn in nouns:
            if nn in required:
                return nn
        
        return EC.NO_REQUIREMENT_SPECIFIED

    def properNounExtractor(self, text):
        
        InputProperNouns = []
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            words = [word for word in words if word not in set(stopwords.words('english'))]
            tagged = nltk.pos_tag(words)
            for (word, tag) in tagged:
                if tag == 'NNS': 
                    InputProperNouns.append(word)

        return InputProperNouns
        
    def tag_entities(self, text):
               
        doc = nlp(text)
        entities = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]

        tag = {
            'teams'         : [],
            'player'        : [],
            'event'         : [],
            'date'          : [],
            'requirement'   : []
        }

        for entity in entities:

            if entity[3] == 'PERSON':
                tag['player'].append(entity[0])
            if entity[3] == 'EVENT':
                tag['event'].append(entity[0])
            if entity[3] == 'DATE':
                tag['date'].append(entity[0])
            if entity[0] in self.teams:
                tag['teams'].append(entity[0])

        tag['requirement'] = self.parseRequirement(self.properNounExtractor(text))
        tag['date'] = self.parseDate(tag['date'])
        return tag

    def parseQuery(self, text):

        tagged_entities = self.tag_entities(text)
        return tagged_entities
    
if __name__ ==  "__main__":
    ip = InputParser()
    query = "how many runs did Rohit Sharma scored in India vs Australia in November 2020 in Asia cup"
    print(ip.parseQuery(query))