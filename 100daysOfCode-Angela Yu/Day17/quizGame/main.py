from questionModel import Question
from data import question_data
from quizBrain import QuizBrain

questionBank = []
for question in question_data:
    questions = Question(question['text'], question['answer'])
    questionBank.append(questions)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()



