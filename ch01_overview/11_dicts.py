"""

    11_dicts.py
    Working with dictionaries.

"""
print('\nCreating and accessing dicts:')
my_dict = {}
my_dict = dict()
my_dict = {'pet1': 'dog', 'pet2': 'fish' }
my_dict = dict(pet1='dog', pet2='fish')

my_dict['pet3'] = 'cat'
print(my_dict['pet2'])
print(my_dict)


print('\nIterating dicts:')
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:                     # iterating a dictionary returns the keys
    print(item, end=' ')


print('\n\nIterating dict values:')
for val in d1.values():             # iterating the values
    print(val, end=' ')


print('\nIterating keys and values:')
for item in d1.items():         # iterating both keys and values
    print(f'Key: {item[0]}, Value: {item[1]}')


print('\nAccessing dicts:')
print(d1.get('Green'))              # returns None
print(d1.get('Green', 'N/A'))       # returns N/A
# print(d1['Green'])                 # generates a KeyError


print('\nSorting with dicts:')
list1 = sorted(d1)
list2 = sorted(d1.values())
list3 = sorted(d1.items())
print(list1, list2, list3)

list4 = sorted(d1.items(), key=lambda item: item[1])
print(list4)

back_to_dict = dict(list3)
print(back_to_dict)