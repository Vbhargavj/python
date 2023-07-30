from pydub import AudioSegment
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Welcome to the audio trim bot!")


def trim_audio(update, context):
    if not update.message.audio:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Please send an audio file.")
        return

    audio_file = context.bot.get_file(update.message.audio.file_id)
    audio_file.download("input.mp3")

    audio = AudioSegment.from_file("input.mp3")
    start_sec_handlers()
    def start_sec_handlers(update, context):
        update.message.reply_text('Enter the starting second')
        return "end_sec"

    def end_sec_handlers(update, context):
        try:
            i = int(update.message.text)
        except Exception as e:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=str(e) + " Some error in i")
            return ConversationHandler.END

        update.message.reply_text('Enter the ending second')
        context.user_data['start_time'] = i
        return "final_sec"

    def final_sec_handler(update, context):
        try:
            f = int(update.message.text)
        except Exception as e:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=str(e) + " Some error in f")
            return ConversationHandler.END

        l = 1  # Adjust the value of l as needed

        i = context.user_data['start_time'] * 1000
        f = f * 1000

        trimmed_audio = audio[i:f]
        trimmed_audio = trimmed_audio + l

        # trimmed_audio = trimmed_audio.normalize()

        trimmed_audio.export("Trimed.mp3", "mp3")

        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_AUDIO)
        context.bot.send_audio(
            chat_id=update.effective_chat.id, audio=open("Trimed.mp3", "rb"))

        return ConversationHandler.END

    def cancel_handler(update, context):
        update.message.reply_text('Operation Terminated')
        return ConversationHandler.END

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.audio, start_sec_handlers)],
        states={
            "end_sec": [MessageHandler(Filters.text & ~Filters.command, end_sec_handlers)],
            "final_sec": [MessageHandler(Filters.text & ~Filters.command, final_sec_handler)]
        },
        fallbacks=[CommandHandler('cancel', cancel_handler)]
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please send the audio trim details.")
    context.user_data.clear()

    return conv_handler


def main():
    # Create the Updater and pass in your bot's token
    updater = Updater("5891764356:AAH7uJXkdJHEShG4WLbCuGjiqzzkuUMR8yg", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.audio,trim_audio))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == "__main__":
    main()
