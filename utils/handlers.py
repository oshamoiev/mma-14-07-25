from .decorators import input_error
from models import AddressBook, Record


@input_error
def add_contact(args, book: AddressBook):
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
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if record is None:
        return "No contact found!"

    if record.edit_phone(old_phone, new_phone):
        return f"{name}'s phone has been successfully changed."
    else:
        return f"Phone number {old_phone} not found for contact {name}."


@input_error
def phone_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if record is None:
        return "No contact found!"

    phones = record.get_phone()
    return f"{name}'s phone numbers: {phones}"


@input_error
def all_contacts(args, book: AddressBook):
    if not book:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_date, *_ = args
    record = book.find(name)
    message = "The address book has been updated."

    if record is None:
        message = "No contact found!"
    else:
        record.add_birthday(birthday_date)
        message = f"{name}'s birthday date has been successfully added."

    return message


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if record is None:
        return "No contact found!"

    birthday = record.show_birthday()
    return f"{name}'s birthday date: {birthday}"


@input_error
def birthdays(args, book: AddressBook):
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
