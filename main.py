import csv
import sys
from datetime import date


def main():
    print('Hello, this is bot assistant. Type "hello" to see list of commands')
    while True:
        command = input()
        handler(command)


def handler(command: str):
    COMMANDS[command]()


def hello_command():
    print('How can i help you?')
    print('Type "add" to add contact to your phone book.')
    print('Type "change" to change contact in your phone book.')
    print('Type "show all" to get all your contacts.')
    print('Type "phone" to find person phone number by name.')
    print('Type "exit" or "qiut" or "good bye" to finish my work.')


def exit_command():
    print('Good bye!')
    sys.exit()


def add_command():
    name = input('Type contact name:')
    phone = input('Type contact phone number:')

    print(f'{name} saved to your phone book.')


def change_command():
    pass


def get_phone():
    pass


def show_all():
    pass


COMMANDS = {
    'hello': hello_command,
    'exit': exit_command,
    'quit': exit_command,
    'good bye': exit_command,
    'add': add_command,
    'change': change_command,
    'phone': get_phone,
    'show all': show_all,
}

if __name__ == '__main__':
    main()
