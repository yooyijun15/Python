# 연애 이름 궁합

print("The Love Calculator is calculating your score...")

# 이름 입력
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# 이름 합친 후, 소문자로 변경
combine_names = name1 + name2
lower_names = combine_names.lower()
# 내장함수 lower()

# 해당 문자 포함 갯수만큼 카운트
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
# 내장함수 count()

# 궁합 점수
true_total = str(t + r + u + e)
love_total = str(l + o + v + e)
total = true_total + love_total
int_total = int(total)
# 내장함수 str()

# 출력
print(int_total)
if 10 > int_total or int_total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 50 >= int_total >=40:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
