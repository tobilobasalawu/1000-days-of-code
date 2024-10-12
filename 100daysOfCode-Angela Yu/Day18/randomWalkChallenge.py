import turtle
from turtle import Turtle, Screen
import random
Txtle = Turtle()
turtle.colormode(255)

def randomColour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

pos = [0, 90, 180, 270]

for i in range(5000):
    Txtle.color(randomColour())
    Txtle.pensize(10)
    Txtle.speed('fastest')
    Txtle.forward(30)
    Txtle.setheading(random.choice(pos))

screen = Screen()
screen.exitonclick()