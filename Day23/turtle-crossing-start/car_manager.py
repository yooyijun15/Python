from turtle import Turtle
from random import randint, choice
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = 5

    def create(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shapesize(1, 2)
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.y_random = randint(-250, 250)
            new_car.goto(300, new_car.y_random)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

