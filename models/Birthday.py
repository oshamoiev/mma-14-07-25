from datetime import datetime

from .Field import Field


class Birthday(Field):
    date_format = "%d.%m.%Y"

    def __init__(self, value):
        try:
            parsed_date = datetime.strptime(value, self.date_format)
        except ValueError:
            raise ValueError("Invalid date format. Use 'DD.MM.YYYY'.")
        super().__init__(parsed_date)

    def __str__(self):
        return self.value.strftime(Birthday.date_format)
