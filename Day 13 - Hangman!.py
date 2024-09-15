import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

wordlist = 'British'
guessedWord = []
lives = 6

def runGame():
    while lives > 0:
        for i in wordlist:
            if i in guessedWord:
                print(i, end=" ")
            else:
                print('_', ' ')

