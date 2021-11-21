import functools
import sys

from AdressBook import AdressBook, Record


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
            print(
                'Type "bday Username" to find username birthday and count days before birthday.')
            print(
                'Type "bday Username YYYY-MM-DD" to set username birthday in ISO format.')
            print('Type "exit" or "quit" or "good bye" to finish my work.')

        elif command == 'add':
            if len(commands) != 3:
                print('Incorrect command usage.')
            else:
                name, phone_numbers = commands[1], commands[2:]
                if user_book.data.get(name):
                    user_book.data[name].add_phone(phone_numbers)
                else:
                    new_record = Record(name, phone_numbers)
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
