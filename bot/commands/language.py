from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from bot.database.models.user import User
from bot.framework.chat import Chat
from bot.framework.message_handler_wrapper import message_handler
from bot.localization import _, languages


@message_handler
async def do_language_command(user: User, chat: Chat) -> None:
    button_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(language.name, callback_data=language_tag)]
        for language_tag, language in languages.items()
    ])
    await chat.send_message('language.select', markup=button_markup)
