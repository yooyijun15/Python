from turtle import Screen, shape
from state import State

import pandas
current_count = 0
total_count = 50

# 스크린
screen = Screen()
screen.title("U.S. State Game")
screen.tracer(0)

# 이미지 불러오기
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)
screen.update()

# .csv 파일 불러오기
data = pandas.read_csv("50_states.csv")

# (+) state 열의 값을 리스트로 받아서, 해당 리스트에 존재 여부 판별 가능

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"({current_count}/{total_count}) Guess the State", prompt="What's another state's name?")
    if answer_state is None:
        game_is_on = False
    if answer_state == "Exit":
        # 입력한 값을 리스트에 별도 저장하여, 입력하지 않은 값 .csv 파일 추출 가능
        game_is_on = False
    else:
        # title() : 첫 글자 대문자로 변경
        answer_state = answer_state.title()
        # 입력 값 존재할 경우
        # 1-1
        # # isin() : 값 존재 여부
        # # any() : 하나라도 True면 True 반환
        # answer_exist = data["state"].isin([answer_state]).any()
        # 1-2
        # # answer_state 행 추출 후, 행의 수 0보다 크면 존재
        # answer = data[data.state == answer_state]
        # if len(answer) > 0:
        #     print("Exist")
        # 1-3
        if answer_state in data.values:
            # 행 추출 > 열 추출
            # 해당 행 추출
            state_data = data[data.state == answer_state]
            # 해당 행의 x 열 추출
            goto_x = int(state_data["x"])
            # 해당 행의 y 열 추출
            goto_y = int(state_data["y"])
            state = state_data.state
            # 객체 생성
            new_state = State()
            # new_state.create(int(state_data.x), int(state_data.y), state_data.state)
            new_state.create(goto_x, goto_y, state)
            current_count += 1
            screen.update()

screen.exitonclick()