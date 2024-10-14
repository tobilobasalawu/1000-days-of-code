import pycaesarcipher

studentData = {
    's45561076' : 'password',
    's45558799' : 'password',
    's45597382' : 'password',
    's45590908' : 'password'
}

userName = input("Enter Full Name: ")
userId = input("Enter ID: ").lower()
userPassword = input("Enter your password: ").lower()
key = pycaesarcipher.pycaesarcipher()

gradingScore = ''
gradingData = []
encryptedPassword = key.caesar_encipher(userPassword, 4)

def gradingCalaculation():
    studentCount = 1
    if userId in studentData and userPassword == studentData[userId]:
        print("\nWelcome to the Grading system📈")
        studentNumber = int(input("How many Students grades are to be calculated: "))
        while studentCount <= studentNumber:
            grade = int(input("\nEnter your score: "))
            studentCount+=1
            if grade >= 90:
                gradingScore = 'A'
                print("\n'A'")
                gradingData.append(gradingScore)
            elif grade >= 80:
                gradingScore = 'B'
                print("\n'B'")
                gradingData.append(gradingScore)
            elif grade >= 60:
                gradingScore = 'D'
                print("\n'D'")
                gradingData.append(gradingScore)
            else:
                gradingScore = 'F'
                print("'F'")
                gradingData.append(gradingScore)
        print("\nGrades Allocated✅")
        programResultOutput()
    else:
        print('\nIncorrect ID or Password')

def programResultOutput():
    result = f"Name: {userName}\nID: {userId}\nPassword(encrypted): {encryptedPassword}\nGrades: {gradingData}"
    try:
        with open("Output.txt", 'x+') as file:
            file.write(result)
    except FileExistsError:
        with open("Output.txt", 'a+') as file:
            file.write(result)

gradingCalaculation()

