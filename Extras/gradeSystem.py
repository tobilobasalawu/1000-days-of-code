from gc import garbage

studentData = {
    's45561076' : '4321',
    's45558799' : '4321',
    's45597382' : '4321',
    's45590908' : '4321'
}

userName = input("Enter Full Name: ")
userId = input("Enter ID: ").lower()
userPassword = input("Enter your password: ")

studentCount = 0
gradingScore = ''
if userId in studentData and userPassword == studentData[userId]:
    print("\nWelcome to the Grading system📈")
    studentNumber = int(input("How many Students grades are to be calculated: "))
    grade = int(input("\nEnter your score: "))
    while studentCount <= studentNumber:
        studentCount+=1
        if grade >= 90:
            gradingScore = 'A'
            print("\n'A'")
        elif grade >= 80:
            gradingScore = 'B'
            print("\n'B'")
        elif grade >= 60:
            gradingScore = 'D'
            print("\n'D'")
        else:
            gradingScore = 'F'
            print("'F'")