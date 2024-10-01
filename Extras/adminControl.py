

def userManagement():
    while True:
        operation = input("What operation 'add', 'remove', 'update', or 'quit': ").lower()
        userID = input("The user ID: ").lower()
        userpassword = 'default'
        username = 'default'

        details = {
            'default': {
                'username': username,
                'password': userpassword
            }
        }
        if userID == 'default':
            if operation.lower() == 'add':
                addname = input("Enter new username: ").lower()
                addpassowrd = input("Enter new password: ").lower()
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
                    addname = input("Enter new username: ").lower()
                    print('UserName updated')
                    details['default']['username'] = addname
                elif update == 'password':
                    addpassowrd = input("Enter new password: ").lower()
                    print('Password updated')
                    details['default']['password'] = addpassowrd
                elif update == 'both':
                    addname = input("Enter new username: ").lower()
                    addpassowrd = input("Enter new password: ").lower()
                    print('New Password and UserName has been set')
                    details['default']['username'] = addname
                    details['default']['password'] = addpassowrd
                else:
                    print('Enter the correct Detail')

                print(details)

            elif operation == 'quit':
                print('program Ended')
                break

            else:
                print("Select the correct option")
        else:
            print('Incorrect ID')

userManagement()



