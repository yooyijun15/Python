# 평균 키
heights = input("Please enter the heights(Separate with ,) : ").split(", ")

list = []
total_height = 0
count = 0

# for문 - 데이터 타입 변경 후 새로운 리스트에 추가
for height in heights:
    list.append(float(height))
# 내장함수 .append()

# for문 - 리스트 값 더하기
for element in list:
    total_height += element

# for문 - 리스트 요소 갯수 구하기
for i in list:
    count += 1

avg = round(total_height / count, 2)

print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {avg}")
