﻿from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.commands.start import do_start_command
from bot.database.models.user import get_user
from bot.handler_wrapper import handler
from bot.localization import _, languages, set_current_language


@handler
async def handle_language_buttons(update: Update, context: CallbackContext) -> None:
    user, user_created = get_user(update)
    query = update.callback_query
    language_tag = query.data

    if language_tag not in languages.keys():
        return

    language = languages[language_tag]
    user.language = language_tag
    user.save()
    set_current_language(language_tag)

    await query.answer()
    await query.delete_message()
    await context.bot.send_message(update.effective_chat.id, _("language.selected", language=language.name), parse_mode=ParseMode.MARKDOWN)

    if not user.is_welcomed:
        user.is_welcomed = True
        user.save()
        await do_start_command(update, context)