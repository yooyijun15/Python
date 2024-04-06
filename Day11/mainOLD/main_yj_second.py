from art import logo
import random

card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
is_game_over = False

def score():
  print(f"Your cards: {user_card}, current score: {sum(user_card)}")
  print(f"Computer's first card: {computer_card[0]}")

def final_score():
  print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
  print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")

def blackjack(cards):
  if 11 in cards and 10 in cards:
      return 0
  if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
      return sum(cards)

def onemore_card():
  if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
    user_card.append(random.choice(card_list))
    if sum(user_card) > 21:
      final_score()
      print("You went over. You lose 😭")
    else:
      score()
      onemore_card()
  else:
    final_score()
    if sum(user_card) > sum(computer_card):
      print("You win 😁")
    elif  sum(computer_card) > sum(user_card):
      print("You lose 😭")
    else:
      print("Draw 🙃")

def computer_play():
  if sum(computer_card) < 21:
    again_value = [0,1]
    if random.choice(again_value) == 1:
      computer_card.append(random.choice(card_list))
      if sum(computer_card) > 21:
        final_score()
        print("Opponent went over. You win 😉")
        return 0
      else:
        computer_play()

while not is_game_over:
  if input("Do you want to play a game of a Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    user_card = []
    computer_card = []
    computer_card = random.sample(card_list,2)
    user_card = random.sample(card_list,2)
    if blackjack(user_card) == 0:
      final_score()
      print("Your's blackjack! 😎")
      is_game_over = True
    elif blackjack(computer_card) == 0:
      final_score()
      print("Computer's blackjack! 🤯")
      is_game_over = True
    else:
      score()
      if computer_play() != 0:
        onemore_card()
      is_game_over = True
