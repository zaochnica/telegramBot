from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import TG_TOKEN, TG_API_URL


def sms(bot, update):
    print('Кто отправил команду /start .')
    bot.message.reply_text('Здраствуйте, {}, я Бот!'.format(bot.message.chat.first_name))


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()


main()
