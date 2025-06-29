from data2 import question_data
from question_model import Question
from quiz_brain import QuizBrain

# creating the list of question objects from the data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    # question_bank.append(question["text"])   # appends all "text" to question_bank list
    # print(question["text"], question["answer"])   # this prints each of the "text" and their corresponding "answer"

# initializing the QuizBrain class
quiz = QuizBrain(question_bank)    # the value input for the q_list parameter in the quiz_brain module is the question_bank

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz. ")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


