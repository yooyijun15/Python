# if - elif - else
# 피자 주문

print("Thank you for choosing Python Pizza Deliveries!")

# 사이즈, 페퍼로니, 치즈 옵션 선택
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

# 변수 선언 - 가격
bill = 0

# 옵션 별 가격
if size == 'S':
  bill += 15
  if add_pepperoni == 'Y':
    bill += 2
else:
  if size == 'M':
    bill += 20
  else:
    bill += 25
  if add_pepperoni == 'Y':
    bill += 3
if extra_cheese == 'Y':
  bill += 1

# 출력
print(f"Your final bill is: ${bill}.")
