import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

Wordlist = ['Telephone', 'British', 'Chat', 'Evil']
randomWords = random.choice(Wordlist)
print(randomWords)

lives = 5

def runGame():
    while True:
        userInput = input('Choose a Letter: ')
        if userInput in randomWords:
            print('You found a letter')
        else:
            print('Nope, not in there')


runGame()