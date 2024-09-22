import random, time, os
print("🔨 CHARACTER BUILDER 🔨\n")

def mainGame():
    charName = input("Name your Legend: \n")
    charType = input("Character Type(Human, Elf, Wizard, Orc): \n")
    print(f'\n{charName}')
    healthStat = ((random.randint(1,6) * random.randint(1,12)) / 2) + 10
    strengthStat = ((random.randint(1,6) * random.randint(1,8)) / 2) + 10

    time.sleep(0.7)
    return (f'HEALTH: {healthStat}\nSTRENGTH: {strengthStat} \n\nMay your name go down in Legend..\n')

    time.sleep(0.7)

while True:
    run = mainGame()
    print(run)
    time.sleep(1)
    menu = input("Again?:\n")
    if menu.lower() == 'yes':
        os.system("cls")
        time.sleep(1)
    else:
        break





