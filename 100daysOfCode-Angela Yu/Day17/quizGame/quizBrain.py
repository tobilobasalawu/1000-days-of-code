class QuizBrain:
    def __init__(self,q_list):
        self.questionNumber = 0
        self.questionList = q_list

    def stillHasQuestion(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        currentQues = self.questionList[self.questionNumber]
        self.questionNumber = self.questionNumber + 1
        userAnswerInput = input(f"Q.{self.questionNumber}: {currentQues.text} (True/False): ")
        self.checkAnswer(userAnswerInput, currentQues.answer)

    def checkAnswer(self, userAnswerInput, correctAnswer):
        if userAnswerInput.lower() == correctAnswer.lower():
            print('You got it right!')
        else:
            print("That's Wrong")
        print(f"The correct answer is {correctAnswer}")