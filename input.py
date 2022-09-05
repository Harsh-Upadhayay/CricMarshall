import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import outputGenerator
import InputParsing

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say Something")
    # read the audio data from the default microphone
    audio_data = r.record(source, duration = 5)
    # convert speech to text  
    text = r.recognize_google(audio_data)
    print(text)
    if(text == "wake up Marshal" or text == "wakeup Marshal"):
        outputGenerator.WakeUp()
    elif(text == "hello Marshall"):
        outputGenerator.IntroMessage()
    else:
        InputParsing.StepOne(text)