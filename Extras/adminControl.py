operation = input("What operation: ")
addname = input("What the users details name: ")
addpassowrd = input("What password you want the users: ")
username = input("What username you want the users: ")


def userManagement(operation, addname, addpassowrd, username: str) -> str:
    userpassword = '242425'
    username = 'aser'

    details = {
        'userdefault': {
            'username': username,
            'password': userpassword
        }
    }
    if operation.lower() == 'add':
        username = input('Whats the user name: ')
        if username == details['userdefault']:
            addname = input("Enter username: ")
            addpassowrd = input("Enter password: ")

            details['userdefault']['username'] = addname
            details['userdefault']['password'] = addpassowrd

            print('Done')


userManagement(operation, addname, addpassowrd, username)



