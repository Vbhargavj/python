from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import json


from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

"""_summary_
this is assign the value from the database and after bot was start
    
    """
def fetch():
    
    with open('data.json', 'r') as file:
        data = json.load(file)
    print(data)
    return data
profession_options=[]

async def starter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global profession_options
    profession_options=fetch()
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global profession_options
    user = update.effective_user
    
    reply_markup=ReplyKeyboardMarkup(
        profession_options, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_html(
        rf"hello {user.mention_html()} Welcome to the  course vbj bot i am helping to find the course!",reply_markup=reply_markup
    )
    

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    mas=update.message.text.lower()
    
    if "it" in mas:
        await update.message.reply_text("this is bhargav from it"
    )
    else:
        await update.message.reply_text("I dont understood fuck")
        
def main() -> None: 
    """
    The main function creates an application for a bot and adds handlers for different commands and
    messages.
    """
    """Run the bot."""
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        "5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0").build()

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("s", starter))

    application.add_handler(MessageHandler(filters.TEXT,msg))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
  
