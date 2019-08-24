import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Updater

from config import BOT_TOKEN
from src.messages import HELP_CMD, START_CMD_CHANNEL, START_CMD_GROUP, START_CMD_USER

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

END_CONV = ConversationHandler.END


def start(update: Update, context: CallbackContext):
    """ Manages the start command """
    # https://python-telegram-bot.readthedocs.io/en/stable/telegram.user.html
    chat = update.effective_chat
    message = START_CMD_GROUP
    chat_type = chat.type
    if chat_type == chat.CHANNEL:
        message = START_CMD_CHANNEL
    elif chat_type == chat.PRIVATE:
        message = START_CMD_USER
    context.bot.send_message(chat_id=chat['id'], text=message)
    result = -1
    return result


def help_cmd(update: Update, context: CallbackContext):
    """ Manages the help command """
    chat = update.effective_chat
    message = HELP_CMD
    context.bot.send_message(chat_id=chat['id'], text=message)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handler for the /start command
    # https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)

    # Handler for the /help command
    # https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html
    help_handler = CommandHandler('help', help_cmd)
    dp.add_handler(help_handler)

    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
