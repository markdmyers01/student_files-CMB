"""

    04_inheritance_classic.py
    Classic Python Inheritance

"""


class Contact:
    def __init__(self, name='', address='', phones=None):
        self.name = name
        self.address = address
        self.phones = phones

    def __str__(self):
        return f'{self.name} {self.address} {self.phones}'


class BusinessContact(Contact):
    def __init__(self, name='', address='', phones=None,
                 email='', company='', position=''):
        Contact.__init__(self, name, address, phones)
        self.email = email
        self.company = company
        self.position = position


bc = BusinessContact('John Smith', '123 Main St.', {'work': '(970)322-9088', 'home': '(970)455-2390'}, 'bob@bobmail.com')
bc.name = 'Johnny Doe'
print(bc)
