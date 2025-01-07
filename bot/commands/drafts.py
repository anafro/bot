from bot.database.models.user import User
from bot.framework.chat import Chat
from bot.framework.message_handler_wrapper import message_handler


@message_handler
async def do_drafts_command(user: User, chat: Chat) -> None:
    drafts = user.get_drafts()

    if len(drafts) == 0:
        await chat.send_message("draft.empty")
    else:
        await chat.send_message("draft.list")

    await chat.send_message(chat.recall("order_type") or "no type selected")