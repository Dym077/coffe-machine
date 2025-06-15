from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def get_available_drinks(menu, resources):
    """Filters the menu to only return available drinks"""
    available_drinks = []
    for drink in menu.menu:
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > resources[item]:
                can_make = False
                break
        if can_make:
            available_drinks.append(drink)
    return available_drinks


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    available_drinks = get_available_drinks(menu, coffee_maker.resources)

    if available_drinks:
        print("Available drinks:")
        for available_drink in available_drinks:
            print(f"- {available_drink.name} (${available_drink.cost})")
    else:
        print("We're sorry We can't make anything right now.")
        break

    user_input = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

    # TODO 1: Print report
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
        print("Machine is off")
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if drink in available_drinks:
                # TODO 6: Customize drink
                extra_water = int(input("Extra water (ml)? (0 for none):"))
                extra_milk = int(input("Extra milk (ml)? (0 for none):"))
                extra_coffee = int(input("Extra coffee (ml)? (0 for none):"))

                drink.customize(extra_water, extra_milk, extra_coffee)


                # TODO 3: Process coins
                # TODO 4: Check transaction successful
                if money_machine.make_payment(drink.cost):
                    # TODO 5: Make coffee
                    coffee_maker.make_coffee(drink)