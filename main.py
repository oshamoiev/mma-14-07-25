from utils import (
    add_contact,
    change_contact,
    phone_contact,
    all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    parse_input,
    load_data,
    save_data,
)


def run_bot():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        parsed = parse_input(user_input)

        if parsed is None:
            continue
        command, *args = parsed

        if command in ["close", "exit"]:
            save_data(book)
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
            print(birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    run_bot()
