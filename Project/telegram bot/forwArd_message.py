from telegram.ext import Updater, CommandHandler


def forward_document(update, context):
    chat_id = update.effective_chat.id
    message_id = 8659
    fchat_id = 1241390756
    context.bot.forward_message(
        chat_id=chat_id, from_chat_id=fchat_id, message_id=message_id)

updater = Updater(
    '1925876251:AAGU1-DU8IpE5pC8oj1YVAxd6goLPJBRUSc', use_context=True)

updater.dispatcher.add_handler(CommandHandler(
    'forward_document', forward_document))

updater.start_polling()
updater.idle()
