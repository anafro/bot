from typing import NewType

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler

from bot.database.models.user import User, get_user
from bot.framework.chat import Chat
from bot.framework.message_handler_wrapper import message_handler
from bot.localization import _


OrderConversationState: type = NewType("OrderConversationState", int)
(ASK_FOR_REFERENCES, KEEP_ASKING_FOR_REFERENCES) = range(2)

@message_handler
async def create_order_and_ask_for_type(user: User, chat: Chat) -> int:
    await chat.send_message("order.start")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(_(f"order.type.{order_type}"), callback_data=order_type)]
        for order_type in ['landing', 'platform', 'portfolio', 'other']
    ])

    await chat.send_message("order.type.select", markup=keyboard)
    return ASK_FOR_REFERENCES


@message_handler
async def handle_type_and_ask_for_reference(user: User, chat: Chat) -> int:
    order = user.get_draft()
    order_type = chat.get_pressed_button_data()
    order.type = order_type
    order.save()

    await chat.send_message("order.reference.ask")

    return KEEP_ASKING_FOR_REFERENCES


@message_handler
async def handle_reference_and_ask_for_reference(user: User, chat: Chat) -> int:
    order = user.get_draft()
    order.add_reference(chat.update.message.text)

    button_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(_("order.reference.stop-asking"), callback_data="stop")]
    ])
    await chat.send_message("order.reference.keep-asking", markup=button_markup)

    return KEEP_ASKING_FOR_REFERENCES


@message_handler
async def stop_asking_for_references_and_ask_show_price(user: User, chat: Chat) -> int:
    await chat.send_message("order.created")

    return ConversationHandler.END