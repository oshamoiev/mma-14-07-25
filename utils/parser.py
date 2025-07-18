import re
from datetime import datetime
from models import Phone, Email, Birthday


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
        try:
            phone = Phone(field)
            phones.append(phone)
            continue
        except ValueError:
            pass

        try:
            if email is None:  # Only one email allowed
                email_obj = Email(field)
                email = email_obj
                continue
        except ValueError:
            pass

        try:
            if birthday is None:
                birthday_obj = Birthday(field)
                birthday = birthday_obj
                continue
        except ValueError:
            pass

        warnings.append(f"Ignored unrecognized or invalid field: {field}")

    return phones, email, birthday, warnings

