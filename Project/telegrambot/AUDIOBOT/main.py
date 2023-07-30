from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler
from common import *
from audio import *
    

def main():
    log("bot was started successfully")
    updater = Updater(
        token='5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0', use_context=True)
    updater.bot.send_message(chat_id=1241390756, text="i am online")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # Register the start command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('br', broadcast))
    dispatcher.add_handler(CommandHandler('total', total))
    dispatcher.add_handler(CommandHandler('unban', unban))
    dispatcher.add_handler(CommandHandler('mode', mode))
    dispatcher.add_handler(CommandHandler('fs', fs))
    dispatcher.add_handler(CommandHandler('ba', ba))
    # dispatcher.add_handler(CommandHandler('ed', edit_message))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.audio, msg_handler)],
        states={
            "cmd": [MessageHandler(Filters.text & ~Filters.command, cmd_handler)],
            # these for fade
            "start_sec": [MessageHandler(Filters.text & ~Filters.command, start_sec_take_handler)],
            "end_sec": [MessageHandler(Filters.text & ~Filters.command, end_sec)],
            "night": [MessageHandler(Filters.text & ~Filters.command, apply_nightcore_effect)],
            "speedup": [MessageHandler(Filters.text & ~Filters.command,speedu)],
            "volb": [MessageHandler(Filters.text & ~Filters.command, volbust)],
            "reverb": [MessageHandler(Filters.text & ~Filters.command, reverb)],
            "pitch": [MessageHandler(Filters.text & ~Filters.command, pitch)],
            "remove": [MessageHandler(Filters.text & ~Filters.command, remove_dc)],
            "gain": [MessageHandler(Filters.text & ~Filters.command, gain)],
            "fade":[MessageHandler(Filters.text & ~Filters.command, fade_in_taker)],
            "startf_sec":[MessageHandler(Filters.text & ~Filters.command, fade_out_taker)]
            
        },
        fallbacks=[CommandHandler('cancel', cancel_handler)]
    )
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(MessageHandler(Filters.audio, msg_handler))

    
    updater.start_polling()
    
    updater.idle()
if __name__ =="__main__":
    main()