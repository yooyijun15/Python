from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

# 게임 화면 설정
game_screen = Screen()
game_screen.setup(600, 600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
# tracer : 출력 제어
# 옵션 - 0 : OFF, 수동 업데이트 필수 / 1 : ON
game_screen.tracer(0)

# 객체 생성
snake = Snake()
food = Food()
score = Scoreboard()

# 키보드 조작
game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")


# 게임 실행
game_is_on = True
while game_is_on:
    # segments의 객체(Snake) 하나로 보이기 위한 것
    # 변경된 화면 동시 업데이트
    game_screen.update()
    # while 루프 반복 시간 조절
    time.sleep(0.1)
    snake.move()
    # 점수 획득
    # snake.head <-> food 거리
    if snake.head.distance(food) < 15:
        print("delicious")
        snake.extend()
        food.reflush()
        score.get_score()
    # 벽 충돌
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    # 객체(Snake) 머리와 몸통 충돌
    # segments[1:] : Slice(슬라이스) 활용해 객체(Snake)의 머리 제외
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


game_screen.exitonclick()