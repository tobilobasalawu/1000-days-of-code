from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')

# for i in range(4):
#     turtle.fd(100)
#     turtle.lt(90)


# for i in range(10):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.forward(20)
#     turtle.pendown()


def square():
    for i in range(4):
        turtle.color('blue')
        turtle.forward(90)
        turtle.rt(90)

def triangle():
    turtle.color('red')
    for i in range(3):
        turtle.forward(100)
        turtle.rt(120)

def pentagon():
    turtle.color('brown')
    for i in range(5):
        turtle.forward(100)
        turtle.rt(72)

def hexagon():
    turtle.color('green')
    for i in range(6):
        turtle.forward(100)
        turtle.rt(60)

def mainTurtle():
    square()
    triangle()
    pentagon()
    hexagon()

mainTurtle()













screen = Screen()
screen.exitonclick()