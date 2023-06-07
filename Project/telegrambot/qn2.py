from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

# Define the conversation states
QUESTION_STATE = 1

# Define the function to handle the /start command
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Ask", callback_data='ask')],
        [InlineKeyboardButton("Notify", callback_data='notify')],
        [InlineKeyboardButton("Banned", callback_data='banned')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Press a button:', reply_markup=reply_markup)

# Define the function to handle button presses
def button_callback(update, context):
    query = update.callback_query
    query.answer()
    
    if query.data == 'ask':
        return qna(update, context)
    elif query.data == 'notify':
        # Handle notify button press
        pass
    elif query.data == 'banned':
        # Handle banned button press
        pass

# Define the function to initiate the question and answer conversation
def qna(update, context):
    query = update.callback_query
    query.message.reply_text("Enter the question")
    return QUESTION_STATE

# Define the function to handle the user's input
def handle_question(update, context):
    question = update.message.text
    # Process the user's question here
    
    # Reply with the answer or further instructions
    update.message.reply_text("Here is the answer.")

    # End the conversation
    return ConversationHandler.END

# Create an updater and dispatcher
updater = Updater(token="5975659245:AAFEebUbu3783BNxp-3FdBLCxkUNxAZF3Js", use_context=True)
dispatcher = updater.dispatcher

# Create a conversation handler
conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("qna", qna)],
    states={
        QUESTION_STATE: [MessageHandler(Filters.text, handle_question)]
    },
    fallbacks=[]
)

# Register the command and button handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(conversation_handler)
dispatcher.add_handler(CallbackQueryHandler(button_callback))

# Start the bot
updater.start_polling()
