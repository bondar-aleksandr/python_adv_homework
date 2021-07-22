import config
try:
    import serialize
except ImportError:
    print('Wrong serializer format specified! Only json/pickle/csv are allowed')
    exit()

import model
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


def main(records):

    def operate(actions: dict, code: str):
        try:
            actions.get(code, model.default_operation)()
        except KeyError:
            print('No such user!')
        except ValueError:
            print('Name/phone syntax error! Name must be symbols, phone must be numbers')
        finally:
            with open(serialize.FILENAME, f'w{serialize.file_access_mode}', newline='') as f:
                serialize.dump(records, f)

    def generate_actions(name: str=None, phone: str=None):
        actions = {
            '1': functools.partial(model.create_record, records=records, name=name, phone=phone),
            '2': functools.partial(model.read_record, records=records, name=name),
            '3': functools.partial(model.update_record, records=records, name=name, phone=phone),
            '4': functools.partial(model.delete_record, records=records, name=name),
            '5': functools.partial(model.show_all, records=records),
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
    phonebook.load()
    while True:
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

        actions = {
            '1': phonebook.create_record,
            # '2': functools.partial(model.read_record, records=records, name=name),
            # '3': functools.partial(model.update_record, records=records, name=name, phone=phone),
            # '4': functools.partial(model.delete_record, records=records, name=name),
            # '5': functools.partial(model.show_all, records=records),
            # '6': exit,
        }
        actions.get(operation_code)()




    # try:
    #     with open(serialize.FILENAME, f'r{serialize.file_access_mode}') as f:
    #         records = serialize.load(f)
    # except FileNotFoundError:
    #     records = {}
    #     main(records)
    # except serialize.FileError:
    #     print(f'Wrong file format for file {config.filename}!')
    # else:
    #     main(records=records)