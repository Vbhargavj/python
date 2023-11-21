from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ConversationHandler,
)
from user_store import store_user
from add_key import store_user as add_key
from display import display,display_info

# Define a few command handlers. These usually take the two arguments update and
# context.
key = ''
content = ''
NAMING, KEY, CONTENT, SURE = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"hello {user.mention_html()} Welcome to the udemy course vbj bot i am helping to find the course!"
    )
    # print(user.id,user.first_name,user.username)
    store_user(user.id, user.username, user.first_name)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "This bot is help to find the best course on udemy if any query then contact the devloper @Vbj01"
    )

async def user_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(display_info(update.message.id))

def add(id, key, content):
    add_key(id, key, content)


async def users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(display())


async def start_taker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int():
    await update.message.reply_text("Please enter the name")
    return NAMING


async def key_taker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global key
    key = update.message.text
    await update.message.reply_text("Please enter the content")
    return KEY


async def content_taker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global content
    content = update.message.text
    await update.message.reply_text("Are you sure")
    return CONTENT


async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.message.id
    sure = update.message.text
    global key,content
    print(sure)
    if sure == "yes":
        add(id, key, content)
        print("YEs")
    else:
        await update.message.reply_text("ok i am not adding")
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("6863076777:AAGHU8kxoOy_b6SK7_iNx6s8hmfziZlxt_s")
        .build()
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_taker", start_taker)],
        states={
            NAMING: [MessageHandler(filters.TEXT & ~filters.COMMAND, key_taker)],
            KEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, content_taker)],
            CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("users", users))
    application.add_handler(CommandHandler("dis", user_profile))
    application.add_handler(conv_handler)
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
