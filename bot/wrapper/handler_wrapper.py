from collections.abc import Callable
from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from bot.database.models.user import get_user
from bot.localization import set_current_language


def handler(handler: Callable[[Update, CallbackContext], None]) -> Callable[[Update, CallbackContext], None]:
    @wraps(handler)
    def wrapped_handler(update: Update, context: CallbackContext) -> None:
        user, _ = get_user(update)
        set_current_language(user.language)
        return handler(update, context)

    return wrapped_handler