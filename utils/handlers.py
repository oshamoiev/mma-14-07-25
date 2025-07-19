from models import Record, AddressBook
from .decorators import input_error
from .parser import parse_contact_fields


@input_error
def add_contact(args, book):
    check_args(args, "name")

    name, *fields = args
    record = book.find(name)
    is_new = record is None

    phones, email, birthday = parse_contact_fields(fields)

    if not phones:
        raise ValueError("At least one phone number is required to add a contact.")

    if is_new:
        record = Record(name)
        book.add_record(record)

    for phone in phones:
        record.add_phone(phone)

    if email and hasattr(record, 'add_email'):
        record.add_email(email)

    if birthday and hasattr(record, 'add_birthday'):
        record.add_birthday(birthday)

    status = "added" if is_new else "updated"
    message = f"{'New contact' if is_new else 'Contact'} {name} has been {status}."

    return message


@input_error
def change_contact(args, book):
    check_args(args, "name")

    name, *fields = args
    record = get_record(book, name)

    phones, email, birthday = parse_contact_fields(fields)

    for phone in phones:
        record.add_phone(phone)

    if email and hasattr(record, 'add_email'):
        record.add_email(email)

    if birthday and hasattr(record, 'add_birthday'):
        record.add_birthday(birthday)

    return f"Contact {name} has been updated."



@input_error
def phone_contact(args, book):
    check_args(args, "name")

    name, *_ = args

    record = get_record(book, name)

    phones = record.get_phone()
    return f"{name}'s phone numbers: {phones}"


@input_error
def all_contacts(args, book):
    if not book:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())


@input_error
def add_birthday(args, book):
    check_args(args, "name", "birthday")

    name, birthday_date, *_ = args

    record = get_record(book, name)

    record.add_birthday(birthday_date)
    return f"{name}'s birthday date has been successfully added."


@input_error
def show_birthday(args, book):
    check_args(args, "name")

    name, *_ = args

    record = get_record(book, name)

    birthday = record.show_birthday()
    return f"{name}'s birthday date: {birthday}"


@input_error
def birthdays(book):
    if not book:
        return "No contacts found."

    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays found."

    messages = [
        f"{birthday['name']}'s upcoming birthday will be on {birthday['congratulation_date']}"
        for birthday in upcoming_birthdays
    ]

    return "\n".join(messages)

@input_error
def add_email(args, book: AddressBook):
    check_args(args, "name", "email")

    name, email, *_ = args
    record = get_record(book, name)
    record.add_email(email)
    return f"{name}'s email has been successfully added."

@input_error
def show_email(args, book: AddressBook):
    check_args(args, "name")

    name, *_ = args
    record = get_record(book, name)
    email = record.show_email()
    return f"{name}'s email: {email}"


def check_args(args, *fields):
    if len(args) < len(fields):
        raise ValueError(f"Please provide: {', '.join(fields)}.")


def get_record(book, name):
    record = book.find(name)

    if not record:
        raise KeyError(f"No contact found for name: {name}.")

    return record
