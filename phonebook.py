import serialize
import person
import config


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
                            setattr(per, attr, value)
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

    def create_record(self, name=None, phone=None, email=None, address=None):
        if not name:
            name = input('enter name: ')
        if not phone:
            phone = input('enter phone: ')
        if not email:
            email = input('enter email: ')
        if not address:
            address = input('enter address: ')
        self.records[name] = person.Person(name=name, phone=phone, email=email, address=address)
        print('Success!')

    def read_record(self, name=None):
        if not name:
            name = input('Enter name:')
        if not name.isalpha():
            raise ValueError('Name must be letters!')
        try:
            print(config.SEPARATOR)
            print(self.records[name])
            print(config.SEPARATOR)
        except KeyError:
            print(f'User {name} doesn\'t exists!')

    def update_record(self, name=None):
        if not name:
            name = input('Enter name to update: ')
        try:
            record = self.records[name]
            record: person.Person
        except KeyError:
            print(f'User {name} doesn\'t exists!')
        else:
            msg = f'There are next field available for update:\n'
            for attr in vars(record):
                msg += f'{attr}\n'
            print(msg)
            attr = input('Please enter field to update: ')
            if attr not in vars(record):
                print('Wrong field entered!')
                return
            if attr.lstrip('_') == 'name':
                new_name = input('enter new name: ')
                self.create_record(name=new_name, phone=record.phone, email=record.email, address=record.address)
                del self.records[name]
            else:
                new_value = input(f'Enter new value for {attr}: ')
                setattr(record, attr, new_value)
                print('Success!')

    def delete_record(self, name=None):
        if not name:
            name = input('Enter name to delete:')
        if not name.isalpha():
            raise ValueError('Name must be letters!')
        try:
            del self.records[name]
            print('Success!')
        except KeyError:
            print(f'User {name} doesn\'t exists!')

    def show_all(self):
        for record in self.records:
            print(config.SEPARATOR)
            print(self.records[record])
        print(config.SEPARATOR)