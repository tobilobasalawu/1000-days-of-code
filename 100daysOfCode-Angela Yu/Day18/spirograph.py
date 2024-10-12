import turtle as t
from turtle import Turtle, Screen
import random

txl = t.Turtle()
t.colormode(255)

def randomColour():
    r = random.choice(255)
    g = random.choice(255)
    b = random.choice(255)
    return (r,g,b)


txl.circle(100)







screen = Screen()
screen.exitonclick()