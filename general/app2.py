from collections import deque
from math import pi

print('==================================')
print('studiyng data structures in python (part 2)')
print('==================================\n')

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

# the 3 tranposed codes below do the same thing..

# 1
transposed = [[row[i] for row in matrix] for i in range(4)]
print(f'transposed: {transposed}')

# 2
other_transposed = []
for i in range(4):
    other_transposed.append([row[i] for row in matrix])
print(f'other_transposed: {other_transposed}')

# 3
other_transposed_2 = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    other_transposed_2.append(transposed_row)

print(f'other_transposed_2: {other_transposed_2}')

# 4
other_transposed_3 = list(zip(*matrix))
print(f'other_transposed_3: {other_transposed_3}')

# take a look at the built-in function
# link: https://docs.python.org/3/library/functions.html
# example: enumerate(..) e zip(..)



