from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = True
coffeeMenu = Menu()
coffeeMoney = MoneyMachine()
coffeeMake = CoffeeMaker()

def Main():
    coffeeMachine = True
    while coffeeMachine:
        menuInput = input(f"\nWhat would you like? ({coffeeMenu.get_items()}):\n").lower()
        if menuInput == 'report':
            coffeeMoney.report()
            coffeeMake.report()

        else:
            drink = coffeeMenu.find_drink(menuInput)
            if coffeeMake.is_resource_sufficient(drink) and coffeeMoney.make_payment(drink):
                coffeeMake.make_coffee()


Main()


