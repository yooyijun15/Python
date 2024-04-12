from game_data import data
from random import choice
from art import logo, vs
#from replit import clear

# 리스트 생성
star_list = []

# 원소 0~49 : game_data 리스트의 인덱스
for i in range(len(data)):
    # append : 리스트 값 추출
    star_list.append(i)

# 데이터 형식 변환
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."

# 대상 A
def target_A(numA, first_time):
  # choice() : 리스트에서 랜덤 값 추출
  # 한번만 A값 랜덤 추출
  while first_time == True:
    numA = choice(star_list)
    # 추출 값 제거
    # 중복 추출 막기 위한 것
    star_list.remove(numA)
    first_time = False
  print(f"Compare A : {format_data(data[numA])}")
  #print(f"Compare A : {data[numA]['name']}, a {data[numA]['description']}, from {data[numA]['country']}.")
  return numA, first_time

# 대상 B (단, A와 다른 대상)
def target_B(numB):
  numB = choice(star_list)
  star_list.remove(numB)
  print(f"Against B : {format_data(data[numB])}")
  #print(f"Against B : {data[numB]['name']}, a {data[numB]['description']}, from {data[numB]['country']}.")
  return numB

# 대상 A, B 비교 결과
def check_result(A_follower, B_follower:
  if A_follower > B_follower:
    result = 'A'
elif B_follower > A_follower:
    result = 'B'
    numA = numB
  else:
    result = 'C'
  # , 사용하여 여러 값 반환
  return result, numA

# User 답변
def user_answer(result, answer, score, game_over):
    if result == answer:
      score += 1
      #clear()
    else :
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True
    return score, game_over

# 게임 시작
def game():
  game_over = False
  first_time = True
  score = 0
  valueA = 0
  valueB = 0

  while not game_over:
    print(logo)
    print(f"Score: {score}")
    valueA, first_time = target_A(valueA, first_time)
    print(vs)
    valueB = target_B(valueB)
    A_follower = data[numA]['follower_count']
    B_follower = data[numB]['follower_count']
    # , 사용하여 여러 값 반환
    result, valueA = check_result(A_follower, B_follower)
    # 답변
    answer = input("Who has more followers? Type 'A' or 'B': ")
    score, game_over = user_answer(result, answer, score, game_over)

game()
