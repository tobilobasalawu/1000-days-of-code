import time
print('Math Game!')

userInput = int(input("Name your multiples: "))

def runGame():
    score = 0
    for i in range(1, 11):
        valueInput = int(input(f"{i} x {userInput} = \n"))
        if valueInput == i * userInput:
            score += 1
            print('Great Work! 🥳' or 'Flex!💅🏾')
        else:
            print(f'Sike! 😂 The answer is {i * userInput}')
    print('. . .')
    time.sleep(1)
    print(f'\nYou scored {score} out of 10')

runGame()