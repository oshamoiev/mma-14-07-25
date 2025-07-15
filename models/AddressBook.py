from datetime import datetime, timedelta
from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    def find(self, contact_name):
        return self.data.get(contact_name)

    def delete(self, contact_name):
        print(f"{contact_name} was successfully removed!")
        return self.data.pop(contact_name, None)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=6)
        upcoming = []

        for name, record in self.data.items():
            try:
                birthday_date = record.birthday.value
                birthday_this_year = birthday_date.replace(year=today.year).date()

                if birthday_this_year.weekday() == 5:
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year += timedelta(days=1)

                if today <= birthday_this_year <= next_week:
                    upcoming.append(
                        {
                            "name": record.name.value,
                            "congratulation_date": datetime.strftime(
                                birthday_this_year, "%A, %B %d"
                            ),
                        }
                    )
            except (AttributeError, ValueError):
                continue

        return upcoming
