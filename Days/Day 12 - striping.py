names = []

while True:
    firstName = input('First Name: ')
    lastName = input('Last Name: ')

    firstName = firstName.strip().capitalize()
    lastName = lastName.strip().capitalize()
    fullName = f'{firstName} {lastName}\n'

    if fullName in names:
        print('ERROR: Duplicate Name\n')
        print(fullName)
    else:
        names.append(fullName)
        #print(names)
        print(fullName)