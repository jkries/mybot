from botConfig import confidenceLevel
from difflib import SequenceMatcher
import csv
import random

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getResponse(sendMsg):
    #return "You said: " + sendMsg
    #Loop through CSV knowledge file.  If a question is equal to or greater than the confidence level, add it to a list of possible responses. Then return a random responses
    lineCount = 0
    successCount = 0
    comeBacks = []
    with open('data/chatbot.csv') as g:
        lines = csv.reader(g)
        for line in lines:
            lineCount += 1
            if not line[0] or not line[1]:
                emptyCount += 1
                print("WARNING: I had to skip row #" + str(lineCount) + " due to missing data.")
            if lineCount > 1 and line[0] and line[1]:
                userText = line[0]
                botReply = line[1]
                checkMatch = similar(sendMsg, userText)
                if checkMatch >= confidenceLevel:
                    successCount += 1
                    comeBacks.append(botReply)
                #Better than the confidenceLevel?
                #print("Match is: " + str(checkMatch))
    if successCount >= 1:
        botResponsePick = random.choice(comeBacks)
    else:
        botResponsePick = "IDKresponse"
    return botResponsePick
