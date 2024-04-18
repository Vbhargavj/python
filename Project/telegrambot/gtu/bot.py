from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import json
import telebot

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

profession_options = []
it = [["ds"], ["ada"], ["cn"]]
it_sem5 = []
it_sem6 = []
MAIN_USER_CHAT_ID = 1241390756


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    await update.message.reply_html(
        rf"hello {user.mention_html()} Welcome to the  course vbj bot i am helping to find the course!"
    )


async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mas = update.message.text.lower()

    if "it" in mas:
        reply_markup = ReplyKeyboardMarkup(
            it, one_time_keyboard=True, resize_keyboard=True
        )
        await update.message.reply_text(
            "this is bhargav from it", reply_markup=reply_markup
        )

    elif "ds" in mas:
        await update.message.reply_text("this is the way")
    elif "ada" in mas:
        await update.message.reply_text("this is the 2 way")
    else:
        await update.message.reply_text("I dont understood fuck")



async def notify_ending(message):
    
    token = '5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0'
    chat_id =1241390756    
    
def main() -> None:
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0")
        .build()
    )
    bot = telebot.TeleBot("6050075547:AAHc8zkVYGA2T8UdC8LensCcGlbNIbO2WYk")
    bot.send_message(adminid,"bhargav")

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT, msg))

    # Run the bot until the user presses Ctrl-C
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    notify_ending("start")
    main()
