# 페인트 면적 계산

# math 모듈
import math

# 사용자 함수 정의 - paint_calc
# 매개변수 - height, width, cover
def paint_calc(height, width, cover):
  canCount = math.ceil((height * width) / cover)
  print(f"You'll need {canCount} cans of paint.")
# math 모듈 .ceil() 함수

test_h = int(input("Please enter the height : "))
test_w = int(input("Please enter the width : "))
coverage = 5

# 사용자 함수 호출
paint_calc(height=test_h, width=test_w, cover=coverage)
