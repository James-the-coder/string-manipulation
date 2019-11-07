import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

card_value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

suit = suits[random.randint(0,3)]

card = card_value[random.randint(0,12)]

print(card + " of " + suit)
