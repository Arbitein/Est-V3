import sqlite3
import Speech

def CreateNote():
    Speech.Say("What is the content of the note?")
    print("EST: What is the content of the note?")
    note = input("Input: ")
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes VALUES ('%s')" % note)
    conn.commit()
    Speech.Say("I have memorised that for you")
    print("EST: I have memorised that for you")
    conn.close()

def ViewNotes():
    index = 0
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    notes = c.execute("SELECT * from notes")
    if notes.__sizeof__() > 0:
        Speech.Say("You have asked me to memorise the following notes")
        print("EST: You have asked me to memorise the following notes:")
        for note in notes:
            index += 1
            Speech.Say("Number " + str(index) + ". " + note[0])
            print(str(index) + ") %s" % note[0])
    else:
        Speech.Say("I have no notes saved in my memory")
        print("EST: I have no notes saved in my memory")
    conn.close()

def DeleteNotes():
    userInput = input("Input: ")
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes where 1=1")
    conn.commit()
    Speech.Say("I have deleted all your notes from my memory")
    print("EST: I have deleted all your notes from my memory")
    conn.close()