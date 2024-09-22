import random
from itertools import count

print('🪓 CHARACTER STAT GENERATOR 🪓\n')

charNumber = int(input('How many characters : '))
count = charNumber

def generateHealth():
    warriorName = input('Name your warrior: ')
    sidedRoll6 = random.randint(1,6)
    sidedRoll8 = random.randint(1, 8)

    rollMultiplication =  sidedRoll8 * sidedRoll6
    return (f"Their health is {rollMultiplication}hp\n")

while count > 0:
    warr = generateHealth()
    print(warr)
    count-=1

