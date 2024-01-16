print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combine_names = name1 + name2
lower_names = combine_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

true_total = str(t + r + u + e)
love_total = str(l + o + v + e)
total = true_total + love_total
int_total = int(total)

if 10 > int_total or int_total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 50 >= int_total >=40:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
