# class란 무엇인가?

# class 생성
class User:
    print("new user being created...\n")

    # init 함수 생성
    # init 함수 : 생성 및 초기화
    def __init__(self, user_id, user_name):
        # user_id, user_name : 매개변수
        self.id = user_id
        self.name = user_name
        # follwers, follwing 변수 0으로 초기화
        self.follwers = 0
        self.follwing = 0
        print(f"< Create user >\nID : {self.id}\nName : {self.name}\nfollwers : {self.follwers}\nfollwing : {self.follwing}\n")

    def follow(self, user):
        user.follwers += 1
        self.follwing += 1


user_1 = User('001', 'june')
user_2 = User('002', 'jommy')


user_1.follow(user_2)

print(f"user_1.follwing : {user_1.follwing}\nuser_1.follwers : {user_1.follwers}")
print(f"user_2.follwing : {user_2.follwing}\nuser_2.follwers : {user_2.follwers}")





