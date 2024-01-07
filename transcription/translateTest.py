import whisper
model = whisper.load_model("base")
result = model.transcribe("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/russian_sample.mp4")
print(result['text'])