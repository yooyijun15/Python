# 필요한 페인트 캔 갯수 구하기

# math 모듈
import math

# 사용자 함수 정의 - paint_calc
# 매개변수 - height, width, cover
def paint_calc(height, width, cover):
  canCount = math.ceil((height * width) / cover)
  print(f"You'll need {canCount} cans of paint.")
# math 모듈 .ceil() 함수

input_h = int(input("Please enter the height : "))
input_w = int(input("Please enter the width : "))
coverage = 5

# 사용자 함수 호출
paint_calc(height=input_h, width=input_w, cover=coverage)
