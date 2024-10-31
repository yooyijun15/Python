# 가위바위보

# random 모듈
import random

# 주먹, 보자기, 가위 특수문자
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

# 리스트
list = [rock, paper, scissors]

# 0 - 주먹, 1 - 보자기, 2 - 가위
user_choice = int(input("What do you choose? Tpye 0 for Rock, 1 for Paper, or 2 for Scissors. 2 : "))
computer_choice = random.randint(0, 2)
# random 함수 .randint()

# 리스트의 인덱스 활용하여 특수문자 출력
print(f"< Your choice > {list[user_choice]}\n")
print(f"< Computer's choice > {list[computer_choice]}\n")

# 연산
# 버전 (3)
# 0 < 1, 0 > 2, 1 < 2
# 0 일 때를 제외하고 크면 승리
if user_choice == computer_choice:
    print("Game Again!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lost...")
elif user_choice > computer_choice:
    print("You Win!")
else:
    print("You Lost...")

# 버전 (2)
# if user_choice == computer_choice:
#     print("Game Again!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You Win!")
# elif user_choice == 1 and computer_choice == 0:
#     print("You Win!")
# elif user_choice == 2 and computer_choice == 1:
#     print("You Win!")
# else:
#     print("You Lost...")

# 버전 (1)
# if user_choice == computer_choice:
#     print("Game Again!")
# elif user_choice == 0:
#     if computer_choice == 1:
#         print("You Lost...")
#     else:
#         print("You Win!")
# elif user_choice == 1:
#     if computer_choice == 0:
#         print("You Win!")
#     else:
#         print("You Lost...")
# else:
#     if computer_choice == 0:
#         print("You Lost...")
#     else:
#         print("You Win!")
