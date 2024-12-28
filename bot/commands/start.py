from telegram import Update, ForceReply
from telegram.ext import ContextTypes

from bot.commands.language import do_language_command
from bot.conversation import send_message
from bot.database.models.user import User, get_user
from bot.localization import _


async def do_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user = update.effective_user
    user, user_created = get_user(update)

    if user_created:
        await do_language_command(update, context)
    else:
        await send_message(update, context, "welcome", user_mention=telegram_user.mention_markdown())