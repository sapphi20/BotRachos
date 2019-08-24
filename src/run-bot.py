import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Updater

from config import BOT_TOKEN
from src.messages import START_CMD

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

END_CONV = ConversationHandler.END


def start(update: Update, context: CallbackContext):
    """ Manages the start command """
    # https://python-telegram-bot.readthedocs.io/en/stable/telegram.user.html
    user = update.effective_user
    context.bot.send_message(chat_id=user['id'], text=START_CMD)
    result = -1
    return result


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
