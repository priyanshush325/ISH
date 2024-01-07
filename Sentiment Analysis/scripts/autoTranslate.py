import requests
from googletrans import Translator

translator = Translator()

input = open("/Users/priyanshusharma/VSCode Projects/research/Sentiment Analysis/input/train_splits/1.txt", "r")
data = input.read()
result = translator.translate(data, src = "ru", dest ="en")

with open("1.json", "w") as file:
    file.write(result.text)

