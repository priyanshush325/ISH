import argparse, requests, sys
from bs4 import BeautifulSoup
from time import sleep

languageCodes = {
    "Amharic": "am",
    "Arabic": "ar",
    "Basque": "eu",
    "Bengali": "bn",
    "Portuguese": "pt",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish":  "fi",
    "French": "fr",
    "German": "de",
    "Gujarati": "gu",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Norwegian": "no",
    "Polish": "pl",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Chinese-Simplified": "zh-CN",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Chinese-Traditional": "zh-TW",
    "Turkish": "tr",
    "Urdu": "ur",
    "Ukranian": "uk",
    "Vietnamese": "vi",
    "Welsh": "cy"
}

def readCSV(filepath):
    output = []
    with open(filepath, 'r') as file: 
        for line in file:
            value = line.split(',')
            if value[1].endswith('\n'):
                value[1] = value[1][:-1]
            output.append(value)
    return output

def processText(text):
    processedText = text.replace(" ", "%20")
    return processedText

def urlGenerator(sourceLang, translateLang, formattedText):
    base = "https://translate.google.com/?"
    code1 = languageCodes.get(sourceLang)
    code2 = languageCodes.get(translateLang)
    if code1 is None:
        print("Error: language " + sourceLang + " is not currently supported by the script. ")
        sys.exit()
    if code2 is None:
        print("Error: language " + translateLang + " is not currently supported by the script.")
        sys.exit()
    base += "sl=" + code1 + "&tl=" + code2 + "&text=" + formattedText + "&op=translate"
    return base

def getTranslation(url):
    raw = requests.get(url).text
    processed = BeautifulSoup(raw, 'lxml')
    divs = processed.find_all("div")
    for div in divs:
        print(div)
    #container = processed.find("div", class_="OPPzxe")
    #translationContainer = processed.find("c-wiz", class_ = "sciAJc")
    # translationBox = processed.find("div", class_ = "usGWQd")
    # nextBox = translationBox.find("div", class_ = "KkbLmb")
    # print(nextBox)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", dest="file_path", required=True)
    parser.add_argument("-o", "--output", action ="store", dest="output_path", required=True)
    parser.add_argument("langs", action="store", nargs = 2)

    args = parser.parse_args()
    filepath = args.file_path
    output = args.output_path
    languages = args.langs

    # parsedFile = readCSV(filepath)
    # outputFile = open(output, 'w')
    # for entry in parsedFile: 
    #     outputFile.write(entry[0] + ": " + entry[1])

    #formatted = processText("Hello World!")
    #url = urlGenerator(languages[0], languages[1], formatted)
    parsedInput = readCSV(filepath)
    outputFile = open(output, 'w')
    for entry in parsedInput:
        outputFile.write(entry[0] + "," + urlGenerator(languages[0], languages[1], processText(entry[1])) + '\n')
        #print(entry)
    getTranslation("https://translate.google.com/?sl=en&tl=ru&text=hello&op=translate")

if __name__ == "__main__":
    main()
