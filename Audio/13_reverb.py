import numpy as np
from pedalboard import Gain, LadderFilter, Pedalboard, Chorus, Reverb
from pydub import AudioSegment
from pydsm.utils import convert_audio_to_float32

def main():
    # r = float(update.message.text)
    r = 0.25
    board = Pedalboard([Reverb(room_size=r)])

    # Load the input audio as an AudioSegment object
    input_audio = AudioSegment.from_file('file_0.mp3')

    # Convert the AudioSegment to a numpy array
    audio_array = np.array(input_audio.get_array_of_samples())

    # Convert the audio to 32-bit floating-point format
    audio_float32 = convert_audio_to_float32(audio_array, input_audio.sample_width)

    # Get the sample rate and number of channels from the AudioSegment
    sample_rate = input_audio.frame_rate
    num_channels = input_audio.channels

    # Create an empty numpy array to store the processed audio
    output_array = np.empty_like(audio_float32)

    # Process the audio in chunks
    chunk_size = int(sample_rate)
    for i in range(0, len(audio_float32), chunk_size):
        chunk = audio_float32[i:i + chunk_size]

        # Run the audio through the pedalboard
        effected = board(chunk, sample_rate, reset=False)

        # Store the processed audio in the output array
        output_array[i:i + chunk_size] = effected

    # Convert the output array back to the original audio format
    output_audio = np.array(output_array, dtype=audio_array.dtype)
    output_audio = AudioSegment(
        output_audio.tobytes(),
        frame_rate=sample_rate,
        sample_width=input_audio.sample_width,
        channels=num_channels
    )

    # Save the output audio as an audio file
    output_audio.export('output3.mp3', format='mp3')


if __name__ == "__main__":
    main()
