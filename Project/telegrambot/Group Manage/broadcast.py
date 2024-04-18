


# from origin import original2
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ConversationHandler,
)





# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"hello {user.mention_html()} Welcome to the udemy course vbj bot i am helping to find the course!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "This bot is help to find the best course on udemy if any query then contact the devloper @Vbj01"
    )


async def br(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    members = context.bot.get_chat_members(chat_id)
    
    usernames = []
    for member in members:
        if member.user.username:
            usernames.append(member.user.username)
    
    # Send the usernames as a message
    await update.message.reply_text(f"Usernames in this group: {', '.join(usernames)}")













def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("6119920821:AAEt6k__xUpgi5tJyNHSlOVEvfiv0dUubPc")
        .build()
    )
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("br", br))
    # application.add_handler(CommandHandler("course", course_command))
    

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
