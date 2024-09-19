from os import remove

print("TODO LIST MANAGEMENT APP")
todoList = []

def todoProgram():
    while True:
        menu = input("\n1: Add\n2: View\n3: Remove\n4: Edit\n\n> ")
        if menu.lower() == 'add':
            print('ADD')
            task = input("\nWhat is it? ")
            taskTime = input("What is it due? ")
            taskPriority = input("How Important? ")
            row = [task.lower(), taskTime.lower(), taskPriority.lower()]
            todoList.append(row)
        elif menu.lower() == 'view':
            print('VIEW')
            viewMenu = int(input("\n1: View All\n2: View Priority\n\n> "))
            if viewMenu == 1:
                for row in todoList:
                    for item in row:
                        print(f"{item}:^10", end=' | ')
            elif viewMenu == 2:
                levelPriority = input("Which Priority: ")
                for row in todoList:
                    for item in row:
                        if levelPriority in row:
                            print(f"{item}:^10", end=' | ')
                        elif levelPriority not in row:
                            print(f"No Priority named '{levelPriority}' is stored ")

        elif menu.lower() == 'remove':
            removeTask = input("What would you like to remove?\n> ").lower()
            for row in todoList:
                if removeTask in row:
                    todoList.remove(row)


todoProgram()