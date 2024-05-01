from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


game_screen = Screen()
game_screen.setup(800, 600)
game_screen.bgcolor("black")
game_screen.title("Pong Game")
game_screen.tracer(0)


paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))
ball = Ball()
score = Score()


game_screen.listen()
game_screen.onkey(paddle_R.up, "Up")
game_screen.onkey(paddle_R.down, "Down")
game_screen.onkey(paddle_L.up, "w")
game_screen.onkey(paddle_L.down, "s")


game_is_on = True
while game_is_on:
 time.sleep(ball.move_speed)
 game_screen.update()
 ball.move()

 if ball.ycor() > 280 or ball.ycor() < -275:
  ball.bounce_y()

 if (ball.distance(paddle_R) < 50 and ball.xcor() > 320) or (ball.distance(paddle_L) < 50 and ball.xcor() < -320):
  ball.bounce_x()

 if ball.xcor() > 380:
  ball.reset_position()
  score.L_get_score()

 if ball.xcor() < -390:
  ball.reset_position()
  score.R_get_score()

game_screen.exitonclick()