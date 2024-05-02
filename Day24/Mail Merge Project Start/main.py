#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open('./Input/Names/invited_names.txt') as list:
#     # readlines() : 한 줄씩 받아오는 것
#     names = list.readlines()
#     print(names)

LETTERS = './Input/Letters/starting_letter.txt'
NAMES = './Input/Names/invited_names.txt'
OUTPUT_FOLDER = './Output/ReadyToSend'

# 공백 및 개행 문자 제거
# strip()
# rstrip()
with open(NAMES) as name_file:
    names = [line.rstrip() for line in name_file]

# ./Input/Letters/starting_letter.txt : 같은 레벨
with open(LETTERS) as file:
    contents = file.read()

for name in names:
    # replace : 파일의 [name] 부분 대체
    personalized_letter = contents.replace("[name]", name)
    # 생성될 파일 경로 지정
    output_file = f"{OUTPUT_FOLDER}/{name}_letter.txt"
    # 파일 생성 및 쓰기
    with open(output_file, 'w') as file:
        file.write(personalized_letter)





