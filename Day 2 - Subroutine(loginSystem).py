print('REPLIT LOGIN SYSTEM!')

savedUsername = 'tobilobasalawu'
savedPassword = 'A2gaut1503'

def loginSystem():
    while True:
        userName = input('What is your username: ')
        password = input('What is your password: ')
        if userName != savedUsername and password != savedPassword:
            print('Try Again')
        else:
            print('Welcome to KALI🐍')
            break

loginSystem()