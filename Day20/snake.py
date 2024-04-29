from turtle import Turtle

# < 변수 선언 >
# 초기 객체 생성 위치
STARTING_POSITION = [(20, 0), (0, 0), (-20, 0)]
# 이동 거리
MOVE_DISTANCE = 20
# 각도
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # (1) 해당 객체 (Snake)는 정 사각형 모여서 이루어 진 것으로, 이를 저장 위한 공간
        self.segments = []
        # (2) create 함수 실행
        self.create()
        #
        self.head = self.segments[0]

    def create(self):
        # 최초 객체(Snake)로 최초 1회 실행
        # 해당 위치(STARTING_POSITION)에 객체 추가
        for position in STARTING_POSITION:
            # (3) add_segment 함수 실행
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.shapesize(1, 1)
        new_snake.penup()
        new_snake.goto(position)
        # 생성된 객체 리스트(segments) 추가
        self.segments.append(new_snake)

    # (6) 객체(Snake) 확장
    def extend(self):
        # position() : 현재 turtle 위치
        # segments 마지막 turtle 위치에 객체(Snake) 1개 추가
        self.add_segment(self.segments[-1].position())

    def move(self):
        # (4) 객체(Snake) 이동
        # ex) 2 -> 1, 1 - > 0
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # (5) 키보드 조작
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

