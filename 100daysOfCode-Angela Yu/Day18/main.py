from turtle import Turtle, Screen
import random

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

color = ["red", 'yellow', 'black', 'blue', 'dark salmon', 'dark sea green', 'DarkGoldenrod1', 'OrangeRed3', 'tomato', 'green', 'dark slate gray']

def drawShape(noOfSides):
    turtle.color(random.choice(color))
    for i in range(noOfSides):
        angle = 360 / noOfSides
        turtle.forward(100)
        turtle.rt(angle)

def mainTurtle():
    for i in range(3,11):
        drawShape(i)

mainTurtle()













screen = Screen()
screen.exitonclick()