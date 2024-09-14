print('ToDo List Manager')

def toDo():
    task = ['test','yes']
    userInput = input('Do you want to view, add or edit the todo list?\n')
    userInput = userInput.lower()
    print('')

    if userInput == 'add':
        userAdd = input('What task do you want to add:\n')
        task.append(userAdd)
        for i in task:
            print(f'{i}')

    elif userInput == 'view':
        for i in task:
            print(f'{i}')

    elif userInput == 'edit':
        editInput = input('What task do you want to remove:\n')
        task.remove(editInput.lower())
        for i in task:
            print(f'\n{i}')


toDo()
