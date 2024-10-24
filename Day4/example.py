# 보물 찾기
# 맵에서 A1 ~ C3 중의 한칸 선택하면, 해당 칸 X로 변경

# 초기 맵
# line1 = ["A1", "B1", "C1"]
# line2 = ["A2", "B2", "C2"]
# line3 = ["A3", "B3", "C3"]
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# ex) map[0][0] = A1
# ex) map[2][3] = C3

print("Hiding your treasure! X marks the spot.")
position = input("Please enter the position(ex. A2) : ")

# 입력받은 알파벳과 숫자의 각 인덱스 찾기
num_index = int(position[1])-1

ABC = ['A', 'B', 'C']
ABC_index = ABC.index(position[0])
# 내장함수 .index()

# 해당 칸 X로 변경
map[num_index][ABC_index] = 'X'

# 출력
print(f"{line1}\n{line2}\n{line3}")
# ex) ['X', '️⬜️', '️⬜️']
#     ['⬜️', '⬜️', '️⬜️']
#     ['⬜️️', '⬜️️', '⬜️️']
