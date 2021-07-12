import config
try:
    import serialize
except ImportError:
    print('Wrong serializer format specified! Only json/pickle/csv are allowed')
    exit()

import model
import functools


def main(records):

    operation_actions = {
        '1': functools.partial(model.create_record, records=records),
        '2': functools.partial(model.read_record, records=records),
        '3': functools.partial(model.update_record, records=records),
        '4': functools.partial(model.delete_record, records=records),
        '5': functools.partial(model.show_all, records=records),
        '6': exit,
    }

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