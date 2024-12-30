from collections.abc import Callable
from functools import wraps
from typing import TypeAlias

from telegram import Update
from telegram.ext import CallbackContext

from bot.database.models.user import get_user, User
from bot.framework.chat import Chat
from bot.localization import set_current_language


TelegramHandler: TypeAlias = Callable[[User, Chat], None]
FrameworkHandler: TypeAlias = Callable[[Update, CallbackContext], None]


def message_handler(handler: FrameworkHandler) -> TelegramHandler:
    @wraps(handler)
    def telegram_handler(update: Update, context: CallbackContext) -> None:
        user, _ = get_user(update)
        chat = Chat(update, context)
        set_current_language(user.language)
        return handler(user, chat)

    return telegram_handler