from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")
def trim():
    global audio
    i=int(input("Enter the starting second"))
    f=int(input("Enter the ending second"))
    l=int(input("Enter the value of louder"))
    i=i*1000
    f=f*1000
    audio=audio[i:f]
    audio=audio+l
    
    # audio = audio.normalize()

    audio.export("Trimed.mp3","mp3")    

if __name__ == "__main__":
    trim()