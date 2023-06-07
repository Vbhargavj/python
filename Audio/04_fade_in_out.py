from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")
def fade():
    global audio
    fi=int(input("Enter the fade in value"))
    fo=int(input("Enter the fade out value"))
    fi=fi*1000
    fo=fo*1000
    audio=audio.fade_in(fi).fade_out(fo)
    audio.export("Fadeinout.mp3",format="mp3")
if __name__=="__main__":
    fade()