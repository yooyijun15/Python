line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

num = int(position[1])-1

if position[0] == 'A':
  map[num][0] = 'X'
elif position[0] == 'B':
  map[num][1] = 'X'
else:
  map[num][2] = 'X'

print(f"{line1}\n{line2}\n{line3}")
