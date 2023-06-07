from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# Define states
option, que = range(2)

# Define handler functions for each state

qu="how was bot give me ratting?"
def start_handler(update, context):
    update.message.reply_text(
        'Enter the question')
    return que


def que_handler(update, context):
    user_input = update.message.text
    qu=user_input
    # Process user input and update conversation context if needed

    update.message.reply_text('Great! Now, Enter options separated by commas')
    return option


def option_handler(update, context):
    user_input = update.message.text
    options=user_input.split(',')
    print(options)
    
    # Process user input and update conversation context if needed

    update.message.reply_text(f'Thanks! Now, now updated que is {qu}')
    
    return ConversationHandler.END

def cancel_handler(update, context):
    update.message.reply_text('Registration canceled.')
    return ConversationHandler.END


# Create an Updater and pass your bot's token
updater = Updater(
    token='6119920821:AAEt6k__xUpgi5tJyNHSlOVEvfiv0dUubPc', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Create the ConversationHandler with entry point, states, and handlers
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_handler)],
    states={
        que: [MessageHandler(Filters.text & ~Filters.command, que_handler)],
        option: [MessageHandler(Filters.text & ~Filters.command, option_handler)],
    },
    fallbacks=[CommandHandler('cancel', cancel_handler)]
)

# Add the ConversationHandler to the dispatcher
dispatcher.add_handler(conv_handler)

# Start the bot
updater.start_polling()
