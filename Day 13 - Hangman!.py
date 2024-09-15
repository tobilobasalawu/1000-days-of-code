import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

Wordlist = ['Telephone', 'British', 'Chat', 'Evil']
randomWords = random.choice(Wordlist)
print(randomWords)

lives = 5

userInput = input('Choose a Letter: ')

if userInput in randomWords:
    print('You found a letter')

