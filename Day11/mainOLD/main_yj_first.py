from art import logo
import random

card_list = [1,2,3,4,5,6,7,8,9,10,10,10,10]
user_card = []
computer_card = []

def score():
  print(f"Your cards: {user_card}, current score: {sum(user_card)}")
  print(f"Computer's first card: {computer_card[0]}")

def final_score():
  print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
  print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")

def new_card():
  if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
    user_card.append(random.choice(card_list))
    # 리스트에 새로운 값 추가
    # user_card.append = random.choice(card_list)
    # AttributeError: 'list' object attribute 'append' is read-only 발생
    # https://www.delftstack.com/ko/howto/python/python-attributeerror-list-object-attribute-append-is-read-only/
    score()
    if sum(user_card) > 21:
      final_score()
      print("You went over. You lose 😭")
      game()
    else:
      new_card()
  else:
    final_score()
    result()
    game()

def game():
  if input("Do you want to play a game of a Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    global user_card, computer_card
    computer_card = random.sample(card_list,2)
    user_card = random.sample(card_list,2)
    #computer_card = random.choice(card_list) // 리스트에서 하나의 랜덤 값만 추출
    #computer_card = random.sample(card_list,2) // 리스트에서 다수(ex.2)의 랜덤 값 추출
    blackjack()
    score()
    computer_play()
    new_card()

def computer_play():
  if sum(computer_card) < 21:
    again_value = [0,1]
    if random.choice(again_value) == 1:
      computer_card.append(random.choice(card_list))
      computer_play()
      if sum(computer_card) > 21:
        final_score()
        print("Opponent went over. You win 😉")
        game()

def result():
  if sum(user_card) > sum(computer_card):
    print("You win 😁")
  elif  sum(computer_card) > sum(user_card):
    print("You lose 😭")
  else:
    print("Draw 🙃")

def blackjack():
    if 1 in user_card and 10 in user_card:
        print("Your's blackjack! 😎")
        game()
    if 1 in omputer_card and 10 in omputer_card:
        print("Computer's blackjack! 🤯")
        game()

game()
