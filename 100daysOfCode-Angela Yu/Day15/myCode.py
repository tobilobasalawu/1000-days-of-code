from menuData import MENU

def main():
    userRequest = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if userRequest == 'report':
        print(f"Water: {MENU['default']['water']}ml\nMilk: {MENU['default']['milk']}ml\nCoffee: {MENU['default']['coffee']}g\nMoney: ${MENU['default']['money']}")


main()