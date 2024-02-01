import os
from telegram import Update, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from transliterate import translit
from urllib.parse import quote


TOKEN = os.environ.get("BOT_TOKEN")

# Mapping of language codes to flags
LANGUAGE_FLAGS = {
    "en": "🇬🇧",
    "ru": "🇷🇺",
    "uk": "🇺🇦",
}


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Kartuli Reverse Transliterate Bot! Send me Latin text, and I will convert it to Georgian."
    )


def generate_translate_link(language_code: str, georgian_url: str) -> str:
    return f"https://translate.yandex.com/?lang=ka-{language_code}&text={georgian_url}"


def latin_to_georgian(update: Update, context: CallbackContext) -> None:
    try:
        latin_text = update.message.text
        georgian_text = translit(latin_text, "ka")
        georgian_url = quote(georgian_text, safe="")

        translate_languages = ["en", "ru", "uk"]

        # Send the plain Georgian text in the first message
        response_message = (
            f"You can copy text from here for paste it in your favorite translate app:\n"
            f"```\n{georgian_text}\n```\n"
        )
        update.message.reply_text(
            response_message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )

        for language_code in translate_languages:
            translate_link = generate_translate_link(
                language_code, georgian_url)
            response_message = (
                f"\n- {LANGUAGE_FLAGS[language_code]} {language_code.upper()} "
                f"[Google.Translate]({translate_link})"
            )
            # Send each link as a separate message
            update.message.reply_text(
                response_message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
            )

    except Exception as e:
        error_message = "An error occurred while processing your request. Please try again later."
        update.message.reply_text(error_message)


def main() -> None:
    try:
        if TOKEN is None:
            raise ValueError("BOT_TOKEN environment variable is not set.")

        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~
                       Filters.command, latin_to_georgian))

        updater.start_polling()
        updater.idle()

    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
