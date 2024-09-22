import random, time, os
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

    time.sleep(1)
    os.system('cls')

    print('The battle begins!\n')

    while healthstat2 > 0 or healthstat1 > 0:
        roundWin1 = random.randint(1,6)
        roundWin2 = random.randint(1,6)
        diffStr = strstat2-strstat1
        if roundWin1 > roundWin2:
            print(f'{charName1} wins the blow\n{charName2} takes a hit, with {abs(diffStr) + 1} damage')
            print(f'{charName1}\nHEALTH:{healthstat1-diffStr}\n\n{charName2}\nHEALTH:{healthstat2}')
        else:
            print(f'{charName2} wins the blow\n{charName1} takes a hit, with {abs(diffStr) + 1} damage')
            print(f'{charName1}\nHEALTH:{healthstat1}\n\n{charName2}\nHEALTH:{healthstat2-diffStr}')
            break
runGame()
