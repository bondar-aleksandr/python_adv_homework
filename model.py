import config


def check_existence(f):
    def wrapper(*args, records, name=None, **kwargs):
        if not name:
            name = input('Enter name:')
        if records.get(name) is not None:
            result = f(*args, records, name, **kwargs)
            return result
        else:
            raise KeyError('No such user!')
    return wrapper


def check_phone(phone: str) -> bool:
    return phone.isdigit()


def check_name(name: str) -> bool:
    return name.isalpha()


def create_record(records: dict, name:str = None, phone:str = None):
    if not name:
        name = input('enter name: ')
    if not phone:
        phone = input('enter phone: ')
    if not check_name(name) or not check_phone(phone):
        raise ValueError
    records[name] = phone
    print('Success!')


@check_existence
def read_record(records, name):
    if not check_name(name):
        raise ValueError
    phone = records[name]
    print(phone)


@check_existence
def update_record(records, name, phone=None):
    if not phone:
        phone = input('enter phone: ')
    if not check_phone(phone):
        raise ValueError
    records[name] = phone
    print('Success!')


@check_existence
def delete_record(records, name):
    if not check_name(name):
        raise ValueError
    del records[name]
    print('Success!')


def show_all(records):
    print(config.SEPARATOR)
    for name, phone in records.items():
        print(f'name: {name}, phone: {phone}')
    print(config.SEPARATOR)


def default_operation():
    print('Wrong operation code entered!')
