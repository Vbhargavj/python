import telegram
from common import bannedUserList, f, banned, forcesub, log
from pedalboard.io import AudioFile
from pedalboard import Chorus, Pedalboard, Reverb
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from pydub import AudioSegment
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler

group_id = '-1001962750280'
adminid = 1241390756
userDict = [1241390756]
bannedUserList = [12,]
forcesub = [1241390756,]
f = False
banned = False
# audio section________________________________

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
    if f:
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
        update.message.reply_text(
            "Enter the value of room size", reply_markup=reply_markup)
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
        update.message.reply_text(
            "Enter the fadein seconds", reply_markup=reply_markup)
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


def reverb(update, context):
    global r, audi
    try:
        r = float(update.message.text)
    except:
        update.message.reply_text("i am reverb not wel")

    print(r)

    board = Pedalboard([Reverb(room_size=r), Chorus()])
    global audi, file_name
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
    but("Reverb effect aplied", update)
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


def volbust():

    global audi
    # b = int(update.message.text)
    print("Before volume boost")
    audi = audi+4
    # but("Volume boost to audio", update)
    print("After volume boost")
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


# ||__||__||__||__||__||__||here start all the function of mode||__||__||__||__||__||__||__||__||
# mode is use optional feature for the admin and bot


def log(text, context=True):
    bot_token = '5981185830:AAH5CPc5vf0IkIIVjn1yQdI5wjAe6V113Q0'
    chat_id = '-1001834878605'  # Replace with your group's chat ID
    bot = telegram.Bot(token=bot_token)

    if context:
        text = f'{text}'

    bot.send_message(chat_id=chat_id, text=text)


def mode(update, context):
    if update.message.from_user.id == adminid:
        log("admin use mode function")
        # here the all of the mode changes here
        t1 = f"Status of force sub is {f}\nStatus of banned user is {banned}\n*info*\nf false means force sub is deactive\nbanned True means banned user allow to access the bot\n*Command*\n `/fs` is used to force sub allowed denied access\n`/ba` is used to active or deactive of banned user permission"
        update.message.reply_text(text=t1, parse_mode='MarkdownV2')
    else:
        log(str(update.message.from_user.name) + " is try to access the command")
        update.message.reply_text(text="Abe lauvde aukat me reh")


def ba(update, context):
    # this is handle true and false of f
    if update.message.from_user.id == adminid:
        log("Admin use ba function")
        global banned
        if banned is False:
            log("Now ba is active. banned user can access the bot")
            banned = True
            update.message.reply_text(
                text="Now banned user not allowed to access the bot")
        else:
            log("Now ba is dective. banned user can not access the bot")
            banned = False
            update.message.reply_text(
                text="Now banned user allowed to access the bot")
    else:
        log(str(update.message.from_user.name) + " is try to access the command")
        update.message.reply_text(text="Abe lauvde aukat me reh")

# fs is used to force-subscribe the channel


def fs(update, context):
    # this is handle true and false of f
    if update.message.from_user.id == adminid:
        log("admin access the fs command")
        global f
        if f is False:
            log("Now fs is dective. user have must be join channel")
            f = True
            update.message.reply_text(text="Now force subcribe is active")
        else:
            log("Now fs is active. user have no need to must be join channel")
            f = False
            update.message.reply_text(text="Now force subcribe is deactive")
    else:
        log(str(update.message.from_user.name) + " is try to access the command")
        update.message.reply_text(text="Abe lauvde aukat me reh")

# ||__||__||__||__||__||__||here close the function of mode||__||__||__||__||__||__||__||__||


