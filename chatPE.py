from flask import Flask, render_template, request
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel
from botRespond import getResponse

##Experimental Date Time
from dateTime import getTime, getDate


chatbotName = myBotName
print("Bot Name set to: " + chatbotName)
print("Confidence level set to " + str(confidenceLevel))


#Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

app = Flask(__name__)

def tryGoogle(myQuery):
	#print("<br>Try this from my friend Google: <a target='_blank' href='" + j + "'>" + query + "</a>")
	return "<br><br>You can try this from my friend Google: <a target='_blank' href='https://www.google.com/search?q=" + myQuery + "'>" + myQuery + "</a>"

@app.route("/")
def home():
    return render_template("index.html", botName = chatbotName, chatBG = chatBG, botAvatar = botAvatar, codeCheck = check)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    if botReply is "IDKresponse":
        botReply = str(getResponse('IDKnull')) ##Send the i don't know code back to the DB
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
