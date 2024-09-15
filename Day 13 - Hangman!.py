import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

wordlist = 'wagawan'
guessedWord = []
lives = 6

def runGame():
    while lives > 0:
        for i in wordlist:
            if i in guessedWord:
                print(i, end=" ")
            else:
                print('_', ' ')

        userInput = input("Enter a word:\n").lower()

        if userInput in guessedWord:
            print(f'You already guessed the letter {userInput}')
            continue

        elif userInput in wordlist:
            print('Correct Guess!')
            guessedWord.append(userInput)







