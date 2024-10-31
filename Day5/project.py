# 랜덤 비밀번호 생성기

# random 모듈
import random

# 알파벳, 기호, 숫자 리스트
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
    '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 알파벳, 기호, 숫자 갯수 입력
letter_cnt = int(input("How many letters would you like in your password? "))
symbol_cnt = int(input("How many symbols would you like in your password? "))
number_cnt = int(input("How many number would you like in your password? "))

password_list = []
password_char = ""

# 비밀번호 리스트의 항목 랜덤 추가
for i in range(0, letter_cnt):
    password_list += random.choice(letters)

for j in range(0, symbol_cnt):
    password_list += random.choice(symbols)

for k in range(0, number_cnt):
    password_list += random.choice(numbers)

random.shuffle(password_list)
# random 함수 .shuffle()
# 문자열은 섞을 수 없으므로, 리스트 타입으로 섞은 후 문자열로 변경

# 리스트 -> 문자열 변환
for element in password_list:
    password_char += element

# 출력
print(f"random password : {password_char}")
