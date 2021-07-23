from phonebook import SaveError, LoadError
try:
    import serialize
except ImportError:
    print('Wrong serializer format specified! Only json/pickle are allowed')
    exit()
import functools
import sys
import argparse
import phonebook

args = None

if len(sys.argv) > 1:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=False, type=str, help='name to operate upon')
    parser.add_argument("--phone", required=False, type=str, help='phone to operate upon')
    parser.add_argument("--operation", required=True, type=str, choices=['create', 'read', 'update', 'delete', 'show'])
    args = parser.parse_args(sys.argv[1:])


def main():

    def default_operation():
        print('Wrong operation code entered!')

    def operate(actions: dict, code: str):
        actions.get(code, default_operation)()
        try:
            phonebook.save()
        except SaveError:
            print('Cannot save phonebook!')

    def generate_actions(name: str=None, phone: str=None, email=None, address=None):
        actions = {
            '1': functools.partial(phonebook.create_record, name=name, phone=phone, email=email, address=address),
            '2': functools.partial(phonebook.read_record, name=name),
            '3': functools.partial(phonebook.update_record, name=name, phone=phone, email=email, address=address),
            '4': functools.partial(phonebook.delete_record, name=name),
            '5': functools.partial(phonebook.show_all),
            '6': exit,
        }
        return actions

    if args:
        if args.operation == 'create':
            name = args.name
            phone = args.phone
            actions = generate_actions(name=name, phone=phone)
            operate(actions=actions, code='1')

        elif args.operation == 'update':
            name = args.name
            phone = args.phone
            actions = generate_actions(name=name, phone=phone)
            operate(actions=actions, code='3')

        elif args.operation == 'read':
            name = args.name
            actions = generate_actions(name=name)
            operate(actions=actions, code='2')

        elif args.operation == 'delete':
            name = args.name
            actions = generate_actions(name=name)
            operate(actions=actions, code='4')

        elif args.operation == 'show':
            actions = generate_actions()
            operate(actions=actions, code='5')

    while not args:
        operation = input('''
        Please enter operation code as below:
          '1 - create user record;
          '2 - read user record;
          '3 - update user record;
          '4 - delete user record;
          '5 - show all records;
          '6 - exit;
        ''')
        operation_code = operation.strip()
        actions = generate_actions()
        operate(actions=actions, code=operation_code)


if __name__ == '__main__':
    phonebook = phonebook.Phonebook()
    try:
        phonebook.load()
    except LoadError:
        exit()
    else:
        main()