print('MokéBeast')


def runGame():
    beastName = input("Beast Name: ")
    beastType = input("Type: ")
    specialMove = input("Special Move: ")
    hp = int(input("HP: "))
    mp = int(input("MP: "))

    print()
    beast = {"Beast Name": beastName, 'Type': beastType, 'Special Move': specialMove, 'HP': hp, 'MP': mp}

    for key, values in beast.items():
        if beast['Type'].lower() == 'fire':
            print(f'\033[31m{key}: {values}')
        elif beast['Type'].lower() == 'water':
            print(f'\033[34m{key}: {values}')
        elif beast['Type'].lower() == 'air':
            print(f'\033[32m{key}: {values}')



runGame()