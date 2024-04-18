from pydub import AudioSegment

def bass_boost_mp3(input_file, output_file, boost_factor=1.5):
    # Load the MP3 audio file
    audio = AudioSegment.from_file(input_file, format="mp3")

    # Apply bass boost effect by manipulating the audio's low-frequency components
    boosted_audio = audio.low_pass_filter(200 + boost_factor * 100)

    # Export the bass-boosted audio to a new file
    boosted_audio.export(output_file, format="mp3")

# Usage example
input_audio_file = "songs.mp3"  # Replace with your input MP3 audio file
output_audio_file = "output_audio_bass_boosted.mp3"  # Replace with the desired output file name

bass_boost_mp3(input_audio_file, output_audio_file, boost_factor=1.5)  # Adjust the boost_factor as needed
