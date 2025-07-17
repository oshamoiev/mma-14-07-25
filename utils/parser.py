import re


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

    for field in fields:
        if field.isdigit():
            phones.append(field)
        elif "@" in field:
            email = field
        elif re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", field):
            birthday = field

    return phones, email, birthday
