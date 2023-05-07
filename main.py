from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(text=item["text"], answer=item["answer"])
    question_bank.append(new_question)


quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz ")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
