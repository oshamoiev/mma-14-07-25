from models import Record
from utils.table_provider import get_note_table, get_record_table, get_help_table
from .decorators import input_error
from .parser import parse_contact_fields
from rich.console import Console


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
def remove_contact(args, book):
    check_args(args, "name")
    name = args[0]

    get_record(book, name)

    book.delete(name)
    return f"Contact {name} has been removed."


@input_error
def get_contact(args, book):
    check_args(args, "name")

    name, *_ = args

    record = get_record(book, name)

    return get_record_table([record])


@input_error
def get_contacts(args, book):
    if not book:
        return "No contacts found."

    return get_record_table(book.values())


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
def birthdays(args, book):
    days = 7  
    if args and args[0].isdigit():
        days = int(args[0])
    
    if not book:
        return "No contacts found."

    upcoming_birthdays = book.get_upcoming_birthdays(days)
    if not upcoming_birthdays:
        return f"No upcoming birthdays found in the next {days} days."

    messages = [
        f"{birthday['name']}'s upcoming birthday will be on {birthday['congratulation_date']}"
        for birthday in upcoming_birthdays
    ]

    return "\n".join(messages)


@input_error
def add_email(args, book):
    check_args(args, "name", "email")

    name, email, *_ = args
    record = get_record(book, name)
    record.add_email(email)
    return f"{name}'s email has been successfully added."


@input_error
def show_email(args, book):
    check_args(args, "name")

    name, *_ = args
    record = get_record(book, name)
    email = record.show_email()
    return f"{name}'s email: {email}"


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
        raise ValueError(f"Please provide: {', '.join(fields)}.")


def get_record(book, name):
    record = book.find(name)

    if not record:
        raise KeyError(f"No contact found for name: {name}.")

    return record


def help_command(*args):
    console = Console()
    console.print(get_help_table())
    return ""