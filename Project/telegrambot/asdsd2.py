from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

userDict = {1241390756,}


def send_document(update, context):
    # Get the file ID from the command arguments
    try:
       file_id = context.args[0]
       # Send the document using the file ID
       context.bot.send_document(
        chat_id=update.effective_chat.id, document=file_id)
    except Exception as e:
        # context.bot.repl
        pass
                           
def document_id_handler(update: Update, context):
    # Check if the message has a document
    if update.message.document:
        # Get the document object
        document = update.message.document

        # Extract the document ID
        document_id = document.file_id

        # Reply with the document ID
        update.message.reply_text(
            f"The document ID is: `{document_id}`", parse_mode='MarkdownV2')
# def image_id_handler(upd)
def start(update: Update, context):
    # Define the start message
    start_message = "Welcome to the hide Telegram Bot!\nSend a document to get its ID."
    # Create a keyboard markup with the button
    update.message.reply_text(start_message)
    new_user_message = update.message
    nUser=new_user_message.from_user.id
    
    if nUser not in userDict:
        userDict.add(nUser)
    
    # Build the notification message
        notification_text = "ToTaL UsEr: {}\nUser_id: {}\nNew user: {}\nUsername: @{}".format(len(userDict),nUser,
        new_user_message.from_user.first_name, new_user_message.from_user.username)
        context.bot.send_message(chat_id="1241390756", text=notification_text)
    
def total(update:Update,context):
    update.message.reply_text(len(userDict))
    

def broadcast(update: Update, context):
    
    if update.message.from_user.id == 1241390756:
        # Join the arguments into a single string
        message = ' '.join(context.args)
        i = 0
        for user in userDict:
            try:
                context.bot.send_message(chat_id=str(user), text=message)
            except Exception as e:
                i += 1
        context.bot.send_message(chat_id="1241390756",
                                 text="Total user"+str(len(userDict)))
        context.bot.send_message(
        chat_id="1241390756", text="Total sucessfull msg : "+str(len(userDict)-i))
        context.bot.send_message(chat_id="1241390756",
                             text="Total unsuccessfull send msg : "+str(i))
    else:
        update.message.reply_text('You cannot access this command, mc')
    
def main():
    # Create an Updater object and replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(
        token='5422764153:AAH2YpB4J8Pt4Uc0xeyhHNUU-_OC7r4O25Q', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Register the document_id_handler to handle document messages
    dispatcher.add_handler(MessageHandler(
        Filters.document, document_id_handler))
    

    # Register the send_document command handler
    dispatcher.add_handler(CommandHandler('send_doc', send_document))
    dispatcher.add_handler(CommandHandler('br', broadcast))
    dispatcher.add_handler(CommandHandler('total', total))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()


if __name__ == '__main__':
    main()
