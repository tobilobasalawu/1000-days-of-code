from turtle import Turtle, Screen
import random

color = ["red", 'yellow', 'black', 'blue', 'dark salmon', 'dark sea green', 'DarkGoldenrod1', 'OrangeRed3', 'tomato', 'green', 'dark slate gray']

turtle = Turtle()

turtle.color(random.choice(color))
turtle.pensize(10)
turtle.forward(30)
turtle.lt(90)
turtle.forward(30)
turtle.rt(90)


screen = Screen()
screen.exitonclick()