
import moviepy.editor as mp

def mp4_to_mp3(mp4_path, mp3_path):
    clip = mp.VideoFileClip(mp4_path)
    clip.audio.write_audiofile(mp3_path)
    return

def trim_audio(audio_path, start_time, end_time):
    clip = mp.AudioFileClip(audio_path)
    new_clip = clip.subclip(start_time, end_time)
    new_clip.write_audiofile("trimmed_audio.mp3")
    return
