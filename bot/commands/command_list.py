﻿from telegram.ext import Application, CommandHandler

from bot.commands.language import do_language_command
from bot.commands.order import do_order_command
from bot.commands.start import do_start_command


command_list = [
    ("start", do_start_command),
    ("language", do_language_command),
    ("order", do_order_command),
]


def add_command_handlers(application: Application) -> None:
    for command_name, command_function in command_list:
        application.add_handler(CommandHandler(command_name, command_function))