from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # 기본 20 * 20,
        # 따라서 (5, 1)로 설정 시, 실제 100 * 20
        self.shapesize(5, 1)
        self.goto(position)
        self.color("white")
        self.penup()

    def up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)