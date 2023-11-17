import re

def camel_to_snake_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()