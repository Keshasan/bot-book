import sys
import os
import pickle
from AdressBook import AdressBook


def main():
    print('Hello, this is bot assistant. Type "hello" or "help" to see list of commands \n')
    command = None

    if os.path.exists('data.bin'):
        user_book = load_book()
    else:
        user_book = AdressBook()

    # page iterator for command next - to show next records
    page_iterator = None
    while command not in ('exit', 'quit', 'good'):
        commands = input('>> ').strip().split(' ')
        command = commands[0].lower()

        if command in ('hello', 'help'):
            ''' Prints info about commands'''
            print('How can i help you?')
            print('Type "add Username 066*******" to add contact to your phone book.')
            print('Type "change username 066******** +380*********" to change phone number in your phone book.')
            print('Type "show all" to get all your contacts.')
            print('Type "phone Username" to find person phone number by name.')
            print('Type "bday Username" to find username birthday and count days before birthday.')
            print('Type "bday Username YYYY-MM-DD" to set username birthday in ISO format.')
            print('Types "pages 3" to define pagination for 3 records in book')
            print('Types "pages next" to show next 3 records')
            print('Types "search text" to show contacts which contains text.')
            print('Type "exit" or "quit" or "good bye" to finish my work.')

        elif command == 'add':
            if len(commands) < 3:
                print('Incorrect command usage.')
            else:
                name, phone_numbers = commands[1], commands[2:]
                if user_book.data.get(name):
                    user_book.data[name].add_phone(phone_numbers)
                else:

                    user_book.add_record([name]+phone_numbers)

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

        elif command == 'pages':
            if commands[1].isdigit():
                number_records = int(commands[1])
                page_iterator = user_book.page_iterator(number_records)
            elif commands[1] == 'next':
                if page_iterator is None:
                    print('Type "pages 3" to start pagination')
                    continue

                try:
                    for record in next(page_iterator):
                        print(record)
                except StopIteration:
                    page_iterator = None
                    print('*End Book*')

        elif command == 'search':
            text = ' '.join(commands[1:])
            for record in user_book:
                if text in record.name.value:
                    print(record)

                for phone_number in record.phones:
                    if text in phone_number.value:
                        print(record)

        elif command in ('quit', 'exit'):
            print('Good bye!')
            break
        else:
            print("Incorrect command. I don't understand you =(")

    save_book(user_book)
    sys.exit()


def load_book():
    with open('data.bin', 'rb') as file:
        return pickle.load(file)


def save_book(book):
    with open('data.bin', 'wb') as file:
        pickle.dump(book, file)


if __name__ == '__main__':
    main()
