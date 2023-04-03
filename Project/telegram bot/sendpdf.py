import logging
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('hello welcome to  my bot')

def download(update, context):
    context.bot.sendDocument(update.effective_chat.id,document=open('D:\\coding\\code program\\python\\telegram bot\\br.pdf','rb'))
    update.message.reply_text('this file downloading')

def echo(update, context):
    context.bot.sendDocument(update.effective_chat.id, update.message.id)

def main():
    updater= Updater('5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0',use_context=True)
    
    dp=updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('download',download))

    dp.add_handler(MessageHandler(Filters.text,echo))

    updater.start_polling()

if __name__ == '__main__':
    main()