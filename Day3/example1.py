# if - else
# 윤년 계산

year = int(input("Please enter the year : "))

# 윤년이란?
# (A)4의 배수이지만 (B)100의 배수는 아닌 것
# 단, (A),(B) 모두 충족 시  윤년

if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year.")
elif year % 4 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
