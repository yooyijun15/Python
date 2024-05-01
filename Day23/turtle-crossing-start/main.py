import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    car_manager.create()
    car_manager.move()

    if player.finish_line():
        player.level_up()
        car_manager.level_up()
        scoreboard.level_up()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()



