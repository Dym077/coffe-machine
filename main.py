from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    # TODO 1: Print report
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
        print("Machine is off")

    # TODO 2: Check Resources sufficient?

    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                # TODO 3: Process coins
                # TODO 4: Check transaction successful
                if money_machine.make_payment(drink.cost):
                    # TODO 5: Make coffee
                    coffee_maker.make_coffee(drink)
