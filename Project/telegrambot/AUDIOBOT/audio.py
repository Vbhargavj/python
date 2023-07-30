from pydub import AudioSegment
from telegram import ChatAction, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from pedalboard import Chorus, Pedalboard, Reverb
from pedalboard.io import AudioFile
from common import bannedUserList, f, banned,forcesub,log
import os
i = j = 0
fi = fo = 0
file_name = None

audi = None
button_labels = [
    ["Trim", "Reverb"], ["Volume Boost"], ["Speed Down", "Speed Up"],
    ["Gain", "Fade"], ["Pitch", "Night"], ["Remove Dc", "Merge"], ["Export"]
    
    
]


def msg_handler(update, context):
    user = update.message.from_user.id
    if not banned:
        if user in bannedUserList:
            update.message.reply_text("you are banned")
            return
    if f :
        if user not in forcesub:
            return 
       
    global audi, file_name

    file_id = update.message.audio.file_id
    file_name = update.message.audio.file_name

    # Download the file
    downloading_message = update.message.reply_text("Downloading...")
    file_path = context.bot.get_file(file_id).download()
    context.bot.edit_message_text(
        chat_id=user, message_id=downloading_message.message_id,
        text="Download complete!")
    audio_path = file_path
    audi = AudioSegment.from_file(audio_path)
    
    button_rows = []

    button_rows = [list(map(KeyboardButton, row)) for row in button_labels]
    reply_markup = ReplyKeyboardMarkup(button_rows, resize_keyboard=True)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Choose funtion to perform ", reply_markup=reply_markup)
    return "cmd"


def but(s, update):
    button_rows = [list(map(KeyboardButton, row)) for row in button_labels]
    reply_markup = ReplyKeyboardMarkup(button_rows, resize_keyboard=True)

    update.message.reply_text(s, reply_markup=reply_markup)


def cmd_handler(update, context):

    msg = update.message.text
    reply_markup = ReplyKeyboardRemove()

    if msg == "Trim":
        update.message.reply_text(
            text="Enter the stating seconds", reply_markup=reply_markup)
        return "start_sec"

    elif msg == "Reverb":
        update.message.reply_text("Enter the value of room size", reply_markup=reply_markup)
        return "reverb"

    elif msg == "Volume Boost":
        update.message.reply_text(
            "Enter the value of the boost", reply_markup=reply_markup)
        return "volb"

    elif msg == "Speed Up":
        update.message.reply_text(
            "Enter the value of the speed up", reply_markup=reply_markup)
        return "speedup"

    elif msg == "Speed Down":
        update.message.reply_text("Comming soon..")
        # update.message.reply_text(
        #     "Enter the value of the speed down ", reply_markup=reply_markup)
        return "cmd"

    elif msg == "Night":
        update.message.reply_text(
            "Enter the value of the night value", reply_markup=reply_markup)
        return "night"

    elif msg == "Gain":
        update.message.reply_text(
            "Enter the value of gain booster", reply_markup=reply_markup)
        return "gain"

    elif msg == "Fade":
        update.message.reply_text("Enter the fadein seconds", reply_markup=reply_markup)
        return "fade"

    elif msg == "Pitch":
        update.message.reply_text(
            "Enter the value of pitch", reply_markup=reply_markup)
        return "pitch"

    elif msg == "Export":
        export(update, context)
    elif msg == "Remove Dc":
        update.message.reply_text(
            "Enter right for 1 and left for 2", reply_markup=reply_markup)
        return "remove"

    elif msg == "Merge":
        update.message.reply_text(
            "please send the another song", reply_markup=reply_markup)
        return "merge"
    else:
        print("Something went wrong")
        

# this section for pitch
def pitch(update):

    global audi

    p = float(update.message.text)
    try:
        audi = audi._spawn(audi.raw_data, overrides={
            # Adjust the speed factor as needed
            "frame_rate": int(audi.frame_rate * p)
        })
        audi = audi.set_frame_rate(audi.frame_rate).speedup(float(2/p))
    except Exception as e:
        update.message.reply_text("Something went wrong")
    but("pitching audio", update)
    return "cmd"

