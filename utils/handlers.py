from .decorators import input_error
from models import AddressBook, Record


@input_error
def add_contact(args, book):
    check_args(args, "name", "phone")

    name, phone, *_ = args
    record = book.find(name)

    message = "The address book has been updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "New contact has been added."

    if phone:
        if record.add_phone(phone):
            message = f"Phone {phone} added to contact {name}."
        else:
            message = f"Phone {phone} already exists for contact {name}."

    return message


@input_error
def change_contact(args, book):
    check_args(args, "name", "old phone", "new phone")

    name, old_phone, new_phone, *_ = args

    record = get_record(book, name)

    if record.edit_phone(old_phone, new_phone):
        return f"{name}'s phone has been successfully changed."
    else:
        return f"Phone number {old_phone} not found for contact {name}."


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


def check_args(args, *fields):
    if len(args) < len(fields):
        raise ValueError(f"Please provide: {", ".join(fields)}.")


def get_record(book, name):
    record = book.find(name)

    if not record:
        raise KeyError(f"No contact found for name: {name}.")

    return record
