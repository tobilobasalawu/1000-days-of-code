import random
print('🪓 CHARACTER STAT GENERATOR 🪓\n')

warriorName = input('Name your warrior: ')


def generateHealth():
    sidedRoll6 = random.randint(1,6)
    sidedRoll8 = random.randint(1, 8)

    rollMultiplication =  sidedRoll8 * sidedRoll6

    return f"Their health is {rollMultiplication}hp"

generateHealth()
print(generateHealth())
