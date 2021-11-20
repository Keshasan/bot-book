import functools
import sys

DEFAULT_PHONE_BOOK = {
    'Emergency': '112',
    'Operator': '*101#',
    'Firefighter': '101',
    'Police': '102',
    'Medic': '103',
}


def input_error(func):
    @functools.wraps(func)
    def input_error_wrapper(*args, **kwargs):
        for arg in args:
            if arg == '':
                print('Name or phone cannot be empty.')
                return
            elif arg is None:
                print('Incorrect command usage.')
                return
        try:
            val = func(*args, **kwargs)
            return val
        except ValueError:
            print('Invalid data was given.')
        except KeyError:
            print('There is no such name in your phone book')
        except IndexError:
            print('Give me name and phone please')
    return input_error_wrapper


def hello_command():
    ''' Prints info about commands'''
    print('How can i help you?')
    print('Type "add" to add contact to your phone book.')
    print('Type "change" to change contact in your phone book.')
    print('Type "show all" to get all your contacts.')
    print('Type "phone" to find person phone number by name.')
    print('Type "exit" or "qiut" or "good bye" to finish my work.')


def exit_command():
    print('Good bye!')
    sys.exit()


def show_all():
    return DEFAULT_PHONE_BOOK


@input_error
def add_command(name, phone_number):
    '''Adds new name with phone number to phone book'''
    DEFAULT_PHONE_BOOK[name] = phone_number
    return True


@input_error
def change_command(name, phone_number):
    '''Changes new name with phone number to phone book'''
    if name not in DEFAULT_PHONE_BOOK.keys():
        return False
    DEFAULT_PHONE_BOOK[name] = phone_number
    return True


@input_error
def get_phone(name):
    '''Returns phone number'''
    return DEFAULT_PHONE_BOOK[name]


DEFAULT_COMMANDS = {
    'hello': hello_command,
    'help': hello_command,
    'exit': exit_command,
    'quit': exit_command,
    'good bye': exit_command,
}


def main():
    print('Hello, this is bot assistant. Type "hello" to see list of commands')
    command = None

    while command not in ('exit', 'quit', 'good'):
        commands = input('>> ').lower().strip().split(' ')
        command = commands[0]
        if DEFAULT_COMMANDS.get(command):
            DEFAULT_COMMANDS[command]()

        elif command == 'add':
            if len(commands) != 3:
                print('Incorrect command usage.')
            else:
                name = commands[1]
                phone_number = commands[2]
                if add_command(name, phone_number):
                    print(f'[+] {name} is saved to your phone book')

        elif command == 'change':
            if len(commands) != 3:
                print('Incorrect command usage.')
            else:
                name = commands[1]
                new_phone_number = commands[2]
                if change_command(name, new_phone_number):
                    print(
                        f'[+] {name} is updated in your phone book with a phone number {new_phone_number}.')
                else:
                    print(
                        f'[-] {name} have not been found in your phone book.')

        elif command == 'phone':
            if len(commands) != 2:
                print('Incorrect command usage.')
            else:
                name = commands[1]
                phone_number = get_phone(name)
                if phone_number:
                    print(f'"{name}" phone number is - {phone_number}')

        elif command == 'show':
            phone_book = show_all()
            for name, phone_number in phone_book.items():
                print(f'{name} : {phone_number}')
        else:
            print("Incorrect command. I don't understand you =(")

    exit_command()


if __name__ == '__main__':
    main()
