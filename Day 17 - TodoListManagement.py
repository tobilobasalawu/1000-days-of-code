from multiprocessing.managers import Value
from os import remove

print("TODO LIST MANAGEMENT APP")
todoList = []

def todoProgram():
    while True:
        try:
            menu = int(input("\n1: Add\n2: View\n3: Remove\n4: Edit\n\n> "))
            if menu == 1:
                print('ADD')
                task = input("\nWhat is it? ")
                taskTime = input("What is it due? ")
                taskPriority = input("How Important? ")
                row = [task.lower(), taskTime.lower(), taskPriority.lower()]
                todoList.append(row)
            elif menu == 2:
                print('VIEW')
                viewMenu = int(input("\n1: View All\n2: View Priority\n\n> "))
                if viewMenu == 1:
                    if todoList == []:
                        print('No Tasks Available')
                    else:
                        for row in todoList:
                            for item in row:
                                print(f"{item:^10}", end=' | ')
                            print()
                        print()

                elif viewMenu == 2:
                    levelPriority = input("Which Priority: ")
                    if levelPriority in todoList:
                        for row in todoList:
                            for item in row:
                                print(f"{item:^10}", end=' | ')
                            print()
                    else:
                        print(f"No Priority named '{levelPriority}' is stored ")

            elif menu == 3:
                removeTask = input("What would you like to remove?\n> ").lower()
                if removeTask in todoList:
                    for row in todoList:
                        for item in row:
                            todoList.remove(row)
                            print(f"{item:^10}", end=' | ')
                        print()

                else:
                    print(f"No Task named '{removeTask}' is stored ")

            elif menu == 4:
                print('EDIT\n')

                newTitle = input("New title: ")
                newDate = input("New Due date: ")
                newPriority = input("New Priority: ")
                edit = [newTitle, newDate, newPriority]

                todoList.append(edit)
                print('\nUpdated')


        except ValueError:
            print("Please select a number from the menu")


todoProgram()