import telegram
from telegram import Update  # Add this import statement
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio
TOKEN = '5369531550:AAFdpCUzqBJxcG0th98XQGddqZc3vSRBwKI'  # Replace with your actual bot token

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def remove_forward_id(update: Update, context: CallbackContext) -> None:
    if update.message.forward_from or update.message.forward_from_chat:
        if update.message.caption:
            update.message.edit_caption(update.message.caption_html.replace('forwarded from:', ''))
        elif update.message.document:
            file_caption = update.message.document.file_name
            update.message.edit_caption(file_caption.replace('forwarded from:', ''))

def main() -> None:
    update_queue = asyncio.Queue()  # Create the update queue
    updater = Updater(TOKEN, update_queue=update_queue)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.forwarded, remove_forward_id))
    dispatcher.add_handler(MessageHandler(filters.document, remove_forward_id))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


