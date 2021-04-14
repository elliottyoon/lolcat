import json
import os
import requests
# imports gui dependencies
from tkinter import *
# imports file dialog module
from tkinter import filedialog
# imports pillow for the image
from PIL import ImageTk, Image 

def addText(inputText):
    s = display_text.get()
    s += inputText
    display_text.set(s)

def translation():
    # imports the translation key thingy
    url = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
    resp = requests.get(url)
    lolDict = json.loads(resp.text)

    filename = filedialog.askopenfilename(initialdir = "~", title = "Select a file", filetypes = [("Text files", "*.txt")])
    file = open(filename, "r")
    original_file = file.readlines()

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
        addText(some_text)

    for row in original_file:
        replace_words(row)

    label_file_explorer.configure(text="Access translated file at: "+newFilePath)

# arbitrary filepath
filename = ""


# Creates root window
window = Tk()

# Set window title
window.title('lolspeak Translator')

# Set window size
window.geometry("605x1000")

# Set minimum window size
window.minsize(605,680)

# Create file explorer label
label_file_explorer = Label(window, text="Choose a file!", width = 100, wraplength=500, height=4)

# Creates translation button
button_translate = Button(window, text="Translate your file!", command=translation)

# Creates header image
my_image = ImageTk.PhotoImage(Image.open("cat.jpeg"))
imageLabel = Label(image=my_image)

# Creates translation output
label_translationText = Label(window, text="Translation preview below:", pady=20)
display_text = StringVar()
translationText = Label(window, width=590, borderwidth=2, relief = "sunken", wraplength=580, padx=5, pady=10, textvariable=display_text)

# Displays the buttons and labels
imageLabel.pack()
label_file_explorer.pack()
button_translate.pack()
label_translationText.pack(pady=20)
translationText.pack(padx=5, pady=10)

# Actually creates the window
window.mainloop()
