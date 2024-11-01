# 소수 검사기
# 주어진 숫자가 N일 때,
# N을 2부터 N-1까지 나누었을 때, 나누어 떨어지지 않으면 소수

# 사용자 함수 정의 - prime_checker
# 매개변수 - num

# 방법 (2) - 2부터 N-1까지 전부 나누고, 최종 check_true 값으로 판별
def prime_checker(num):
    check_true = True
    for i in range(2,num):
        if num % i == 0:
            check_true = False
    if check_true == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# 방법 (1) - 2부터 N-1까지 나누어 떨어지는 하나의 경우 발생 시, for문 즉시 종료
# def prime_checker(num):
#     check_true = True
#     for i in range(2,num):
#         if num % i == 0:
#             check_true = False
#             print("It's a not prime number.")
#             break
#     if check_true == True:
#         print("It's a prime number.")

input_n = int(input("Please enter the number : "))

# 사용자 함수 호출
prime_checker(num=input_n)
