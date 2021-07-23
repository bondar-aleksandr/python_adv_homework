import serialize
import person


class LoadError(Exception):
    pass


class SaveError(Exception):
    pass


class Phonebook:
    def __init__(self):
        self.records = {}

    def __len__(self):
        return len(self.records)

    def __repr__(self):
        return f'Phonebook(records={len(self)})'

    def load(self):
        try:
            with open(serialize.FILENAME, f'r{serialize.file_access_mode}') as f:
                raw_data = serialize.load(f)
        except FileNotFoundError:
            raise LoadError(f'Cannot load phonebook from file {serialize.FILENAME}!')
        else:
            for record in raw_data:
                per = person.Person()
                for key, value in raw_data[record].items():
                    for attr in vars(per):
                        if attr == key:
                            per.__setattr__(attr, value)
                            break
                if per.name is None:
                    raise LoadError(f'"name" attribute is missing in file {serialize.FILENAME}!')
                self.records[per.name] = per

    def save(self):
        raw_data = {}
        for name in self.records:
            raw_data[name] = vars(self.records[name])
        try:
            with open(serialize.FILENAME, f'w{serialize.file_access_mode}', newline='') as f:
                serialize.dump(raw_data, f)
        except Exception:
            raise SaveError(f'Cannot save phonebook to file {serialize.FILENAME}!')

    def create_record(self, name=None, phone=None):
        if not name:
            name = input('enter name: ')
        if not phone:
            phone = input('enter phone: ')
        self.records[name] = person.Person(name=name, phone=phone)
        print('Success!')

    def delete_record(self, name=None):
        if not name:
            name = input('Enter name:')
        if not name.isalpha():
            raise ValueError('Name must be letters!')
        try:
            del self.records[name]
            print('Success!')
        except KeyError:
            print(f'User {name} doesn\'t exists!')