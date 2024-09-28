import random
import sys

def startGameInput():
    startGame = input("Do you want to play the game of BlackJack? Type 'y' or 'n': ").lower()
    if startGame == 'y':
        return '🎴 BLACKJACK'
    else:
        return ''


def gameAlogrithm():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    userCards = []
    computerCards = []

    userRandom = random.randint(0,10), random.randint(1,10)
    for i in userRandom:
        userCards.append(i)

    computerRandom = random.randint(0,10)
    computerCards.append(computerRandom)


    userScore = sum(userCards)


    return f"Your Cards: {userCards}, current score: {userScore}\n Computer's first Card: {computerCards}"

print(gameAlogrithm())





#print(startGameInput())

