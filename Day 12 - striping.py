names = []

while True:
    firstName = input('First Name: ')
    lastName = input('Last Name: ')

    firstName = firstName.capitalize().strip()
    lastName = lastName.capitalize().strip()
    fullName = f'{firstName} {lastName}\n'

