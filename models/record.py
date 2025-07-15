from .name import Name
from .phone import Phone
from .birthday import Birthday


def formatDateCustom(date):
    return date.value.strftime("%d.%m.%Y") if date is not None else "-"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def find_phone(self):
        if not self.phones:
            return "-"
        return "; ".join(phone.value for phone in self.phones)

    def add_phone(self, new_phone):
        if any(phone.value == new_phone for phone in self.phones):
            return False
        self.phones.append(Phone(new_phone))
        return True

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def remove_phone(self, phone_to_remove):
        for phone in self.phones:
            if phone.value == phone_to_remove:
                self.phones.remove(phone)
                return True
        return False

    def add_birthday(self, new_date):
        self.birthday = Birthday(new_date)

    def show_birthday(self):
        return formatDateCustom(self.birthday)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "-"
        return f"Contact >>> name: {self.name.value}, phones: {phones_str}, birthday: {formatDateCustom(self.birthday)}"
