from socket import timeout
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import outputGenerator
import InputParsing

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say Something")
    # read the audio data from the default microphone
    # audio_data = r.record(source, duration = 1)
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source)
    # convert speech to text  
    text = r.recognize_google(audio_data)
    print(text)
    if(text == "wake up Marshal" or text == "wakeup Marshal" or text == "wake up Marshall" or text == "wakeup Marshall"):
        outputGenerator.WakeUp()
    elif(text == "hello Marshall" or text == "hello"):
        outputGenerator.IntroMessage()
    else:
        InputParsing.StepOne(text)