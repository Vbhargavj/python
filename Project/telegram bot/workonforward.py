from telegram import Bot

bot = Bot(token="1925876251:AAGU1-DU8IpE5pC8oj1YVAxd6goLPJBRUSc")

destination_chat_id = 1241390756
original_chat_id = 
message_id = 8839

bot.forwardMessage(chat_id=destination_chat_id,
                   from_chat_id=original_chat_id, message_id=message_id)
