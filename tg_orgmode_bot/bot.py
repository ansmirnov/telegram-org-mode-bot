import os
import sys
from telegram.ext import Updater, MessageHandler, Filters

INBOX_FILENAME = '~/inbox.org'

class Bot:
    def __init__(self, bot_token, working_dir, inbox_filename, chat_id):
        self.bot_token = bot_token
        self.working_dir = working_dir
        self.inbox_filename = inbox_filename
        self.chat_id = chat_id

    def save_inbox(self, bot, update):
        print(update)
        with open(self.inbox_filename, 'at+') as f:
            item = "* {}\n".format(update.message.text)
            f.write(item)
            update.message.reply_text("Sucessfull added!")

    def forbidden(self, bot, update):
        print("Forbidden!")
        print(update)
        msg = "Forbidden! Your chat_id: {} is not allowed!".format(update.message.chat.id)
        update.message.reply_text(msg)


    def run(self):
        updater = Updater(self.bot_token)

        chat_filters = Filters.chat(int(self.chat_id))
        
        updater.dispatcher.add_handler(MessageHandler(chat_filters, self.save_inbox))
        updater.dispatcher.add_handler(MessageHandler(~chat_filters, self.forbidden))

        updater.start_polling()
        updater.idle()
        
    
def run():
    bot_token = os.getenv("BOT_TOKEN")
    working_dir = os.getenv("WORKING_DIR", "~/")
    inbox_filename = os.getenv("INBOX_FILE", working_dir + "inbox.org")
    chat_id = os.getenv("CHAT_ID", None)

    if bot_token is None:
        print("You need to set BOT_TOKEN environment variable! See README.org file.")
    
    if chat_id is None:
        print("You need to set CHAT_ID environment variable! See README.org file.")
        return

    bot = Bot(bot_token, working_dir, inbox_filename, chat_id)

    bot.run()
