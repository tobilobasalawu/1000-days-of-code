def calc_type(a, b, res):
    addition = a + b
    subtraction = a - b
    multiply = a * b
    divide = a / b

    if res == addition:
        return 'addition'
    elif res == subtraction:
        return 'subtraction'
    elif res == multiply:
        return 'multiplication'
    else:
        return 'division'

