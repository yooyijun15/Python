from question_model import Question
from data import question_data
from random import choice

num_list = []
count = len(question_data)
score = 0

for i in range(count):
    num_list.append(i)

for j in range(count):
    num = choice(num_list)
    num_list.remove(num)
    quiz = Question(question_data[num]["text"], question_data[num]["answer"])
    print(quiz.answer)
    if input(f"Q{j+1}. {quiz.text} (True or False) ") == quiz.answer:
        print("You got it right!")
        score += 1
    else:
        print("That's wrong.")
    print(f"Your current score : {score}/{j+1}")

print("You've completed the quiz")
print(f"Your final score : {score}/{count}")