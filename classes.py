import sys
from collections import UserDict
from main import input_error


class AdressBook(UserDict):
    @input_error
    def add_record(self, record):
        self.data[record.name.value] = record

    def show_all_records(self):
        for name, phones in self.data.items():
            print(f'{name}: {self.data[name].get_phones()}')


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

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

    def get_phones(self):
        return [phone.value for phone in self.phones]


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


def main():
    print('Hello, this is bot assistant. Type "hello" to see list of commands')
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
            print('Type "exit" or "qiut" or "good bye" to finish my work.')

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
