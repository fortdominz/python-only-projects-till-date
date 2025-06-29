# The quiz_brain, the next question() method, the still_has_questions() method and the check_answer() method.
import sys


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # TODO: checking if we are are at the end of the quiz
    def still_has_questions(self):
        n_of_questions = len(self.question_list)
        return self.question_number < n_of_questions

    # TODO: checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == "off":
            sys.exit()
        elif user_answer.lower() == correct_answer.lower():
            print(f"Correct!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your currect score is: {self.score}/{self.question_number}\n")

