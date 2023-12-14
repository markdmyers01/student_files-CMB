"""

    03_legb.py
    Understanding variable scope and visibility.

"""
x = 10 # Global
my_list = (1, 2, 3)

y = 0


def f1(x_val):
    global x
    x = x_val + 50 # Enclosing
    # global y
    # y += 1

    def f2():
        # list(my_list)
        x = 30 # Local
        print(x)
    print(x)
    f2()


f1(x)
print(x)
# print(my_list)
# print(y)

print(globals(), '\n\n\n')
print(globals()['__file__'])
