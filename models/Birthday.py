import re
from datetime import datetime

from .Field import Field


class Birthday(Field):
    def __init__(self, value):
        if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", str(value)):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date. Make sure the date is correct.")
        super().__init__(parsed_date)
