import whisper
model = whisper.load_model("base")
result = model.transcribe("/Users/priyanshusharma/VSCode Projects/research/transcription/inputs/videoplayback.mp4", verbose = True)
print(result["text"])