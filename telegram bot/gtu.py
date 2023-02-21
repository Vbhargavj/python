from telegram import *
from telegram.ext import *
from requests import *
updater = Updater(token="5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0")
dispatcher = updater.dispatcher
likes = 0
dislikes = 0

allowedUsernames = []

# this commands is use to
print("Bot starting.....................\n")
# print(Update._effective_user.name)


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('sem1&sem2')], [KeyboardButton('sem3')]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to my bot! ", reply_markup=ReplyKeyboardMarkup(buttons))


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

    # SEM3
    if 'send' in update.message.text:
        chat_id = update.message.chat_id
        file_url = "https://files.smallpdf.com/files/6f5d810d3c4a7d1abeada35c8fd4e5a8.jpg?name=-5847955727556131000_121.jpg"
        context.bot.send_document(
            chat_id=chat_id, document=file_url, caption='This is a forwarded document')
        
    if 'D.S.A.' in update.message.text:
        # here forward the massage for dsa
        message = update.message
        update.message.reply_text('BOOKs')
        context.bot.send_message(chat_id=1241390756, text=message.text)
        # update.message.forward_from_message_id(8532)
        update.message.reply_text('PYSQs')
        # here you can forward the dsa pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the dsa notes

    if 'D.B.M.S.' in update.message.text:
        # here forward the massage for dbms
        update.message.reply_text('BOOKs')
        # here you can forward the dbms books
        update.message.reply_text('PYSQs')
        # here you can forward the dbms pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the dbms notes

    if 'd.f.' in update.message.text:
        # here forward the massage for d.f.
        update.message.reply_text('BOOKs')
        # here you can forward the d.f. books
        update.message.reply_text('PYSQs')
        # here you can forward the d.f. pysqs
        update.message.reply_text('NOTEs')
        # here you can forward the d.f. notes

    if 'p&s' in update.message.text:
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
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
