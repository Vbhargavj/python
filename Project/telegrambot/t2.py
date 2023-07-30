import json
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from truecallerpy import search_phonenumber
# from server import server
userDict = [1241390756,]
adminid = 1241390756


def main():
    bot = telebot.TeleBot("6050075547:AAHc8zkVYGA2T8UdC8LensCcGlbNIbO2WYk")
    bot.send_message(adminid, "bhargav")

    @bot.message_handler(commands=['start'])
    def start(message):
        nUser = message.from_user.id
        if nUser in userDict:
            bot.reply_to(
                message, "Hello, you can find the name of a phone number without adding +91.")
        else:
            keyboard = [
                [InlineKeyboardButton("Add", callback_data=nUser)]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            bot.send_message(
                adminid, f'{message.from_user.first_name} {message.from_user.id}',reply_markup=reply_markup)

            bot.reply_to(
                message, "You do not have access to this bot. If you need access, contact 'mere mai bap ko'.")

    @bot.callback_query_handler(func=lambda call: True)
    def button_callback(call):
        user = call.from_user.id
        query = call.data
        print(call)
        print(query)
        print(user)
        bot.send_message(chat_id=adminid, text=query)

        if query.text == "Add":
            userDict.append(user)
        print(userDict)
    @bot.message_handler(commands=['add'])
    def add(message):
        id = int(message.text.split()[1])
        userDict.append(id)
        bot.reply_to(message, f"{id} added successfully.")

    @bot.message_handler(func=lambda message: True)
    def true(message):
        if message.from_user.id in userDict:
            number = message.text.strip().replace(' ', '')
            if number.replace("+", "").isnumeric():
                id = 'a1i0a--ftoz2jF1F_PHVBXRDdFKu_la7mME-fhFbTaLbVOtjCSUUNChLp6pkqNw9'
                response = search_phonenumber(number, "IN", id)
                data = response
                try:
                    name = data["data"][0]["name"]
                    email = data["data"][0]["internetAddresses"][0]["id"] if data["data"][0]["internetAddresses"] else None
                    carrier = data["data"][0]["phones"][0]["carrier"]
                    city = data["data"][0]["addresses"][0].get("city", None)
                    timezone = data["data"][0]["addresses"][0]["timeZone"]
                    gender = data["data"][0].get("gender", None)
                    userprofile = f'Name:{name}\nGender:{gender}\nEmail: {email}\nCarrier:{carrier}\nCity:{city}\nTimeZone:{timezone}'
                    bot.send_message(adminid, f'Num: {number}\n{userprofile}')
                    bot.reply_to(message, userprofile)
                except Exception as e:
                    try:
                        name = data["data"][0]["name"]
                        phone = data["data"][0]["phones"][0]["e164Format"]
                        email = data["data"][0]["internetAddresses"][0]["id"] if data["data"][0]["internetAddresses"] else None
                        city = data["data"][0]["addresses"][0]["city"]
                        country = data["data"][0]["addresses"][0]["countryCode"]
                        gender = data["data"][0].get("gender", None)
                        userprofile = f'Name:{name}\nGender:{gender}\nEmail: {email}\nCarrier:{carrier}\nCity:{city}\nTimeZone:{timezone}'
                        bot.send_message(
                            adminid, f'Num:{number}\n{userprofile}')
                        bot.reply_to(message, userprofile)
                        bot.send_message(adminid, str(e))
                    except Exception as e:
                        formatted_json = json.dumps(response, indent=4)
                        bot.reply_to(message, formatted_json)
                        bot.send_message(adminid, str(e))
            else:
                bot.reply_to(message, "Please enter a valid number.")
        else:
            bot.reply_to(message, "You do not have access to this bot.")

    bot.polling()


if __name__ == "__main__":
    #   server()
    main()
