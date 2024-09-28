from replit import clear

from gameData import data
from art import logo,vs
import random

def logoFunction():
    print(logo)
def vsFunction():
    print(vs)


def main():
    score = 0
    index = 0
    index2 = 1

    correct = True

    randomA = data[index]
    randomB = data[index2]

    while correct:
        A = f"Compare A: a {randomA['name']}, a {randomA['description']}, from {randomA['country']}.\n"
        B = f"Against B: a {randomB['name']}, a {randomB['description']}, from {randomB['country']}."

        logoFunction()
        print(A)
        vsFunction()
        print(B)

        higher = max(randomA['follower_count'],randomB['follower_count'])

        userChoice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if userChoice == 'a' and higher == randomA['follower_count']:
            score+=1
            index2 += 1
            index += 1

            randomA = data[index]
            randomB = data[index2]
            print(f"You're right! Current score: {score}")
        else:
            print(f"You're wrong, your final score: {score}")
            break
            clear()

main()

