'''
my2DList = [
    ['Jonny', 10, 'Mac'],
    ['Sian', 19, 'PC'],
    ['Jonny', 10, 'Mac']
]

my2DList[0][2] = 'Linux'
print(my2DList[0])

'''

import random
print("David's Nan's Bingo Card Generator")
print()

number = random.randint(1, 90)
numbers = []

for i in range(8):
    numbers.append(number)
numbers.sort()

print()

bingo = [
        [ numbers[0], numbers[1], numbers[2] ],
        [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
]

