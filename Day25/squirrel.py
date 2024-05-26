import pandas

# # (pandas) .csv 파일 읽기
data = pandas.read_csv('squirrel.csv')

# # (pandas) 버전 1
# # 1-1
# # DataFrame() : 특정 칼럼(Primary Fur Color) 선택해 데이터 프레임 생성
# df = pandas.DataFrame(data["Primary Fur Color"])
# # value_counts() : 특정 칼럼의 각 값 개수 세기
# count_data = df["Primary Fur Color"].value_counts()
# print(count_data)
#
# # 1-2
# # 전체 데이터 프레임 특정 칼럼의 각 값 개수 세기
# count_data = data["Primary Fur Color"].value_counts()
# print(count_data)

# # (pandas) 버전 2
# # 2-1
# # Step 1. 데이터 추출
# # (1) Primary Fur Color 열의 값이 Gray를 갖는 특정 행 저장
# Gray_data = data[data["Primary Fur Color"] == "Gray"]
# # (2) 행의 개수 세기
# len_Gray = len(Gray_data)
# # (3) 출력
# print(f"Gray : {len_Gray}")
#
# Cinnamon_data = data[data["Primary Fur Color"] == "Cinnamon"]
# len_Cinnamon = len(Cinnamon_data)
# print(f"Cinnamon : {len_Cinnamon}")
#
# Black_data = data[data["Primary Fur Color"] == "Black"]
# len_Black = len(Black_data)
# print(f"Black : {len_Black}")
#
# # Step 2. 딕셔너리 생성
# color_data = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "Count": [len_Gray, len_Cinnamon, len_Black]
# }
#
# # Step 3. 데이터프레임 변환
# squirrel_color_data = pandas.DataFrame(color_data)
# print(squirrel_color_data)
# # to_csv() : .csv 변환 및 파일 생성
# squirrel_color_data.to_csv("squirrel_color_data.csv")

# # # (기타)
# from collections import Counter
# # Step 1. 리스트 변환
# color_list = data["Primary Fur Color"].to_list()
# # 내장 함수 set - 리스트 중복 값 제거, 목록 확인
# set_color = set(color_list)
# # collections 모듈의 Counter - 중복 횟수 카운트
# counter_data = Counter(color_list)
# # print(set_color)
# # print(counter_data)
#
#
# # 반복문
# for color in set_color:
#     if str(color).lower() != "nan":
#         color_data = data[data["Primary Fur Color"] == color]
#         print(f"{color} : {len(color_data)}")
