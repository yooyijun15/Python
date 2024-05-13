# List Comprehension

# # 1. 리스트 값 1씩 증가
# # 방법 (1)
# numbers = [1, 2, 3]
# new_list = []
# for i in numbers:
#     add = i + 1
#     new_list.append(add)
# print(new_list)
#
# # 방법 (2) - List Comprehension
# numbers = [1, 2, 3]
# new_list = [i + 1 for i in numbers]
# print(new_list)

# # 2. 대문자 변환
# name = "Angela"
# new_list = [letter.upper() for letter in name]
# print(new_list)

# names = ["Alex", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names]
# print(new_list)

#
# # 3. range( , ) 활용
# new_list = [i * 2 for i in range(1, 5)]
# print(new_list)

# Conditional List Comprehension

# # 4. if 조건절 사용
# names = ["Alex", "Dave", "Eleanor", "Freddie"]
# new_list = [name for name in names if len(name) < 5]
# print(new_list)

