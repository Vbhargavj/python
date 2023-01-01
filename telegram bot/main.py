# import telegram

# # Replace YOUR_BOT_TOKEN with the bot token you received from the Bot Father
# bot = telegram.Bot(token='api_key')

# # Define a custom keyboard with buttons for the user to choose from
# keyboard = [['Option 1', 'Option 2'], ['Option 3']]

# YOUR_CHAT_ID = 1241390756
# GROUP_CHAT_ID = 5422764153
# MESSAGE_ID = 14
# # Create a reply markup object with the custom keyboard
# reply_markup = telegram.ReplyKeyboardMarkup(keyboard)

# # Send a message with the custom keyboard
# bot.send_message(chat_id=YOUR_CHAT_ID,
#                  text='Please choose an option:', reply_markup=reply_markup)

# # Handle the update that contains the callback query


# def handle_update(update):
#     # Check if the update contains a callback query
#     if update.callback_query:
#         # Get the data from the callback query
#         data = update.callback_query.data
#         # Check if the data is "Option 1"
#         if data == 'Option 1':
#             # Get the message that contains the document you want to forward
#             message = bot.get_message(
#                 chat_id='GROUP_CHAT_ID', message_id='MESSAGE_ID')
#             # Forward the document
#             bot.forward_message(chat_id=update.callback_query.message.chat_id,
#                                 from_chat_id='GROUP_CHAT_ID', message_id=message.message_id)


# # Set the update handler
# updater = telegram.ext.Updater(bot=bot)
# updater.dispatcher.add_handler(
#     telegram.ext.CallbackQueryHandler(handle_update))

# # Start the bot
# updater.start_polling()
import telegram
YOUR_BOT_TOKEN = '5369531550:AAFekKbGtdylAHeTTj06Zyd5YuMWyHrdH_0'
# Replace YOUR_BOT_TOKEN with the bot token you received from the Bot Father
bot = telegram.Bot(token=YOUR_BOT_TOKEN)

# Define a custom keyboard with buttons for the user to choose from
keyboard = [['Option 1', 'Option 2'], ['Option 3']]

# Replace YOUR_CHAT_ID and GROUP_CHAT_ID with the actual chat IDs
YOUR_CHAT_ID = bot.get
GROUP_CHAT_ID = 67890

# Replace MESSAGE_ID with the actual message ID of the message that contains the document you want to forward
MESSAGE_ID = 14

# Create a reply markup object with the custom keyboard
reply_markup = telegram.ReplyKeyboardMarkup(keyboard)

# Send a message with the custom keyboard
bot.send_message(chat_id=YOUR_CHAT_ID,
                 text='Please choose an option:', reply_markup=reply_markup)

# Handle the update that contains the callback query


def handle_update(update):
    # Check if the update contains a callback query
    if update.callback_query:
        # Get the data from the callback query
        data = update.callback_query.data
        # Check if the data is "Option 1"
        if data == 'Option 1':
            # Get the message that contains the document you want to forward
            message = bot.get_message(
                chat_id=GROUP_CHAT_ID, message_id=MESSAGE_ID)
            # Forward the document
            bot.forward_message(chat_id=update.callback_query.message.chat_id,
                                from_chat_id=GROUP_CHAT_ID, message_id=message.message_id)


# Set the update handler
updater = telegram.ext.Updater(bot=bot)
updater.dispatcher.add_handler(
    telegram.ext.CallbackQueryHandler(handle_update))

# Start the bot
updater.start_polling()
