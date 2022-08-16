import os 
import speech_recognition as sr 
import nltk
import datefinder
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()

# Function to extract the proper nouns 

# NN    noun, singular ‘table’
# NNS   noun plural ‘undergraduates’
# NNP   proper noun, singular ‘Rohan'
# NNPS  proper noun, plural ‘Indians’

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
        

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=10)
    # print("Recognizing...")
    # convert speech to text  
    text = r.recognize_google(audio_data)
    # print(text)
    tokens = nltk.sent_tokenize(text)
    wordToken = nltk.word_tokenize(text)   
    # print(wordToken)
    ProperNounExtractor(text)
    dateExtractor(text)