from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def Main():
    coffeeMenu = Menu()
    menuInput = input(f"What would you like? ({coffeeMenu.get_items()}): ").lower()

    coffeeMoney = MoneyMachine()
    coffeeMake = CoffeeMaker()

    if menuInput == 'report':
        coffeeMoney.report()
        coffeeMake.report()

Main()