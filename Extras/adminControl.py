operation = input("What operation 'add', 'remove', 'useradd','update', or 'quit': ").lower()
userID = input("The user ID: ").lower()
name = input("Enter new username: ").lower()
passcode = input("Enter new password: ").lower()
IDnew = input("Enter new ID: ").lower()

details = {
        'default': {
            'username': name,
            'password': passcode
        }
    }

def initial():
    userDetail(name, passcode)
    if userID == 'default':
        operationAlgorithm(name, passcode, details, IDnew)
        print(details)
    else:
        print('Incorrect ID')


def userDetail(addname, addpassowrd: str) -> str:
    userpassword = 'default'
    username = 'default'

def operationAlgorithm(addname, addpassowrd, details, newID: str) -> str:
    if operation.lower() == 'add':
        if userID == 'default':
            details['default']['username'] = addname
            details['default']['password'] = addpassowrd

            print('New Password and UserName has been set')
        else:
            print('Wrong Username')

    elif operation.lower() == 'remove':
        details['default']['username'] = None
        details['default']['password'] = None

        print('New Password and UserName has been deleted')
        print(details)

    elif operation.lower() == 'update':
        update = input('What do you want to update: ').lower()
        if update == 'username':
            print('UserName updated')
            details['default']['username'] = addname
        elif update == 'password':
            print('Password updated')
            details['default']['password'] = addpassowrd
        elif update == 'both':
            print('New Password and UserName has been set')
            details['default']['username'] = addname
            details['default']['password'] = addpassowrd
        else:
            print('Enter the correct Detail')

        print(details)

    elif operation.lower() == 'useradd':
        details.update({newID : 'newId'})
        print(details)
        #details[str(newID)].update({'username': addname, 'password': addpassowrd})
        #print('New User Added')

    else:
        print("Select the correct option")




def main():
    while operation != "quit":
        initial()
        if operation == 'quit':
            print('Program Ended')
            break


print(details)

