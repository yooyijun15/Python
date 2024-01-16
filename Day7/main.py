import random
from replit import clear

from hagman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# import hagman_words
# chosen_word = random.choice(hagman_words.word_list)

from hagman_art import stages, logo
print(logo)

print(f"Pssst, the solution is {chosen_word}.")

display = []

for _ in range(word_length):
    display += "_"
# print(display)

while end_of_game == False:
  guess = input("Guess a letter: ").lower()
  clear()

  if guess in display:
    print(f"You've already guessed {guess}.")

  for i in range(word_length):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = guess

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in {guess}.")
    lives -= 1
    if lives == 0:
      print("You lose...")
      end_of_game = True

  if "_" not in display:
    print("\nYou win!")
    end_of_game = True

  print(stages[lives])
  print(f"{' '.join(display)}")
  print(f"You have {lives} lives left.")
