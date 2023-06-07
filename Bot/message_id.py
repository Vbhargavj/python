from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

def document_id_handler(update: Update, context):
    # Check if the message has a document
    if update.message.document:
        # Get the document ID
        document_id = update.message.document.file_id

        # Reply with the document ID
        update.message.reply_text(f"The document ID is: {document_id}")

def main():
    # Create an Updater object and replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(token='5422764153:AAH2YpB4J8Pt4Uc0xeyhHNUU-_OC7r4O25Q', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the document_id_handler to handle document messages
    dispatcher.add_handler(MessageHandler(Filters.document, document_id_handler))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()

if __name__ == '__main__':
    main()
