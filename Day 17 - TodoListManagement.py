print("TODO LIST MANAGEMENT APP\n")

menu = input("1: Add\n2: View\n3: Remove\n4: Edit\n\n>")

def todoProgram():
    if menu.lower() == 'add' or '1':
        task = input("\nWhat is it? ")
        taskTime = input("\nWhat is it due? ")
        taskPriority = input("\nHow Important? ")