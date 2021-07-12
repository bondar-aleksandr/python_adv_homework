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
if len(sys.argv) > 1:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=False, type=str, help='username to operate upon')
    parser.add_argument("--phone", required=False, type=str, help='phone to operate upon')
    parser.add_argument("--operation", required=True, type=str, choices=['create', 'read', 'update', 'delete', 'show'])
    args = parser.parse_args()


def main(records, args:argparse.Namespace = None):

    operation_actions = {
        '1': functools.partial(model.create_record, records=records),
        '2': functools.partial(model.read_record, records=records),
        '3': functools.partial(model.update_record, records=records),
        '4': functools.partial(model.delete_record, records=records),
        '5': functools.partial(model.show_all, records=records),
        '6': exit,
    }

    if args:
        if args.create:
            user = args.user
            phone = args.phone
            model.create_record(records=records, name=user, phone=phone)


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
        try:
            operation_actions.get(operation_code, model.default_operation)()
        except KeyError:
            print('No such user!')
        except ValueError:
            print('Name/phone syntax error! Name must be symbols, phone must be numbers')
        finally:
            with open(serialize.FILENAME, f'w{serialize.file_access_mode}', newline='') as f:
                serialize.dump(records, f)


if __name__ == '__main__':
    try:
        with open(serialize.FILENAME, f'r{serialize.file_access_mode}') as f:
            records = serialize.load(f)
    except FileNotFoundError:
        records = {}
        main(records)
    except serialize.FileError:
        print(f'Wrong file format for file {config.filename}!')
    else:
        main(records)