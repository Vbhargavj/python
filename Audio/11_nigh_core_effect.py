from pydub import AudioSegment
from pydub.playback import play

def apply_nightcore_effect(input_file, output_file):
    # Load the input file
    audio = AudioSegment.from_mp3(input_file)

    # Increase the tempo (speed) by 20%
    faster_audio = audio.speedup(playback_speed=1.2)

    # Increase the pitch by 2 semitones
    nightcore_audio = faster_audio + 2

    # Export the modified audio to a new file
    nightcore_audio.export(output_file, format="mp3")

    print("Nightcore effect applied successfully.")

# Example usage
input_file = "input.mp3"
output_file = "output_nightcored.mp3"

apply_nightcore_effect(input_file, output_file)
