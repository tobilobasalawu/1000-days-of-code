# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('orange')
# timmy.forward(100)
#
# for steps in range(10):
#     for c in ('blue', 'red', 'green', 'yellow'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.left(30)
#
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
#print(tb)

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", 'Electric'],
    ["Squirtle", "Water"],
    ["Charmander", 'Fire'],
])

table.align = 'r'

print(table)