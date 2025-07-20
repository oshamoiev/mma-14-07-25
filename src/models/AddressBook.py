import pickle
from pathlib import Path
from collections import UserDict

from models.NoteBook import NoteBook
from utils import upcoming_birthdays


class AddressBook(UserDict):
    """
    AddressBook manages contacts and notes.
    Contacts are stored in a dictionary, and notes are managed via an embedded NoteBook.
    """

    FILENAME = Path.home() / "address-book.pkl"

    def __init__(self):
        """
        Initialize AddressBook and its embedded NoteBook.
        """
        super().__init__()
        self.note_book = NoteBook()

    @classmethod
    def load_or_create_book(cls):
        """
        Load AddressBook from file if it exists, otherwise create a new one.
        """
        try:
            with open(cls.FILENAME, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return cls()

    def add_record(self, new_record):
        """
        Add a new contact record to the address book.
        """
        self.data[new_record.name.value] = new_record

    def find(self, contact_name):
        """
        Find and return a contact record by name.
        """
        return self.data.get(contact_name)

    def delete(self, contact_name):
        """
        Delete a contact record by name.
        """
        return self.data.pop(contact_name, None)

    def save_to_file(self):
        """
        Save the address book to a file using pickle.
        """
        with open(AddressBook.FILENAME, "wb") as file:
            pickle.dump(self, file)

    def get_upcoming_birthdays(self, days=7):
        """
        Get contacts with birthdays in the next 'days' days.
        """
        return upcoming_birthdays(self, days)

    def add_note(self, key, content):
        """
        Add a note to the notebook.
        """
        self.note_book.add_note(key, content)

    def delete_note(self, key):
        """
        Delete a note from the notebook.
        """
        self.note_book.delete_note(key)

    def change_note(self, key, new_content):
        """
        Change the content of an existing note.
        """
        self.note_book.change_note(key, new_content)

    def find_notes(self, search_content):
        """
        Find notes containing the search content.
        """
        return self.note_book.find_notes(search_content)

    def get_note(self, key):
        """
        Get a specific note by key.
        """
        return self.note_book.get_note(key)

    def get_all_notes(self):
        """
        Get all notes from the notebook.
        """
        return self.note_book.get_all_notes()

    def tag_note(self, key, tag):
        """
        Add a tag to a note.
        """
        self.note_book.add_tag(key, tag)
