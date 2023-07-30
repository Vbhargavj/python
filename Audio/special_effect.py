from pysndfx import AudioEffectsChain
from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")

def speedd():

    audio = AudioSegment.from_file("input.mp3")
    slowed_down = audio._spawn(audio.raw_data, overrides={
        # Adjust the speed factor as needed
        "frame_rate": int(audio.frame_rate * 0.8)
    })
    slowed_down = slowed_down.set_frame_rate(audio.frame_rate).speedup(1.3)
    slowed_down.export("ot.wav", format="wav")


def apply_nightcore_effect():
    # Load the input file
    # audio = AudioSegment.from_mp3(input_file)
    global audio
    # Increase the tempo (speed) by 20%
    faster_audio = audio.speedup(playback_speed=1.2)

    # Increase the pitch by 2 semitones
    nightcore_audio = faster_audio + 2

    # Export the modified audio to a new file
    nightcore_audio.export("ot.wav", format="wav")

    print("Nightcore effect applied successfully.")


# Load the audio file
audio_file = "D:\coding\Code\python\Audio\ot.wav"

# Create an AudioEffectsChain object
fx = AudioEffectsChain()

# Add effects to the chain
fx.highshelf()  # Apply a highshelf filter
fx.pitch(0.5)  # Apply a pitch shift

# Apply the effects to the audio file
output_file = 'D:\coding\Code\python\Audio\vbj.wav'
fx("D:\coding\Code\python\Audio\ot.wav", "vbj.wav")
