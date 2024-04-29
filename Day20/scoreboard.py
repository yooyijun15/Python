from turtle import Turtle
# < 상수 선언 >
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Turtle 클래스 상속
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    # 점수 업데이트
    def update_scoreboard(self):
        self.write(f"SCORE = {self.score}", align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)





