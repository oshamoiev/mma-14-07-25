from collections import namedtuple

from rich.console import Console

from models import AddressBook
from utils import (
    parse_input,
    add_contact,
    change_contact,
    remove_contact,
    get_contact,
    get_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    show_email,
    add_note,
    delete_note,
    get_note,
    get_all_notes,
    find_notes,
    change_note,
    tag_note,
    get_help,
    autocomplete
)

CommandRow = namedtuple("CommandRow", ["category", "command", "description"])

COMMANDS = [
    CommandRow("General", "help", "Show this help message"),
    CommandRow("General", "exit", "Save book and exit"),
    CommandRow("General", "close", "Save book and exit"),
    CommandRow("Contacts", "add-contact", "Add contact <name> <phone> [birthday] [email]"),
    CommandRow("Contacts", "change-contact", "Change phone <name> <phone> [birthday] [email]"),
    CommandRow("Contacts", "remove-contact", "Remove contact <name>"),
    CommandRow("Contacts", "contact", "Show contact <name>"),
    CommandRow("Contacts", "contacts", "Show all contacts"),
    CommandRow("Contacts", "add-birthday", "Add birthday <name> <DD.MM.YYYY>"),
    CommandRow("Contacts", "show-birthday", "Show birthday <name>"),
    CommandRow("Contacts", "birthdays [days]", "Show birthdays in next N days (default 7)"),
    CommandRow("Contacts", "add-email", "Add email <name> <email>"),
    CommandRow("Contacts", "show-email", "Show email <name>"),
    CommandRow("Notes", "add-note", "Add a new note"),
    CommandRow("Notes", "delete-note", "Delete note <note key>"),
    CommandRow("Notes", "change-note", "Edit note <note key> <text>"),
    CommandRow("Notes", "note", "Show note <note key>"),
    CommandRow("Notes", "notes", "Show all notes"),
    CommandRow("Notes", "tag-note", "Tag note <note key> <tag>"),
    CommandRow("Notes", "find-notes", "Find notes <one or more keywords>"),
]


def run_bot():
    book = AddressBook.load_or_create_book()

    autocomplete.setup_autocomplete()
    console = Console()

    print("\n   Welcome to the assistant bot! Press [`Tab`] to autocomplete commands.")
    console.print(get_help(COMMANDS))

    try:
        while True:
            user_input = input("Enter a command: ")
            parsed = parse_input(user_input)

            if not parsed:
                continue
            command, *args = parsed

            if command in ["close", "exit"]:
                book.save_to_file()
                print("Good bye!")
                break
            elif command == "add-contact":
                print(add_contact(args, book))
            elif command == "change-contact":
                print(change_contact(args, book))
            elif command == "remove-contact":
                print(remove_contact(args, book))
            elif command == "contact":
                console.print(get_contact(args, book))
            elif command == "contacts":
                console.print(get_contacts(args, book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(args, book))
            elif command == "add-email":
                print(add_email(args, book))
            elif command == "show-email":
                print(show_email(args, book))
            elif command == "add-note":
                print(add_note(args, book))
            elif command == "delete-note":
                print(delete_note(args, book))
            elif command == "change-note":
                print(change_note(args, book))
            elif command == "find-notes":
                console.print(find_notes(args, book))
            elif command == "note":
                console.print(get_note(args, book))
            elif command == "notes":
                console.print(get_all_notes(book))
            elif command == "tag-note":
                console.print(tag_note(args, book))
            elif command == "help":
                console.print(get_help(COMMANDS))
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        book.save_to_file()
        print("\nGood bye!")


if __name__ == "__main__":
    run_bot()
