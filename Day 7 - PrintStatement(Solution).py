def newPrint(color, word):
    if color.lower() == 'red':
        print("\033[31m", end = "")
    elif color.lower() == 'green':
        print('\033[32m', end="")
    elif color.lower() == 'blue':
        print('\033[34m', end="")
    else:
        print('\033[0m', end="")

print("Super Subroutine")
print("With my", end=" ")
