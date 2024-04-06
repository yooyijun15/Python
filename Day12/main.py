# art.py 파일의 LOGO 모듈 불러오기
from art import logo
# random 모듈의 randint 함수 불러오기
from random import randint

# 전역상수 정의하기 - 난이도별 시도 횟수
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

# 난이도 선택 함수
def choose_difficulty():
    # while True : 유효하지 않은 값 입력 시, 무한 반복
    # 따라서 'easy' or 'hard' 이외 값 입력 시, 무한 반복
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            # return으로 전역상수 값 반환하기
            return EASY_ATTEMPTS
        elif difficulty == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Please select'easy' or 'hard'.")

# 추측값-정답 비교 함수
def check_guess(guess, NUMBER):
    if guess == NUMBER:
        print(f"You got it😜 The answer was {NUMBER}.")
        # 추측값과 정답 같을 시, True 반환
        return True
    elif guess > NUMBER:
        print("Too high.")
    else:
        print("Too low.")

# 게임 함수
def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 정답에 랜덤 값 부여
    NUMBER = randint(1,100)
    # 난이도 별 시도 횟수 부여
    attempts = int(choose_difficulty())
    # 게임 종료 변수
    gameStop = False

    # 추측 시도 - 게임 종료 False & 시도 횟수 유효할 경우
    while not gameStop and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # 추측값 입력받기
        guess = int(input("Make a guess: "))
        # 비교 함수에서 True 반환 시, 게임 종료
        gameStop = check_guess(guess, NUMBER)
        # 시도 횟수 차감
        attempts -= 1
        # 비교 함수에 의해 게임 종료가 True로 변경될 경우 제외하기 위한 조건문
        if not gameStop and attempts > 0:
            print("Guess again")
    # 시도 횟수 0이지만 게임 종료 False인 경우
    if not gameStop:
        print(f"You lose😭 The answer was {NUMBER}.")

# 게임 시작 조건문
if input("Do you want to play a game of a Number Guessing Game? Type 'y' or 'n': ") == 'y':
    main()
