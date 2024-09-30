operation = input("What operation: ").lower()
addname = input("Enter new username: ").lower()
addpassowrd = input("Enter new password: ").lower()
userID = input("The user ID: ").lower()

def userManagement(operation, addname, addpassowrd: str) -> str:
    userpassword = '242425'
    username = 'aser'

    details = {
        'default': {
            'username': username,
            'password': userpassword
        }
    }

    if operation.lower() == 'add':
        if userID == 'default':
            details['default']['username'] = addname
            details['default']['password'] = addpassowrd

            print('New Password and UserName has been set')
        else:
            print('Wrong Username')


userManagement(operation, addname, addpassowrd)



