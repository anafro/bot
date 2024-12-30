from peewee import ForeignKeyField, CharField

from bot.database.base_model import BaseModel
from bot.database.models.user import User


class Order(BaseModel):
    user = ForeignKeyField(User, backref='orders')
    company_name = CharField(null=False)