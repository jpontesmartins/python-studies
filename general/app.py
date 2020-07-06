from collections import deque
from math import pi

print('==================================')
print('studiyng data structures in python (part 1)')
print('==================================\n')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana' ]

number_of_apples = fruits.count('apple')
print(f'number of apples: {number_of_apples}')

number_of_tangerines = fruits.count('tangerine')
print(f'number of tangerines: {number_of_tangerines}')

index_of_banana = fruits.index('banana')
print(f'index of banana: {index_of_banana}')

next_index_of_banana = fruits.index('banana',4)
print(f'next index of banana after index 4: {next_index_of_banana}')

print(f'fruits: {fruits}')

fruits.reverse()
print(f'same basket fruits in reverse order: {fruits}')

another_basket = fruits[::]
print(f'another basket of fruits: {another_basket}')

another_basket_reversed = fruits[::-1]
print(f'another basket of fruits reversed: {another_basket_reversed}')

another_basket_reversed.sort()
print(f'basket in order: {another_basket_reversed}')

another_basket_reversed.pop()
print(f'using POP for remove last element: {another_basket_reversed}')

print('------')

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')

print(f'list: {queue}')
print(f'saida: {queue.popleft()}')
print(f'list now: {queue}')
queue.pop()
print(f'list now: {queue}')

print('for in queue')
for i in queue:
    print(f'data: {i} - type: {type(i)}')

print('list comprehensions')

square = []
for x in range(10):
    square.append(x**2)
print(square)

print('other way...')

squares_2 = list(map(lambda x: x**2, range(10)))
print(f'squares_2: {squares_2}')

squares_3_calculation = map(lambda y: y**2, range(5))
print(f'squares_3: {list(squares_3_calculation)}')

square_4 = [x**2 for x in range(4)]
print(f'squares_4: {square_4}')

vec = [-4, -2, 0, 2, 4]
print(vec)

vec_double_values = [x*2 for x in vec]
print(vec_double_values)

vec_positive_numbers = [x for x in vec if x >=0]
print(vec_positive_numbers)

vec_other = [abs(y) for y in vec_double_values]
print(vec_other)

pi_decimal_cases = [str(round(pi, i)) for i in range(1,6)]
print(pi_decimal_cases)

# Links
## https://docs.python.org/3/tutorial/datastructures.html

## https://docs.python.org/3/tutorial/stdlib.html
## https://docs.python.org/3/library/functions.html#enumerate

# Mutable functions doesn't return a value

# You might have noticed that methods like insert, remove, sort or reverse 
# that only modify the list have no return value printed – 
# they return the default None. 
# This is a design principle for all mutable data structures in Python.
# https://docs.python.org/3/tutorial/datastructures.html




