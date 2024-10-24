print("Welcome to the TIP calcalator.")

# 가격, 팁, 인원수 입력 받기
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# 팁 계산
tip_amount = bill * (tip / 100)

# 전체 및 인당 지불 금액 계산
total_bill = bill + tip_amount
bill_per_person = total_bill / people

# 출력
print(f"Each person should pay: ${bill_per_person:.2f}")
