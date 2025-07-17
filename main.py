from rich.console import Console

from models import AddressBook
from utils import (
    add_contact,
    change_contact,
    phone_contact,
    all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    add_note,
    delete_note,
    get_note,
    get_all_notes,
    parse_input,
    find_notes,
    change_note
)


def run_bot():
    console = Console()
    book = AddressBook.load_or_create_book()
    print("Welcome to the assistant bot!")

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
            elif command == "hello":
                print("How can I help you?")
            elif command == "add-contact":
                print(add_contact(args, book))
            elif command == "change-contact":
                print(change_contact(args, book))
            elif command == "phone":
                print(phone_contact(args, book))
            elif command == "show-contacts":
                print(all_contacts(args, book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(book))
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
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        book.save_to_file()
        print("\nGood bye!")


if __name__ == "__main__":
    run_bot()
