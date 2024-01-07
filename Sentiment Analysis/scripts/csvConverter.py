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

def convert2(filepath):
    outputPath = filepath[:-3] + "json"
    id = 0
    output = open(outputPath, 'w')
    output.write("[\n")
    for text in getText(filepath):
        output.write("{\n")
        output.write("\t\"text\": " + '"' + text.strip() + '",\n')
        output.write("\t\"id\": " + str(id) + "\n")
        output.write("},\n")
        id = id + 1


    



convert2("test2.csv")