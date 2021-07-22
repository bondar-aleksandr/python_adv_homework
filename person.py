class Person:
    def __init__(self, name, phone, email=None, address=None):
        if not name.isalpha:
            raise ValueError('Name must be letters!')
        self.name = name

        if not phone.isdigit:
            raise ValueError('Phone must be digits!')
        self.phone = phone

        self.email = email
        self.address = address

    def __repr__(self):
        return f'Person(name={self.name}, phone={self.phone}, email={self.email}, address={self.address})'

