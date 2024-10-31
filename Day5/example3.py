# 특정 값까지 모든 짝수의 합
num = int(input("Please enter the number: "))

sum = 0

# for문 - range
for i in range(0,num+1,2):
    print(i)
    sum += i

print(sum)
