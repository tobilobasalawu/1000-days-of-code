import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

wordlist = 'wagawan'
guessedWord = []

def runGame():
    lives = 6
    while lives > 0:
        for i in wordlist:
            if i in guessedWord:
                print(i, end=" ")
            else:
                print('_', end=' ')
        print()

        userInput = input("Enter a word:\n").lower()

        if userInput in guessedWord:
            print(f'You already guessed the letter {userInput}')

        elif userInput in wordlist:
            print('\nCorrect Guess!')
            guessedWord.append(userInput)

        else:
            print('\nWrong Guess!')
            lives -= 1
            print(f'You have {lives} lives left')



runGame()






