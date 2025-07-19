from .handlers import (
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
    tag_note
)
from .parser import parse_input
from .get_birthdays import upcoming_birthdays
from .table_provider import (
    get_note_table,
    get_record_table
)
