print("TODO LIST MANAGEMENT APP\n")

menu = input("1: Add\n2: View\n3: Remove\n4: Edit\n\n> ")
todoList = []

def todoProgram():
    if menu.lower() == 'add':
        print('ADD')
        task = input("\nWhat is it? ")
        taskTime = input("What is it due? ")
        taskPriority = input("How Important? ")
        row = [task, taskTime, taskPriority]
        todoList.append(row)
    elif menu.lower() == 'view':
        print('VIEW')
        viewMenu = int(input("\n1: View All\n2: View Priority\n\n> "))
        if viewMenu == 1:
            print(todoList)

todoProgram()