from telegram import *
from telegram.ext import *
from requests import *
updater = Updater(token="5369531550:AAFdpCUzqBJxcG0th98XQGddqZc3vSRBwKI")
dispatcher = updater.dispatcher

allowedUsernames = [1241390756,1030952653]

# this commands is use to
print("Bot starting.....................\n")
# print(Update._effective_user.name)


def startCommand(update: Update, context: CallbackContext):
    u_id= update.message.from_user.id
    name = update.message.from_user.first_name
    if u_id not in allowedUsernames:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="you are banned by admin ")
    else:
        
        buttons = [[KeyboardButton('sem1&sem2')], [KeyboardButton('sem3')]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"{name} Welcome to my bot! ", reply_markup=ReplyKeyboardMarkup(buttons))
        print(name)
        print(u_id)
    

def check_user(update: Update, context: CallbackContext):
    u_id= update.message.from_user.id
    if u_id in allowedUsernames:
        return True
    return False
    
    
def sem3(update: Update, context: CallbackContext):
    update.message.reply_text('bhargavbhai')
    sem3_button = [[KeyboardButton('D.S.A.')], [KeyboardButton('D.B.M.S.')], [KeyboardButton('p&s')], [
        KeyboardButton('ETC')], [KeyboardButton('ic')], [KeyboardButton('d.f.')], [KeyboardButton('exit')]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to my bot! ", reply_markup=ReplyKeyboardMarkup(sem3_button))


def messageHandler(update: Update, context: CallbackContext):

    if 'exit' in update.message.text:
        # function call to messege handeler
        startCommand(update, context)
    # if 'Exit' in update.message.text:

    if 'sem3' in update.message.text:
        # if 'dsa' in update.message.text:
        sem3(update, context)

        # //how to create exit button in python telegram bot?

    if 'sem1&sem2' in update.message.text:
        sem1_button = [[KeyboardButton('B.M.E.')], [KeyboardButton('MATHS1')], [KeyboardButton('MATHS2')], [KeyboardButton('ENGLISH')], [KeyboardButton('E.G.D')], [
            KeyboardButton('Environmental Science')], [KeyboardButton('P.P.S.')], [KeyboardButton('B.E.E.')], [KeyboardButton('Physics')], [KeyboardButton('B.E.')], [KeyboardButton('exit')]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Welcome to my bot! ", reply_markup=ReplyKeyboardMarkup(sem1_button))


    def forward_to_user(chat_id, message_id, user_id, bot):
        try:
            bot.forward_message(
                chat_id=user_id, from_chat_id=chat_id, message_id=message_id)
        except Exception as e:
            print("Failed to forward message to user:", e)
            
    def forward_document_to_user(chat_id, document_id, user_id, bot):
        try:
            bot.send_document(chat_id=user_id, document=document_id)
        except Exception as e:
            print("Failed to forward document to user:", e)
    # SEM3
    if 'send' in update.message.text:
        chat_id = update.message.chat_id
        file_url = "https://drive.google.com/uc?export=download&id=163zCrXnaqzzlch36DR8NnzouFBejnPB4"
        try:
            context.bot.send_document(
            chat_id=chat_id, document=file_url, caption='This is a my document')
        except Exception as e:
            print(e)
            print("Failed to send") 
            context.bot.send_message(chat_id=update.effective_chat.id,text="Somethingwentrong")
    if 'D.S.A.' in update.message.text:
        # here forward the massage for dsa
        message = update.message
        chat_id = update.message.chat_id
        update.message.reply_text('BOOKs')
        file_url = "https://drive.google.com/uc?export=download&id=11j0xsgTVU7JjncJQZKirVBzhey-uKMk9"
        context.bot.send_document(chat_id=chat_id, document=file_url, caption='This is a my document')
        # context.bot.send_message(chat_id=1241390756, text=message.text)
        # update.message.forward_from_message_id(8532)
        update.message.reply_text('PYSQs')
        # here you can forward the dsa pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the dsa notes

    if 'D.B.M.S.' in update.message.text:
        # here forward the massage for dbms
        update.message.reply_text('BOOKs')
        try:
            context.bot.forward_message(
                chat_id=update.effective_chat.id, from_chat_id=5369531550, message_id=1241390756)
            
        except Exception as e:
            print(e)
        # here you can forward the dbms books
        update.message.reply_text('PYSQs')
        # here you can forward the dbms pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the dbms notes

    if 'd.f.' in update.message.text:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        print(message_id)
        print(chat_id)
        print(type(chat_id))
    # Forward the message to the user
        user_id = update.message.from_user.id
        forward_to_user(chat_id, message_id, user_id, context.bot)
        
        # here forward the massage for d.f.
        update.message.reply_text('BOOKs')
        # here you can forward the d.f. books
        update.message.reply_text('PYSQs')
        # here you can forward the d.f. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the d.f. notes

    if 'p&s' in update.message.text:
        if update.message.document is not None:
        # Get the chat ID and document ID
            chat_id = update.message.chat_id
            document_id = "BQACAgUAAxkBAAMqZG4Dz5OCgjoSCENlodJcKDvamAsAApUNAAIgI3FXWLpws2zwVXgvBA"

        # Forward the document to the user
            user_id = update.message.from_user.id
            forward_document_to_user(chat_id, document_id, user_id, context.bot)

        # Reply to the group
            update.message.reply_text('Document forwarded to the user.')
        else:
            update.message.reply_text('No document found in the message.')
            
        # here forward the massage for p&s
        update.message.reply_text('BOOKs')
        # here you can forward the p&s books
        update.message.reply_text('PYSQs')
        # here you can forward the p&s pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the p&s notes

    if 'ETC' in update.message.text:
        # here forward the massage for ETC
        update.message.reply_text('BOOKs')
        # here you can forward the ETC books
        update.message.reply_text('PYSQs')
        # here you can forward the ETC pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the ETC notes

    if 'ic' in update.message.text:
        # here forward the massage for ic
        update.message.reply_text('BOOKs')
        # here you can forward the ic books
        update.message.reply_text('PYSQs')
        # here you can forward the ic pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the ic notes

    # ==SEM1 AND SEM2==#
    if 'B.M.E.' in update.message.text:
        # here forward the massage for B.M.E.
        update.message.reply_text('BOOKs')
        # here you can forward the B.M.E. books
        update.message.reply_text('PYSQs')
        # here you can forward the B.M.E. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the B.M.E. notes

    if 'MATHS1' in update.message.text:
        # here forward the massage for MATHS1
        update.message.reply_text('BOOKs')
        # here you can forward the MATHS1 books
        update.message.reply_text('PYSQs')
        # here you can forward the MATHS1 pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the MATHS1 notes

    if 'MATHS2' in update.message.text:
        # here forward the massage for MATHS2
        update.message.reply_text('BOOKs')
        # here you can forward the MATHS2 books
        update.message.reply_text('PYSQs')
        # here you can forward the MATHS2 pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the MATHS2 notes

    if 'ENGLISH' in update.message.text:
        # here forward the massage for ENGLISH
        update.message.reply_text('BOOKs')
        # here you can forward the ENGLISH books
        update.message.reply_text('PYSQs')
        # here you can forward the ENGLISH pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the ENGLISH notes

    if 'E.D.G.' in update.message.text:
        # here forward the massage for E.D.G.
        update.message.reply_text('BOOKs')
        # here you can forward the E.D.G. books
        update.message.reply_text('PYSQs')
        # here you can forward the E.D.G. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the E.D.G. notes

    if 'Environmental Science' in update.message.text:
        # here forward the massage for Environmental Science
        update.message.reply_text('BOOKs')
        # here you can forward the Environmental Science books
        update.message.reply_text('PYSQs')
        # here you can forward the Environmental Science pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the Environmental Science notes

    if 'P.P.S.' in update.message.text:
        # here forward the massage for P.P.S.
        update.message.reply_text('BOOKs')
        # here you can forward the P.P.S. books
        update.message.reply_text('PYSQs')
        # here you can forward theP.P.S. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the P.P.S. notes

    if 'B.E.E.' in update.message.text:
        # here forward the massage for B.E.E.
        update.message.reply_text('BOOKs')
        # here you can forward the B.E.E. books
        update.message.reply_text('PYSQs')
        # here you can forward theB.E.E. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the B.E.E. notes

    if 'B.E.' in update.message.text:
        # here forward the massage for B.E.
        update.message.reply_text('BOOKs')
        # here you can forward the B.E. books
        update.message.reply_text('PYSQs')
        # here you can forward theB.E. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the B.E. notes

    if 'Physics' in update.message.text:
        # here forward the massage for Physics
        update.message.reply_text('BOOKs')
        # here you can forward the Physics books
        update.message.reply_text('PYSQs')
        # here you can forward thePhysics pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the Physics notes


dispatcher.add_handler(CommandHandler("start", startCommand))
# dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
