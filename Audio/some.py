from telegram.ext import Updater, MessageHandler, Filters

# Define a variable to store the audio file path
audio_path = None

# Define a function to handle incoming messages with media files


def handle_media(update, context):
    global audio_path
    # Check if the message has a media file
    if update.message.audio:
        # Get the file ID and file name
        file_id = update.message.audio.file_id
        file_name = update.message.audio.file_name

        # Download the file
        file_path = context.bot.get_file(file_id).download()

        # Save the file path
        audio_path = file_path

        # Reply with a message indicating successful saving
        update.message.reply_text(f"Music '{file_name}' saved successfully!")
    else:
        # Reply with a message if no audio file is attached
        update.message.reply_text("Please send an audio file!")


def main():
    # Initialize the Telegram bot
    # Replace 'YOUR_BOT_TOKEN' with your bot token
    updater = Updater('5891764356:AAH7uJXkdJHEShG4WLbCuGjiqzzkuUMR8yg', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a handler for media messages
    dispatcher.add_handler(MessageHandler(Filters.audio, handle_media))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()


if __name__ == '__main__':
    main()
