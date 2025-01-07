from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from termcolor import colored

from bot.commands.cancel import do_cancel_command
from bot.commands.command_list import add_command_handlers
from bot.database.database_management import create_database_tables
from bot.environment import environment
from bot.exception_hooking import initialize_custom_exception_hook
from bot.localization import load_language_messages, set_current_language
from bot.message_handlers.button_handler_list import add_button_handlers
from bot.message_handlers.order_message_handlers import ASK_FOR_REFERENCES, create_order_and_ask_for_type, \
    handle_type_and_ask_for_reference, KEEP_ASKING_FOR_REFERENCES, handle_reference_and_ask_for_reference, \
    stop_asking_for_references_and_ask_show_price


def main() -> None:
    application: Application = Application.builder().token(environment.telegram_api_token).build()

    initialize_custom_exception_hook()
    load_language_messages()
    create_database_tables()
    add_command_handlers(application)
    add_button_handlers(application)
    set_current_language('russian')

    order_conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler('order', create_order_and_ask_for_type)
        ],

        states={
            ASK_FOR_REFERENCES: [CallbackQueryHandler(handle_type_and_ask_for_reference)],
            KEEP_ASKING_FOR_REFERENCES: [
                MessageHandler(callback=handle_reference_and_ask_for_reference, filters=filters.TEXT),
                CallbackQueryHandler(callback=stop_asking_for_references_and_ask_show_price, pattern="^stop$")
            ]
        },

        fallbacks=[
            CommandHandler("cancel", do_cancel_command)
        ],
    )

    print(colored(' Running ', 'white', 'on_light_blue'), 'The Telegram bot is running and receiving messages. Ctrl+C to stop.')
    application.add_handler(order_conversation_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()