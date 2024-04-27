from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed(20)

def move_forward():
    my_turtle.forward(20)


def move_backward():
    my_turtle.backward(20)


def clockwise():
    my_turtle.circle(100, 10)


def counter_clockwise():
    my_turtle.circle(100, -10)


def turn_right():
    my_turtle.setheading(my_turtle.heading() - 10)


def turn_left():
    my_turtle.setheading(my_turtle.heading() + 10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screem = Screen()
# 키보드 입력 받기
my_screem.listen()
# fun : 함수를 입력으로 받는다.
my_screem.onkey(key="f", fun=move_forward)
my_screem.onkey(key="b", fun=move_backward)
my_screem.onkey(key="c", fun=clockwise)
my_screem.onkey(key="v", fun=counter_clockwise)
my_screem.onkey(key="r", fun=turn_right)
my_screem.onkey(key="l", fun=turn_left)
my_screem.onkey(key="space", fun=clear)
my_screem.exitonclick()



