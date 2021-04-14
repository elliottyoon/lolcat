import json
import os
import requests
# imports gui dependencies
from tkinter import *
# imports file dialog module
from tkinter import filedialog


def translation():
    # imports the translation key thingy
    url = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
    resp = requests.get(url)
    lolDict = json.loads(resp.text)

    #with open('lolDict.json') as json_file:
    #    lolDict = json.load(json_file)
    filename = filedialog.askopenfilename(initialdir = "~", title = "Select a file", filetypes = [("Text files", "*.txt")])
    #filePath = input("enter .txt filepath here: ")
    file = open(filename, "r")
    original_file = file.readlines()
    original_file[0:15]

    # create new file name
    newFilePath = filename.replace(".txt", "_lolcat.txt")
    new_file_to_save = open(newFilePath, "w")


    def replace_words(some_text):
        splits = some_text.split()
        for split in splits:
            splitNoReturn = split.replace("\n", "")
            if splitNoReturn in lolDict:
                some_text = some_text.replace(splitNoReturn, lolDict[splitNoReturn])

        new_file_to_save.write(some_text)

    for row in original_file:
        replace_words(row)

    label_file_explorer.configure(text="File Translated: "+newFilePath)

# arbitrary filepath
filename = ""


# Creates root window
window = Tk()

# Set window title
window.title('lolspeak Translator')

# Set window size
window.geometry("500x500")

# Create file explorer label
label_file_explorer = Label(window, text="Choose a file!", width = 100, height=4)

# Creates translation button
button_translate = Button(window, text="Translate your file!", command=translation)

# Displays the buttons and labels
label_file_explorer.grid(column=0, row=0)
button_translate.grid(column=0, row=2)

# Actually creates the window
window.mainloop()