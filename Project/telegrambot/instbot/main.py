import os
import time
# from telegram.ext import Update,Dispatcher
from instaloader import Instaloader as ig
from instascrape import Reel

def inst():
    # url=update.message.text
    
    # ig.sessionid: "55125682065%3AFfcInA7RidxpMz%3A24%3AAYcEA9Vb9l4efQQL47WrLEA6iD7ma5bx21GfwOSiQA"

    
    sample_reel = Reel(
        'https://www.instagram.com/reel/CqFP7bNtDOB/?igshid=MTc4MmM1YmI2Ng==')
    sample_reel.scrape()
    reeldir = os.getcwd()
    sample_reel.download(fp=f"{reeldir}\\reel{int(time.time())}.mp4")
    print(dir)
    print(f"This reel has {sample_reel.video_view_count:,} views.")
    
    
    
# def main():
    
    
#     updater=Update(token="")
    
#     updater.bot.send_message(chat_id=1241390756, text="i am online")
    
#     dispatcher=updater.dispatcher
    
#     dispatcher.add_handler()
    
#     updater.start_polling()
    
#     updater.idle()
    
if __name__ =="__main__":
    inst()
    
# from flask import Flask
# from threading import Thread

app = Flask('')


@app.route('/')
def ping():
  return "pong "


def run():
  app.run(host='0.0.0.0', port=8000)


def server():
  t = Thread(target=run)
  t.start()
