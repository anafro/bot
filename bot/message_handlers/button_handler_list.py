import re

from telegram.ext import Application, CallbackQueryHandler

from bot.localization import languages
from bot.message_handlers.language import handle_language_buttons


def add_button_handlers(application: Application) -> None:
    language_callback_data_pattern = "|".join(map(re.escape, languages.keys()))
    application.add_handler(CallbackQueryHandler(handle_language_buttons, pattern=f"^({language_callback_data_pattern})$"))