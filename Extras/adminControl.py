operation = ''
addname = ''
addpassowrd = ''
userID = ''

def userManagement(operation, addname, addpassowrd: str) -> str:
    operation = input("What operation: ").lower()
    userpassword = '242425'
    username = 'aser'

    details = {
        'default': {
            'username': username,
            'password': userpassword
        }
    }

    userID = input("The user ID: ").lower()

    if operation.lower() == 'add':
        addname = input("Enter new username: ").lower()
        addpassowrd = input("Enter new password: ").lower()
        if userID == 'default':
            details['default']['username'] = addname
            details['default']['password'] = addpassowrd

            print('New Password and UserName has been set')
        else:
            print('Wrong Username')

    if operation.lower() == 'delete':
        if userID == 'default':
            details['default']['username'] = None
            details['default']['password'] = None

            print('New Password and UserName has been deleted')
            print(details)
        else:
            print('Wrong Username')


userManagement(operation, addname, addpassowrd)



