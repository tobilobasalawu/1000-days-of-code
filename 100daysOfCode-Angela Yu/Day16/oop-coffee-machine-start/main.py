from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = True
coffeeMenu = Menu()
coffeeMoney = MoneyMachine()
coffeeMake = CoffeeMaker()

while coffeeMachine:
    menuInput = input(f"\nWhat would you like? ({coffeeMenu.get_items()}):\n").lower()
    if menuInput == 'report':
        coffeeMoney.report()
        coffeeMake.report()

    elif menuInput == 'quit':
        coffeeMachine = False

    else:
        drink = coffeeMenu.find_drink(menuInput)
        isSufficient = coffeeMake.is_resource_sufficient(drink)
        isPayment = coffeeMoney.make_payment(drink.cost)
        if isSufficient and isPayment:
            #coffeeMoney.process_coins()
            coffeeMake.make_coffee(drink)

