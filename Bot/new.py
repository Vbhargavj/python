from telegram.ext import *

updater = Updater(
    token="5369531550:AAFdpCUzqBJxcG0th98XQGddqZc3vSRBwKI", use_context=True)


def start(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f'Hello, {name}!')

def echo(update, context):
    message=update.message.reply



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
