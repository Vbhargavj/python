import logging
from telegram.ext import Updater, CommandHandler


# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Define the handler function for the /send_document command
def send_document(update, context):
    # Get the file ID from the command arguments
    file_id = context.args[0]

    # Send the document using the file ID
    context.bot.send_document(
        chat_id=update.effective_chat.id, document=file_id)


def main():
    # Set up the Telegram Bot token
    token = '5422764153:AAH2YpB4J8Pt4Uc0xeyhHNUU-_OC7r4O25Q'

    # Create the Updater and dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Add the command handler for the /send_document command
    send_document_handler = CommandHandler('send_document', send_document)
    dispatcher.add_handler(send_document_handler)

    # Start the bot
    updater.start_polling()
    logger.info('Bot started.')

    # Run the bot until Ctrl-C is pressed
    updater.idle()


if __name__ == '__main__':
    main()
