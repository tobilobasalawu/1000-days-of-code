from turtle import Turtle, Screen
import random
turtle = Turtle()


color = ["red", 'yellow', 'black', 'blue', 'dark salmon', 'dark sea green', 'DarkGoldenrod1', 'OrangeRed3', 'tomato', 'green', 'dark slate gray']
pos = [90, 180, 360]

def random1():
    for i in range(20):
        turtle.color(random.choice(color))
        turtle.speed(9)
        turtle.pensize(10)
        turtle.forward(30)
        turtle.lt(random.choice(pos))


def random2():
    for i in range(40):
        turtle.color(random.choice(color))
        turtle.speed(9)
        turtle.pensize(10)
        turtle.forward(30)
        turtle.rt(random.choice(pos))

def main():
    second = [random1(), random2()]
    random.choice(second)

main()


screen = Screen()
screen.exitonclick()