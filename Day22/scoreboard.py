from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.R_score = 0
        self.L_score = 0
        self.update()

    def update(self):
        self.write(f"{self.L_score} : {self.R_score}", align=ALIGNMENT, font=FONT)

    def R_get_score(self):
        self.R_score += 1
        self.clear()
        self.update()

    def L_get_score(self):
        self.L_score += 1
        self.clear()
        self.update()


