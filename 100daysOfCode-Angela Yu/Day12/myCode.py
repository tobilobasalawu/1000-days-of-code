import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

userInput = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

randomNumber = random.randint(1,100)
easyScore = 10
hardScore = 5

if userInput == 'easy':
    while 0 < easyScore <= 10:
        print(f"You have {easyScore} attempts remaining to guess the number")
        userGuess = int(input('\nMake a guess: '))
        if userGuess > randomNumber:
            print('Too high\nGuess again.')
            easyScore-=1
        elif userGuess < randomNumber:
            print('Too Low\nGuess again.')
            easyScore-=1
        else:
            print(f'\n😁Yayy,You won\nThe secret Number is {randomNumber}')
            break
    else:
        print("\nYou've run out of guesses, ☹ You lose.")
else:
    while 0 < hardScore <= 5:
        print(f"You have {hardScore} attempts remaining to guess the number")
        userGuess = int(input('\nMake a guess: '))
        if userGuess > randomNumber:
            print('Too high\nGuess again.')
            hardScore-=1
        elif userGuess < randomNumber:
            print('Too Low\nGuess again.')
            hardScore-=1
        else:
            print(f'\n😁Yayy,You won\nThe secret Number is {randomNumber}')
            break
    else:
        print("\nYou've run out of guesses, ☹ You lose.")