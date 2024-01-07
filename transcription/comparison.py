import whisper
import requests

model1 = whisper.load_model("base")
model2 = whisper.load_model("large")

def compare(input, output):
    with open(output, 'w') as file:
        result = model1.transcribe(input, task = "translate")
        file.write(result['text'])
        result2 = model2.transcribe(input, task = "translate")
        file.write("\n---\n")
        file.write(result2['text'])

compare("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/2017-10-09_1158_RU_Первый_Новости_с_субтитрами.mp4", "test1.txt")
compare("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/Putin´s Speech - International Women´s Day (with Russian and English subtitles).mp4", "test2.txt")
compare("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/RUSSIAN SPEECH_ Vladimir Putin - Victory Day (with Russian and English subtitles).mp4", "test3.txt")
compare("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/russian_sample.mp4", "test4.txt")
compare("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/videoplayback.mp4", "test5.txt")