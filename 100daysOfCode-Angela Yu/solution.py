import random
def deal_card(): #returns random card from deck
    cards = [11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
game_over = False

def calculate_score(cards): #calculating scores
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)#calculating user score
    computer_score = calculate_score(computer_cards) #calculating computer score
    print(f"Your Cards: {user_cards}, current score: {user_score}\n Computer's Card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:#game ends if blackjack in user&computer or greater than 21
        game_over = True
    else:
        userInput = input("Type 'y' to get another card, type 'n' to pass: ")
        if userInput == 'y':
            user_cards.append(deal_card()) #if user selects another card, it should be added to current card list
        else:
            game_over=True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)