import re
from .Field import Field

email_pattern = re.compile(
    r"^(?=.{1,254}$)"                           # вся адреса максимум 254 символи 
    r"(?=.{1,64}@)"                             # частина перед @ максимум 64 символи
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"          # перша група символів 
    r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"   # додаткові групи після крапки, без пустих (щоб не було "..")
    r"@"
    r"(?:[A-Za-z0-9]"                           # домен починається з букви чи цифри
    r"(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"   # може містити дефіси всередині, але не на початку чи кінці
    r"[A-Za-z]{2,}$"                            # кінцева частина домену мінімум 2 літери
)

class Email(Field):
    def __init__(self, value):
        if email_pattern.fullmatch(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid email format. Example: john@example.com")
