from datetime import datetime, timedelta


def upcoming_birthdays(book):
    today = datetime.today().date()
    next_week = today + timedelta(days=6)
    upcoming = []

    for name, record in book.data.items():
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
