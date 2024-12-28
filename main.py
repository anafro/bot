from telegram import Update
from telegram.ext import Application, CommandHandler
from termcolor import colored

from bot.commands.command_list import command_list
from bot.environment import load_environment_variables, Environment
from bot.exception_hooking import initialize_custom_exception_hook
from bot.localization import load_language_messages


def main() -> None:
    initialize_custom_exception_hook()
    load_language_messages()
    environment: Environment = load_environment_variables()
    application: Application = Application.builder().token(environment.telegram_api_token).build()

    for command in command_list:
        application.add_handler(CommandHandler(command.__name__, command))

    print(colored(' Running ', 'white', 'on_light_blue'), 'The Telegram bot is running and receiving messages. Ctrl+C to stop.')
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()