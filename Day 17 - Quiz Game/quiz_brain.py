
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.list = question_list

    def still_has_questions(self):
        """Checks if there are still questions to be asked"""
        return self.question_number < len(self.list)

    def next_question(self):
        """Keeps track of current question, displays the question to the user, asks the user fro their answer, and calls
        the check_answer function to check if the user's answer is correct"""
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks if the user's answer is correct and displays the appropriate message. If the user is correct,
        their score increases by 1. Also displays the correct answer and their current score. """
        if user_answer.lower() == correct_answer.lower():
            print("\nYou got it right!")
            self.score += 1
        else:
            print(f"\nThat's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")

