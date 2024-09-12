import random, time
print('🔪 BATTLE TIME 🔪')

def runGame():
    #print('Who are they battling ?')
    fighters = 2

    healthstat = ((random.randint(1,6) * random.randint(1, 12))/2) + 10
    strstat = ((random.randint(1,6) * random.randint(1, 8))/2) + 10
    while fighters > 0:
        if fighters == 1:
            print('\nWho are they battling?')
        print('')
        charName = input("Name your Legend:\n")
        charType = input("Character Type (Human, Elf, Wizard, Orc)):\n")

        print(f'\n{charName}\nHEALTH: {healthstat}\nSTRENGTH: {strstat}')
        fighters-=1





runGame()