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


def square():
    ranColour = random.choice(['red', 'blue', 'green', 'brown'])
    for i in range(4):
        turtle.color(ranColour)
        turtle.forward(90)
        turtle.rt(90)















screen = Screen()
screen.exitonclick()