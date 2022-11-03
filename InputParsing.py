import os
import nltk
import datefinder
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

import spacy
from spacy import displacy
from spacy import tokenizer

nlp = spacy.load('en_core_web_sm')

"""
Function to extract the proper nouns 
NN    noun, singular ‘table’
NNS   noun plural ‘undergraduates’
NNP   proper noun, singular ‘Rohan'
NNPS  proper noun, plural ‘Indians’
"""

InputProperNouns = []
def ProperNounExtractor(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        # print(tagged)
        for (word, tag) in tagged:
            # if tag == 'NNP' or tag == 'NNPS' or tag == 'NN' or tag == 'NNS': 
            #     print(word)
            if tag == 'NNP': 
                InputProperNouns.append(word)
                # print(word)
        
        # for(word,tag) in tagged:
        #     if tag == 'CD':
        #         print(word)
    
    # print(InputProperNouns)

# Inputdates = []
# def dateExtractor(text):
#     dates = datefinder.find_dates(text)
#     for date in dates:
#         Inputdates.append(date)
#         # print(date)

#     # print(Inputdates)


def NameEntityRecognition(text):
    #Load the text and process it
    doc = nlp(text)
    #doc2 = nlp(text2)
    sentences = list(doc.sents)
    # print(sentences)
    # tokenization
    # for token in doc:
    #     print(token.text)
    # print entities
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    print(ents)
    ents
    # print(NER)
    # now we use displaycy function on doc2
    getTeam(ents)
    displacy.render(doc, style='ent', jupyter=True)
    
InputTeams = []  # list of input teams
InputPlayers = []   # list of input players
InputEvent = [] # list of input events: world cup, asia cup etc
InputDates = [] # list of input dates
def getTeam(NER):
    teams = ['Pakistan', 'Middlesex', 'South Africa', 'Zimbabwe', 'Gibraltar', 'China', 'Sylhet Super Stars', 'Kuwait', 'Cumilla Warriors', 'Rwanda', 'Warwickshire', 'Tanzania', 'Loughborough Lightning', 'Royal Challengers Bangalore', 'Khulna Tigers', 'Mali', 'Warriors', 'Kent', 'Panama', 'Cayman Islands', 'Argentina', 'Pune Warriors', 'Sydney Sixers', 'Romania', 'Botswana', 'Spirit', 'Nigeria', 'Guyana', 'Italy', 'Cape Town Blitz', 'Dhaka Dynamites', 'Sapphires', 'Perth Scorchers', 'St Lucia Stars', 'Sylhet Sixers', 'Otago', 'Trinidad & Tobago Red Steel', 'Dhaka Gladiators', 'West Indies', 'Trent Rockets', 'Norway', 'New South Wales', 'Trailblazers', 'Greece', 'Sierra Leone', 'Victoria', 'United States of America', 'Lightning', 'London Spirit', 'Munster Reds', 'Queensland', 'Hungary', 'Colombo Stars', 'Bhutan', 'Barisal Burners', 'Lesotho', 'Trinbago Knight Riders', 'England', 'Peshawar Zalmi', 'Finland', 'Birmingham Phoenix', 'Canterbury', 'St Helena', 'Gujarat Lions', 'Qatar', 'Japan', 'Mumbai Indians', 'Belize', 'Samoa', 'Kandy Warriors', 'Auckland', 'Thailand', 'Lancashire', 'Welsh Fire', 'Israel', 'Chattogram Challengers', 'Khulna Royal Bengals', 'Paarl Rocks', 'Delhi Capitals', 'Barmy Army', 'Fortune Barishal', 'Leinster Lightning', 'Seychelles', 'Comilla Victorians', 'Philippines', 'Khulna Titans', 'Barisal Bulls', 'Northern Districts', 'Northern Diamonds', 'Quetta Gladiators', 'Thunder', 'Impi', 'Lahore Qalandars', 'Isle of Man', 'Northern Superchargers', 'Nottinghamshire', 'Kandy Tuskers', 'Kochi Tuskers Kerala', 'Rajasthan Royals', 'Galle Gladiators', 'Rajshahi Royals', 'Manchester Originals', 'Jamaica', 'Ghana', 'Falcons', 'Oman', 'South East Stars', 'Bahamas', 'Asia XI', 'Africa XI', 'Gambia', 'Croatia', 'Balkh Legends', 'Scotland', 'Rangpur Riders', 'Delhi Daredevils', 'Slovenia', 'Surrey', 'Uganda', 'Knights', 'France', 'Malta', 'Dambulla Giants', 'Oval Invincibles', 'Luxembourg', 'Eswatini', 'Jaffna Kings', 'Hobart Hurricanes', 'Rising Pune Supergiant', 'Bahrain', 'Tornadoes', 'Western Storm', 'Trinidad and Tobago', 'India', 'Rangpur Rangers', 'Islamabad United', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Belgium', 'Jaffna Stallions', 'Australia', 'Nepal', 'Nangarhar Leopards', 'Nelson Mandela Bay Giants', 'Estonia', 'Guyana Amazon Warriors', 'Cameroon', 'Saudi Arabia', 'Malawi', 'Chittagong Kings', 'St Kitts and Nevis Patriots', 'Ireland', 'Gujarat Titans', 'Chittagong Vikings', 'Netherlands', 'Wellington', 'Colombo Kings', 'Kabul Zwanan', 'Lions', 'Indonesia', 'Birmingham Bears', 'Singapore', 'Hong Kong', 'Boland', 'Western Australia', 'Southern Vipers', 'Myanmar', 'Minister Group Dhaka', 'Southern Brave', 'Leicestershire', 'Windward Islands', 'Duronto Rajshahi', 'Sussex', 'Sydney Thunder', 'Malaysia', 'Lucknow Super Giants', 'Hampshire', 'Kenya', 'Swaziland', 'Leeward Islands', 'United Arab Emirates', 'Punjab Kings', 'Portugal', 'Sunrisers', 'Zambia', 'Derbyshire', 'Mozambique', 'Austria', 'Durham', 'Czech Republic', 'Sylhet Thunder', 'Central Districts', 'Antigua Hawksbills', 'Barbados Tridents', 'Glamorgan', 'Central Sparks', 'Barbados', 'Papua New Guinea', 'Brisbane Heat', 'Somerset', 'Canada', 'Warriors (FairBreak)', 'Rising Pune Supergiants', 'ICC World XI', 'Suriname', 'Surrey Stars', 'Iran', 'Namibia', 'Guernsey', 'Tshwane Spartans', 'North West', 'Cape Cobras', 'Adelaide Strikers', 'Northamptonshire', 'Lancashire Thunder', 'Chennai Super Kings', 'Jersey', 'Sweden', 'Bermuda', 'Supernovas', 'Velocity', 'Kandahar Knights', 'Vanuatu', 'Durban Heat', 'Afghanistan', 'Rajshahi Kings', 'Sylhet Royals', 'Tasmania', 'Sri Lanka', 'Titans', 'Melbourne Renegades', 'Germany', 'Yorkshire', 'Denmark', 'St Lucia Zouks', 'St Lucia Kings', 'New Zealand', 'Melbourne Stars', 'Cyprus', 'Serbia', 'Karachi Kings', 'Western Province', 'Barbados Royals', 'Yorkshire Diamonds', 'Brazil', 'Multan Sultans', 'Essex', 'North-West Warriors', 'Turkey', 'Paktia Panthers', 'Spain', 'Bulgaria', 'Northern Knights', 'Deccan Chargers', 'Dhaka Platoon', 'Jozi Stars', 'Bangladesh', 'Fiji', 'Switzerland', 'Jamaica Tallawahs', 'South Australia', 'Sunrisers Hyderabad', 'Sylhet Sunrisers', 'Dambulla Viiking', 'Dolphins', 'Maldives', 'South Korea', 'Worcestershire', 'Cook Islands', 'Gloucestershire']

    for e in NER:
        # print(e)
        # print(e[0])
        if e[3] == 'PERSON':
            InputPlayers.append(e[0])
        if e[3] == 'EVENT':
            InputEvent.append(e[0])
        if e[3] == 'DATE':
            InputDates.append(e[0])
        for i in teams:
            if e[0] == i:
                InputTeams.append(e[0])

    print(InputTeams)
    print(InputPlayers)
    print(InputEvent)
    print(InputDates)

def StepOne(text):
    tokens = nltk.sent_tokenize(text)
    wordToken = nltk.word_tokenize(text)   
    # print(wordToken)
    # ProperNounExtractor(text)
    # dateExtractor(text)
    NameEntityRecognition(text)
    
