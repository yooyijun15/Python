logo = r'''
 _____ ______ __   ________  _____  _____  _____ ______   ___  ___  ___
/  __ \| ___ \\ \ / /| ___ \|_   _||  _  ||  __ \| ___ \ / _ \ |  \/  |
| /  \/| |_/ / \ V / | |_/ /  | |  | | | || |  \/| |_/ // /_\ \| .  . |
| |    |    /   \ /  |  __/   | |  | | | || | __ |    / |  _  || |\/| |
| \__/\| |\ \   | |  | |      | |  \ \_/ /| |_\ \| |\ \ | | | || |  | |
 \____/\_| \_|  \_/  \_|      \_/   \___/  \____/\_| \_|\_| |_/\_|  |_/
'''

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 버전 (2)
# 암호 처리 및 출력
def cryptogram(act,message,shift_num):
    new_msg = ""
    if act == "decode":
        shift_num *= -1
    # + : encode, - : decode
    for i in range(0,len(message)):
        # 알파벳이 아닌 다른 문자 및 숫자 입력되는 경우 고려
        if message[i] in alphabet:
            ind_msg = alphabet.index(message[i])
            # 알파벳 갯수를 초과한 숫자가 입력되는 경우 고려
            # 내장함수 .index()
            new_ind = ind_msg + shift_num
            new_msg += (alphabet[new_ind % len(alphabet)])
    # 출력
    print(f"result : The {act}ed text is '{new_msg}''")


# (특이사항) check_true 변수 사용
check_again = True
while check_again == True:
    # 행위 지정 - encode, decode
    while True:
        user_act = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        # 내장함수 .lower()
        if user_act in ['encode', 'decode']:
            # in ['',''...]
            break
        print("Invalid input. Please type 'encode' or 'decode'.")
    # 입력
    user_message = input("Type your message: ")
    user_shift_num = int(input("Type the shift number: "))
    cryptogram(user_act,user_message,user_shift_num)
    # 재실행 여부
    while True:
        again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        # 내장함수 .lower()
        if again in ['yes', 'no']:
            # in ['',''...]
            break
        print("Invalid input. Please type 'yes' or 'no'.")
    if again == 'no':
        check_again = False
        print("Bye~")


# # 버전 (1)
# # 행위 지정 - encode, decode
# def action():
#     while True:
#         act = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
#         # 내장함수 .lower()
#         if act == 'encode':
#             shift = 1
#             break
#         elif act == 'decode':
#             shift = -1
#             break
#         else:
#             print("You entered it incorrectly. Please enter again.")
#     return act, shift
#     # return - 사용자 함수의 매개변수 반환
# # 입력 및 암호 처리 및 출력
# def answer(act, shift):
#     message = input("Type your message: ")
#     shift_num = int(input("Type the shift number: "))
#
#     len_msg = len(message)
#     new_msg = ""
#
# # # + : encode, - : decode
#     for i in range(0,len_msg):
#         # 알파벳이 아닌 다른 문자 및 숫자 입력되는 경우 고려
#         if message[i] in alphabet:
#             ind_msg = alphabet.index(message[i])
#             # 알파벳 갯수를 초과한 숫자가 입력되는 경우 고려
#             # 내장함수 .index()
#             new_ind = ind_msg + shift_num
#             new_msg += (alphabet[new_ind % len(alphabet)])
#     # 출력
#     print(f"result : The {act}ed text is '{new_msg}''")
#
# # 재실행 여부
# def again():
#     while True:
#         again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
#         if again == "yes":
#             return True
#             break
#         elif again == "no":
#             return False
#             break
#         else:
#             print("You entered it incorrectly. Please enter again.")
#
# # (특이사항) check_true 변수 사용
# check_true = True
# while check_true == True:
#     user_act, user_shift = action()
#     # 사용자 함수로부터 반환(return)받은 매개변수
#     answer(user_act, user_shift)
#     check_true = again()
