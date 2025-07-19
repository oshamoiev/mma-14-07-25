import pickle
from collections import UserDict

from models.NoteBook import NoteBook
from utils import upcoming_birthdays


class AddressBook(UserDict):
    FILENAME = "addressbook.pkl"

    def __init__(self):
        super().__init__()
        self.note_book = NoteBook()

    @classmethod
    def load_or_create_book(cls):
        try:
            with open(cls.FILENAME, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return cls()

    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    def find(self, contact_name):
        return self.data.get(contact_name)

    def delete(self, contact_name):
        print(f"{contact_name} was successfully removed!")
        return self.data.pop(contact_name, None)

    def save_to_file(self):
        with open(AddressBook.FILENAME, "wb") as file:
            pickle.dump(self, file)

    def get_upcoming_birthdays(self):
        return upcoming_birthdays(self)

    def add_note(self, key, content):
        self.note_book.add_note(key, content)

    def delete_note(self, key):
        self.note_book.delete_note(key)

    def change_note(self, key, new_content):
        self.note_book.change_note(key, new_content)

    def find_notes(self, search_content):
        return self.note_book.find_notes(search_content)

    def get_note(self, key):
        return self.note_book.get_note(key)

    def get_all_notes(self):
        return self.note_book.get_all_notes()

    def tag_note(self, key, tag):
        self.note_book.add_tag(key, tag)
