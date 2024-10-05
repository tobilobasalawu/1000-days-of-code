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

        elif menuInput == 'espresso':
            coffeeMoney.make_payment(coffeeMenu.find_drink(menuInput).cost)

        elif menuInput == 'latte':
            coffeeMoney.make_payment(coffeeMenu.find_drink(menuInput).cost)

        elif menuInput == 'quit':
            coffeeMachine = False
            print('\nCoffee Machine, Turned Off')

Main()



