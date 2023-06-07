from telegram import Bot
from telegram.error import TelegramError
from telegram.ext import Updater, CommandHandler

bot_token = '6119920821:AAEt6k__xUpgi5tJyNHSlOVEvfiv0dUubPc'
channel_id = '-1001962750280'


def is_user_subscribed(channel_id, user_id):
    bot = Bot(token=bot_token)
    try:
        chat_member = bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return chat_member.status == 'member' or chat_member.status == 'creator'
    except TelegramError:
        return False


def start(update, context):
    user_id = update.effective_user.id
    if is_user_subscribed(channel_id, user_id):
        update.message.reply_text(
            "Welcome to the bot! You are subscribed to the channel.")
        # Add your bot's functionality here
    else:
        update.message.reply_text(
            "Sorry, you are not subscribed to the channel. Please subscribe to access the bot.")


# Create an updater and dispatcher
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Register the start command handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
