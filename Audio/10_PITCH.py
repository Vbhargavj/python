# import nightcore as nc

# # Additional keyword args are passed to AudioSegment.from_file
# audio = nc.nightcore("D:\coding\Code\python\Audio",
#                      nc.Semitones(2), format="mp3")

# from pydub import AudioSegment
# from pydub.playback import speedup

# audio = AudioSegment.from_file("input.mp3")
# pitch_shifted = audio._spawn(audio.raw_data, overrides={
#     # Adjust the factor as needed for desired pitch shift
#     "frame_rate": int(audio.frame_rate * 1.2)
# })
# pitch_shifted = pitch_shifted.set_frame_rate(audio.frame_rate)
# pitch_shifted.export("my.mp3", format="mp3")
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup

sound = AudioSegment.from_file('output.wav', format="wav")

# shift the pitch up by half an octave (speed will increase proportionally)
octaves = 1.5

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# keep the same samples but tell the computer they ought to be played at the
# new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
hipitch_sound = sound._spawn(sound.raw_data, overrides={
                             'frame_rate': new_sample_rate})

# now we just convert it to a common sample rate (44.1k - standard audio CD) to
# make sure it works in regular audio players. Other than potentially losing audio quality (if
# you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
hipitch_sound = hipitch_sound.set_frame_rate(44100)
# hipitch_sound = hipitch_sound.time_stretch(1.25)
# Play pitch changed sound

# play(hipitch_sound)

# export / save pitch changed sound
hipitch_sound.export("out.wav", format="wav")
