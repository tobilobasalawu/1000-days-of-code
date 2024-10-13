from turtle import Turtle, Screen
import random
import turtle

t = Turtle()
turtle.colormode(255)

colorList = [(243, 242, 239), (171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (242, 237, 240), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244)]

for i in range(10):
    t.dot(20, random.choice(colorList))
    t.forward(50)









screen = Screen()
screen.exitonclick()