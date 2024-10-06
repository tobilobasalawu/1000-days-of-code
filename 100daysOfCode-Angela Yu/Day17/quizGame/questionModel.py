class Question:

    def __init__(self, question, result):
        self.text = question
        self.answer = result

newQuestion = Question('YES', False)
print(newQuestion.text)