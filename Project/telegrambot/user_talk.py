from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler

# Define a function to handle the /start command
bannedUserList = {12}
qna_stats = {}
options = ['a', 'b', 'c', 'd']
group_id = '-1001962750280'
adminid = '1241390756'
userDict = [1241390756,]


def start(update, context):
    update.message.reply_text(
        text='Hello welcome to the bot', reply_markup=ReplyKeyboardRemove())
    if is_user_subscribed(context.bot, group_id, update.effective_user.id):
        print('hio')
    else:
        print("vbj")
    keyboard = [
        [InlineKeyboardButton(
            "ask", callback_data=update.message.from_user.id)],
        [InlineKeyboardButton("notify", callback_data='button2')],
        [InlineKeyboardButton("banned", callback_data='banned')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    new_user_message = update.message
    nUser = new_user_message.from_user.id
    if nUser not in userDict:
        userDict.append(nUser)

    # Build the notification message
        notification_text = "ToTaL UsEr: {}\nUser_id: {}\nNew user: {}\nUsername: @{}".format(len(userDict), nUser,                                                                         new_user_message.from_user.first_name, new_user_message.from_user.username)
        context.bot.send_message(chat_id="1241390756", text=notification_text)

        context.bot.send_message(
        chat_id=adminid, text='Press a button:', reply_markup=reply_markup)


# ..............define some function to ask question to the user...............
# intisilize the some needs
# Define states
option, que, ans = range(3)
qu = "how was bot give me ratting?"

# Define handler functions for each state


# when admin want to ask question to the user trigger from this command
def start_handler(update, context):
    update.message.reply_text(
        'Enter the question')
    return que


# after recieving the que it will store in qu and ask for option
def que_handler(update, context):
    user_input = update.message.text
    global qu
    qu = user_input
    # Process user input and update conversation context if needed

    update.message.reply_text('Great! Now, Enter options separated by commas')
    return option


# after options that are separated one by one


def option_handler(update, context):
    user_input = update.message.text
    global options
    options = user_input.split(',')
    print(options)

    # Process user input and update conversation context if needed

    update.message.reply_text(f'Thanks! Now, now updated que is {qu}')

    return ConversationHandler.END


def qnagen_answer(update, context):
    answer = update.message.text
    user_id = update.effective_user.id

    # Store the answer in the stats dictionary
    qna_stats[user_id] = answer
    print(qna_stats)
    update.message.reply_text('Thank you for your response!')

    return ConversationHandler.END

# if amdin want to cancel the genarating question


def cancel_handler(update, context):
    update.message.reply_text('Registration canceled.')
    return ConversationHandler.END
## ..........close here  que genaration was closed............##

# here that function is used to ask the question and option to the user

# this function is used to display question and option


def qnagen(update, context):
    keyboard = [[KeyboardButton(option, callback_data=option)]
                for option in options]

    update.message.reply_text(qu, reply_markup=ReplyKeyboardMarkup(keyboard))

# this function is used to ban user


def ban(user_id):
    try:
        bannedUserList.add(user_id)
    except Exception as e:
        return False

# this function is used to unban the user


def unban(update, context):
    try:
        user = context.args[0]
        bannedUserList.remove(user)
    except Exception as e:
        update.message.reply_text(e)


def button_callback(update, context):
    user = update.effective_user.id
    query = update.callback_query
    query.answer()

    context.bot.send_message(chat_id="1241390756", text=query.data)
    if query.data == 'button2':
        qna(update, context)
    # query.edit_message_text(text=f"Button {query.data} pressed!")
    if query.data == 'banned':

        ban(user)
        context.bot.send_message(chat_id="1241390756",
                                 text=f"`/unban {user}`", parse_mode='MarkdownV2')

# it check the user in channel if not bot not work


def is_user_subscribed(bot, group_id, user_id):
    chat_member = bot.get_chat_member(chat_id=group_id, user_id=user_id)
    return chat_member.status == 'member' or chat_member.status == 'creator'


def qna(update, context):
    query = update.callback_query
    query.answer()

    context.bot.send_message(chat_id="1241390756", text=query.data)
    if query.data == 'button2':
        update.effective_message.reply_text("Enter the question")
    # here implement the ban option...........................................

# Create an updater and dispatcher
updater = Updater(
    token="5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0", use_context=True)
dispatcher = updater.dispatcher

# here Conversational handler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('startq', start_handler)],
    states={
        que: [MessageHandler(Filters.text & ~Filters.command, que_handler)],
        option: [MessageHandler(
            Filters.text & ~Filters.command, option_handler)]
    },
    fallbacks=[CommandHandler('cancel', cancel_handler)]
)

# Add the ConversationHandler to the dispatcher
dispatcher.add_handler(conv_handler)
# Register the command and button handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("q", qnagen))
dispatcher.add_handler(CommandHandler("unban", unban))
dispatcher.add_handler(CallbackQueryHandler(button_callback))


# Start the bot
updater.start_polling()
