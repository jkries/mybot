#! /usr/bin/python3

#from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#For getting the spreadsheet data from csv
import os
import csv

import logging
logging.basicConfig(level=logging.INFO)

lineCount = 0
successCount = 0
emptyCount = 0
with open('data/trainingdata.yml', 'w') as f:
    f.write("categories:\r\n")
    f.write("- Conversations")
    f.write("\r\nconversations:")
    with open('data/chatbot.csv') as g:
        lines = csv.reader(g)
        for line in lines:
            lineCount += 1
            if not line[0] or not line[1]:
                emptyCount += 1
                print("WARNING: I had to skip row #" + str(lineCount) + " due to missing data.")
            if lineCount > 1 and line[0] and line[1]:
                successCount += 1
                f.write("\r\n- - " + line[0])
                f.write("\r\n  - " + line[1])

print("==============================================")
print("There are " + str(lineCount - 1) + " rows in chatbot.csv")
print("==============================================")
print("There were " + str(emptyCount) + " empty cells that I could not use for training.")
print("==============================================")
print("I have successfully imported " + str(successCount) + " rows of info and will now retrain...")
print("==============================================")

if os.path.exists("botData.sqlite3"):
    os.remove("botData.sqlite3")
    print("Clearing my old training data.")

bot = ChatBot(
    "Chat Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="botData.sqlite3"
)

#You can comment these out for production later since you won't be training everytime:
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("data/trainingdata.yml")

print("I am all trained up and ready to chat!")
print("If on PythonAnywhere, run this command: cp botData.sqlite3 ../botData.sqlite3")
