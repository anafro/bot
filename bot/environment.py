import os
from dataclasses import dataclass
import dotenv


@dataclass
class Environment:
    telegram_api_token: str


def load_environment_variables() -> Environment:
    is_any_variable_set = dotenv.load_dotenv(encoding='utf-8')

    if not is_any_variable_set:
        raise ValueError("No env variable set")

    telegram_api_token = get_environment_variable("TELEGRAM_API_TOKEN")
    return Environment(telegram_api_token)


def get_environment_variable(variable_name: str) -> str:
    environment_variable = os.getenv(variable_name)

    if environment_variable is None:
        raise ValueError(f'The required environment variable "{variable_name}" does not exist. Add it to .env file.')
    else:
        return environment_variable