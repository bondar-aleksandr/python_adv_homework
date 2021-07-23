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
        except serialize.FileError:
            print(f'Wrong file format for file {serialize.FILENAME}!')
            raise LoadError(f'Wrong file format for file {serialize.FILENAME}!')
        except FileNotFoundError:
            raw_data = {}

        for name in raw_data:
            try:
                per = person.Person.from_dict(raw_data[name])
            except KeyError:
                raise LoadError(f'Wrong person attributes specified in file {serialize.FILENAME}!')
            except ValueError:
                raise LoadError(f'Wrong chars found in "name" or "phone" attributes!')
            self.records[per.name] = per

    def save(self):
        raw_data = {}
        for name in self.records:
            raw_data[name] = self.records[name].to_dict()
        try:
            with open(serialize.FILENAME, f'w{serialize.file_access_mode}') as f:
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
        try:
            self.records[name] = person.Person(name=name, phone=phone, email=email, address=address)
        except ValueError:
            print('Name must be letters, phone must be digits!')
            return
        print('Success!')

    def read_record(self, name=None):
        if not name:
            name = input('Enter name:')
        if not name.isalpha():
            print('Name must be letters!')
            return
        try:
            print(config.SEPARATOR)
            print(self.records[name])
            print(config.SEPARATOR)
        except KeyError:
            print(f'User {name} doesn\'t exists!')

    def update_record(self, name, **kwargs):
        if not name:
            name = input('Enter name to update: ')
        try:
            record = self.records[name]
            record: person.Person
        except KeyError:
            print(f'User {name} doesn\'t exists!')
        else:
            msg = f'There are next field available for update:\n'
            for attr in record.to_dict():
                msg += f'{attr}\n'
            print(msg)
            attr = input('Please enter field to update: ')
            if attr not in record.to_dict().keys():
                print('Wrong field entered!')
                return
            if attr == 'name':
                new_name = input('enter new name: ')
                if not new_name.isalpha():
                    print('Name must be letters!')
                    return
                self.create_record(name=new_name, phone=record.phone, email=record.email, address=record.address)
                del self.records[name]
            else:
                new_value = input(f'Enter new value for {attr}: ')
                try:
                    setattr(record, attr, new_value)
                except ValueError:
                    print('Wrong value provided! Name must be letters, phone must be digits!')
                    return
                print('Success!')

    def delete_record(self, name=None):
        if not name:
            name = input('Enter name to delete:')
        if not name.isalpha():
            print('Name must be letters!')
            return
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