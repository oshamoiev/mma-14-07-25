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
    exit_command,
    autocomplete,
)

CommandRow = namedtuple("CommandRow", ["command", "category", "description", "function"])

COMMANDS = [
    CommandRow("help", "General", "Show this help message",
               lambda args, book, console: console.print(get_help(COMMANDS))),
    CommandRow("exit", "General", "Save book and exit",
               lambda args, book, console: exit_command()),
    CommandRow("close", "General", "Save book and exit",
               lambda args, book, console: exit_command()),
    CommandRow("add-contact", "Contacts", "Add contact <name> <phone> [birthday] [email]",
               lambda args, book, console: print(add_contact(args, book))),
    CommandRow("change-contact", "Contacts", "Change phone <name> <phone> [birthday] [email]",
               lambda args, book, console: print(change_contact(args, book))),
    CommandRow("delete-contact", "Contacts", "Delete contact <name>",
               lambda args, book, console: print(remove_contact(args, book))),
    CommandRow("contact", "Contacts", "Show contact <name>",
               lambda args, book, console: console.print(get_contact(args, book))),
    CommandRow("contacts", "Contacts", "Show all contacts",
               lambda args, book, console: console.print(get_contacts(args, book))),
    CommandRow("add-birthday", "Contacts", "Add birthday <name> <DD.MM.YYYY>",
               lambda args, book, console: print(add_birthday(args, book))),
    CommandRow("birthday", "Contacts", "Show birthday <name>",
               lambda args, book, console: print(show_birthday(args, book))),
    CommandRow("birthdays", "Contacts", "Show birthdays in next N days (default 7)",
               lambda args, book, console: console.print(birthdays(args, book))),
    CommandRow("add-email", "Contacts", "Add email <name> <email>",
               lambda args, book, console: print(add_email(args, book))),
    CommandRow("email", "Contacts", "Show email <name>",
               lambda args, book, console: print(show_email(args, book))),
    CommandRow("add-note", "Notes", "Add a new note",
               lambda args, book, console: print(add_note(args, book))),
    CommandRow("delete-note", "Notes", "Delete note <note key>",
               lambda args, book, console: print(delete_note(args, book))),
    CommandRow("change-note", "Notes", "Edit note <note key> <text>",
               lambda args, book, console: print(change_note(args, book))),
    CommandRow("note", "Notes", "Show note <note key>",
               lambda args, book, console: console.print(get_note(args, book))),
    CommandRow("notes", "Notes", "Show all notes",
               lambda args, book, console: console.print(get_all_notes(book))),
    CommandRow("tag-note", "Notes", "Tag note <note key> <tag>",
               lambda args, book, console: console.print(tag_note(args, book))),
    CommandRow("find-notes", "Notes", "Find notes <one or more keywords>",
               lambda args, book, console: console.print(find_notes(args, book))),
]

def run_bot():
    book = AddressBook.load_or_create_book()

    commands = [row.command for row in COMMANDS]
    autocomplete.setup_autocomplete(commands)
    console = Console()

    print("\n   Welcome to the assistant bot! Press [`Tab`] to autocomplete commands.")
    console.print(get_help(COMMANDS))

    command_to_function_map = {row.command: row.function for row in COMMANDS}

    try:
        while True:
            user_input = input("Enter a command: ")
            parsed = parse_input(user_input)

            if not parsed:
                continue

            command, *args = parsed

            function = command_to_function_map.get(command)

            if function:
                function(args, book, console)
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        book.save_to_file()
        print("\nGood bye!")


if __name__ == "__main__":
    run_bot()
