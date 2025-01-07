from dataclasses import dataclass
from typing import Optional

from telegram import Update
from telegram._utils.types import ReplyMarkup
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.localization import _


parse_mode: str = ParseMode.HTML

@dataclass
class Chat:
    update: Update
    context: CallbackContext

    async def send_message(
            self,
            message_tag: str,
            *,
            markup: Optional[ReplyMarkup] = None,
            **message_placeholders: object
    ) -> None:
        await self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=_(message_tag, **message_placeholders),
            parse_mode=parse_mode,
            reply_markup=markup,
        )

    async def send_photo(
            self,
            photo_file_name: str,
            message_tag: str,
            **message_placeholders: object
    ) -> None:
        await self.context.bot.send_photo(self.update.effective_chat.id, open(f"./photos/{photo_file_name}", "rb"),  _(message_tag, **message_placeholders), parse_mode=parse_mode)

    def get_pressed_button_data(self) -> str:
        return self.update.callback_query.data

    @property
    def storage(self) -> dict[str, str]:
        return self.context.user_data

    def remember(self, data_tag: str, data: str) -> None:
        self.context.user_data[data_tag] = data

    def recall(self, data_tag: str) -> Optional[str]:
        return self.storage.get(data_tag)
