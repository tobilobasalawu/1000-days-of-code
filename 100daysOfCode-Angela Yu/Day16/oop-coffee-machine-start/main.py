from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeeMachine = True

def Main():
    while coffeeMachine:
        coffeeMenu = Menu()
        menuInput = input(f"\nWhat would you like? ({coffeeMenu.get_items()}):\n").lower()

        coffeeMoney = MoneyMachine()
        coffeeMake = CoffeeMaker()

        if menuInput == 'report':
            coffeeMoney.report()
            coffeeMake.report()

Main()