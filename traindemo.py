#from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.trainers import ChatterBotCorpusTrainer

#For getting the spreadsheet data from csv
import os
import csv

import logging
logging.basicConfig(level=logging.INFO)

lineCount = 0
with open('data/demodata.yml', 'w') as f:
    f.write("categories:\r\n")
    f.write("- Conversations")
    f.write("\r\nconversations:")
    with open('testbot.csv') as g:
        lines = csv.reader(g)
        for line in lines:
            lineCount += 1
            f.write("\r\n- - " + line[0])
            f.write("\r\n  - " + line[1])

print("I have successfully imported " + str(lineCount) + " rows of info and will now retrain...")

if os.path.exists("demoData.sqlite3"):
    os.remove("demoData.sqlite3")
    print("Clearing my old training data.")

bot = ChatBot(
    "Chat Bot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I don\'t have a response for that. What else can we talk about?'
        }
    ],
    response_selection_method=get_random_response, #Comment this out if you want best response
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="demoData.sqlite3"
)

bot.read_only=True #Comment this out if you want the bot to learn based on experience
print("Bot Learn Read Only:" + str(bot.read_only))

#You can comment these out for production later since you won't be training everytime:
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("data/demodata.yml")

print("I am all trained up and ready to chat!")
