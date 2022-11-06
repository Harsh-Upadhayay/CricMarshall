from timefhuman import timefhuman
import nltk
from nltk.corpus import stopwords 
from QueryProcessor import QueryProcessor 
import spacy
import calendar

nlp = spacy.load('en_core_web_sm')
qp = QueryProcessor()

"""
Function to extract the proper nouns 
NN    noun, singular ‘table’
NNS   noun plural ‘undergraduates’
NNP   proper noun, singular ‘Rohan'
NNPS  proper noun, plural ‘Indians’
"""

def formatDate(dt):
    dt = dt[0].split()
    dt.sort()

    monthMap = ({month: index for index, month in enumerate(calendar.month_name) if month})
    monthMap.update({month: index for index, month in enumerate(calendar.month_abbr) if month})
    for x in monthMap:
        if len(str(monthMap[x])) == 1 :
            monthMap[x] = '0' + str(monthMap[x])
        else :
            monthMap[x] = str(monthMap[x])
    
    if(len(dt) == 1):
        return dt[0]

    elif(len(dt) == 2):
        dt[1] = monthMap[dt[1]]
        return '-'.join(dt)

InputProperNouns = []


def ProperNounExtractor(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP': 
                InputProperNouns.append(word)


def NameEntityRecognition(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    return ents
    
InputTeams = []  # list of input teams
InputPlayers = []   # list of input players
InputEvent = [] # list of input events: world cup, asia cup etc
InputDates = [] # list of input dates

def tag_entities(NER):
    teams = qp.getAllTeams()
    for e in NER:
        if e[3] == 'PERSON':
            InputPlayers.append(e[0])
        if e[3] == 'EVENT':
            InputEvent.append(e[0])
        if e[3] == 'DATE':
            InputDates.append(e[0])
        for i in teams:
            if e[0] == i:
                InputTeams.append(e[0])

    return (InputTeams, InputPlayers, InputEvent, InputDates)

def StepOne(text):
    tokens = nltk.sent_tokenize(text)
    wordToken = nltk.word_tokenize(text)   
    entities = NameEntityRecognition(text)
    tagged_entities = tag_entities(entities)
    return tagged_entities
    
if __name__ ==  "__main__":
    query = "how many runs did Rohit Sharma scored in Rajisthan royals vs Royal challengers banglore in 2020 in Asia cup"
    team, player, comp, date = (StepOne(query))
    print(qp.matchByDateN2Teams(formatDate(date), team[0], team[1]))