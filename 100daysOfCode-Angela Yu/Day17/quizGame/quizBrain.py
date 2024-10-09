class QuizBrain:
    def __init__(self,q_list):
        self.questionNumber = 0
        self.questionList = q_list

    def nextQuestion(self):
        currentQues = self.questionList[self.questionNumber]
        userAnswerInput = input(f"Q.{self.questionNumber}: {currentQues.text} (True/False): ")