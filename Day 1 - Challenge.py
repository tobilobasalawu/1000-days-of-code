import time
print('Math Game!')

userInput = int(input("Name your multiples: "))
score = 0

def runGame():
    for i in range(1, 4):
        valueInput = int(input(f"{i} x {userInput} = "))
        if valueInput == i * userInput:
            print('Great Work! 🥳')


runGame()