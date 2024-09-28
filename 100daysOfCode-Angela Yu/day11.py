import random
import sys


def startGameInput():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    userCards = []
    computerCards = []

    r = random.randint(1,12)
    deckRandom = random.randint(1,r)
    userRandom = random.randint(0, 10), random.randint(1, 10)
    computerRandom = random.randint(1, 10)

    userScore = 0
    computerScore = 0

    blackJack = 21

    startGame = input("Do you want to play the game of BlackJack? Type 'y' or 'n': ").lower()
    if startGame == 'y':
        print('🎴 BLACKJACK')
        for i in userRandom:
            userCards.append(i)
        computerCards.append(computerRandom)

        userScore = sum(userCards)
        print(f"Your Cards: {userCards}, current score: {userScore}\n Computer's first Card: {computerCards}")

        userInput = input("Type 'y' to get another card, type 'n' to pass: ")
        if userInput.lower() == 'y':
            userCards.append(deckRandom)
            userScore = sum(userCards)
            #computerScore = sum(computerCards)

            print(f"Your Cards: {userCards}, current score: {userScore}\n Computer's Card: {computerCards}\n")

        else:
            if userScore > blackJack and computerScore == blackJack:
                print(f"Your Cards: {userCards}, current score: {userScore}\n Computer's Card: {computerCards}, final Score:{computerScore}\nYou Lose!!")
            elif userScore == blackJack and computerScore > blackJack:
                print(f"Your Cards: {userCards}, current score: {userScore}\n Computer's Card: {computerCards}\nYou Win!!")
            elif userScore < blackJack and computerScore < blackJack:
                print(f"Your Cards: {userCards}, current score: {userScore}\n Computer's Card: {computerCards}\n{max(computerScore,userScore)}")



    else:
        print('')


#startGameInput()





print(startGameInput())

