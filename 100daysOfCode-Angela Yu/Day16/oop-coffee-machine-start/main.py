from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

name = 'Latte'
cost = 2.5
milk = 45
coffee = 29
water = 50

items = MenuItem(name, cost, milk, coffee, water)
print(items)


