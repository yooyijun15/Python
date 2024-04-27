from turtle import *
from random import *
import colorgram

point_turtle = Turtle()
colormode(255)


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     point_color = (r, g, b)
#     return point_color

colors = colorgram.extract('color.jpeg', 20)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


point_turtle.hideturtle()
point_turtle.penup()

# setheading를 사용하는 방법도 있다.
def draw_point(size_of_gap):
    for i in range(int(200 / size_of_gap)):
        for _ in range(int(300 / size_of_gap)):
            # point_turtle.color(random_color())
            point_turtle.dot(5, choice(rgb_colors))
            point_turtle.forward(size_of_gap)
        point_turtle.goto(0, size_of_gap * (i + 1))


draw_point(20)


screen = Screen()
screen.exitonclick()