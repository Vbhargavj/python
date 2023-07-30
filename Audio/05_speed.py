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
def speedd():
    
    audio = AudioSegment.from_file("input.mp3")
    slowed_down = audio._spawn(audio.raw_data, overrides={
        # Adjust the speed factor as needed
        "frame_rate": int(audio.frame_rate * 0.8)
    })
    slowed_down = slowed_down.set_frame_rate(audio.frame_rate).speedup(1.3)
    slowed_down.export("ot.wav", format="wav")
    
def rev():
    global audio
    # s = int(input("Ente the speed up"))
    print(audio.frame_rate)
    su = audio.remove_dc_offset(1)
    su.export("spee2dup.mp3", format="mp3")
    
if __name__ == "__main__":
    speedd()
