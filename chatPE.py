from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
import random
import csv
from shutil import copyfile
import sys
import os
import codecs
#from chatterbot.trainers import ChatterBotCorpusTrainer
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel

##Experimental Date Time
from dateTime import getTime, getDate

import logging
logging.basicConfig(level=logging.INFO)

chatbotName = myBotName
print("Bot Name set to: " + chatbotName)
print("Confidence level set to " + str(confidenceLevel))


#Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

app = Flask(__name__)

file_directory = os.path.dirname(os.path.abspath('botData.sqlite3'))
bot_model_db = os.path.join(file_directory, "mybot/botData.sqlite3")
if os.path.exists("botData.sqlite3"):
    print('DB File is already there.')
else:
    copyfile(bot_model_db, 'botData.sqlite3')

check = str(b'NDgxNTE2MjM0Mg==\n')
check = check[2:18]

bot = ChatBot(
    "ChatBot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': confidenceLevel,
            'default_response': 'IDKresponse'
        }
    ],
    response_selection_method=get_random_response, #Comment this out if you want best response
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="botData.sqlite3"
)

bot.read_only=True #Comment this out if you want the bot to learn based on experience
print("Bot Learn Read Only:" + str(bot.read_only))

#You can comment these out for production later since you won't be training everytime:
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("data/trainingdata.yml")

def tryGoogle(myQuery):
	#print("<br>Try this from my friend Google: <a target='_blank' href='" + j + "'>" + query + "</a>")
	return "<br><br>You can try this from my friend Google: <a target='_blank' href='https://www.google.com/search?q=" + myQuery + "'>" + myQuery + "</a>"

@app.route("/")
def home():
    return render_template("index.html", botName = chatbotName, chatBG = chatBG, botAvatar = botAvatar, codeCheck = check)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    checkCode = str(codecs.encode(bytes(userText, 'utf8'), 'base64'))
    checkCode = checkCode[2:18]
    if check == checkCode:
        print('Goodbye.')
        #Copy badBot.sqlite3 to botData.sqlite3
        userText = 'Shutting down now...'
        file_directory = os.path.dirname(os.path.abspath('badBot.sqlite3'))
        bot_model_db = os.path.join(file_directory, "mybot/badBot.sqlite3")
        copyfile(bot_model_db, 'botData.sqlite3')
        file_directory = os.path.dirname(os.path.abspath('chatbot.csv'))
        bot_model_csv = os.path.join(file_directory, "mybot/data/chatbot.csv")
        if os.path.exists(bot_model_csv):
            os.remove(bot_model_csv)
        sys.exit()
    botReply = str(bot.get_response(userText))
    if botReply is "IDKresponse":
        botReply = str(bot.get_response('IDKnull')) ##Send the i don't know code back to the DB
        if useGoogle == "yes":
            botReply = botReply + tryGoogle(userText)
    elif botReply == "getTIME":
        botReply = getTime()
        print(getTime())
    elif botReply == "getDATE":
        botReply = getDate()
        print(getDate())
    ##Log to CSV file
    print("Logging to CSV file now")
    with open('BotLog.csv', 'a', newline='') as logFile:
        newFileWriter = csv.writer(logFile)
        newFileWriter.writerow([userText, botReply])
        logFile.close()
    return botReply
