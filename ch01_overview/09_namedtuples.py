"""

    09_namedtuples.py
    Creating the classic namedtuple.

"""
from collections import namedtuple

c = namedtuple('Contact', 'first last age email')

records = [
    c('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    c('Ellen', 'James',   32, 'jamestel@google.com'),
    c('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    c('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]
records.sort(key=lambda one_rec: one_rec.age, reverse=True)

for record in records:
    print(record.last, record.age, record.email)

# records[0].age = 44

print(type(records[0]))
