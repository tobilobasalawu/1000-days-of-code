import time
print('Math Game!')

userInput = int(input("Name your multiples: "))

def runGame():
    for i in range(1, 11):
        valueInput = int(input(f"{i} x {userInput} = \n"))
        score = 0
        if valueInput == i * userInput:
            score += 1
            print('Great Work! 🥳' or 'Flex!💅🏾')
        else:
            print(f'Sike! 😂 The answer is {i * userInput}')


runGame()