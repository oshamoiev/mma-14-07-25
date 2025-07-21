from .Birthday import Birthday
from .Name import Name
from .Phone import Phone
from .Email import Email


class Record:
    """
    Represents a contact record containing name, phones, email, and birthday.

    Provides methods to add, edit, and retrieve contact details.
    """

    def __init__(self, name):
        """
        Initialize a Record with a name.

        Args:
            name: The contact's name (string).
        """
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None

    def add_phone(self, new_phone):
        """
        Add a new phone number to the record.

        Args:
            new_phone: Phone object or string.

        Returns:
            True if phone was added, False if it already exists.
        """
        if isinstance(new_phone, Phone):
            phone_obj = new_phone
        else:
            phone_obj = Phone(new_phone)

        if any(phone.value == phone_obj.value for phone in self.phones):
            return False

        self.phones.append(phone_obj)
        return True

    def edit_phone(self, old_phone, new_phone):
        """
        Edit an existing phone number.

        Args:
            old_phone: The phone number to be replaced (string).
            new_phone: The new phone number (string).

        Returns:
            True if phone was edited, False if not found.
        """
        phone_to_edit = self.__find_phone(old_phone)

        if phone_to_edit:
            phone_to_edit.value = new_phone
            return True
        else:
            return False

    def add_birthday(self, new_date):
        """
        Add or update the birthday for the record.

        Args:
            new_date: Birthday object or date string.
        """
        if isinstance(new_date, Birthday):
            self.birthday = new_date
        else:
            self.birthday = Birthday(new_date)

    def show_birthday(self):
        """
        Show the birthday for the record.

        Returns:
            Birthday object if set, otherwise None.
        """
        return self.birthday

    def add_email(self, email):
        """
        Add or update the email for the record.

        Args:
            email: Email object or email string.
        """
        if isinstance(email, Email):
            self.email = email
        else:
            self.email = Email(email)

    def show_email(self):
        """
        Show the email address for the record.

        Returns:
            Email string if set, otherwise '-'.
        """
        return self.email.value if self.email else "-"

    def __find_phone(self, phone_string):
        """
        Find a phone object by its value.

        Args:
            phone_string: Phone number string to search for.

        Returns:
            Phone object if found, otherwise None.
        """
        found_phones = [phone for phone in self.phones if phone.value == phone_string]
        return found_phones[0] if found_phones else None
