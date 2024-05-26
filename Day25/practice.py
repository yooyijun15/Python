# 1. 파일 불러오기
# # (ㄱ) 일반
# with open('weather_data.csv') as data_file:
#     weather = data_file.readlines()
#     # readlines() : 한 줄씩 불러오기
# print(weather)

# # (ㄴ) csv 라이브러리
# import csv
#
# with open('weather_data.csv') as data_file:
#     # (1) csv reader 객체 생성
#     data = csv.reader(data_file)
#     # (2) 각 행 출력
#     for row in data:
#         print(row)

# 2. 특정 칼럼 값 불러오기 - 두번째 열 불러오기
# # (ㄱ) csv 라이브러리
# import csv
#
# with open('weather_data.csv') as data_file:
#     # (1) csv reader 객체 생성
#     data = csv.reader(data_file)
#     # (2) 빈 리스트 생성
#     temperatures = []
#     # (3) 각 행 출력
#     for row in data:
#         # (4) 특정 열 출력
#         if row[1] != "temp":
#             # 첫 번째 리스트[1]의 값은 temp, 따라서 제외
#             temperatures.append(int(row[1]))
#         # print(row)
#     print(temperatures)

# 3. pandas 라이브러리
import pandas
# # (a) pandas 사용, .csv로 파일 읽기
data = pandas.read_csv('weather_data.csv')
# print(data)
# # (b) 칼럼 식별 및 특정 칼럼 출력
# print(data["temp"])
# # 동일, print(data.temp)
# # (c) 데이터 구조 확인
# print(type(data))  # 데이터프레임
# print(type(data["temp"]))  # 시리즈
# # (d) 딕셔너리로 변환
# data_dict = data.to_dict()
# print(data_dict)
# # (e) 특정 칼럼 식별 후 Python 리스트로 변환
# temp_list = data["temp"].to_list()
# print(temp_list)

# (예제) 평균 온도 구하기
# for data in temp_list:
#     sum += data
# temp_avg = round(sum / len(temp_list),2)
# ------------------------------
# temp_avg = round(sum(temp_list) / len(temp_list),2)
# print(temp_avg)

# (f) 각종 함수
# print(data["temp"].mean())  # 평균
# print(data["temp"].max())  # 최대값

# (g) 특정 행 출력
# print(data[data.day == "Monday"])

# (예제) 가장 높은 온도의 행 출력
# print(data[data.temp == data["temp"].max()])

# (예제) 월요일 온도 출력
# (h) 특정 행의 열 출력
# monday = data[data.day == "Monday"]
# print(monday.temp[0])

# 딕셔너리
# data_dict = {
#     "students" : ['A', 'B', 'C'],
#     "scores" : [55, 70, 92]
# }
# 데이터프레임 생성
# data = pandas.DataFrame(data_dict)
# print(data)
# # .csv 파일 생성
# data.to_csv("new_data.csv")