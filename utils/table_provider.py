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
