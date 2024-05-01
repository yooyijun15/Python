# 파일 열기
file = open("test.txt")
contents = file.read()
print(contents)
# 파일 닫기
file.close()

# with : 작업 완료 후 자동 파일 닫기
# 파일 읽기
with open("test.txt") as file:
    contents = file.read()
    print(contents)

# mode : 파일 읽기(r, 기본), 쓰기(w), 추가(a) 모드 지정
# a, w 모드의 경우, 파일 없을 시 자동 생성 후 내용 추가
# 파일 쓰기
with open("test.txt", mode="a") as file:
    file.write("\nNew contents.")