from telegram.ext import ConversationHandler

from bot.database.models.user import User
from bot.framework.chat import Chat
from bot.framework.message_handler_wrapper import message_handler


@message_handler
async def do_cancel_command(user: User, chat: Chat) -> int:
    await chat.send_message("order.cancel")
    return ConversationHandler.END