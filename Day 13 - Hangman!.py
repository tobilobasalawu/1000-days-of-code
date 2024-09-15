import random
from urllib.parse import uses_netloc

print('HANGMAN GAME💅🏾\n')

Wordlist = ['Telephone', 'British', 'Chat', 'Evil']
randomWords = random.choice(Wordlist)
print(randomWords)

letterPrint = []
lives = 5

def runGame():
    while True:
        userInput = input('Choose a Letter: ')
        if userInput in letterPrint:
            print('You have already chosen the letter')
            continue

        if userInput in randomWords:
            print('You found a letter')
            letterPrint.append(userInput)
        else:
            print('Nope, not in there')

runGame()