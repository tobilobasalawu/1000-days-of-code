import turtle as t
from turtle import Turtle, Screen
import random

txl = t.Turtle()
t.colormode(255)

def randomColour():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(100):
    txl.color(randomColour())
    txl.speed('fastest')
    txl.left(5)
    txl.circle(100)







screen = Screen()
screen.exitonclick()