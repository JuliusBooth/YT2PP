from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_audio(title, url):
    audio_file_name = f"audio/{title}.mp3"
    if os.path.exists(audio_file_name):
        return audio_file_name
    youtube = YouTube(url)
    video = youtube.streams.first()
    video_file_name = video.download()
    audio = AudioFileClip(video_file_name)
    audio.write_audiofile(audio_file_name)
    if os.path.exists(video_file_name):
        os.remove(video_file_name)
    return audio_file_name


