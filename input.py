from socket import timeout
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import outputGenerator
from inputParsing import InputParser

r = sr.Recognizer()
ip = InputParser()

with sr.Microphone() as source:
    print("say Something")
    # read the audio data from the default microphone
    r.adjust_for_ambient_noise(source)

    # audio_data = r.record(source, duration = 1)

    audio_data = r.listen(source)
    # convert speech to text  

    text = r.recognize_google(audio_data)
    # text = "how many runs did Rohit scored in India versus Australia match on 16 November 2016"
    print(text)
    if(text == "wake up Marshal" or text == "wakeup Marshal" or text == "wake up Marshall" or text == "wakeup Marshall"):
        outputGenerator.WakeUp()
    elif(text == "hello Marshall" or text == "hello"):
        outputGenerator.IntroMessage()
    elif(text == "thank you" or text == "thankyou Marshal"):
        outputGenerator.myPleasure()
        exit()
    else:
        ip.parseQuery(text)

    while(text != "thankyou Marshal" or text != "thank you"):
        with sr.Microphone() as source:
            print("say Something")
            # read the audio data from the default microphone
            r.adjust_for_ambient_noise(source)
            # audio_data = r.record(source, duration = 1)
            audio_data = r.listen(source)
            # convert speech to text  
            text = r.recognize_google(audio_data)
            print(text)
            if(text == "wake up Marshal" or text == "wakeup Marshal" or text == "wake up Marshall" or text == "wakeup Marshall"):
              outputGenerator.AlreadyWakeUp()
            elif(text == "hello Marshall" or text == "tell me something about yourself"):
                outputGenerator.IntroMessage()
            elif(text == "thank you"):
                outputGenerator.myPleasure()
                break
            else:
                ip.parseQuery(text)