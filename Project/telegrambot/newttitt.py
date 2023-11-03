from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram.error import Unauthorized
from telegram.utils.helpers import mention_html

group_id = -1001962750280
admin_id = 1241390756
userDict = set()
banned_user_list = set()
forcesub = set()
f = False

# Conversation states
QUE, OPT, ANS = range(3)
qu, options = "", []

# Here start all the function of mode
# Mode is used for optional features for the admin and bot

def mode(update, context):
    if update.message.from_user.id == admin_id:
        t = "Switch on/off the mode\nUse `/fs` command to activate/deactivate force subscribe"
        update.message.reply_text(text=t, parse_mode="MarkdownV2")
    else:
        update.message.reply_text(text="You don't have the permission to use this command.")

# Function to handle force subscribe command

def fs(update, context):
    if update.message.from_user.id == admin_id:
        global f
        f = not f
        update.message.reply_text("Now force subscribe is active" if f else "Now force subscribe is deactive")
    else:
        update.message.reply_text(text="You don't have the permission to use this command.")

# Start function

def start(update, context):
    user_id = update.effective_user.id
    update.message.reply_text(text="Hello, welcome to the bot")

    if f:
        if is_user_subscribed(context.bot, group_id, user_id):
            if user_id in forcesub:
                forcesub.remove(user_id)
            update.message.reply_text("You are now channel/group subscribed, so you can continue")
        else:
            forcesub.add(user_id)
            update.message.reply_text("You are not channel/group subscribed, so you cannot continue")

    try:
        if user_id not in userDict:
            userDict.add(user_id)

            # Build the notification message
            notification_text = f"Total User: {len(userDict)}\nUser ID: {user_id}\nNew User: {update.effective_user.first_name}\nUsername: {mention_html(update.effective_user.id, update.effective_user.first_name)}"
            context.bot.send_message(chat_id=admin_id, text=notification_text, parse_mode="HTML")

            keyboard = [
                [InlineKeyboardButton("Ask", callback_data=f"ask:{user_id}")],
                [InlineKeyboardButton("Notify", callback_data=f"notify:{user_id}")],
                [InlineKeyboardButton("Banned", callback_data=f"banned:{user_id}")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            context.bot.send_message(chat_id=admin_id, text="Press a button:", reply_markup=reply_markup)

    except Exception as e:
        print(e)

# Function to check if a user is subscribed to the channel/group

def is_user_subscribed(bot, group_id, user_id):
    chat_member = bot.get_chat_member(chat_id=group_id, user_id=user_id)
    return chat_member.status == "member" or chat_member.status == "creator"

# Function to ban a user

def ban(update, context):
    if update.message.from_user.id == admin_id:
        try:
            user_id = context.args[0]
            banned_user_list.add(int(user_id))
            update.message.reply_text("User banned successfully")
        except Exception as e:
            update.message.reply_text(str(e))
    else:
        update.message.reply_text("You don't have the permission to use this command.")

# Function to unban a user

def unban(update, context):
    if update.message.from_user.id == admin_id:
        try:
            user_id = context.args[0]
            banned_user_list.discard(int(user_id))
            update.message.reply_text("User unbanned successfully")
        except Exception as e:
            update.message.reply_text(str(e))
    else:
        update.message.reply_text("You don't have the permission to use this command.")

# Button callback function

def button_callback(update, context):
    query = update.callback_query
    query.answer()

    if not query.data:
        return

    action, user_id = query.data.split(':')
    
    if action == "ask":
        context.bot.send_message(chat_id=admin_id, text=f"Ask button pressed by user {user_id}")
    elif action == "notify":
        context.bot.send_message(chat_id=admin_id, text=f"Notify button pressed by user {user_id}")
    elif action == "banned":
        context.bot.send_message(chat_id=admin_id, text=f"{ban(user_id)}\n/unban {user_id}")

# Broadcast function

def broadcast(update, context):
    if update.message.from_user.id == admin_id:
        message = " ".join(context.args)
        success_count, failure_count = 0, 0

        for user_id in userDict:
            try:
                context.bot.send_message(chat_id=user_id, text=message)
                success_count += 1
            except Unauthorized:
                failure_count += 1
        
        update.message.reply_text(f"Total Users: {len(userDict)}")
        update.message.reply_text(f"Total Successful Messages: {success_count}")
        update.message.reply_text(f"Total Unsuccessful Messages: {failure_count}")

    else:
        update.message.reply_text("You don't have the permission to use this command.")

# Total users function

def total(update, context):
    if update.message.from_user.id == admin_id:
        update.message.reply_text(f"Total Users: {len(userDict)}")

# Main function to start the bot

def main():
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("br", broadcast))
    dispatcher.add_handler(CommandHandler("total", total))
    dispatcher.add_handler(CommandHandler("unban", unban, pass_args=True))
    dispatcher.add_handler(CommandHandler("ban", ban, pass_args=True))
    dispatcher.add_handler(CommandHandler("mode", mode))
    dispatcher.add_handler(CommandHandler("fs", fs))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
