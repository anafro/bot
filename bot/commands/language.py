from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from bot.handler_wrapper import handler
from bot.localization import _, languages


@handler
async def do_language_command(update: Update, context: CallbackContext) -> None:
    button_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(language.name, callback_data=language_tag)]
        for language_tag, language in languages.items()
    ])
    await update.message.reply_markdown(_('language.select'), reply_markup=button_markup)