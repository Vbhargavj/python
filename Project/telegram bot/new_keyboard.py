import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a function to handle the /send command


def send_command(update, context):
    # Get the chat ID of the user to send the document to
    # Send the document to the user
    context.bot.forward_message(
        chat_id=update.message.chat_id, from_chat_id=1241390756, message_id=8651)


# Create the Updater and pass it the bot's token
updater = Updater(
    "5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0", use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Add a command handler to handle the /send command
dp.add_handler(CommandHandler("send", send_command))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
