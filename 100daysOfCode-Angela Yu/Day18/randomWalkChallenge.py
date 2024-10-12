from turtle import Turtle, Screen
import random
turtle = Turtle()


color = ["red", 'yellow', 'black', 'blue', 'dark salmon', 'dark sea green', 'DarkGoldenrod1', 'OrangeRed3', 'tomato', 'green', 'dark slate gray']
pos = [0, 90, 180, 270]


for i in range(200):
    turtle.color(random.choice(color))
    turtle.pensize(10)
    turtle.speed('fastest')
    turtle.forward(30)
    turtle.setheading(random.choice(pos))

screen = Screen()
screen.exitonclick()