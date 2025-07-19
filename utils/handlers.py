from models.Record import Record
from utils.table_provider import get_note_table
from .decorators import input_error


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


@input_error
def add_note(args, book):
    check_args(args, "Key", "Content")

    key, *content_words = args

    content = " ".join(content_words)
    book.add_note(key, content)

    return f"Note with Key = '{key}' has been added."


@input_error
def delete_note(args, book):
    check_args(args, "Key")

    key, *_ = args
    book.delete_note(key)

    return f"Note with Key = '{key}' has been deleted."


@input_error
def change_note(args, book):
    check_args(args, "Key", "New Content")

    key, *new_content_words = args

    new_content = " ".join(new_content_words)
    book.change_note(key, new_content)

    return f"Note with Key = '{key}' has been changed."


@input_error
def find_notes(args, book):
    check_args(args, "search content")

    found_notes = book.find_notes(args)

    if not found_notes:
        return "No notes found with the given content."

    return get_note_table(found_notes)


@input_error
def get_note(args, book):
    check_args(args, "Key")

    key, *_ = args

    note = book.get_note(key)

    return get_note_table([note])


def get_all_notes(book):
    notes = book.get_all_notes()

    if not notes:
        return "No Notes in the book."

    return get_note_table(notes)


@input_error
def tag_note(args, book):
    check_args(args, "Key", "Tag")

    key, *tag_strings = args

    tag = " ".join(tag_strings)
    book.tag_note(key, tag)

    return f"Tag '{tag}' has been added to note with Key = '{key}'."


def check_args(args, *fields):
    if len(args) < len(fields):
        raise ValueError(f"Please provide: {", ".join(fields)}.")


def get_record(book, name):
    record = book.find(name)

    if not record:
        raise KeyError(f"No contact found for name: {name}.")

    return record
