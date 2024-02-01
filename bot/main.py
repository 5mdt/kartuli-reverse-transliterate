import os
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from transliterate import translit

# Retrieve the Telegram Bot Token from the environment variable
TOKEN = os.environ.get("BOT_TOKEN")


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Latin to Georgian Transliteration Bot! Send me Latin text, and I will convert it to Georgian."
    )


def latin_to_georgian(update: Update, context: CallbackContext) -> None:
    latin_text = update.message.text
    georgian_text = translit(
        latin_text, "ka"
    )

    update.message.reply_text(f"Converted to Georgian: {georgian_text}")


def main() -> None:

    if TOKEN is None:
        raise ValueError("BOT_TOKEN environment variable is not set.")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~
                   Filters.command, latin_to_georgian))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
