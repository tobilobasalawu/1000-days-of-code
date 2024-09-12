import random, time
print('🔪 BATTLE TIME 🔪\n')


def runGame():
    healthstat1 = ((random.randint(1, 6) * random.randint(1, 12)) / 2) + 10
    strstat1 = ((random.randint(1, 6) * random.randint(1, 8)) / 2) + 10

    healthstat2 = ((random.randint(1, 6) * random.randint(1, 18)) / 2) + 10
    strstat2 = ((random.randint(1, 6) * random.randint(1, 26)) / 2) + 10


    charName1 = input("Name your Legend:\n")
    charType1 = input("Character Type (Human, Elf, Wizard, Orc)):\n")
    print(f'\n{charName1}\nHEALTH: {int(healthstat1)}\nSTRENGTH: {int(strstat1)}')

    print('\nWho are they battling?\n')

    charName2 = input("Name your Legend:\n")
    charType2 = input("Character Type (Human, Elf, Wizard, Orc)):\n")
    print(f'\n{charName2}\nHEALTH: {int(healthstat2)}\nSTRENGTH: {int(strstat2)}')


runGame()