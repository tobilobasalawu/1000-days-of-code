print('ToDo List Manager')

task = ['yes', 'no']
def toDo():
    userInput = input('Do you want to view, add or edit the todo list?\n')
    userInput = userInput.lower()
    print('')

    if userInput == 'view':
        for i in task:
            print(f'{i}')
toDo()
