from telegram import Update, ForceReply
from telegram.ext import ContextTypes

from bot.localization import _


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(_('start.welcome', user_mention=user.mention_html()))