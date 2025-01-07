from peewee import ForeignKeyField, CharField, BooleanField, AutoField, IntegerField
from telegram import Update

from bot.database.base_model import BaseModel


class User(BaseModel):
    id = AutoField()
    telegram_id = IntegerField(unique=True)
    language = CharField(default='russian', null=False)
    is_welcomed = BooleanField(default=False, null=False)

    def get_draft(self) -> 'Order':
        draft = (Order
                .get((Order.user == self) & (Order.is_draft == True)))

        if draft is not None:
            return draft

        return Order.create(user=self)


class Order(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref='orders')
    type = CharField(null=True)
    is_draft = BooleanField(null=False, default=True)

    def get_references(self) -> list['OrderReference']:
        return (OrderReference
                .select()
                .where(OrderReference.order == self))

    def add_reference(self, text: str) -> None:
        OrderReference.create(order=self, text=text)


class OrderReference(BaseModel):
    id = AutoField()
    order = ForeignKeyField(model=Order, backref="order_references")
    text = CharField(null=False)


def get_user(update: Update) -> tuple[User, bool]:
    return User.get_or_create(telegram_id=update.effective_user.id)