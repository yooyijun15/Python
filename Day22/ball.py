from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8)
        self.penup()
        self.x_goto = 10
        self.y_goto = 10
        self.move_speed = 0.1

    def move(self):
        # if self.xcor() > 375 or self.xcor() < -380:
        #     self.x_goto *= -1
        # elif self.ycor() > 280 or self.ycor() < -275:
        #     self.y_goto *= -1
        new_xcor = self.xcor() + self.x_goto
        new_ycor = self.ycor() + self.y_goto
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_goto *= -1

    def bounce_x(self):
        self.x_goto *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()






