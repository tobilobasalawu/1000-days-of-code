from menuData import MENU
power = True

dime = 0.10
quarter = 0.25
nickle = 0.05
penny = 0.01

def main():
    defaultWater = MENU['default']['water']
    defaultMilk = MENU['default']['milk']
    defaultCoffee = MENU['default']['coffee']
    defaultMoney = MENU['default']['money']

    while power:
        userRequest = input("\nWhat would you like? (espresso/latte/cappuccino):\n").lower()
        if userRequest == 'latte':
            if defaultWater > MENU['latte']['ingredients']['water'] and defaultMilk > MENU['latte']['ingredients'][
                'milk'] and defaultCoffee > MENU['latte']['ingredients']['coffee']:
                print('\nPlease Insert Coins')
                quarterInput = int(input("how many quarters?: "))
                dimeInput = int(input("how many dimes?: "))
                nickleInput = int(input("how many nickles?: "))
                penniesInput = int(input("how many pennies?: "))
                total = (quarterInput * quarter) + (dimeInput * dime) + (nickleInput * nickle) + (penniesInput * penny)
                if total > MENU['latte']['cost']:
                    defaultWater -= MENU['latte']['ingredients']['water']
                    defaultMilk -= MENU['latte']['ingredients']['milk']
                    defaultCoffee -= MENU['latte']['ingredients']['coffee']
                    defaultMoney += MENU['latte']['cost']

                    costChange = total - MENU['latte']['cost']
                    print(f'\nHere is ${costChange} in change.\nHere is your latte ☕. Enjoy!')
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif defaultWater < MENU['latte']['ingredients']['water'] and defaultMilk > MENU['latte']['ingredients'][
                'milk'] and defaultCoffee > MENU['latte']['ingredients']['coffee']:
                print('Sorry there is not enough water.')
            elif defaultWater > MENU['latte']['ingredients']['water'] and defaultMilk < MENU['latte']['ingredients'][
                'milk'] and defaultCoffee > MENU['latte']['ingredients']['coffee']:
                print('Sorry there is not enough milk.')
            elif defaultWater > MENU['latte']['ingredients']['water'] and defaultMilk > MENU['latte']['ingredients'][
                'milk'] and defaultCoffee < MENU['latte']['ingredients']['coffee']:
                print('Sorry there is not enough coffee.')
            else:
                print('Sorry there is not enough water.')


        elif userRequest == 'report':
            print(f"Water: {defaultWater}ml\nMilk: {defaultMilk}ml\nCoffee: {defaultCoffee}g\nMoney: ${defaultMoney}")


        elif userRequest == 'espresso':
            if defaultWater > MENU['espresso']['ingredients']['water'] and defaultCoffee > MENU['espresso']['ingredients']['coffee']:
                print('\nPlease Insert Coins')
                quarterInput = int(input("how many quarters?: "))
                dimeInput = int(input("how many dimes?: "))
                nickleInput = int(input("how many nickles?: "))
                penniesInput = int(input("how many pennies?: "))
                total = (quarterInput * quarter) + (dimeInput * dime) + (nickleInput * nickle) + (penniesInput * penny)
                if total > MENU['espresso']['cost']:
                    defaultWater -= MENU['espresso']['ingredients']['water']
                    defaultCoffee -= MENU['espresso']['ingredients']['coffee']
                    defaultMoney += MENU['espresso']['cost']

                    costChange = total - MENU['espresso']['cost']
                    print(f'\nHere is ${costChange} in change.\nHere is your espresso ☕. Enjoy!')
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif defaultWater < MENU['espresso']['ingredients']['water'] and defaultCoffee > MENU['espresso']['ingredients']['coffee']:
                print('Sorry there is not enough water.')
            elif defaultWater > MENU['espresso']['ingredients']['water'] and defaultCoffee < MENU['espresso']['ingredients']['coffee']:
                print('Sorry there is not enough coffee.')

        elif userRequest == 'cappuccino':
            if defaultWater > MENU['cappuccino']['ingredients']['water'] and defaultMilk > MENU['cappuccino']['ingredients'][
                'milk'] and defaultCoffee > MENU['cappuccino']['ingredients']['coffee']:
                print('\nPlease Insert Coins')
                quarterInput = int(input("how many quarters?: "))
                dimeInput = int(input("how many dimes?: "))
                nickleInput = int(input("how many nickles?: "))
                penniesInput = int(input("how many pennies?: "))
                total = (quarterInput * quarter) + (dimeInput * dime) + (nickleInput * nickle) + (penniesInput * penny)
                if total > MENU['espresso']['cost']:
                    defaultWater -= MENU['cappuccino']['ingredients']['water']
                    defaultMilk -= MENU['cappuccino']['ingredients']['milk']
                    defaultCoffee -= MENU['cappuccino']['ingredients']['coffee']
                    defaultMoney += MENU['cappuccino']['cost']

                    costChange = total - MENU['espresso']['cost']
                    print(f'\nHere is ${costChange} in change.\nHere is your cappuccino ☕. Enjoy!')
                else:
                    print("Sorry that's not enough money. Money refunded.")


            elif defaultWater < MENU['cappuccino']['ingredients']['water'] and defaultMilk > MENU['cappuccino']['ingredients'][
                'milk'] and defaultCoffee > MENU['cappuccino']['ingredients']['coffee']:
                print('Sorry there is not enough water.')
            elif defaultWater > MENU['cappuccino']['ingredients']['water'] and defaultMilk < MENU['cappuccino']['ingredients'][
                'milk'] and defaultCoffee > MENU['cappuccino']['ingredients']['coffee']:
                print('Sorry there is not enough milk.')
            elif defaultWater > MENU['cappuccino']['ingredients']['water'] and defaultMilk > MENU['cappuccino']['ingredients'][
                'milk'] and defaultCoffee < MENU['cappuccino']['ingredients']['coffee']:
                print('Sorry there is not enough coffee.')


main()