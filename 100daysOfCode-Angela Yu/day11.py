import random
import sys

def startGameInput():
    startGame = input("Do you want to play the game of BlackJack? Type 'y' or 'n': ").lower()
    if startGame == 'y':
        return '🎴 BLACKJACK'
    else:
        return ''


card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(startGameInput())

