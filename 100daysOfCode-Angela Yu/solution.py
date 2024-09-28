import random
def deal_card(): #returns random card from deck
    cards = [11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())