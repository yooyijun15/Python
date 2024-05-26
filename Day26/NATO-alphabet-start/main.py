#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# 딕셔너리 {키: 값, ...} 형식으로 .csv 파일 저장

# 방법 1 - Dictionary Comprehension
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# # 방법 2 - 일반
# for (index, row) in data.iterrows():
#     # (1) 키 - 위치 취급
#     # (기존) 키 - 위치 취급
#     # (현재) 키 - 레이블 취급
#     # 따라서 위치 취급 위해서 (인덱스 접근) .iloc 사용
#     # .iloc : 위치 기반 접근
#     # dict_key = row.iloc[0]
#     # dict_value = row.iloc[1]
#     # (2) 키 - 레이블 취급
#     dict_key = row["letter"]
#     dict_value = row["code"]
#     dictionary[dict_key] = dict_value

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input(f"Enter a word: ").upper()

# List Comprehension
out_put_list = [phonetic_dict[each] for each in word]
print(out_put_list)



