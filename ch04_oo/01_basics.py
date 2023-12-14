"""

    01_basics.py
    A basic Python Class

"""


class Contact:
    def __init__(self, name='', address=''):
        self.name = name
        self.address = address

    def __str__(self):
        return self.name


c = Contact('John Smith', '123 Main St.')
print(c.address)
print(c)
c.foo = 'bar'
print(c.foo)
d = Contact('John Smith', '123 Main St.')
d.name = 'Johnny Doe'
print(d.name)
