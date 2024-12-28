from peewee import IntegerField, CharField, BooleanField
from telegram import Update

from bot.database.base_model import BaseModel


class User(BaseModel):
    telegram_id = IntegerField(unique=True)
    language = CharField(default='russian', null=False)
    is_welcomed = BooleanField(default=False, null=False)


def get_user(update: Update) -> tuple[User, bool]:
    return User.get_or_create(telegram_id=update.effective_user.id)