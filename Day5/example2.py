# 가장 높은 점수 찾기
scores = input("Please enter the scores(Separate with ,) : ").split(", ")

list = []
highest = 0

# for문 - 데이터 타입 변경 후 새로운 리스트에 추가
for score in scores:
    list.append(int(score))
# 내장함수 .append()

# for문 - 가장 큰 값 찾기
for element in list:
    if element > highest:
        highest = element

# 출력
print(f"The highest score in the class is: {highest}")
