from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters,CommandHandler


def send_document(update, context):
    # Get the file ID from the command arguments
    
    file_id = context.args[0]
    # Send the document using the file ID
    context.bot.send_document(
    chat_id=update.effective_chat.id, document=file_id)
    
def document_id_handler(update: Update, context):
    # Check if the message has a document
    if update.message.document:
        # Get the document object
        document = update.message.document

        # Extract the document ID
        document_id = document.file_id

        # Reply with the document ID
        update.message.reply_text(f"The document ID is: {document_id}")


def main():
    # Create an Updater object and replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(token='5422764153:AAH2YpB4J8Pt4Uc0xeyhHNUU-_OC7r4O25Q', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the document_id_handler to handle document messages
    dispatcher.add_handler(MessageHandler(
        Filters.document, document_id_handler))
    dispatcher.add_handler(CommandHandler('send_doc',send_document))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()


if __name__ == '__main__':
    main()
