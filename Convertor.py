import telebot
from telebot import types
from currency_converter import CurrencyConverter
bot = telebot.TeleBot('token')

cur = CurrencyConverter()
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'hello! vvedite summu: ')
    bot.register_next_step_handler(message, summ)

def summ(message):
    global money
    try:
        money = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Syntax error, vvedite vernoe znachenie')
        bot.register_next_step_handler(message, summ)
        return
    if money > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        bot1 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        bot2 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        markup.add(bot1, bot2)
        bot.send_message(message.chat.id, 'choose any: ', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Error! Try again:')
        bot.register_next_step_handler(message, summ)

bot.polling(non_stop=True)
