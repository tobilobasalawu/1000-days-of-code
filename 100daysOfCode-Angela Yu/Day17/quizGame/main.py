from questionModel import Question
from data import question_data
from quizBrain import QuizBrain

questionBank = []
for question in question_data:
    questions = Question(question['question'], question['correct_answer'])
    questionBank.append(questions)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()
print(f"You've completed the quiz\nYour final score was: {quiz.userScore}/{quiz.questionList}")


