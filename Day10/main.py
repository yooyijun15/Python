# art.py 파일의 LOGO 모듈 불러오기
from art import LOGO
print(LOGO)

# 연산 함수 생성하기
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

# 연산 함수의 ★딕셔너리★ 생성하기
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

# 계산기 함수 생성하기
def calculable():
  # 첫번째 값 입력받기
  first_num = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  # 재실행 여부 판단 역할
  shoud_continue = True

  while shoud_continue:
    # 딕셔너리의 key 입력받기  ex) +
    operations_symbol = input("Pick an operation from the line above: ")
    # 입력 받은 key의 value 불러오기  ex) add
    calculation_function = operations[operations_symbol]
    # 두번째 값 입력받기
    next_num = float(input("What's the next number? "))
    # 위의 결과에 따른 사칙연산 함수 불러오기  ex) add(5,3)
    result = calculation_function(first_num, next_num)
    # 연산 결과 출력하기
    print(f"{first_num} {operations_symbol} {next_num} = {result}")
    # 재실행 여부 입력받기
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
      # 기존 연산 계속할 경우, 연산 결과를 첫번째 값으로 바꾸기
      first_num = result
    else:
      # 새로운 연산 시작할 경우, while 문 종료
      shoud_continue = False
      # 재귀함수를 사용하여, 연산 계산기 다시 불러오기
      calculable()
# 계산기 함수 불러오기
calculable()
