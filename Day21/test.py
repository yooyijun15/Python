class Animal:
    def __init__(self):
        self.num_life = 3

    def breathe(self):
        print("Inhale - Exhale.")


# Animal 클래스 상속
class Fish(Animal):
    def __init__(self):
        # 상위 클래스 불러오기
        super().__init__()

    def swim(self):
        print("-- In water --")

    def breathe(self):
        # 상위 클래스 특정 함수 불러오기
        super().breathe()
        print("(In water)")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"LIFE : {nemo.num_life}")


