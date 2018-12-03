from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text(
        'Hello {}, send the photo or image'.format(update.message.from_user.first_name))

def img(bot, update):
    print(update.message.photo)
    file = bot.getFile(update.message.photo[-1].file_id)
    print ("file_id: " + str(update.message.photo[-1].file_id))
    try:
        import os
        os.remove('photo.jpg')
    except Exception as e:
        print(e)

    print("downloading")
    file.download('photo.jpg')

    #Get data from image
    import OLP
    datas, predicted = OLP.run('photo.jpg')

    update.message.reply_text(str(predicted))

updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, img))

updater.start_polling()
updater.idle()