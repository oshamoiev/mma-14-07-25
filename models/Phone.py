from .Field import Field


class Phone(Field):
    def __init__(self, value):
        # TODO: Add more enhanced validation for phone via regex
        if not value.isdigit() or len(value) != 3:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)
