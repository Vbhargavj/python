import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters,ConversationHandler

# Define your API token
TOKEN = "5975659245:AAFEebUbu3783BNxp-3FdBLCxkUNxAZF3Js"

# Create an Updater
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Define a command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot. How can I assist you?")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Define an echo message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(filters.text & ~filters.command, echo)
dispatcher.add_handler(echo_handler)

# Start the bot
updater.start_polling()

# Run the bot until you send a signal to stop (e.g., Ctrl+C)
updater.idle()
