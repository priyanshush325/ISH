import json
import csv

def formatter(sentiments, texts, output):
    sentimentFile = csv.DictReader(open(sentiments, 'r'))
    sentimentDict = []
    for col in sentimentFile:
        sentimentDict.append(col['sentiment'])
    textsFile = json.load(open(texts, 'r'))
    outputFile = open(output, 'w')
    outputFile.write("id,text,sentiment\n")
    for text in textsFile:
        outputFile.write(str(text["id"]) + ',"' + text["text"][:-1] + '",' + sentimentDict[text["id"]] + "\n")


formatter("../output/output.csv", "../input/data.json", "formattedOutput.csv")
