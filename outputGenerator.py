import pyttsx3

engine = pyttsx3.init()


def WakeUp():
    WakeUpMessage = "Marshall Never Sleep."
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 190)
    engine.say(WakeUpMessage)
    engine.runAndWait()

def AlreadyWakeUp():
    WakeUpMessage = "Marshall is not sleeping"
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 190)
    engine.say(WakeUpMessage)
    engine.runAndWait()

def IDontKnow():
    WakeUpMessage = "Sorry, I am unable to fetch result. can you please tell me more what you exactly want ?"
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 190)
    engine.say(WakeUpMessage)
    engine.runAndWait()

# Program to see the available languages
# voices = engine.getProperty('voices')
# for voice in voices: 
#     print("Voice:") 
#     print(" - ID: %s" % voice.id) 
#     print(" - Name: %s" % voice.name) 
#     print(" - Languages: %s" % voice.languages) 
#     print(" - Gender: %s" % voice.gender) 
#     print(" - Age: %s" % voice.age)

#Copy the ‘id’ of the language that you want to use, and let’s paste it into our program. We are using setProperty method to define the spoken language.

def IntroMessage():
    test = "Hello, My Name is Marshall. I know everything about Cricket. You can ask me anything."
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 190)
    engine.say(test)
    engine.runAndWait()

