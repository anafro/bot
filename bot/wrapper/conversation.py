from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.localization import _


parse_mode: str = ParseMode.HTML


async def send_message(update: Update, context: CallbackContext, message_tag: str, **message_placeholders: object) -> None:
    await context.bot.send_message(update.effective_chat.id, _(message_tag, **message_placeholders), parse_mode=parse_mode)


async def send_photo(update: Update, context: CallbackContext, photo_file_name: str, message_tag: str, **message_placeholders: object) -> None:
    await context.bot.send_photo(update.effective_chat.id, open(f"./photos/{photo_file_name}", "rb"),  _(message_tag, **message_placeholders), parse_mode=parse_mode)
