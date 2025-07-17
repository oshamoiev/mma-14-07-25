import pickle
from collections import UserDict

from utils import upcoming_birthdays


class AddressBook(UserDict):
    FILENAME = "addressbook.pkl"

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
        return self.data.pop(contact_name, None)

    def save_to_file(self):
        with open(AddressBook.FILENAME, "wb") as file:
            pickle.dump(self, file)

    def get_upcoming_birthdays(self):
        return upcoming_birthdays(self)
