import re
from .Field import Field



class Email(Field):
    def __init__(self, value):
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        if email_pattern.fullmatch(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid email format. Example: john@example.com")
