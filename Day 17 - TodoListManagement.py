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
            row = [task, taskTime, taskPriority]
            todoList.append(row)
        elif menu.lower() == 'view':
            print('VIEW')
            viewMenu = int(input("\n1: View All\n2: View Priority\n\n> "))
            if viewMenu == 1:
                for row in todoList:
                    print(f"{row[0]:^10}|{row[1]:^10}|{row[2]:^10}")
            elif viewMenu == 2:
                levelPriority = input("Which Priority: ")
                for row in todoList:
                    #if levelPriority in row:


todoProgram()