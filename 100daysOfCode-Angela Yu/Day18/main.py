from turtle import Turtle, Screen

from numpy.ma.core import angle
from openpyxl.utils import range_boundaries

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

def drawShape(noOfSides):
    for i in noOfSides:
        angle = 360 / noOfSides
        turtle.forward(100)
        turtle.rt(angle)















screen = Screen()
screen.exitonclick()