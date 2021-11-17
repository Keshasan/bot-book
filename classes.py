import sys
from collections import UserDict
from main import input_error
from datetime import date


class AdressBook(UserDict):
    @input_error
    def add_record(self, record):
        """
            Add new record to AdressBook as 'Record' object
        """
        self.data[record.name.value] = record

    def show_all_records(self):
        """
            Print all records in AdressBook
        """
        for name, phones in self.data.items():
            print(f'{name}: {self.data[name].get_phones()}')


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = None

    def add_phone(self, phone):
        """
            Add 'Phone' object to phones list.
        """
        self.phones.append(Phone(phone))

    @input_error
    def add_birthday(self, birthday_date):
        """
            Add 'Birthday' object
        """
        birthday_date = date.fromisoformat(birthday_date)
        self.birthday = Birthday(birthday_date)

    @input_error
    def delete_phone(self, candidate_phone):
        """
            Delete "Phone" object from phones list.
        """
        candidate_phone = Phone(candidate_phone)
        for phone in self.phones:
            if phone.value == candidate_phone.value:
                self.phones.remove(phone)

    @input_error
    def change_phone(self, old_phone, new_phone):
        """
            Delete "Phone" object from phones list.
        """
        if old_phone in self.get_phones():
            self.delete_phone(old_phone)
            self.add_phone(new_phone)
        else:
            self.add_phone(new_phone)

    def get_phones(self):
        """
            Returns list phones in Record
        """
        return [phone.value for phone in self.phones]

    @input_error
    def get_birthday(self):
        """
            Return record birthday if it is added
        """
        if self.birthday is not None:
            return self.birthday.value
        else:
            print('No birthday')

    @input_error
    def days_to_birthday(self):
        """
            If b-day is added: counts days before next one.

        """

        if self.birthday is None:
            print(f'No b-day added for {self.name.value}')
            return None
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


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        if self.__value:
            return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        if self.__value:
            return self.__value

    @value.setter
    def value(self, value):
        """
            Setter validates input number as phone number
                if number is not valid set it to '*' symbol.
        """
        value = value.replace('+', '').replace('-', '').replace(' ', '').strip()
        if value.isdigit():
            self.__value = value
        else:
            self.__value = '*'


def main():
    print('Hello, this is bot assistant. Type "hello" or "help" to see list of commands \n')
    command = None
    user_book = AdressBook()

    while command not in ('exit', 'quit', 'good'):
        commands = input('>> ').strip().split(' ')
        command = commands[0].lower()
        if command in ('hello', 'help'):
            ''' Prints info about commands'''
            print('How can i help you?')
            print('Type "add Username +380*********" to add contact to your phone book.')
            print(
                'Type "change username +380********* +380*********" to change phone number in your phone book.')
            print('Type "show all" to get all your contacts.')
            print('Type "phone Username" to find person phone number by name.')
            print('Type "bday Username" to find username birthday and count days before birthday.')
            print('Type "bday Username YYYY-MM-DD" to set username birthday in ISO format.')
            print('Type "exit" or "quit" or "good bye" to finish my work.')

        elif command == 'add':
            if len(commands) != 3:
                print('Incorrect command usage.')
            else:
                name, phone_number = commands[1], commands[2]
                if user_book.data.get(name):
                    user_book.data[name].add_phone(phone_number)
                else:
                    new_record = Record(name, phone_number)
                    user_book.add_record(new_record)

        elif command == 'change':
            if len(commands) != 4:
                print('Incorrect command usage.')
            else:
                name, old_phone_number, new_phone_number = commands[1], commands[2], commands[3]
                user_book[name].change_phone(
                    old_phone_number, new_phone_number)

        elif command == 'phone':
            if len(commands) != 2:
                print('Incorrect command usage.')
            else:
                name = commands[1]
                phone_numbers = user_book[name].get_phones()
                if phone_numbers:
                    print(f'"{name}" phone numbers is - {phone_numbers}')

        elif command == 'bday':
            if len(commands) == 2:
                name = commands[1]
                if user_book.data.get(name):
                    user_book.data[name].days_to_birthday()

                else:
                    print("Unknown username")

            elif len(commands) == 3:
                name, birthday_date = commands[1], commands[2]

                if user_book.data.get(name):
                    user_book[name].add_birthday(birthday_date)
                else:
                    print("Unknown username")

            else:
                print('Incorrect command usage!')

        elif command == 'show':
            user_book.show_all_records()

        elif command in ('quit', 'exit'):
            print('Good bye!')
            break
        else:
            print("Incorrect command. I don't understand you =(")

    sys.exit()


if __name__ == '__main__':
    main()
