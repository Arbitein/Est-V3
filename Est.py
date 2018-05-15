# EST V3 - Originally developed in 2015, currently being remade in 2018
# https://realpython.com/python-speech-recognition/ -> Contains tutorials on the use of speech_recognition
# To do: Add speech synthesizer

import Notes
import Speech
import random
import speech_recognition as sr

# Command phrases
creationPhrases = ["create", "add", "make", "memorise", "remember"]
destructionPhrases = ["destroy", "delete", "remove", "discard", "forget"]
editPhrases = ["edit", "change", "redo"]
viewPhrases = ["see", "view", "look", "look at", "show"]

# Non-command phrases
greetingPhrases = ["Hello", "Good Day", "Welcome Back", "Welcome", "Hey!"]
partingPhrases = ["Goodbye", "See you soon", "Farewell"]

chosenGreeting = greetingPhrases[random.randint(0, 4)]
Speech.Say(chosenGreeting)
print("EST: " + chosenGreeting)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
#print(mic.list_microphone_names()) # Used to list active mics on the system

with mic as source:
    audio = r.listen(source)

userInput = r.recognize_google(audio)
print("You: " + userInput)

if userInput.__contains__("note"):
    # If the user said "note" then they will likely want to make a command in the notes module, using "note" functions
    split_input = userInput.split(' ')
    for word in split_input:
        if creationPhrases.__contains__(word):
            Notes.CreateNote()
        elif viewPhrases.__contains__(word):
            Notes.ViewNotes()
        elif destructionPhrases.__contains__(word):
            Notes.DeleteNotes()

elif userInput.__contains__("notes"):
    # If the user said "notes" then they will likely want to make a command in the notes module, using "notes" functions
    split_input = userInput.split(' ')
    for word in split_input:
        if viewPhrases.__contains__(word):
            Notes.ViewNotes()
        elif destructionPhrases.__contains__(word):
            Notes.DeleteNotes()