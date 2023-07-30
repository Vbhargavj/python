from instagrapi import Client
Username = 'skullcoder_.01'
Password = 'vbjvbj@147147'
# Your Instagram username and password goes here.
import os

Path = r'D:\coding\Code'

import requests

from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ChatAction,InputFile
)
from telegram.ext import (
    Updater,
    Filters,
    CommandHandler,
    MessageHandler
)


main_keyboard = [
    ['ℹ Help', '💰 Donate']
]


def start(update, context):
    update.message.reply_text(
        '👋 Welcome to my bot! It can download any type of media on Instagram! (Public accounts only)',
        reply_markup=ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True),
    )


def help(update, context):
    update.message.reply_text(
        'Send an Instagram link for a PUBLIC Post, Video, IGTV or Reel to download it! Stories are not currently supported.\n\n'
        'To download a user profile image, just send its username',
        reply_markup=ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True),
    )


def donate(update, context):
    update.message.reply_text(
        'Thank you for donating! ❤\n\nThis will help covering the costs of the hosting',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'Buy Me A Coffee', 'https://www.buymeacoffee.com/simonfarah'
                    )
                ]
            ]
        ),
    )


def send_post(update, context):
    link = update.message.text
    print(link)
    try:
        cl = Client()
        cl.login(Username, Password)
        info = cl.media_pk_from_url(link)
        clip_url = cl.media_info(info).video_url
        print(clip_url)
        try:
            context.bot.send_chat_action(
                chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_VIDEO)
            context.bot.send_video(
                chat_id=update.message.chat_id, video=clip_url, supports_streaming=True)
        except Exception as e:
            # for download on PC
            cl.clip_download_by_url(clip_url,filename="reel", folder=Path)
            video = open('reel.mp4','rb')
            context.bot.send_video(chat_id=update.effective_chat.id,video=InputFile(video))
            os.remove("reel.mp4")
            print("save video")
            
        print("done")
    except Exception as e:
        print(e)


def send_dp(update, context):
    username = update.message.text
    url = f'https://instagram.com/bhargav_4096/'

    try:
        visit = requests.get(url).json()
        user_profile = visit['graphql']['user']['profile_pic_url_hd']
        update.message.reply_chat_action('upload_photo')
        update.message.reply_photo(user_profile)
    except:
        update.message.reply_text('Send Me Only Existing Instagram Username')


def main():
    BOT_TOKEN = '5922164932:AAFB9kD-zjZIeOGayDZNHB8JNjcyr_nbEY8'
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('Help'), help))
    dp.add_handler(MessageHandler(Filters.regex('Donate'), donate))
    dp.add_handler(MessageHandler(Filters.text, send_post))
    # dp.add_handler(MessageHandler(Filters.text, send_dp))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Bot is running...')
    main()
