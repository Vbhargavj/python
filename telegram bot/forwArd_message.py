from telegram.ext import Updater, CommandHandler


def forward_document(update, context):
    chat_id = update.effective_chat.id
    message_id = 8659
    fchat_id = 1241390756
    context.bot.forward_message(
        chat_id=chat_id, from_chat_id=fchat_id, message_id=message_id)

updater = Updater(
    '5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0', use_context=True)

updater.dispatcher.add_handler(CommandHandler(
    'forward_document', forward_document))

updater.start_polling()
updater.idle()
