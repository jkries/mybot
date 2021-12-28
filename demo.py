#! /usr/bin/python3
from flask import Flask, render_template, request
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel
from botRespond import getResponse

##Experimental Date Time
from dateTime import getTime, getDate

app = Flask(__name__)

chatbotName = 'Demo ChatBot'
botAvatar = '/static/bot.png'

@app.route("/")
def home():
    return render_template("index.html", botName = chatbotName, botAvatar = botAvatar)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    noResponse = ["I don't know.", "I'm not sure about that.", "Is there a different way you can ask that?","I don't have a response for that.","I will have to give that some thought.","I don't really know what you are asking."]
    if botReply is "IDKnull":
        botReply = random.choice(noResponse)
    return botReply

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)
