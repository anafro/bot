from pathlib import Path
from dataclasses import dataclass
from typing import Optional

import yaml
from typing_extensions import OrderedDict

from bot.utils.dot_key_access import get_value_by_dot_key
from bot.utils.named_placeholder_formatting import replace_named_placeholders
from bot.utils.semantic_indexing import first_value


@dataclass
class Language:
    messages: dict
    language_name: str

    def get_message(self, message_key: str, message_placeholders: dict[str, str]) -> str:
        language_message: Optional[str] = get_value_by_dot_key(self.messages, message_key)

        if language_message is None:
            return message_key
        else:
            return replace_named_placeholders(language_message, message_placeholders)


languages: OrderedDict[str, Language] = OrderedDict()
current_language: Optional[Language] = None


def load_language_messages() -> None:
    for yaml_path in Path('./languages').rglob("*.yaml"):
        load_language_message_file(yaml_path)

    global current_language
    current_language = first_value(languages)


def load_language_message_file(path: str) -> None:
    with open(path) as yaml_file:
        language_messages = yaml.safe_load(yaml_file)
        language_name = language_messages["name"]
        language_tag = language_messages["tag"]

        if language_name is None:
            raise ValueError(f"The language file must include its name. Add 'name' to '{path}'.")

        if language_tag is None:
            raise ValueError(f"The language file must include its tag. Add 'tag' to '{path}'.")

        languages[language_tag] = Language(language_messages, language_name)


def set_current_language(language_tag: str) -> None:
    global current_language
    current_language = languages[language_tag]


def _(message_key: str, **message_placeholders: str) -> str:
    if current_language is None:
        return message_key
    else:
        return current_language.get_message(message_key, message_placeholders)