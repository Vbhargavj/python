from pydub import AudioSegment
from pydub.effects import equalize

audio=AudioSegment.from_file("input.mp3")

def equlizer():
    global audio
    equalizer_settings = [
        (32, 10),   # Increase by 10 dB at 32 Hz
        (64, 5),    # Increase by 5 dB at 64 Hz
        (128, 3),   # Increase by 3 dB at 128 Hz
        (256, 2),   # Increase by 2 dB at 256 Hz
        (512, 1),   # Increase by 1 dB at 512 Hz
    ]
    audio = equalize(audio, equalizer_settings)
    audio.export("bass.mp3",format="mp3")
    
if __name__ == "__main__":
    equlizer()