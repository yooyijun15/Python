print("Welcome to the TIP calcalator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people
# f 문자열
print(f"Each person should pay: ${bill_per_person:.2f}")
# {bill_per_person:.2f} : 소숫점 2번째 자리까지 표시
