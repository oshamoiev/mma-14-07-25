from rich.table import Table


def get_note_table(notes):
    table = Table(title="Notes")

    table.add_column("Key", justify="center", style="cyan", no_wrap=True)
    table.add_column("Content", justify="left", style="magenta", max_width=50)
    table.add_column("Tags", justify="left", style="green", max_width=35)

    for note in notes:
        table.add_row(note.key, note.content, ", ".join(note.tags))
        table.add_section()

    return table


def get_record_table(records):
    table = Table(title="Contacts")

    table.add_column("Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Phones", justify="left", style="magenta", max_width=50)
    table.add_column("Email", justify="left", style="green", max_width=25)
    table.add_column("Birthday", justify="left", style="blue", max_width=25)

    for record in records:
        table.add_row(str(record.name),
                          ", ".join([str(phone) for phone in record.phones]),
                          str(record.email) if record.email else "",
                          str(record.birthday) if record.birthday else "")
        table.add_section()

    return table

def get_help_table():
    table = Table(title="Available Commands", show_lines=True, padding=(0, 1))
    table.add_column("Category", style="cyan bold", no_wrap=True)
    table.add_column("Command", style="magenta", no_wrap=True)
    table.add_column("Description", style="green")

    table.add_row("General", "hello", "Greet the bot")
    table.add_row("General", "help", "Show this help message")
    table.add_row("General", "exit / close", "Exit and save")

    table.add_row("Contacts", "add-contact", "Add contact <name> <phone> [birthday] [email]")
    table.add_row("Contacts", "change-contact", "Change phone <name> <old_phone> <new_phone>")
    table.add_row("Contacts", "remove-contact", "Remove contact <name>")
    table.add_row("Contacts", "contact", "Show contact <name>")
    table.add_row("Contacts", "contacts [page]", "Show all contacts")
    table.add_row("Contacts", "add-birthday", "Add birthday <name> <DD.MM.YYYY>")
    table.add_row("Contacts", "show-birthday", "Show birthday <name>")
    table.add_row("Contacts", "birthdays [days]", "Show birthdays in next N days")
    table.add_row("Contacts", "add-email", "Add email <name> <email>")
    table.add_row("Contacts", "show-email", "Show email <name>")

    table.add_row("Notes", "add-note", "Add a new note")
    table.add_row("Notes", "delete-note", "Delete note <note_id>")
    table.add_row("Notes", "change-note", "Edit note <note_id> <new_text>")
    table.add_row("Notes", "note", "Show note <note_id>")
    table.add_row("Notes", "notes", "Show all notes")
    table.add_row("Notes", "tag-note", "Tag note <note_id> <tag>")
    table.add_row("Notes", "find-notes", "Find notes <keyword or tag>")

    return table