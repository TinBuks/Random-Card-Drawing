import random

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append((suit, rank))
  random.shuffle(deck)
  return deck

def draw_card(deck, number_of_cards):
  hand = []
  for cards in range(number_of_cards):
    if deck:
      hand.append(deck.pop())
  return hand, deck

deck = create_deck()

def show_card(card):
  space = " "
  if len(card[1]) == 2:
    space = ""
  print (f"""
  +-------+
  |{card[1]}     {space}|
  |       |
  |   {card[0]}   |
  |       |
  |{space}     {card[1]}|
  +-------+
  """)

while len(deck) > 0:
  num_cards = input("How many cards would you like to draw? ")
  num_cards = int(num_cards)
  hand, deck = draw_card(deck, num_cards)
  for card in hand:
    show_card(card)
else:
  print("We are out of cards.")
