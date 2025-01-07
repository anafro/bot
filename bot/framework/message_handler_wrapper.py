from collections.abc import Callable
from functools import wraps
from typing import Any

from telegram import Update
from telegram.ext import CallbackContext

from bot.database.models.user import get_user, User
from bot.framework.chat import Chat
from bot.localization import set_current_language

type TelegramHandler = Callable[[Update, CallbackContext], Any]
type FrameworkHandler = Callable[[User, Chat], Any]


def message_handler(handler: FrameworkHandler) -> TelegramHandler:
    @wraps(handler)
    async def telegram_handler(update: Update, context: CallbackContext) -> None:
        user, _ = get_user(update)
        chat = Chat(update, context)
        set_current_language(user.language)

        if update.callback_query is not None:
            await update.callback_query.answer()

        return await handler(user, chat)

    return telegram_handler