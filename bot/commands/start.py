from telegram import Update, ForceReply
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(f'''
    Hello, {user.mention_html()}!
    ''', reply_markup=ForceReply(selective=True))