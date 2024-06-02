import re


def camel_to_snake_case(string: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()


def trim_minecraft_namespace(string: str) -> str:
    return string.split(":", 1)[1]  # returns the string after the first colon
