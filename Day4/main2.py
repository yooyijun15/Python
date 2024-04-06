import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
value_list = [rock, paper, scissors]
value = int(input("What do you choose? Tpye 0 for Rock, 1 for Paper, or 2 for Scissors. "))
random_value = random.randint(0,2)

print(f"Your's choice: {value_list[value]}")
print(f"Computer's choice: {value_list[random_value]}")

if value == random_value:
  print("Game Again!")
elif value == 0 and random_value == 2:
  print("You Win!")
elif value > random_value:
  print("You Win!")
else:
  print("You Lose!")
