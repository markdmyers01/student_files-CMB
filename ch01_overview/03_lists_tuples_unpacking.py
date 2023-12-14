"""

    03_lists_tuples_unpacking.py
    Ways to create and work with lists and tuples

"""
my_list = []
my_list = list()

my_list = [1, 3, 5]
my_list = [3.3, 'hello', 'hello', 3.3]
my_list = list('hello')
print(my_list)

my_list = [1, 2, 3]
my_list.append(10)
my_list.insert(1, 'hello')
print(my_list)

# --------------------
# Tuples
my_tuple = ()
my_tuple = tuple()

my_tuple = (1, 3, 5)
my_tuple = (3.3, 'hello', 3.3)
my_tuple = tuple('hello')
my_tuple = (1,)
my_tuple = (1, 2, 'hello')

print(type(my_tuple))

contact = ('John Smith', ['123 Main St', 'Los Angeles', 'CA'])
# contact[0] = 'Jonathan Smith'
contact[1][0] = '456 Elm St'
contact[1].append('96210')
print(contact)


# --------------------
# Unpacking
person = ('Carla', 'Esposito', 44, 'cesp@bywaysmast.com')
first, last, age, email = person
print(person[1], last)

first, last, *other = person
print(other)

first, last, age, email, *other = person
print(other)

first, *other, email = person
print(other)
