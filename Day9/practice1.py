# # 1. 생성
# # 기본 (키:값) 딕셔너리 생성
# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # 빈 딕셔너리 생성
# empty_dictionary = {}

# # 2. 출력
# # (1) 특정 키의 값 출력
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
#
# # (2) 딕셔너리의 모든 키 출력
# for key in programming_dictionary:
#     print(key)
#     # 딕셔너리의 모든 값 출력
#
# # (3) 딕셔너리의 모든 값 출력
# for key in programming_dictionary:
#     print(programming_dictionary[key])
#
# # items() : 딕셔너리의 (key, value) 불러오기
# # (1) 딕셔너리의 모든 키 출력
# for (key, value) in programming_dictionary.items():
#     print(key)
#
# # (2) 딕셔너리의 모든 값 출력
# for (key, value) in programming_dictionary.items():
#     print(value)
#
# # (3) 딕셔너리의 모든 키, 값 출력
# for (key, value) in programming_dictionary.items():
#     print(key, value)

# # 3. 삽입
# programming_dictionary["Loop"] = "The action of doing something over and over again"

# # 4. 중첩
# # (ㄱ) 딕셔너리 - 리스트
# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # (ㄴ) 딕셔너리 - 딕셔너리 - 리스트
# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
# print(travel_log["France"]["cities_visited"][0])
# print(travel_log["France"]["total_visite"])

# # (ㄷ) 리스트 - 딕셔너리 - 리스트
# travel_log = [
#   {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12,
#   },
#   {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5,
#   }
# ]