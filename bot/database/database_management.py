from bot.database.database_connection import database_connection
from bot.database.models.user import User


def create_database_tables():
    database_connection.create_tables([
        User,
    ])