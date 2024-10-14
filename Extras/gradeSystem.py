

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
if userId in studentData and userPassword == studentData[userId]:
    print("\nWelcome to the Grading system📈")
    studentNumber = int(input("How many Students grades are to be calculated: "))
    while studentCount <= studentNumber:
        studentCount+=1