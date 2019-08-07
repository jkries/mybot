#! /usr/bin/python3

#from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#For getting the spreadsheet data from csv
import os
import csv
import sys

import logging
logging.basicConfig(level=logging.INFO)

print('Do you want train your bot using recent conversation logs?')
userConfirm = input('Press y or n: ')

if(userConfirm != "y" and userConfirm != "Y"):
    print('Now exiting log training mode...')
    sys.exit()

with open('BotLog.csv') as g:
    lines = csv.reader(g)
    for line in lines:
        userText = line[0]
        botReply = line[1]
        print('##################################################')
        print('User said: ' + userText)
        print('Bot replied: ' + botReply)
        print('##################################################')
        print('To add/ retrain, type the new response, then press Enter.')
        print('To keep/ignore this response, press enter')
        print('##################################################')
        updateResponse = input('Update Response: ')
        if(updateResponse != ""):
            with open('data/chatbot.csv', 'a', newline='') as logFile:
                newFileWriter = csv.writer(logFile)
                newFileWriter.writerow([userText, updateResponse])
                logFile.close()

lineCount = 0
with open('data/trainingdata.yml', 'w') as f:
    f.write("categories:\r\n")
    f.write("- Conversations")
    f.write("\r\nconversations:")
    with open('data/chatbot.csv') as g:
        lines = csv.reader(g)
        for line in lines:
            lineCount += 1
            if lineCount > 1:
                f.write("\r\n- - " + line[0])
                f.write("\r\n  - " + line[1])

print("I have successfully imported " + str(lineCount) + " rows of info and will now retrain...")

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

print('##################################################')
print("I am all trained up and ready to chat!")
print("If on PythonAnywhere, run this command: cp botData.sqlite3 ../botData.sqlite3")
print('##################################################')

print('Shall I delete the recent conversation logs?')
userConfirm = input('Press y or n: ')

if(userConfirm != "y" and userConfirm != "Y"):
    print('Now exiting log training mode...')
    sys.exit()
else:
    if os.path.exists("BotLog.csv"):
        os.remove("BotLog.csv")
        print("I removed the recent chat logs.")
