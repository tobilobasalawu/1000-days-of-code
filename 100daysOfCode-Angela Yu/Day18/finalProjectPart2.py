from turtle import Turtle, Screen
import random
import turtle

t = Turtle()
turtle.colormode(255)

colorList = [(243, 242, 239), (171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (242, 237, 240), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244)]

t.penup()
t.speed('fastest')
t.setheading(255)
t.forward(300)
t.setheading(0)
numOfDots = 100

for dotCount in range(1, numOfDots + 1):
    t.dot(20, random.choice(colorList))
    t.forward(50)

    if dotCount % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(10*50)
        t.setheading(0)

t.hideturtle()







screen = Screen()
screen.exitonclick()