import serialize
import person


class LoadError(Exception):
    pass


class SaveError(Exception):
    pass


class Phonebook:
    def __init__(self):
        self.records = {}

    def load(self):
        try:
            with open(serialize.FILENAME, f'r{serialize.file_access_mode}') as f:
                self.records = serialize.load(f)
        except FileNotFoundError:
            raise LoadError(f'Cannot load phonebook from file {serialize.FILENAME}!')

    def save(self):
        try:
            with open(serialize.FILENAME, f'w{serialize.file_access_mode}', newline='') as f:
                serialize.dump(self.records, f)
        except Exception:
            raise SaveError(f'Cannot save phonebook to file {serialize.FILENAME}!')

    def create_record(self, name=None, phone=None):
        if not name:
            name = input('enter name: ')
        if not phone:
            phone = input('enter phone: ')
        self.records[name] = person.Person(name=name, phone=phone)
        print('Success!')


