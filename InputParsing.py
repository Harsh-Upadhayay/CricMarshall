import os
import nltk
import datefinder
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

"""
Function to extract the proper nouns 
NN    noun, singular ‘table’
NNS   noun plural ‘undergraduates’
NNP   proper noun, singular ‘Rohan'
NNPS  proper noun, plural ‘Indians’
"""


def ProperNounExtractor(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        # print(tagged)
        for (word, tag) in tagged:
            if tag == 'NNP' or tag == 'NNPS' or tag == 'NN' or tag == 'NNS': 
                print(word)
        
        for(word,tag) in tagged:
            if tag == 'CD':
                print(word)

def dateExtractor(text):
    dates = datefinder.find_dates(text)
    for date in dates:
        print(date)


def StepOne(text):
    tokens = nltk.sent_tokenize(text)
    wordToken = nltk.word_tokenize(text)   
    print(wordToken)
    ProperNounExtractor(text)
    dateExtractor(text)