from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from termcolor import colored

from bot.button_handlers.button_handler_list import button_handler_list, add_button_handlers
from bot.commands.command_list import command_list, add_command_handlers
from bot.database.database_management import create_database_tables
from bot.environment import environment
from bot.exception_hooking import initialize_custom_exception_hook
from bot.localization import load_language_messages, set_current_language


def main() -> None:
    application: Application = Application.builder().token(environment.telegram_api_token).build()

    initialize_custom_exception_hook()
    load_language_messages()
    create_database_tables()
    add_command_handlers(application)
    add_button_handlers(application)
    set_current_language('russian')

    print(colored(' Running ', 'white', 'on_light_blue'), 'The Telegram bot is running and receiving messages. Ctrl+C to stop.')
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()