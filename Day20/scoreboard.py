from turtle import Turtle
# < 상수 선언 >
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Turtle 클래스 상속
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # 최고 점수 파일로부터 불러오기
        with open("score.txt") as file:
            contents = file.read()
            self.high_score = contents
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_scoreboard()

    # 점수 업데이트
    def update_scoreboard(self):
        self.write(f"HIGH = {self.high_score}\nSCORE = {self.score}", align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        # 최고 점수 갱신하기
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)






