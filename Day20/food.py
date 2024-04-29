from turtle import Turtle
from random import randint


# Turtle 클래스 상속
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("yellow")
        self.speed("fastest")
        self.reflush()

    # 객체(Food) 위치 변경
    def reflush(self):
        x_goto = randint(-280, 280)
        y_goto = randint(-280, 280)
        self.goto(x_goto, y_goto)
