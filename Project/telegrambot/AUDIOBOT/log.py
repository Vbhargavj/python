import telegram


bot_token = '6050075547:AAHc8zkVYGA2T8UdC8LensCcGlbNIbO2WYk'
bot = telegram.Bot(token=bot_token)

def send_message(chat_id, text):
        bot.send_message(chat_id=chat_id, text=text)


# Replace 'YOUR_CHAT_ID' with the actual chat ID

send_message('-1001834878605', 'bhargav')
