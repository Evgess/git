import telebot

bot = telebot.TeleBot('7397938366:AAHy5QLABEyXEraqLcRPOfAaKnCJH3fdD18')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Welcome!')
