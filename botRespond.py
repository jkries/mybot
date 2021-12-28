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
    exactCount = 0
    comeBacks = []
    exactReply = []
    exactMatch = .9
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
                if checkMatch >= exactMatch:
                    exactCount += 1
                    exactReply.append(botReply)
                    print("Likely match: " + userText)
                    print("Match is: " + str(checkMatch))
                elif checkMatch >= confidenceLevel:
                    successCount += 1
                    comeBacks.append(botReply)
                    print("Possible match: " + userText)
                    print("Match is: " + str(checkMatch))
    if exactCount >= 1:
        botResponsePick = random.choice(exactReply)
    elif successCount >= 1:
        botResponsePick = random.choice(comeBacks)
    else:
        botResponsePick = "IDKresponse"
    return botResponsePick
