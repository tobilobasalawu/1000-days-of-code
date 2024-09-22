import random
print('REPLIT LOGIN SYSTEM!')

savedUsername = 'tobilobasalawu'
savedPassword = 'A2gaut1503'

def loginSystem():
    incorrectOutput = ["Whoops! I don't recognise that username or password", "😬 Invalid details, Try again!"]
    while True:
        userName = input('\nWhat is your username: ')
        password = input('What is your password: ')
        if userName != savedUsername and password != savedPassword:
            print(random.choice(incorrectOutput))
        else:
            print('\nWelcome to KALI!🐍')
            break
loginSystem()