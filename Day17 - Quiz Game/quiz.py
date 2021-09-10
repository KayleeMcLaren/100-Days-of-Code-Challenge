
from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


question_bank = []

for item in question_data:
    """For loop gets the question and answer from the question_data list, passes them to the Question class to create a 
    new_question object. Then appends that new_question object to the question_bank list. The question_bank list is then
    passed to the QuizBrain class to create a quiz object and run the program"""
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"\nYou've completed the quiz! Your final score was {quiz.score}/{quiz.question_number}")
