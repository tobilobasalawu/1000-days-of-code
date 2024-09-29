from menuData import MENU
defaultWater = MENU['default']['water']
defaultMilk = MENU['default']['milk']
defaultCoffee = MENU['default']['coffee']
defaultMoney = MENU['default']['money']

def main():
    userRequest = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if userRequest == 'report':
        print(f"Water: {MENU['default']['water']}ml\nMilk: {MENU['default']['milk']}ml\nCoffee: {MENU['default']['coffee']}g\nMoney: ${MENU['default']['money']}")
    elif userRequest == 'latte':
        if defaultWater > MENU['latte']['ingredients']['water'] and defaultMilk > MENU['latte']['ingredients']['milk'] and  defaultCoffee > MENU['latte']['ingredients']['coffee']:
            print('Please Insert Coins')
            quarterInput = input("how many quarters?: ")

main()