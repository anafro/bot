from telegram.ext import Application, CallbackQueryHandler

from bot.button_handlers.language import handle_language_buttons


button_handler_list = [
    handle_language_buttons,
]


def add_button_handlers(application: Application) -> None:
    for button_handler in button_handler_list:
        application.add_handler(CallbackQueryHandler(button_handler))