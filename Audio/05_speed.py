from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")


def speeed():
    global audio
    s=int(input("Ente the speed up"))
    
    su=audio.speedup(s)
    su.export("speedup.mp3",format="mp3")
# not work
    # sd=audio.set_frame_rate(audio.frame_rate/s)
    # sd.export("speeddown.mp3",format="mp3")
if __name__ == "__main__":
    speeed()
