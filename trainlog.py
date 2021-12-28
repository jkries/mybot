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
                #logFile.close()

print('##################################################')
print("I am all trained up and ready to chat!")
print("If on PythonAnywhere, you may need to restart the application.")
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
