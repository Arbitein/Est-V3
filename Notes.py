import sqlite3

def CreateNote():
    print("EST: What is the content of the note?")
    note = input("Input: ")
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes VALUES ('%s')" % note)
    conn.commit()
    print("EST: I have memorised that for you")
    conn.close()

def ViewNotes():
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    notes = c.execute("SELECT * from notes")
    if notes.__sizeof__() > 0:
        print("EST: You have asked me to memorise the following notes:")
        for note in notes:
            print(note)
    else:
        print("EST: I have no notes saved in my memory")
    conn.close()

def DeleteNotes():
    print("EST: Do you want me to delete all notes or just one?")
    userInput = input("Input: ")
    if userInput.__contains__("all"):
        conn = sqlite3.connect("memory.db")
        c = conn.cursor()
        c.execute("DELETE FROM notes where 1=1")
        conn.commit()
        print("EST: I have deleted all your notes from my memory")
        conn.close()
    else:
        print("EST: That functionality is not available just yet")