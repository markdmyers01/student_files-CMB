"""

       Mini-task 2 - Accessing sequences

"""
records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sinotech.com')
]

# Display Sally Edwards age
print(records[2][2])

# Add a new record into records
records.append(('Ellen', 'James',   32, 'jamestel@google.com'))
print(records)

# Display how many records you then have after this
print(len(records))

# Display how many fields are in the second record from the end record
print(len(records[-3]))

# Display how long Keith Cramer's email is
print(len(records[-2][3]))
