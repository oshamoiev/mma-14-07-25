import readline

commands = [
    "hello", "help", "exit", "close", "add-contact", "change-contact",
    "remove-contact", "contact", "contacts", "add-birthday", "show-birthday",
    "birthdays", "add-email", "show-email", "add-note", "delete-note",
    "change-note", "note", "notes", "tag-note", "find-notes",
]

def completer(text, state):
    options = [cmd for cmd in commands if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    return None

def setup_autocomplete():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
