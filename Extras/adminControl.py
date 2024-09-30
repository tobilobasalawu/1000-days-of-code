operation = input("What operation: ").lower()
addname = input("Enter new username: ").lower()
addpassowrd = input("Enter new password: ").lower()
username = input("The user ID ").lower()

def userManagement(operation, addname, addpassowrd, username: str) -> str:
    userpassword = '242425'
    username = 'aser'

    details = {
        'userdefault': {
            'username': addname,
            'password': addpassowrd
        }
    }

    if operation.lower() == 'add':
        username = username
        if username == 'userdefault':
            addname = addname
            addpassowrd = addpassowrd

            details['userdefault']['username'] = addname
            details['userdefault']['password'] = addpassowrd

            print(details)
        else:
            print('Wrong Username')


userManagement(operation, addname, addpassowrd, username)



