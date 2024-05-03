# with open('weather_data.csv') as data_file:
#     weather = data_file.readlines()
# print(weather)


# csv 라이브러리
# import csv
#
# with open('weather_data.csv') as data_file:
#     # (1) csv reader 객체 생성
#     data = csv.reader(data_file)
#     temperatures = []
#     # (2) 각 행 출력
#     for row in data:
#         # (3) 특정 칼럼 출력
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)
#     print(temperatures)

# import pandas
# (1) pandas 사용, .csv 파일 읽기
# data = pandas.read_csv('weather_data.csv')
# print(data)
# (2) 칼럼 식별 및 특정 칼럼 출력
# print(data["temp"])
# print(data.temp)
# (3) 데이터 구조 확인
# print(type(data))  # 데이터프레임
# print(type(data["temp"]))  # 시리즈
# (4) 딕셔너리 생성
# data_dict = data.to_dict()
# print(data_dict)
# (5) 특정 칼럼 식별 후 Python 리스트로 변환
# temp_list = data["temp"].to_list()
# print(temp_list)

# (예제) 평균 온도 구하기
# for data in temp_list:
#     sum += data
# temp_avg = round(sum / len(temp_list),2)
# ------------------------------
# temp_avg = round(sum(temp_list) / len(temp_list),2)
# print(temp_avg)

# (6) 각종 함수
# print(data["temp"].mean())  # 평균
# print(data["temp"].max())  # 최대값
# (7) 특정 행 출력
# print(data[data.day == "Monday"])

# (예제) 가장 높은 온도의 행 출력
# print(data[data.temp == data["temp"].max()])

# (예제) 월요일 온도 출력
# (8) 특정 행의 열 출력
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