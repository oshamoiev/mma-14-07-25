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


def get_command_table(command_rows):
    table = Table(title="Available Commands", show_lines=True, padding=(0, 1))
    table.add_column("Command", style="magenta", no_wrap=True)
    table.add_column("Category", style="cyan bold", no_wrap=True)
    table.add_column("Description", style="green")

    for command_row in command_rows:
        table.add_row(command_row.command, command_row.category, command_row.description)

    return table

def get_birthday_table(upcoming_birthdays):
    table = Table(title="Upcoming Birthdays", show_lines=True, padding=(0, 1))
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Congratulation Date", style="magenta", no_wrap=True)

    for birthday in upcoming_birthdays:
        table.add_row(birthday["name"], birthday["congratulation_date"])

    return table
