import random

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

password_list = []
password_char = ""


print("Welcome to the PyPassword Generator!")
count_password = int(
    input("How many letters would you like in your password?\n"))
count_symbols = int(input("How mamy symbols would you like?\n"))
count_numbers = int(input("How many numbers would you like?\n"))


for char in range(1, count_password + 1):
    password_list += random.choice(letters)

for char in range(1, count_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, count_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for char in password_list:
    password_char += char

print(f"Here is your password: {password_char}")
