import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, Updater

from config import BOT_TOKEN
from src.messages import HELP_CMD, START_CMD_CHANNEL, START_CMD_GROUP, START_CMD_USER, START_REPEATED

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CONV_STATES = {
    'GROUP': 1,
    'CANDIDATES': 2,
    'RANDOMIZING': 3,
    'EXIT': ConversationHandler.END,
}


def start(update: Update, context: CallbackContext):
    """ Manages the start command """
    # https://python-telegram-bot.readthedocs.io/en/stable/telegram.user.html
    chat = update.effective_chat
    result = CONV_STATES['GROUP']
    message = START_CMD_GROUP
    chat_type = chat.type
    if chat_type == chat.CHANNEL:
        message = START_CMD_CHANNEL
        result = CONV_STATES['EXIT']
    elif chat_type == chat.PRIVATE:
        message = START_CMD_USER
        result = CONV_STATES['EXIT']
    context.bot.send_message(chat_id=chat['id'], text=message)
    return result


def help_cmd(update: Update, context: CallbackContext):
    """ Manages the help command """
    chat = update.effective_chat
    message = HELP_CMD
    context.bot.send_message(chat_id=chat['id'], text=message)


def start_repeated(update: Update, context: CallbackContext):
    """ Manages the start command when it has been used already in a group """
    chat = update.effective_chat
    message = START_REPEATED
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

    # Handler to allow group commands only in groups
    # https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html
    start_handler = ConversationHandler(
        [CommandHandler('start', start)],
        {1: [CommandHandler('start', start_repeated)]},
        [],
    )
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
