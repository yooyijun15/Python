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

# # 5. Dictionary Comprehension
# from random import randint
# names = ["Alex", "Dave", "Eleanor", "Freddie"]
#
# # new_dict = {new_key:new_value for item in list}
# students_score = {student:randint(1, 100) for student in names}
# print(students_score)
# # new_dict = {new_key:new_value for (key,value) in dict.items()}
# # new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# 6. 활용
import pandas

student_dict = {
    "student": ["kim", "lee", "park"],
    "score": [100, 85, 40]
}
# # .items(): 딕셔너리 key, value 얻기
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
#     print(key, value)

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(key)
#     print(value)
#     print(key, value)

for (index, row) in student_df.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)