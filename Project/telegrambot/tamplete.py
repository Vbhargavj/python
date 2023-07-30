from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler


group_id = '-1001962750280'
adminid = 1241390756
userDict = [1241390756]
bannedUserList = [12,]
forcesub = [1241390756,]
f = False

# ||__||__||__||__||__||__||here start all the function of mode||__||__||__||__||__||__||__||__||
# mode is use optional feature for the admin and bot


def mode(update, context):
    if update.message.from_user.id == adminid:
        # here the all of the mode changes here
        t = "Switch on off the mode\n use `/fs` command to active/deactive of force subscribe"
        update.message.reply_text(text=t, parse_mode='MarkdownV2')
    else:
        update.message.reply_text(text="Abe lauvde aukat me reh")

# fs is used to force-subscribe the channel


def fs(update, context):
    # this is handle true and false of f
    if update.message.from_user.id == adminid:
        global f
        if f is False:
            f = True
            update.message.reply_text(text="Now force subcribe is active")
        else:
            f = False
            update.message.reply_text(text="Now force subcribe is deactive")
    else:
        update.message.reply_text(text="Abe lauvde aukat me reh")

# ||__||__||__||__||__||__||here close the function of mode||__||__||__||__||__||__||__||__||


def start(update, context):
    update.message.reply_text(text='Hello welcome to the bot')
    new_user_message = update.message
    nUser = new_user_message.from_user.id

    if f:

        if is_user_subscribed(context.bot, group_id, update.effective_user.id):
            if nUser in forcesub:
                forcesub.remove(nUser)
            update.message.reply_text(
                text="You are now channel/group subscribed, so you can continue")
        else:
            forcesub.append(nUser)
            update.message.reply_text(
                text="You are no channel/group subscribed, so you can not continue")
    try:
        keyboard = [
            [InlineKeyboardButton(
                "ask", callback_data=update.message.from_user.id)],
            [InlineKeyboardButton("notify", callback_data='button2')],
            [InlineKeyboardButton("banned", callback_data='banned')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if nUser not in userDict:
            userDict.append(nUser)

        # Build the notification message
            notification_text = "ToTaL UsEr: {}\nUser_id: {}\nNew user: {}\nUsername: @{}".format(len(
                userDict), nUser,                                                                         new_user_message.from_user.first_name, new_user_message.from_user.username)
            context.bot.send_message(
                chat_id="1241390756", text=notification_text)

            context.bot.send_message(
                chat_id=adminid, text='Press a button:', reply_markup=reply_markup)
    except Exception as e:
        print(e)


def is_user_subscribed(bot, group_id, user_id):
    chat_member = bot.get_chat_member(chat_id=group_id, user_id=user_id)
    return chat_member.status == 'member' or chat_member.status == 'creator'

# this function is used to ban user


def ban(user_id):
    try:
        bannedUserList.append(user_id)
        return ("user banned successfully")
    except Exception as e:
        return str(e)

# this function is used to unban the user


def unban(update, context):
    if update.message.from_user.id == adminid:
        try:
            user = context.args[0]
            bannedUserList.remove(int(user))
            update.message.reply_text("user unbanned successfully")
        except Exception as e:
            update.message.reply_text(str(e))
    else:
        update.message.reply_text(text="Abe lauvde aukat me reh")


def button_callback(update, context):
    user = update.effective_user.id
    query = update.callback_query
    query.answer()

    context.bot.send_message(chat_id="1241390756", text=query.data)
    if query.data == 'button2':
        pass
    # query.edit_message_text(text=f"Button {query.data} pressed!")
    if query.data == 'banned':

        context.bot.send_message(chat_id="1241390756",
                                 text=f"{ban(user) }\n`/unban {user}`", parse_mode='MarkdownV2')

# this function is used to search movie and title





def broadcast(update: Update, context):

    if update.message.from_user.id == adminid:
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


def total(update: Update, context):
    if update.message.from_user.id == adminid:
        update.message.reply_text(len(userDict))
# In this modified code, the rating variable


################# QNA GEN. #########################
qna_stats = {}
option, que, ans = range(3)
qu = "how was bot give me ratting?"
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
def main():
    updater = Updater(
        token='5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # Register the start command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('br', broadcast))
    dispatcher.add_handler(CommandHandler('total', total))
    dispatcher.add_handler(CommandHandler('unban', unban))
    dispatcher.add_handler(CommandHandler('mode', mode))
    dispatcher.add_handler(CommandHandler('fs', fs))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
