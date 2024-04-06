import random
# 화면 비우기 모듈
from replit import clear
# hangman 단어 모듈
from hagman_words import word_list
# import hagman_words
# chosen_word = random.choice(hagman_words.word_list)

# 로고, 스테이지 모듈
from hagman_art import stages, logo
print(logo)

# 랜덤 hangman 단어 선택
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
display = []

# print(f"Pssst, the solution is {chosen_word}.")

# 빈 리스트에 랜덤 hangman 단어 크기 맞게 칸 생성
for _ in range(word_length):
    display += "_"
# print(display)

# True로 바뀔 때까지 while 문 실행
while end_of_game == False:
  guess = input("Guess a letter: ").lower()
  clear()
  # 이미 리스트에 입력 값 있을 경우
  if guess in display:
    print(f"You've already guessed {guess}.")
  # 리스트에 입력 값 없을 경우, hangman 단어와 비교
  for i in range(word_length):
    letter = chosen_word[i]
    # hangman 단어에 입력 값 있을 경우, 리스트에 입력 값 추가
    if letter == guess:
      display[i] = guess
  # hangman 단어에 입력 값 없을 경우, 생명 -1
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in {guess}.")
    lives -= 1
    # 만약 남은 생명 0일 경우, 게임 패배 및 종료
    if lives == 0:
      print("You lose...")
      end_of_game = True
  # 리스트 꽉 찰 경우, 게임 승리 및 종료
  if "_" not in display:
    print("\nYou win!")
    end_of_game = True

  print(stages[lives])
  # 리스트 문자열 출력
  print(f"{' '.join(display)}")
  print(f"You have {lives} lives left.")
