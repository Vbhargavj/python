# import logging
# from telegram import InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# logger = logging.getLogger(name)

# Define the document sending function


def send_document(update, context):
    chat_id = update.message.chat_id
    file_url = "https://files.smallpdf.com/files/6f5d810d3c4a7d1abeada35c8fd4e5a8.jpg?name=-5847955727556131000_121.jpg"

    # Send the document
    context.bot.send_document(
        chat_id=chat_id, document=file_url, caption='This is a forwarded document')


def main():
    # Your bot's token
    token = "5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0"

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the handler for the document sending command
    dp.add_handler(CommandHandler('send_document', send_document))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__== 'main':
    main()
