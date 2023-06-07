from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")

def gain():
    global audio
    g=int(input("Enter the value of gain"))
    audio=audio.apply_gain(g)
    audio.export("gain.mp3",format="mp3")

if __name__ == "__main__":
    gain()