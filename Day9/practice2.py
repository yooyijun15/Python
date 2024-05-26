# 리스트 - 딕셔너리 - 리스트 중첩 생성
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

country = input("Add country name: ") # Italy
visits = int(input("Number of visits: ")) # 7
# eval() : 데이터 타입 평가
list_of_cities = eval(input("create list from formatted string: ")) # ["Venice", "Rome", "Florence"]


# travel_log 리스트에 딕셔너리 추가하는 함수 생성
def add_new_country(country_name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")