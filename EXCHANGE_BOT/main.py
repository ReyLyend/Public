import telebot
from config import TOKEN
from extensions import MoneyExchange
from extensions import APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Welcome to MoneyExchangeBot\n' \
           'Input command in following format:\n' \
           'Currency From\n' \
           'Currency To\n' \
           'Amount\n' \
           'Example: EUR USD 100\n' \
           'List of available currencies: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.send_message(message.chat.id, MoneyExchange.get_list())

@bot.message_handler(content_types=['text'])
def exchange(message: telebot.types.Message):
    if message.text in {'start', 'help', 'Start', 'Help'}:
        start_help(message)
    else:
        try:
            response = message.text.split(' ')
            if len(response) != 3:
                raise APIException('Wrong amount of arguments for exchange. \n'
                                   f'{len(response)} out of 3')
            base, quote, amount = response
        except Exception as error:
            bot.reply_to(message, f'{error}')
        else:
            bot.send_message(message.chat.id, MoneyExchange.get_price(base, quote, amount))

bot.polling()