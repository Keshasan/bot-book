import sys
from collections import UserDict
from main import input_error
from datetime import date


class AdressBook(UserDict):
    @input_error
    def add_record(self, record):
        self.data[record.name.value] = record

    def show_all_records(self):
        for name, phones in self.data.items():
            print(f'{name}: {self.data[name].get_phones()}')

    # def show_birthday(self, name):
    #     print(self.data[name].get_birthday())


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    @input_error
    def add_birthday(self, birthday_date):
        birthday_date = date.fromisoformat(birthday_date)
        self.birthday = Birthday(birthday_date)

    @input_error
    def delete_phone(self, candidate_phone):
        candidate_phone = Phone(candidate_phone)
        for phone in self.phones:
            if phone.value == candidate_phone.value:
                self.phones.remove(phone)

    @input_error
    def change_phone(self, old_phone, new_phone):

        if old_phone in self.get_phones():
            self.delete_phone(old_phone)
            self.add_phone(new_phone)
        else:
            self.add_phone(new_phone)

    @input_error
    def get_phones(self):
        return [phone.value for phone in self.phones]

    @input_error
    def get_birthday(self):
        if self.birthday is not None:
            return self.birthday.value
        else:
            print('No birthday')

    @input_error
    def days_to_birthday(self):
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
        if self.__value:
            return self.__value
        else:
            return '*'

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if value.isdigit():
            super().__init__(value)
        else:
            super().__init__(None)


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
                name = commands[1]
                phone_number = commands[2]
                if user_book.data.get(name):
                    user_book.data[name].add_phone(phone_number)
                else:
                    new_record = Record(name, phone_number)
                    user_book.add_record(new_record)

        elif command == 'change':
            if len(commands) != 4:
                print('Incorrect command usage.')
            else:
                name = commands[1]
                old_phone_number = commands[2]
                new_phone_number = commands[3]
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
                user_book.data[name].days_to_birthday()

            elif len(commands) == 3:
                name = commands[1]
                date_ = commands[2]
                user_book[name].add_birthday(date_)

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
