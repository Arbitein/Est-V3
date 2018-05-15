import pyttsx

def Say(string):
    engine = pyttsx.init()
    engine.say(string)
    engine.runAndWait()