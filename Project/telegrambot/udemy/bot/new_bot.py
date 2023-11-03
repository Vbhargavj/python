"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from newfun import extract_course_info  # this is step 0

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
import name

COURSE = range(1)
infos = {}
print(type(infos))


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


options = [
    ["App Development"],
    ["Web Development"],
    ["Ethical Hacking"],
    ["Web Application"],
    ["Cyber Security"],
    ["Wifi-Hacking"],
    ["Computer Networks"],
    ["Video Editing"],
    ["Chat-gpt"],
    ["Software Development"],
    ["Other"],
]


async def course_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = ReplyKeyboardMarkup(
        options, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text("select one option", reply_markup=keyboard)


def title_xtra(url):
    i = 0
    global infos
    infos = extract_course_info(url)
    titles = ""  # Initialize titles as an empty string
    for info in infos:
        i += 1
        titles += str(i) + ". " + info.get("Title") + "\n"
    return titles, infos


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Echo the user message."""
    msg = update.message.text.lower()  # Convert the message to lowercase
    chat_id = update.message.from_user.id
    
    # Define a dictionary that maps course categories to URLs
    course_categories = {
        "app development": name.android,
        "web development": name.webdev,
        "ethical hacking": name.ethical,
        "web application": name.web,
        "cyber security": name.cyber,
        "wifi-hacking": name.wifi,
        "computer networks": name.cn,
        "video editing": name.videoedit,
        "chat-gpt": name.chat,
        "software development": name.software,
        "other": name.web,  # You can change this URL to the appropriate default URL
    }

    # Check if the user's input is in the course categories dictionary
    if msg in course_categories:
        url = course_categories[msg]
        titles, infos = title_xtra(url)
        await update.message.reply_text(titles)
        return COURSE
    else:
        await update.message.reply_text("Enter a valid keyword from the options.")
    
    return COURSE



async def Direct_Link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    selection = int(update.message.text)
    await update.message.reply_photo(infos[selection].get("Img src"))
    await update.message.reply_text(infos[selection].get("Title"))
    await update.message.reply_text(infos[selection].get("Author"))

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ok don't do it again")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("6863076777:AAGHU8kxoOy_b6SK7_iNx6s8hmfziZlxt_s")
        .build()
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("course", echo)],
        states={
            COURSE: [MessageHandler(filters.Text, Direct_Link)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # application.add_handler(CommandHandler("course", course_command))
    application.add_handler(conv_handler)

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
