print('ToDo List Manager')
task = {''}
print(task)

def toDo():
    while True:
        userInput = input('\nDo you want to view, add, remove or edit the todo list?\n')
        userInput = userInput.lower()
        print('')

        if userInput == 'add':
            userAdd = input('What task do you want to add:\n')
            task.add(userAdd.lower())
            print('Task Added🎉')
            for i in task:
                print(f'{i}')

        elif userInput == 'view':
            for i in task:
                if task == {''}:
                    print('No Tasks Available')
                print(f'{i}')


        elif userInput == 'remove':
            removeInput = input('What task do you want to remove:\n')
            removeCheck = input(f"Are you sure you want to '{removeInput}'?\n")
            if removeCheck.lower() == 'yes':
                task.remove(removeInput.lower())
                print('Task Removed ❌')
            else:
                print(f"'{removeInput}' has not been removed")

        elif userInput == 'edit':
            editInput = input("What do you edit to remove?\n")
            editInput = editInput.lower()
            changeInput = input("What do you want to change it to?\n")
            changeInput= changeInput.lower()
            task.remove(editInput)
            task.add(changeInput)
        else:
            print('\nInvalid Input, Select the Correct Option!')

toDo()