# this section for reverb


def reverb(update,context):
    global r,audi
    try:
        r = float(update.message.text)
    except:
        update.message.reply_text("i am reverb not wel")
    
    print(r)
        
    board = Pedalboard([Reverb(room_size=r),Chorus()])
    global audi,file_name
    # audi.export(file_name)    
    # Open an audio file for reading, just like a regular file:
    with AudioFile(file_name) as f:

        # Open an audio file to write to:
        with AudioFile(file_name, 'w', f.samplerate, f.num_channels) as o:

            # Read one second of audio at a time, until the file is empty:
            while f.tell() < f.frames:
                chunk = f.read(int(f.samplerate))

                # Run the audio through our pedalboard:
                effected = board(chunk, f.samplerate, reset=False)

                # Write the output to our output file:
                o.write(effected)
    context.bot.send_audio(
        chat_id=update.effective_chat.id, audio=open(file_name, "rb"))
    # audi=AudioSegment.from_file(file_name)
    # os.remove(file_name)
    but("Reverb effect aplied",update)
    return "cmd"

# this sectoin for nightcored effect
def apply_nightcore_effect(update, context):

    global audi
    # Increase the tempo (speed) by 20%
    audi = audi.speedup(playback_speed=1.2)

    # Increase the pitch by 2 semitones
    audi = audi + 2

    but("aplying nightcored effect", update)
    return "cmd"

# this section for remove dc effect


def remove_dc(update):
    global audi
    try:
        v = int(update.message.text)
    except:
        update.message.reply_text("i am removedc not wel")
        
    audi = audi.remove_dc_offset(v)

    but("removing dc", update)
    return "cmd"

# this section for gaining audio


def gain(update, context):
    global audi
    try:
        g = int(update.message.text)
    except:
        log("i am not wel")
    audi = audi.apply_gain(g)

    but("Apllying gaining", update)
    return "cmd"

# this section for speeding

# this for speed down


def speedd(update, context):
    pass

# this for speed up


def speedu(update, context):
    global audi
    s = float(update.message.text)
    audi = audi.speedup(s)

    but("speed up to audio", update)
    return "cmd"

# this section for volume booster


def volbust(update,context):

    global audi
    b = int(update.message.text)
    print("Before volume boost")
    
    audi = audi+4
    # but("Volume boost to audio", update)
    # print("After volume boost")
    but("Volume boost to audio", update)
    return "cmd"

# this section for fadein and fadeout


def fade_in_taker(update, context):
    fi = int(update.message.text)
    update.message.reply_text("Enter the fade out seconds")
    "startf_sec"


def fade_out_taker(update, context):
    fo = int(update.message.text)
    update.message.reply_text("ok perform an action")
    fade()


def fade(update, context):
    global fi, fo, audi
    fi = fi*1000
    fo = fo*1000
    audi = audi.fade_in(fi).fade_out(fo)

    but("aplying fade in fadeout effect", update)
    return "cmd"

# this is  for trim section


def start_sec_take_handler(update, context):
    try:
        global i
        i = int(update.message.text)
    except Exception as e:
        i = 0
        print(e)

    update.message.reply_text("Enter the ending seconds")
    return "end_sec"


def end_sec(update, context):
    try:
        global f
        f = int(update.message.text)
        trim_audio(update, context)
    except Exception as e:
        print(e)
    return "cmd"


# here complete the function that take an argument from the user


def trim_audio(update, context):
    global i, f, audi

    l = 1  # Adjust the value of l as needed
    print(i+f)

    i = i * 1000

    f = f * 1000

    audi = audi[i:f]

    audi = audi + l
    but("Trimming  audio", update)
    return "cmd"


# when all the process is done then the audio is ready to export
def export(update, context):
    global audi, file_name
    audi.export(str(file_name), "mp3")

    context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_AUDIO)

    context.bot.send_audio(
        chat_id=update.effective_chat.id, audio=open(str(file_name), "rb"))


def cancel_handler(update, context):
    update.message.reply_text('Process terminated successfully')
    return ConversationHandler.END
