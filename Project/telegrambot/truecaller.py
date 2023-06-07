from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from truecallerpy import search_phonenumber
userDict = [1241390756,]


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

    userDict.append(id)


def true(update, context):

    if update.message.from_user.id in userDict:

        number = update.message.text
        num=str(number)
        num=num.replace(' ','')
    
        print(num)
        if num.replace('+','').isnumeric():            

            id = 'a1i0a--ftoz2jF1F_PHVBXRDdFKu_la7mME-fhFbTaLbVOtjCSUUNChLp6pkqNw9'

            response = (search_phonenumber(number, "IN", id))

            try:
                name = response['data'][0]['name']
                gender = response['data'][0]['gender']
                email = response['data'][0]['internetAddresses'][0]['id']
                carrier = response['data'][0]['phones'][0]['carrier']
                city = response['data'][0]['addresses'][0]['city']
                timezone = response['data'][0]['addresses'][0]['timeZone']

                userprofile = f'Name:{name}\nGender:{gender}\nEmail: {email}\nCarrier:{carrier}\nCity:{city}\nTimeZone:{timezone}'
                update.message.reply_text(userprofile)
            except Exception as e:
                update.message.reply_text("kaik khami avi")
        else:
            update.message.reply_text("Enter valid number")
    else:
        update.message.reply_text("BSDK don't use me")


def main():

    updater = Updater(
        token='6050075547:AAHc8zkVYGA2T8UdC8LensCcGlbNIbO2WYk', use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('add', add))
    dispatcher.add_handler(MessageHandler(Filters.text, true))
    
    
    updater.start_polling()


if __name__ == '__main__':
    main()    # i want number,name,email,carrier,city,country,timezone ,imageurl
