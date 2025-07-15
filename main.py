from utils import (
    add_contact,
    change_contact,
    phone_contact,
    all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    parse_input,
)
from models import AddressBook


def run_bot():
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
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "phone":
                print(phone_contact(args, book))
            elif command == "all":
                print(all_contacts(args, book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(book))
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        book.save_to_file()
        print("\nGood bye!")


if __name__ == "__main__":
    run_bot()
