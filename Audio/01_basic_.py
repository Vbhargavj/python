from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")

# Trim audio from 5 seconds to 10 seconds
audio = audio[5000:100000]

# Increase volume by 6 dB
louder_audio = audio + 6

gain_audio=audio.apply_gain(5)

# Fade in and fade out
faded_audio = louder_audio.fade_in(2000).fade_out(2000)

# Export the edited audio
faded_audio.export("output.mp3", format="mp3")
gain_audio.export("gain.mp3", format="mp3")
