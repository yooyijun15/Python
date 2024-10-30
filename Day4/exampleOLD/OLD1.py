line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

if position[0] == 'A':
  if position[1] == '1':
    line1[0] = 'X'
  elif position[1] == '2':
    line2[0] = 'X'
  else:
    line3[0] = 'X'
elif position[0] == 'B':
  if position[1] == '1':
    line1[1] = 'X'
  elif position[1] == '2':
    line2[1] = 'X'
  else:
    line3[1] = 'X'
else:
  if position[1] == '1':
    line1[2] = 'X'
  elif position[1] == '2':
    line2[2] = 'X'
  else:
    line3[2] = 'X'

print(f"{line1}\n{line2}\n{line3}")
