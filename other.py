# import numpy as np

print('''CALCULATING UDLS WITH PYTHON
 Created by: M.JUBAIR CN_12\n''')


def print_menu():
    print('BEAM SELECTION: \n')
    print('1. cantilever')
    print('2. simply supported beam')
    print('3. over hanging beam\n')


print_menu()

g = input('\nEnter your beam type:\n')
h = 'cantilever'
i = 'simply supported beam'
j = 'over hanging beam'

if (g == h):
    w = float(input('\nEnter magnitude of UDL:\n'))
    u1 = input('Enter unit of load:\n')
    l = float(input('Enter the length of beam:\n'))
    u2 = input('Enter unit of length:\n')
    m = print('\nReaction of your beam is: ')
    Reaction = print(w * l, u1)
    # print(u1)
    n = print('\nMoment in your beam is:')
    Moment = print(w * l ** 2 / 2, u1, u2)

elif (g == i):
    o = float(input('\nEnter magnitude of UDL:\n'))
    u3 = input('Enter unit of load:\n')
    p = float(input('Enter the length of beam:\n'))
    u4 = input('Enter unit of length:\n')
    q = print('\nReaction of your beam is: ')
    r = print(o * p / 2, u3)

elif (g == j):
    s = float(input('\nEnter magnitude of UDL\n '))
    u5 = input('Enter the unit of load\n')
    t = float(input('Enter the length of beam (L1= A to B)\n '))
    u = float(input('Enter the length of beam (L2= B to C)\n '))
    u6 = input('Enter the unit of length\n')
    print('\nReaction of your beam is:')
    w = print(((s * t * 2) / 2 - (s * u * 2) / 2) / t, u5)
    # print(w/t,u5)

else:
    print('''Please make sure your spelling is correct. 
     All letters must be in lower case.''')
    i