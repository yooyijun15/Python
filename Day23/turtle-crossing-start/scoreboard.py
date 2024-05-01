from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
POSITION = (-225, 255)
GAME_OVER_FONT = ("Courier", 34, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)