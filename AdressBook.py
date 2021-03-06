import os
import pickle
from collections import UserDict
from typing import Optional, List
from datetime import date


class Field:
    """Fields of records in contact book : name , phone/phones , etc."""

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Name(Field):
    """Name class field of class Record"""


class Phone(Field):
    """Phone of the contact"""

    def __init__(self, value):
        value = value.replace('+', '').replace(' ', '')
        if value.isdigit():
            super().__init__(value)

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __str__(self):
        return f"Phone:{self.value}"


class Birthday(Field):
    """Birthday field of cls Record"""

    def __init__(self, value):
        try:
            value = date.fromisoformat(value)
            super().__init__(value)
        except ValueError:
            print('Incorrect format date was given.')
            self.value = None
        except TypeError:
            self.value = None


class Record:
    """Records(contacts) in users contact book.
    Only one name , but it can be more than one phone"""

    def __init__(self, name: str, phones: List[str] = None, birthday: Optional[str] = None) -> None:
        if phones:
            self.phones = [Phone(p) for p in phones]
        else:
            self.phones = []
        self.birthday = Birthday(birthday)
        self.name = Name(name)

    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone: str) -> None:
        phone_to_delete = self.__find_phone_single_value(phone)
        self.phones.remove(phone_to_delete) if phone_to_delete else None

    def change_phone(self, old_phone, new_phone) -> None:
        new_phone = Phone(new_phone)
        phone_to_remove = self.__find_phone_single_value(old_phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            self.phones.append(new_phone)

    def __find_phone_single_value(self, phone: str) -> Optional[Phone]:
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        return f"Record of {self.name.value}, phones {[p.value for p in self.phones]}"

    def __repr__(self):
        return f"Record of {self.name.value}, phones {[p.value for p in self.phones]}"

    def get_phones(self):
        return [phone.value for phone in self.phones]

    def add_birthday(self, birthday_date):
        """
            Add 'Birthday' object
        """
        self.birthday = Birthday(birthday_date)

    def days_to_birthday(self):
        """
            If b-day is added: counts days before next one.

        """

        if self.birthday.value is None:
            print(f'No b-day added for {self.name.value}')
            return

        date_now = date.today()
        birthday_date = self.birthday.value
        birthday_date = birthday_date.replace(year=date_now.year)
        # Check if user's birthday passed this year => year + 1
        if birthday_date <= date_now:
            birthday_date = birthday_date.replace(year=date_now.year + 1)

        days_delta = (birthday_date - date_now).days
        print(f"{days_delta} days before {self.name.value}'s Birthday.")
        print(f"Birthday date is: {self.birthday.value.strftime('%d %b %Y')}")
        return days_delta

    def __next__(self):
        return self


class AdressBook(UserDict):
    """All contacts data"""

    def load_data(self) -> None:
        """
            Load data from file
        """
        if os.path.exists('data.bin'):
            with open('data.bin', 'rb') as file:
                self.data = pickle.load(file)

    def save_data(self) -> None:
        """
            Save data to file
        """
        with open('data.bin', 'wb') as file:
            pickle.dump(self.data, file)

    def add_record(self, record: list) -> None:
        new_record = Record(name=record[0], phones=record[1:])
        self.data[new_record.name.value] = new_record

    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value)

    def delete_record(self, value: str) -> None:
        self.data.pop(value)

    def __str__(self):
        return str(self.data)

    def show_all_records(self):
        for record in self:
            print(record)

    def __iter__(self):
        return iter(self.data.values())

    def __len__(self) -> int:
        return len(self.data.values())

    def page_iterator(self, number_records: int = 3):
        """
            Generator  n-sized
        """
        records = [record for record in self]
        for i in range(0, len(records), number_records):
            yield records[i:i + number_records]

    def search_subtext(self, subtext: str) -> list:
        """
            Method returns list with records which contains subtext.
        """
        result_records = []
        for record in self:
                if subtext in record.name.value:
                    result_records.append(record)

                for phone_number in record.phones:
                    if subtext in phone_number.value:
                        result_records.append(record)
        return result_records