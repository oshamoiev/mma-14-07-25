import re
from datetime import datetime

from .Field import Field


class Birthday(Field):
    date_format = "%d.%m.%Y"

    def __init__(self, value):
        if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", str(value)):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        try:
            parsed_date = datetime.strptime(value, self.date_format)
        except ValueError:
            raise ValueError("Invalid date format. Use 'DD.MM.YYYY'.")
        super().__init__(parsed_date)

    def __str__(self):
        return self.value.strftime(Birthday.date_format)