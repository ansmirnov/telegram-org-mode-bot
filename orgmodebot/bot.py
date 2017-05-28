import os
from telegram.ext import Updater, MessageHandler, Filters

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi. I'm bot.")

def update_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.all, start))

