from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# Define conversation states
QUESTION, ANSWER = range(2)

# Define a dictionary to store the questions and answers count
qna_stats = {}
current_question = "How would you rate the bot?"
current_options = ["option1", "option2", "option3", "option4"]


# Define a function to start the Q&A generation


def qnagen_start(update, context):
    keyboard = [[KeyboardButton(option, callback_data=option)]
                for option in current_options]
    update.message.reply_text(
        current_question, reply_markup=ReplyKeyboardMarkup(keyboard))
    return QUESTION

# Define a function to handle the user's answer


def qnagen_answer(update, context):
    answer = update.message.text
    user_id = update.effective_user.id

    # Store the answer in the stats dictionary
    qna_stats[user_id] = answer

    update.message.reply_text('Thank you for your response!')

    return ConversationHandler.END

# Define a function to cancel the Q&A generation


def qnagen_cancel(update, context):
    update.message.reply_text('Q&A generation canceled.')

    return ConversationHandler.END

# Define a function to handle the admin command for updating Q&A settings


def qnagen_update_start(update, context):
    update.message.reply_text('Please enter the new question:')

    return QUESTION

# Define a function to handle the admin's new question input


def qnagen_update_question(update, context):
    global current_question
    current_question = update.message.text

    update.message.reply_text(
        'Please enter the new options (separated by commas):')

    return ANSWER

# Define a function to handle the admin's new options input


def qnagen_update_options(update, context):
    global current_options
    options_input = update.message.text
    current_options = options_input.split(",")
    current_options = [option.strip() for option in current_options]

    update.message.reply_text('Q&A settings updated successfully.')

    return ConversationHandler.END


# Create an Updater and pass your bot's token
updater = Updater(token='5975659245:AAFEebUbu3783BNxp-3FdBLCxkUNxAZF3Js', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Create a ConversationHandler for Q&A generation
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('qnagen', qnagen_start)],
    states={
        QUESTION: [MessageHandler(Filters.text & ~Filters.command, qnagen_answer)],
    },
    fallbacks=[CommandHandler('cancel', qnagen_cancel)]
)

# Create a ConversationHandler for updating Q&A settings
update_conv_handler = ConversationHandler(
    entry_points=[CommandHandler('update_qna', qnagen_update_start)],
    states={
        QUESTION: [MessageHandler(Filters.text & ~Filters.command, qnagen_update_question)],
        ANSWER: [MessageHandler(
            Filters.text & ~Filters.command, qnagen_update_options)]
    },
    fallbacks=[CommandHandler('cancel', qnagen_cancel)]
)

# Add the ConversationHandlers to the dispatcher
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(update_conv_handler)

# Start the bot
updater.start_polling()
