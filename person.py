class Person:
    def __init__(self, name=None, phone=None, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            if not value.isalpha():
                raise ValueError('Name must be letters!')
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value:
            if not value.isdigit():
                raise ValueError('Phone must be digits!')
        self._phone = value

    def to_dict(self):
        return {
            'name':self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

    @classmethod
    def from_dict(cls, d:dict):
        allowed_keys = 'name', 'phone', 'email', 'address'
        if not set(d.keys()) == set(allowed_keys):
            raise KeyError('Wrong keys!')
        return cls(**d)

    def __repr__(self):
        return f'Person(name={self.name}, phone={self.phone}, email={self.email}, address={self.address})'

    def __str__(self):
        return f'name: {self.name}\n' \
               f'phone: {self.phone}\n' \
               f'email: {self.email}\n' \
               f'address: {self.address}'
