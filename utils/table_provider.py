from rich.table import Table


def get_note_table(notes):
    table = Table(title="Notes")

    table.add_column("Key", justify="center", style="cyan", no_wrap=True, )
    table.add_column("Content", justify="left", style="magenta", width=50)

    for note in notes:
        table.add_row(note.key, note.content)
        table.add_section()

    return table
