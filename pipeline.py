from getmp3 import mp4_to_mp3
from transcribe_audio import transcribe_audio, get_timestamps, get_text
import os
import pickle
from process_audio_data import get_lecture_bullets
from power_point_maker import create_presentation
from youtube_downloader import download_audio

if not os.path.exists('audio'):
    os.makedirs('audio')

if not os.path.exists('power_points'):
    os.makedirs('power_points')

if not os.path.exists('pickles'):
    os.makedirs('pickles')

if not os.path.exists("image"):
    os.makedirs("image")

def youtube_to_powerpoint(title, url):
    mp3_file = download_audio(title, url)
    pickle_file_name = f'pickles/{title}_text.pickle'
    if not os.path.exists(pickle_file_name):
        text = get_text(mp3_file)
        with open(pickle_file_name, 'wb') as handle:
            pickle.dump(text, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open(pickle_file_name, 'rb') as handle:
            text = pickle.load(handle)
    lecture_bullets = get_lecture_bullets(text)
    create_presentation(title, lecture_bullets)

if __name__ == "__main__":
    pp_title = "mike cassidy"
    video_url = "https://www.youtube.com/watch?v=grJ0FbpfvOw"
    youtube_to_powerpoint(pp_title, video_url)
