line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# ex) A1
position = input()

ABC = ['A', 'B', 'C']
num_index = int(position[1])-1
# index(): 값의 인덱스 반환
Alpha_index = ABC.index(position[0])

map[num_index][Alpha_index] = 'X'

print(f"{line1}\n{line2}\n{line3
# ex) ['X', '️⬜️', '️⬜️']
#     ['⬜️', '⬜️', '️⬜️']
#     ['⬜️️', '⬜️️', '⬜️️']
