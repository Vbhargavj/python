from pydub import AudioSegment
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import os
audi = None
i = j = 0
fi=fo=0
#  TODO make log of user in group

def start(update, context):
    # try :
    #     os.remove("input.mp3")
    # except Exception as e:
    #     print("Error"+e)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Welcome to the audio trim bot!")


def msg_handler(update, context):
    global audi

    # file_id = update.message.document.file_id
    # file_name = update.message.document.file_name
    file_id = update.message.audio.file_id
    file_name = update.message.audio.file_name

    # Download the file
    file_path = context.bot.get_file(file_id).download()
    audio_path = file_path
    audi=AudioSegment.from_file(audio_path)
        # Download the file
    # file_path = context.bot.get_file(file_id).download()
    # audio_file = context.bot.get_file(update.message.audio.file_id)
    # audio_file.download("input.mp3")
    # audio = AudioSegment.from_file("input.mp3")
    msg=update.message.text
    if msg=="Trim":
        update.message.reply_text("Enter the stating seconds")
        return "start_sec"
    
    elif msg=="Volume_boost":
        update.message.reply_text("Enter the value of the boost")
        return "volb"
    
    elif msg=="speed":
        update.message.reply_text("Enter the value of the speed up")
    
    elif msg=="night":
        pass
    
    elif msg=="bass_boost":
        pass
    
    elif msg=="gain":
        update.message.reply_text("Enter the value of gain booster")
    
    elif msg=="fade":
        update.message.reply_text("Enter the fadein seconds")
    
    elif msg=="pitch":
        pass
    elif msg=="export":
        export()
    elif msg=="remove_dc":
        update.message.reply_text("Enter right for 1 and left for 2")
    else:
        pass


# this section for pitch
def pitch():
    pass


# this section for remove dc effect
def remove_dc(update):
    global audi
    v=int(update.message.text)
    audi=audi.remove_dc_offset(v)


# this section for gaining audio
def gain(update,context):
    global audi
    g=int(update.message.text)
    audi=audi.apply_gain(g)
    


# this section for speeding

def speed(update,context):
    global audi
    s=float(update.message.text)
    audi = audi.speedup(s)


# this section for volume booster
def volbust(update,context):
    
    global audi
    b=int(update.message.text)
    
    audi=audi+b
    

    
 

# this section for fadein and fadeout
def fade_in_taker(update,context):
    fi=int(update.message.text)
    update.message.reply_text("Enter the fade out seconds")
    
def fade_out_taker(update,context):
    fo=int(update.message.text)
    update.message.reply_text("ok perform an action")
    fade()

def fade():
    global fi,fo,audi
    fi = fi*1000
    fo = fo*1000
    audi = audi.fade_in(fi).fade_out(fo)
    

# this is  for trim section
def start_sec_take_handler(update, context):
    try:
        global i
        i=int(update.message.text)
    except Exception as e:
        i=0
        print(e)
        
    update.message.reply_text("Enter the ending seconds")
    return "end_sec"

def end_sec(update,context):
    try:
        global f
        f = int(update.message.text)
        trim_audio(update, context)
    except Exception as e:
        print(e)
    return ConversationHandler.END


def cancel_handler(update, context):
    update.message.reply_text('Process terminated successfully')
    return ConversationHandler.END
# here complete the function that take an argument from the user

def trim_audio(update, context):
    global i,f,audi
    

    l = 1  # Adjust the value of l as needed
    print(i+f)
    
    i = i * 1000
    
    f = f * 1000

    audi = audi[i:f]
    
    audi = audi + l
    return "audi"
    export(update,context)
    

# when all the process is done then the audio is ready to export
def export(update,context):
    global audi
    audi.export("audi.mp3", "mp3")

    context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_AUDIO)
    
    context.bot.send_audio(
        chat_id=update.effective_chat.id, audio=open("audi.mp3", "rb"))
    # os.remove("Trimed.mp3")
# 

def main():
    # Create the Updater and pass in your bot's token
    updater = Updater(
        "5891764356:AAH7uJXkdJHEShG4WLbCuGjiqzzkuUMR8yg", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.audio, msg_handler)],
        states={
            "start_sec": [MessageHandler(Filters.text & ~Filters.command, start_sec_take_handler)],
            
            "end_sec": [MessageHandler(Filters.text & ~Filters.command, end_sec)]
        },
        fallbacks=[CommandHandler('cancel', cancel_handler)]
    )
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(MessageHandler(Filters.audio, msg_handler))

    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == "__main__":
    main()
