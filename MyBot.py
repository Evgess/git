import telebot
from geopy import Photon
import buttons as bt
from telebot import types
import cons


geolocator = Photon(user_agent="geo_locator", timeout=10)

bot = telebot.TeleBot('7397938366:AAHy5QLABEyXEraqLcRPOfAaKnCJH3fdD18')



@bot.message_handler(commands=['start'])

def start(message):
    if cons.lang == 'ru':
        user_id = message.from_user.id
        bot.send_message(user_id, "Добро пожаловать в никуда!)\n\n"
                                  "Введите своё имя: ")
    elif cons.lang == 'en':
        user_id = message.from_user.id
        bot.send_message(user_id, "Welcome to nowhere!)\n\n"
                                  "Enter your name: ")


        bot.register_next_step_handler(message, get_name)
        start_markup = types.ReplyKeyboardMarkup(True, False)

        start_markup.row('English', 'Русский язык')
@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == 'English':
        cons.lang = 'en'
        msg = bot.send_message(message.chat.id, 'Your language is -'+cons.lang+' -')
        bot.register_next_step_handler(msg, start)
    elif message.text == 'Русский язык':
        cons.lang = 'ru'
        msg = bot.send_message(message.chat.id, 'Вы выбрали русский язык-'+cons.lang+' -')
        bot.register_next_step_handler(msg, start)


def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Отлично! Теперь поделитесь своими контактами",
                     reply_markup=bt.phone_number_bt())
    bot.register_next_step_handler(message, get_phone, name)

def get_phone(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Отлично! Теперь отправьте локацию",
                         reply_markup=bt.location_bt())
        bot.register_next_step_handler(message, get_location, name, phone_number)
    else:
        bot.send_message(user_id, "Ошибка! Отправьте свои контакты по кнопке в меню",
                         reply_markup=bt.phone_number_bt())
        bot.register_next_step_handler(message, get_phone, name)
def get_location(message, name, phone_number):
    user_id = message.from_user.id
    location = message.location
    address = geolocator.reverse((location.latitude, location.longitude)).address

    bot.send_message(user_id, "Вы успешно прошли регистрацию!")
    print(name, phone_number, address)

bot.infinity_polling()