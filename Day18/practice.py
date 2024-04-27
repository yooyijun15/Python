# 모듈의 모든 클래스 불러오기
# import turtle
from turtle import *
# from turtle import Turtle, Screen
from random import *

my_turtle = Turtle()

# (1) 사각형 그리기
# for i in range (4):
#     turtle.left(90)
#     turtle.forward(50)

# (2) 점선 그리기
# for i in range(50):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# (3) 삼각형, 사각형, 오각형 ...
# for i in range(3, 11):
#     angle = 360 / i
#     for j in range(i):
#         turtle.forward(50)
#         turtle.right(angle)
# ---------------------------------
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for j in range(num_side):
#         turtle.forward(50)
#         turtle.right(angle)
#
# for shape_side_num in range(3, 11):
#     turtle.color(random.choice(colors))
#     draw_shape(shape_side_num)


# (4) 랜덤 워킹
my_turtle.speed(20)
# my_turtle.pensize(10)
# ---------------------------------
#
# directions = [turtle.left, turtle.right]
#
# for _ in range(100):
#     turtle.color(random.choice(colors))
#     random_direction = random.choice(directions)
#     random_direction(90)
#     turtle.forward(50)
#
# ---------------------------------
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     turtle.color(random.choice(colors))
#     random_direction = random.choice(directions)
#     turtle.right(random_direction)
#     turtle.forward(50)


colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    print(r, g, b)
    tuple_color = (r, g, b)
    return tuple_color


# for _ in range(100):
#     my_turtle.color(random_color())
#     random_direction = choice(directions)
#     my_turtle.right(random_direction)
#     my_turtle.forward(50)

# (5) 스프링
my_turtle.hideturtle()


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)
        # my_turtle.left(5)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()

