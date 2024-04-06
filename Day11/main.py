from art import logo
import random

card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
  return random.choice(card_list)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
# if 11 in user_card and 10 and len(card_list) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def play_game():
  print(logo)

  user_card = []
  computer_card = []
  is_game_over = False

  for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(user_card)

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True

    user_shoud_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_shoud_deal == "y":
      user_card.append(deal_card())
    else:
      is_game_over = True

    while computer_score != 0 and computer_score < 17:
      computer_card.append(deal_card())
      computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
