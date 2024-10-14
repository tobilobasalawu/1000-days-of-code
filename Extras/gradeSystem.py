import pycaesarcipher

studentData = {
    's45561076' : 'password',
    's45558799' : 'password',
    's45597382' : 'password',
    's45590908' : 'password'
}

userName = input("Enter Full Name: ")
userId = input("Enter ID: ").lower()
userPassword = input("Enter your password: ")
key = pycaesarcipher.pycaesarcipher()

studentCount = 1
gradingScore = ''
if userId in studentData and userPassword == studentData[userId]:
    print("\nWelcome to the Grading system📈")
    studentNumber = int(input("How many Students grades are to be calculated: "))
    while studentCount <= studentNumber:
        grade = int(input("\nEnter your score: "))
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
    print("\nGrades Allocated✅")

    encryptedPassword = key.caesar_encipher(userPassword, 4)
    try:
        with open("Output.txt", 'x+') as file:
            file.write(f"Name: {userName}\nID: {userId}\nPassword: {encryptedPassword}")
else:
    print('\nIncorrect ID or Password')