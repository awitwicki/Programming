from telegram.ext import Updater, CommandHandler

def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def bye(bot, update):
    print(update.message.from_user)
    update.message.reply_text('Bye {}'.format(update.message.from_user.first_name))


updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('bye', bye))

updater.start_polling()
updater.idle()