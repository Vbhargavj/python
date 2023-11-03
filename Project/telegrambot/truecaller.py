import json
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from truecallerpy import search_phonenumber
userDict = [1241390756,]
adminid = 1241390756


def start(update, context):
    if update.message.from_user.id in userDict:

        update.message.reply_text(
            "Helloo you can find name of number no need to add +91")
    else:
        context.bot.send_message(
            chat_id="1241390756", text=f'{update.message.from_user.name} {update.message.from_user.id} ')
        update.message.reply_text(
            "you can not access the bot,if you access then contact 'mere mai bap ko ")


def add(update, context):

    id = int(context.args[0])
    update.message.reply_text(text=f'{id} added successfully')

    userDict.append(id)


def true(update, context):
    if update.message.from_user.id in userDict:
        number = update.message.text
        num = str(number)
        num = num.replace(' ', '')
        
        if num.replace('+', '').isnumeric():
            id = 'a1i0a--ftoz2jF1F_PHVBXRDdFKu_la7mME-fhFbTaLbVOtjCSUUNChLp6pkqNw9'
            response = search_phonenumber(number, "IN", id)
            data = response
            print(response)
            try:
                name = data["data"][0]["name"]
                email = data["data"][0]["internetAddresses"][0]["id"] if data["data"][0]["internetAddresses"] else None
                carrier = data["data"][0]["phones"][0]["carrier"]
                city = data["data"][0]["addresses"][0].get("city", None)
                timezone = data["data"][0]["addresses"][0]["timeZone"]
                gender = data["data"][0].get("gender", None)
                userprofile = f'Name:{name}\nGender:{gender}\nEmail: {email}\nCarrier:{carrier}\nCity:{city}\nTimeZone:{timezone}'
                context.bot.send_message(
                    chat_id=adminid, text=f'Num: {num}\n{userprofile}')
                update.message.reply_text(userprofile)
            except Exception as e:
                try:
                    name = data["data"][0]["name"]
                    phone = data["data"][0]["phones"][0]["e164Format"]
                    email = data["data"][0]["internetAddresses"][0]["id"] if data["data"][0]["internetAddresses"] else None
                    city = data["data"][0]["addresses"][0]["city"]
                    country = data["data"][0]["addresses"][0]["countryCode"]
                    gender = data["data"][0].get("gender", None)
                    userprofile = f'Name:{name}\nGender:{gender}\nEmail: {email}\nCarrier:{carrier}\nCity:{city}\nTimeZone:{timezone}'
                    context.bot.send_message(
                        chat_id=adminid, text=f'Num:{num}\n{userprofile}')
                    update.message.reply_text(userprofile)
                except Exception as e:
                    formatted_json = json.dumps(response, indent=4)
                    update.message.reply_text(formatted_json)
                    context.bot.send_message(chat_id=adminid,text=str(e))
                    
        else:
            update.message.reply_text("Enter a valid number")
    else:
        update.message.reply_text("You don't have access to this bot")


def main():

    updater = Updater(
        token='5975659245:AAFEebUbu3783BNxp-3FdBLCxkUNxAZF3Js', use_context=True)
    updater.bot.send_message(chat_id=adminid,text='hello i am online')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(MessageHandler(Filters.text, true))

    updater.start_polling()


if __name__ == '__main__':
    main()    
