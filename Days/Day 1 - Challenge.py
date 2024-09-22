import time
import random
print('Math Game!\n\n')

userInput = int(input("Name your multiples: "))

def runGame():
    score = 0
    correctStatement = ["Great Work! 🥳", "Very Demure!💅🏾"]
    for i in range(1, 11):
        valueInput = int(input(f"\n{i} x {userInput} = \n"))
        if valueInput == i * userInput:
            score += 1
            print(random.choice(correctStatement))
        else:
            print(f'Sike! 😂 The answer is {i * userInput}')
    print('\n. . .')
    time.sleep(1)
    print(f'\nYou scored {score} out of 10!')

runGame()