def start(update, context):
    update.message.reply_text(text='Hello welcome to the bot')
    new_user_message = update.message
    nUser = new_user_message.from_user.id
    log(update.message.from_user.name+"user use start command")

    if f:

        if is_user_subscribed(context.bot, group_id, update.effective_user.id):
            if nUser in forcesub:
                forcesub.remove(nUser)
            update.message.reply_text(
                text="You are now channel/group subscribed, so you can continue")
        else:
            forcesub.append(nUser)
            update.message.reply_text(
                text="You are no channel/group subscribed, so you can not continue")

    try:
        keyboard = [
            [InlineKeyboardButton("Ask", callback_data=nUser)],
            [InlineKeyboardButton("Notify", callback_data='button2')],
            [InlineKeyboardButton("Banned", callback_data='banned')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if nUser not in userDict:
            userDict.append(nUser)

        # Build the notification message
            notification_text = "ToTaL UsEr: {}\nUser_id: {}\nNew user: {}\nUsername: @{}".format(len(
                userDict), nUser, new_user_message.from_user.first_name, new_user_message.from_user.username)
            context.bot.send_message(
                chat_id=adminid, text=notification_text)

            context.bot.send_message(
                chat_id=adminid, text='Press a button:', reply_markup=reply_markup)
    except Exception as e:
        update.message.reply_text(chat_id=adminid, text="I am not ready"+e)


def is_user_subscribed(bot, group_id, user_id):
    log("user checking for subscribed channel")
    chat_member = bot.get_chat_member(chat_id=group_id, user_id=user_id)
    return chat_member.status == 'member' or chat_member.status == 'creator'

# this function is used to ban user


def ban(user_id):
    log("Admin ban the user "+user_id)
    try:
        bannedUserList.append(user_id)
        log(user_id+"user banned successfully")
        return ("user banned successfully")
    except Exception as e:
        log("something error in ban")
        return str(e)

# this function is used to unban the user


def unban(update, context):
    if update.message.from_user.id == adminid:
        log("Admin use unban command")
        try:
            user = context.args[0]
            bannedUserList.remove(int(user))
            update.message.reply_text("user unbanned successfully")
        except Exception as e:
            log("Somthing wrong in unban")
            update.message.reply_text(str(e))
    else:
        log(str(update.message.from_user.name) + " is try to access the command")
        update.message.reply_text(text="Abe lauvde aukat me reh")


def button_callback(update, context):
    user = update.effective_user.id
    query = update.callback_query
    query.answer()

    context.bot.send_message(chat_id="1241390756", text=query.data)
    if query.data == 'ask':
        log("Admin want to question for user")
        qnagen()

    # query.edit_message_text(text=f"Button {query.data} pressed!")
    if query.data == 'banned':
        log("Admin call ban user "+user)
        context.bot.send_message(chat_id="1241390756",
                                 text=f"{ban(user) }\n`/unban {user}`", parse_mode='MarkdownV2')

# this function is used to search movie and title


def broadcast(update: Update, context):

    if update.message.from_user.id == adminid:
        # Join the arguments into a single string
        log("Admin try to broadcast message")
        message = ' '.join(context.args)
        i = 0
        for user in userDict:
            try:
                context.bot.send_message(chat_id=str(user), text=message)
            except Exception as e:
                i += 1
        context.bot.send_message(chat_id="1241390756",
                                 text="Total user"+str(len(userDict)))
        context.bot.send_message(
            chat_id="1241390756", text="Total sucessfull msg : "+str(len(userDict)-i))
        context.bot.send_message(chat_id="1241390756",
                                 text="Total unsuccessfull send msg : "+str(i))
    else:
        update.message.reply_text('You cannot access this command, mc')


def total(update: Update, context):
    if update.message.from_user.id == adminid:
        log("admin want to use total command")
        update.message.reply_text(len(userDict))
# In this modified code, the rating variable


################# QNA GEN. #########################
qna_stats = {}
option, que, ans = range(3)
qu = "how was bot give me ratting?"
# when admin want to ask question to the user trigger from this command


def qnagen(update, context):
    log("admin ask the question")
    keyboard = [[KeyboardButton(option, callback_data=option)]
                for option in options]

    update.message.reply_text(qu, reply_markup=ReplyKeyboardMarkup(keyboard))


def start_handler(update, context):
    log("admin start editing of questions")
    update.message.reply_text('Enter the question')
    return que


# after recieving the que it will store in qu and ask for option
def que_handler(update, context):
    user_input = update.message.text
    global qu
    qu = user_input
    # Process user input and update conversation context if needed
    log("editing in options")
    update.message.reply_text('Great! Now, Enter options separated by commas')
    return option


# after options that are separated one by one
def option_handler(update, context):
    user_input = update.message.text
    global options
    options = user_input.split(',')
    log("Edited question and options ")

    # Process user input and update conversation context if needed

    update.message.reply_text(f'Thanks! Now, now updated que is {qu}')

    return ConversationHandler.END


def qnagen_answer(update, context):
    answer = update.message.text
    user_id = update.effective_user.id
    log("some emplement not done yet")
    # Store the answer in the stats dictionary
    qna_stats[user_id] = answer

    update.message.reply_text('Thank you for your response!')

    return ConversationHandler.END

# if amdin want to cancel the genarating question


def cancel_handler(update, context):

    update.message.reply_text('operation cancelled')
    return ConversationHandler.END
## ..........close here  que genaration was closed............##


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
            "speedup": [MessageHandler(Filters.text & ~Filters.command, speedu)],
            "volb": [MessageHandler(Filters.text & ~Filters.command, volbust)],
            "reverb": [MessageHandler(Filters.text & ~Filters.command, reverb)],
            "pitch": [MessageHandler(Filters.text & ~Filters.command, pitch)],
            "remove": [MessageHandler(Filters.text & ~Filters.command, remove_dc)],
            "gain": [MessageHandler(Filters.text & ~Filters.command, gain)],
            "fade": [MessageHandler(Filters.text & ~Filters.command, fade_in_taker)],
            "startf_sec": [MessageHandler(Filters.text & ~Filters.command, fade_out_taker)]

        },
        fallbacks=[CommandHandler('cancel', cancel_handler)]
    )
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(MessageHandler(Filters.audio, msg_handler))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
