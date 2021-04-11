import json
import os

# imports the translation key thingy
with open('lolDict.json') as json_file:
    lolDict = json.load(json_file)

filePath = input("enter .txt filepath here: ")
file = open(filePath, "r")
original_file = file.readlines()
original_file[0:15]

# create new file name
newFilePath = filePath.replace(".txt", "_lolcat.txt")
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
