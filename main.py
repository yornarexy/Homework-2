import telebot
from mamamdoor import keys
from access import TOKEN
from uextensions import ConvertionException, OldMoney

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hi! для продолжения введите /richbitch')

@bot.message_handler(commands = ['richbitch'])
def richbitch(message: telebot.types.Message):
    text = 'Введите: <количество переводимой валюты>\n <имя переводимой валюты* в ед.ч.>\n <в какую валюту перевести в ед.ч.>\n * список валют доступен по команде /values'
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступно для конвертации:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        amount, quote, base = values

        if quote == 'токен':
           amount = OldMoney.convert_token(amount, quote)
           quote == 'доллар'
        else:
           total_base = OldMoney.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()


