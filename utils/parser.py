import re
from datetime import datetime


def parse_input(user_input):
    if not user_input:
        return None
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def parse_contact_fields(fields):
    phones = []
    email = None
    birthday = None
    warnings = []

    for field in fields:
        if field.isdigit() and len(field) == 10:
            phones.append(field)
        elif re.fullmatch(r"[^@]+@[^@]+\.[^@]+", field):
            email = field
        elif re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", field):
            try:
                datetime.strptime(field, "%d.%m.%Y")
                birthday = field
            except ValueError:
                warnings.append(f"Ignored invalid birthday date: {field}")
        else:
            if re.match(r"\d{1,2}\.\d{1,2}\.\d{2,4}", field):
                warnings.append(f"Ignored invalid birthday format: {field}")
            else:
                warnings.append(f"Ignored unrecognized field: {field}")

    return phones, email, birthday, warnings
