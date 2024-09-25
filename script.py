#!/usr/bin/env python3

print('1. Convert inches -> cm')
print('2. Convert cm -> inches')
X = input('Make your selection (1,2): ')
if X == '1':
    Y = float(input('Enter inches: '))
    Z = Y * 2.54
    print('Number of cm: ' + str(Z))
elif X == '2':
    A = float(input('Enter cm: '))
    B = A / 2.54
    print('Number of inches: ' + str(B))
else:
    print('Invalid entry')
