


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)
from bot import (
    Config,
    INPUT_PHONE_NUMBER,
    INPUT_TG_CODE
)
from bot.modules.start_text_ import start
from bot.modules.my_telegram_org.input_phone_number_ import (
    input_phone_number
)
from bot.modules.my_telegram_org.input_tg_code_ import (
    input_tg_code
)


""" Initial Entry Point """
# Create the Updater and pass it your bot's token.
updater = Updater(Config.TG_BOT_TOKEN)

# Get the dispatcher to register handlers
tg_bot_dis_patcher = updater.dispatcher

# Add conversation handler with the states
conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states={
        INPUT_PHONE_NUMBER: [MessageHandler(
            Filters.text | Filters.contact,
            input_phone_number
        )],

        INPUT_TG_CODE: [MessageHandler(
            Filters.text,
            input_tg_code
        )],
    },

    fallbacks=[CommandHandler('start', start)]
)

tg_bot_dis_patcher.add_handler(conv_handler)

# log all errors
# tg_bot_dis_patcher.add_error_handler(error)

# Start the Bot
if Config.WEBHOOK:
    updater.start_webhook(
        listen="0.0.0.0",
        port=Config.PORT,
        url_path=Config.TG_BOT_TOKEN
    )
    # https://t.me/c/1186975633/22915
    updater.bot.set_webhook(
        url=Config.URL + Config.TG_BOT_TOKEN
    )
else:
    updater.start_polling()

print(
    """
Bot Started: Join @DYNA_SUPPORT (https://t.me/DYNA_SUPPPORT)
    """
)

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
