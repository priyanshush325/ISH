import requests
import json
import os
from bs4 import BeautifulSoup
from time import sleep

def urlGenerator(word, year):
    base = "https://books.google.com/ngrams/graph?content="
    
    base += word

    #All the words have been added to url, append year
    base += "&year_start=" + year

    #All the words and year have been appended, append graph settings
    base += "&year_end=2019&corpus=en-2019&smoothing=0"
    return base

def scrape(url):
    raw = requests.get(url).text
    processed = BeautifulSoup(raw, 'lxml')

    #Gets json data of frequencies from script attribute
    rawData = processed.find('script', type='application/json').text
    processedData = rawData[1:]
    processedData = processedData[:-1]
    #print(processedData)
    jsonData = json.loads(processedData)

    #Return frequency value for the first year
    return jsonData['timeseries'][0]

    #for script in processed.find_all('script', type='application/json'):
        #print(script.string)

def get(filepath):
    output = []
    with open(filepath,'r') as file:
        #To read individual words from txt file (separated by line)
        for line in (file):
            if (line[len(line)-1]) == '\n':
                output.append(line[:-1])
            else:
                output.append(line)
    return output

def getFrequencies(words, years, outputName):
    fileWrite = open(outputName + ".txt", 'w')
    for x in range(len(words)):
        word = words[x]
        year = years[x]
        print("Getting " + word + " for year " + year)
        frequency = (scrape(urlGenerator(word, year)))
        append = word + "_" + year + ": " + str(frequency) + "\n"
        fileWrite.write(append)
        print("Pausing before next request...")
        sleep(3)

words = get("epistemicWords.txt")
years = get("epistemicYears.txt")

getFrequencies(words, years, "epistemicFrequencies")