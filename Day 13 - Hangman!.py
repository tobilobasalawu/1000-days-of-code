import random
import time

print('HANGMAN GAME💅')

listword = ['television', 'grammar', 'software', 'intelligence']
wordChoice = random.choice(listword)
guessedWord = []

def runGame():
    lives = 6
    while lives > 0:
        for i in wordChoice:
            if i in guessedWord:
                time.sleep(0.6)
                print(i, end=" ")
            else:
                time.sleep(0.1)
                print('_', end=' ')
        print()

        userInput = input("\nEnter a word:\n").lower()

        if userInput in guessedWord:
            time.sleep(0.8)
            print(f"\nYou already guessed the letter '{userInput}'")

        elif userInput in wordChoice:
            print('\nCorrect Guess!🎉')
            guessedWord.append(userInput)
        else:
            print('\nWrong Guess!❌')
            lives -= 1
            time.sleep(1)
            print(f'You have {lives} lives left')

        if set(guessedWord) == set(wordChoice):
            print(f"You won, My man you're a star🎉.\nThe word is {wordChoice.upper()}!")
            break

    if lives == 0:
        print(f'\nYou Lost 😪')
        time.sleep(0.3)
        print(f"The word is", end=" ")
        time.sleep(0.8)
        print(f"'{wordChoice.upper()}'")


runGame()






