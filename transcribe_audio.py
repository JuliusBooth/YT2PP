import whisper_timestamped as whisper

# can test with tiny.en to be faster
model = whisper.load_model("medium.en", device="cpu")

def transcribe_audio(mp3_path):
    audio = whisper.load_audio(mp3_path)
    return whisper.transcribe(model, audio)

def get_timestamps(mp3_path):
    transcript = transcribe_audio(mp3_path)
    segments = transcript["segments"]
    timestamps = [[segment["text"], segment["start"], segment["end"]] for segment in segments]
    return timestamps

def get_text(mp3_path):
    transcript = transcribe_audio(mp3_path)
    return transcript["text"]
