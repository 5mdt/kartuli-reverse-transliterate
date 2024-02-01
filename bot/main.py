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


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Kartuli Reverse Trasliterate Bot! Send me Latin text, and I will convert it to Georgian."
    )


def latin_to_georgian(update: Update, context: CallbackContext) -> None:
    latin_text = update.message.text

    georgian_text = translit(latin_text, "ka")

    georgian_url = quote(georgian_text, safe="")

    yandex_translate_link_ka_to_en = (
        f"https://translate.yandex.com/?lang=ka-en&text={georgian_url}"
    )
    yandex_translate_link_ka_to_ru = (
        f"https://translate.yandex.com/?lang=ka-ru&text={georgian_url}"
    )
    yandex_translate_link_ka_to_uk = (
        f"https://translate.yandex.com/?lang=ka-uk&text={georgian_url}"
    )
    google_translate_link_ka_to_en = (
        f"https://translate.google.com/#view=home&op=translate&sl=ka&tl=en&text={georgian_url}"
    )
    google_translate_link_ka_to_ru = (
        f"https://translate.google.com/#view=home&op=translate&sl=ka&tl=ru&text={georgian_url}"
    )
    google_translate_link_ka_to_uk = (
        f"https://translate.google.com/#view=home&op=translate&sl=ka&tl=uk&text={georgian_url}"
    )

    response_message = (
        f"You can copy text from here for paste it in your favorite translate app:\n"
        f"```\n{georgian_text}\n```\n"
        f"Or use this link to popular translate apps:\n"
        f"- [Google.Translate KA🇬🇪>EN🇬🇧]({google_translate_link_ka_to_en})\n"
        f"- [Yandex.Translate KA🇬🇪>EN🇬🇧]({yandex_translate_link_ka_to_en})\n"
        f"\n"
        f"- [Google.Translate KA🇬🇪>RU🇷🇺]({google_translate_link_ka_to_ru})\n"
        f"- [Yandex.Translate KA🇬🇪>RU🇷🇺]({yandex_translate_link_ka_to_ru})\n"
        f"\n"
        f"- [Google.Translate KA🇬🇪>UK🇺🇦]({google_translate_link_ka_to_uk})\n"
        f"- [Yandex.Translate KA🇬🇪>UK🇺🇦]({yandex_translate_link_ka_to_uk})\n"
    )

    update.message.reply_text(
        response_message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


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
