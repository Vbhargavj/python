# from pydub import AudioSegment
# from telegram.ext import Updater
# # Load audio file
# # audio = AudioSegment.from_file("D:\\coding\\Code\\python\\Audio\\input.mp3")

# def gain(update,context):
#     # global audio
#     aud=update.message.audio
#     audio=AudioSegment(aud)
#     # g=int(input("Enter the value of gain"))
#     g=3
#     audio=audio.apply_gain(g)
#     audio.export("gain.mp3",format="mp3")

# if __name__ == "__main__":
#     gain()

from pydub import AudioSegment
from telegram.ext import Updater, MessageHandler, Filters


def gain(update, context):
    # Get the audio file ID
    audio_id = update.message.audio.file_id

    # Get the file object using the audio file ID
    file_obj = context.bot.get_file(audio_id)

    # Download the audio file
    file_obj.download("audio.mp3")

    # Convert the audio file to WAV format
    # audio = AudioSegment.from_file("audio.ogg", format="ogg")
    # audio.export("audio.wav", format="wav")

    # Load the converted audio file
    audio = AudioSegment.from_wav("audio.mp3")

    # Apply gain to the audio
    gain_value = 3  # Set the desired gain value
    audio = audio.apply_gain(gain_value)

    # Export the audio as an MP3 file
    audio.export("gain.mp3", format="mp3")

    # Send the resulting MP3 file as a reply
    context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=open("gain.mp3", "rb")
    )


def main():
    # Create the Telegram Bot updater and dispatcher
    updater = Updater(
        "6119920821:AAEt6k__xUpgi5tJyNHSlOVEvfiv0dUubPc", use_context=True)
    dispatcher = updater.dispatcher

    # Register the gain function as a handler for audio messages
    audio_handler = MessageHandler(Filters.audio, gain)
    dispatcher.add_handler(audio_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
