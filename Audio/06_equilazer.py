from pydub import audio_segment

audio=audio_segment.from_file("input.mp3")

def equlizer():
    global audio
    audio=audio.equlizer()