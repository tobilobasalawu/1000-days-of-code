print("TODO LIST MANAGEMENT APP\n")

menu = input("1: Add\n2: View\n3: Remove\n4: Edit\n\n> ")
todoList = []

def todoProgram():
    if menu.lower() == 'add' or '1':
        print('ADD')
        task = input("\nWhat is it? ")
        taskTime = input("What is it due? ")
        taskPriority = input("How Important? ")
        row = [task, taskTime, taskPriority]

        todoList.append(row)
        print(todoList)


todoProgram()