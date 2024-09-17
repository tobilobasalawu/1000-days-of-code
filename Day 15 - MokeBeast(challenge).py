print('MokéBeast')

beastName = input("Beast Name: ")
beastType = input("Type: ")
specialMove = input("Special Move: ")
hp = int(input("HP: "))
mp = int(input("MP: "))

print()
beast = {"Beast Name" : beastName, 'Type' : beastType, 'Special Move' : specialMove, 'HP' : hp, 'MP': mp}

for key,values in beast.items():
    print(f'{key}:  {values}')
