import os
from dataclasses import dataclass
import dotenv


@dataclass
class Environment:
    telegram_api_token: str
    freelancer_telegram_username: str
    portfolio_link: str


def load_environment_variables() -> Environment:
    is_any_variable_set = dotenv.load_dotenv(encoding='utf-8')

    if not is_any_variable_set:
        raise ValueError("No env variable set")

    return Environment(
        telegram_api_token=get_environment_variable("TELEGRAM_API_TOKEN"),
        freelancer_telegram_username=get_environment_variable("FREELANCER_TELEGRAM_USERNAME"),
        portfolio_link=get_environment_variable("PORTFOLIO_LINK"),
    )


def get_environment_variable(variable_name: str) -> str:
    environment_variable = os.getenv(variable_name)

    if environment_variable is None:
        raise ValueError(f'The required environment variable "{variable_name}" does not exist. Add it to .env file.')
    else:
        return environment_variable


environment = load_environment_variables()