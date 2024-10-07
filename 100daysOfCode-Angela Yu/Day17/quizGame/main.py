from questionModel import Question
from data import question_data

for question in question_data:
    questionBank = Question(question['text'], question['answer'])
