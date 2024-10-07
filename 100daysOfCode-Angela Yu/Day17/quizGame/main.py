from questionModel import Question
from data import question_data

questionBank = []
for question in question_data:
    questions = Question(question['text'], question['answer'])
    questionBank.append(questions)

