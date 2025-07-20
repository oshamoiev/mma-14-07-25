
from datetime import datetime, timedelta

def upcoming_birthdays(book, days=7):
    today = datetime.today().date()
    end_date = today + timedelta(days=days - 1)  
    
    upcoming = []

    for name, record in book.data.items():
        try:
            birthday_date = record.birthday.value
            birthday_this_year = birthday_date.replace(year=today.year).date()

            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            if today <= birthday_this_year <= end_date:
                upcoming.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime("%A, %B %d"),
                    }
                )
        except (AttributeError, ValueError):
            continue

    return upcoming
