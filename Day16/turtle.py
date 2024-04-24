# turtle : 모듈
# Turtle, Screen : 클래스
from turtle import Turtle, Screen

# 클래스 사용하여 객체 생성
timmy = Turtle()
print(timmy)
# 거북이 모양 변경
timmy.shape("turtle")
# 색상 변경
timmy.color("CornflowerBlue")
# 앞으로 100만큼 이동
timmy.forward(100)
# shape(), color(), forward() ... : 함수

my_screen = Screen()
# canvheight : 변수
# 스크린 높이
print(my_screen.canvheight)
# exitonclick() : 함수
# 화면 클릭하기 전까지 스크린 ON
my_screen.exitonclick()