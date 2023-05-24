import json
def getText(filepath):
    text = []
    with open(filepath,'r') as file:
        for line in (file):
            text.append(line) 
    return text

def convert(filepath):
    outputPath = filepath[:-3] + "json"
    id = 0
    output = open(outputPath, 'w')
    jsonObject = []
    for text in getText(filepath):
        textEntry = {}
        textEntry["text"] = text
        textEntry["id"] = id
        id += 1
        jsonObject.append(textEntry)
    output.write(str(jsonObject))



convert("data.csv")