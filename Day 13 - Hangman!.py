import random
import time

print('HANGMAN GAME💅')

wordlist = 'intelligence'
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

        userInput = input("\nEnter a word:\n").lower()

        if userInput in guessedWord:
            print(f"\nYou already guessed the letter '{userInput}'")

        elif userInput in wordlist:
            print('\nCorrect Guess!🎉')
            guessedWord.append(userInput)
        else:
            print('\nWrong Guess!')
            lives -= 1
            print(f'You have {lives} lives left')

        if set(guessedWord) == set(wordlist):
            print(f"You won, My man you're a star🎉🌹.\nThe word is {wordlist.upper()}!")
            break

    if lives == 0:
        print(f'\nYou Lost 😪, the word is {wordlist.upper()}')


runGame()






