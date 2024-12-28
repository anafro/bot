def replace_named_placeholders(string: str, named_placeholders: dict[str, str]) -> str:
    formatted_string = string

    for placeholder_name, placeholder_value in named_placeholders.items():
        formatted_string = formatted_string.replace(f'[{placeholder_name}]', placeholder_value)

    return formatted_string