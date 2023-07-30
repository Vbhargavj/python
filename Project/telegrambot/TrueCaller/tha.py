import json
import telebot
from truecallerpy import search_phonenumber
# from server import server
userDict = {1241390756}
adminid = 1241390756
f=True

def main():
    bot = telebot.TeleBot("1925876251:AAEVFKKTFVCidza_nAV6kkD_kQx47nr7gGI")
    bot.send_message(adminid, "bhargav")
    global f
    @bot.message_handler(commands=['start'])
    def start(message):
        new_user_message = message
        nUser = new_user_message.from_user.id
        if f==False:
            return 
            
        elif nUser not in userDict:
            
            userDict.add(nUser)

        # Build the notification message
            notification_text = "ToTaL UsEr: {}\nUser_id: {}\nNew user: {}\nUsername: @{}".format(len(userDict), nUser,
                                                                                                  new_user_message.from_user.first_name, new_user_message.from_user.username)
            bot.send_message(chat_id="1241390756", text=notification_text)
        
            # bot.send_message(
            #     adminid, f'{message.from_user.first_name} `/add {message.from_user.id}`', parse_mode='MarkdownV2')
            # bot.reply_to(
            #     message, "You do not have access to this bot. If you need access, contact 'mere mai bap ko'.")
        bot.reply_to(
            message, "Hello, you can find the name of a phone number without adding +91.")
    @bot.message_handler(commands=['add'])
    def add(message):
        id = int(message.text.split()[1])
        userDict.add(id)
        bot.reply_to(message, f"{id} added successfully.")

    @bot.message_handler(commands=['f'])
    def fs(message):
        global f
        if f==True:
            f=False
        else:
            f=True
    @bot.message_handler(func=lambda message: True)
    def true(message):
        if f==False:
            return 
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
