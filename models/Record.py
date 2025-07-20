from .Birthday import Birthday
from .Name import Name
from .Phone import Phone
from .Email import Email


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None

    def add_phone(self, new_phone):
        if isinstance(new_phone, Phone):
            phone_obj = new_phone
        else:
            phone_obj = Phone(new_phone)

        if any(phone.value == phone_obj.value for phone in self.phones):
            return False

        self.phones.append(phone_obj)
        return True

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.__find_phone(old_phone)

        if phone_to_edit:
            phone_to_edit.value = new_phone
            return True
        else:
            return False

    def add_birthday(self, new_date):
        if isinstance(new_date, Birthday):
            self.birthday = new_date
        else:
            self.birthday = Birthday(new_date)

    def add_email(self, email):
        if isinstance(email, Email):
            self.email = email
        else:
            self.email = Email(email)

    def show_email(self):
        return self.email.value if self.email else "-"

    def __find_phone(self, phone_string):
        found_phones = [phone for phone in self.phones if phone.value == phone_string]
        return found_phones[0] if found_phones else None
