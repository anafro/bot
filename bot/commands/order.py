from telegram import Update
from telegram.ext import CallbackContext

from bot.database.models.user import get_user, User
from bot.framework.chat import Chat
from bot.framework.message_handler_wrapper import message_handler


@message_handler
async def do_order_command(user: User, chat: Chat) -> None:
    await chat.send_message("order.welcome")
