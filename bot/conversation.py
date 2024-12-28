from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.localization import _


async def send_message(update: Update, context: CallbackContext, message_tag: str, **message_placeholders: object) -> None:
    await context.bot.send_message(update.effective_chat.id, _(message_tag, **message_placeholders), parse_mode=ParseMode.MARKDOWN)
