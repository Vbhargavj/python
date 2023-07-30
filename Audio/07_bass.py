from pydub import AudioSegment


def apply_nightcore_effect(audio_file_path, output_file_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Increase the tempo (speed) by 25% (adjust as desired)
    increased_tempo = audio.speedup(playback_speed=1)

    # Increase the pitch by 4 half steps (adjust as desired)
    increased_pitch = increased_tempo + 4

    # Export the nightcored audio to a file
    increased_pitch.export(output_file_path, format="mp3")


# Usage example
input_file_path = "input.mp3"
output_file_path = "nightcored_output.mp3"

apply_nightcore_effect(input_file_path, output_file_path)
