from collections import UserDict

from models.Note import Note


class NoteBook(UserDict):
    def add_note(self, key, content):
        if key in self.data.keys():
            raise KeyError(f"Note with Key = '{key}' already exists.")

        self.data[key] = (Note(key, content))

    def delete_note(self, key):
        try:
            del self.data[key]
        except IndexError:
            raise KeyError(f"Note with Key = '{key}' does not exist.")

    def change_note(self, key, new_content):
        note = self.get_note(key)
        note.content = new_content

    def find_notes(self, search_content):
        found_notes = []

        for note in self.get_all_notes():
            if any(word.lower() in note.content.lower() for word in search_content):
                found_notes.append(note)

        return found_notes

    def get_note(self, key):
        try:
            return self.data[key]
        except KeyError:
            raise KeyError(f"Note with Key = '{key}' does not exist.")

    def get_all_notes(self):
        return self.data.values()
