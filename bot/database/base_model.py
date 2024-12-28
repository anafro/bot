from peewee import Model

from bot.database.database_connection import database_connection


class BaseModel(Model):
    class Meta:
        database = database_connection