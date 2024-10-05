from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def Main():
    coffeeMenu = Menu()
    print(coffeeMenu.get_items())

Main()