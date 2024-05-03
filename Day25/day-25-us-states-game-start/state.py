from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()

    def create(self, goto_x, goto_y, state):
        self.penup()
        self.hideturtle()
        self.goto(goto_x, goto_y)
        self.write()