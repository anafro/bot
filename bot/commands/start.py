from telegram import Update
from telegram.ext import ContextTypes

from bot.commands.language import do_language_command
from bot.framework.chat import Chat
from bot.database.models.user import get_user
from bot.environment import environment


async def do_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user = update.effective_user
    user, user_created = get_user(update)
    chat = Chat(update, context)

    if user_created:
        await do_language_command(update, context)
    else:
        await chat.send_photo(
            "start.jpg", "start",
            user_mention=telegram_user.mention_html(),
            portfolio_link=environment.portfolio_link,
            freelancer_telegram_username=environment.freelancer_telegram_username,
        )