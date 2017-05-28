import os
from telegram.ext import Updater
import bot

TOKEN = os.environ.get('BOT_TOKEN', '')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)

bot.update_handlers(updater.dispatcher)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)

updater.idle()

