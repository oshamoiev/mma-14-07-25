from collections import UserDict

from models.Note import Note


class NoteBook(UserDict):
    """
    A collection class for managing Note objects.

    Provides methods to add, delete, modify, search, and tag notes.
    Each note is stored with a unique key.
    """

    def add_note(self, key, content):
        """
        Add a new note with the given key and content.

        Args:
            key: Unique identifier for the note.
            content: The content of the note.

        Raises:
            KeyError: If the key already exists.
        """
        if key in self.data.keys():
            raise KeyError(f"Note with Key = '{key}' already exists.")

        self.data[key] = (Note(key, content))

    def delete_note(self, key):
        """
        Delete the note associated with the given key.

        Args:
            key: Unique identifier for the note.

        Raises:
            KeyError: If the key does not exist.
        """
        try:
            del self.data[key]
        except IndexError:
            raise KeyError(f"Note with Key = '{key}' does not exist.")

    def change_note(self, key, new_content):
        """
        Change the content of the note identified by the given key.

        Args:
            key: Unique identifier for the note.
            new_content: The new content to set.

        Raises:
            KeyError: If the key does not exist.
        """
        note = self.get_note(key)
        note.content = new_content

    def find_notes(self, search_content):
        """
        Find and return notes containing any of the words in search_content.

        Args:
            search_content: String of words to search for.

        Returns:
            List of matching Note objects.
        """
        found_notes = []

        for note in self.get_all_notes():
            if any(word.lower() in note.content.lower() for word in search_content):
                found_notes.append(note)

        return found_notes

    def get_note(self, key):
        """
        Retrieve the note associated with the given key.

        Args:
            key: Unique identifier for the note.

        Raises:
            KeyError: If the key does not exist.

        Returns:
            The Note object.
        """
        try:
            return self.data[key]
        except KeyError:
            raise KeyError(f"Note with Key = '{key}' does not exist.")

    def get_all_notes(self):
        """
        Return all notes in the notebook.

        Returns:
            List of all Note objects.
        """
        return self.data.values()

    def add_tag(self, key, tag):
        """
        Add a tag to the note identified by the given key.

        Args:
            key: Unique identifier for the note.
            tag: Tag to add.

        Raises:
            KeyError: If the key does not exist.
        """
        note = self.get_note(key)
        note.add_tag(tag)
