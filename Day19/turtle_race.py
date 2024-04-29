from turtle import Turtle, Screen
from random import randint

is_race_on = False
game_screen = Screen()
# 창 크기 설정
game_screen.setup(500, 400)
# 메세지 창 - 입력 받기
user_bet = game_screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color.")
print(f"You chose '{user_bet}'.")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
y_goto = [-100, -60, -20, 20, 60, 100]

# 다중 객체 생성
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-180, y_goto[turtle_index])
    all_turtles.append(new_turtle)

# 입력 유무
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 170:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The '{winning_color}' turtle is the winner!")
            else:
                print(f"You lose.. The '{winning_color}' turtle is the winner..")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)


game_screen.exitonclick()

