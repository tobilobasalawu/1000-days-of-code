print('ToDo List Manager')
task = []

def toDo():
    while True:
        userInput = input('\nDo you want to view, add or edit the todo list?\n')
        userInput = userInput.lower()
        print('')

        if userInput == 'add':
            userAdd = input('What task do you want to add:\n')
            task.append(userAdd)
            print('\nTask Added🎉')
            for i in task:
                print(f'{i}')

        elif userInput == 'view':
            for i in task:
                if i == None:
                    print('No Tasks Available')
                print(f'{i}')


        elif userInput == 'edit':
            editInput = input('What task do you want to remove:\n')
            task.remove(editInput.lower())
            for i in task:
                print(f'{i}')

        else:
            print('\nInvalid Input, Select the Correct Option!')

toDo()