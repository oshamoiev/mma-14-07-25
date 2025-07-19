from models.Phone import Phone
from models.Email import Email
from models.Birthday import Birthday


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
        try:
            phones.append(Phone(field))
        except ValueError:
            if email is None:
                try:
                    email = Email(field)
                    continue
                except ValueError:
                    pass
            if birthday is None:
                try:
                    birthday = Birthday(field)
                    continue
                except ValueError:
                    pass
            raise ValueError(f"Unrecognized field format: {field}")

    return phones, email, birthday
