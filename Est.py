# EST V3 - Originally developed in 2015, currently being remade in 2018
import Notes
import random

# Command phrases
creationPhrases = ["create", "add", "make"]
destructionPhrases = ["destroy", "delete", "remove", "discard"]
editPhrases = ["edit", "change", "redo"]
viewPhrases = ["see", "view", "look", "look at", "show"]

# Non-command phrases
greetingPhrases = ["Hello", "Good Day", "Welcome Back", "Welcome", "Hey!"]
partingPhrases = ["Goodbye", "See you soon", "Farewell"]

print("EST: " + greetingPhrases[random.randint(0, 4)])
userInput = input("Input: ")

if userInput.__contains__("note") or userInput.__contains__("notes"):
    # If the user said "note" then they will likely want to make a command in the notes module
    split_input = userInput.split(' ')
    for word in split_input:
        if creationPhrases.__contains__(word):
            Notes.CreateNote()
        elif viewPhrases.__contains__(word):
            Notes.ViewNotes()
        elif destructionPhrases.__contains__(word):
            Notes.DeleteNotes()