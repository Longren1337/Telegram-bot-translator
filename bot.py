import telebot, configparser
from telebot  import types, apihelper
from googletrans import Translator

#syntax
#-------------------------------#
bot = telebot.TeleBot(token)
translator = Translator()
#-------------------------------#

#Работа с ботом

#-------------------------------#

@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='🎓Translate', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(information='🕵Info', callback_data=4))
    bot.send_message(message.chat.id, "Добро пожаловать! \nЯ бот-переводчик и готов переводить твои фразы.", reply_markup = markup)