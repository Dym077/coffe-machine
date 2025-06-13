# TODO 7: Calculate cost for extra ingredients
EXTRA_INGREDIENT_COSTS = {
        "water": 0.001, # $0.001 per ml water
        "milk": 0.002, # $0.002 per ml milk
        "coffee": 0.005 # $0.001 per g coffee
    }

# TODO 8: Limit amount of extra ingredients
MAX_EXTRA_INGREDIENTS = {
    "water": 100, # Max 100 ml of extra water
    "milk": 50, # Max 50 ml of extra milk
    "coffee": 10 # Max 10 ml of extra coffee
}


class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def customize(self, extra_water=0, extra_milk=0, extra_coffee=0):
        """Adjusts the ingredients of the drink and calculates the extra cost."""
        if extra_water > MAX_EXTRA_INGREDIENTS["water"]:
            print(f"Sorry, you can only add a maximum of {MAX_EXTRA_INGREDIENTS['water']} ml extra water.")
            extra_water = 0 # Reset allowed amount

        if extra_milk > MAX_EXTRA_INGREDIENTS["milk"]:
            print(f"Sorry, you can only add a maximum of {MAX_EXTRA_INGREDIENTS['milk']} ml extra milk.")
            extra_milk = 0 # Reset allowed amount

        if extra_coffee > MAX_EXTRA_INGREDIENTS["coffee"]:
            print(f"Sorry, you can only add a maximum of {MAX_EXTRA_INGREDIENTS['coffee']} ml extra coffee.")
            extra_coffee = 0 # Reset allowed amount

        self.ingredients["water"] += extra_water
        self.ingredients["milk"] += extra_milk
        self.ingredients["coffee"] += extra_coffee

        extra_cost = (
            extra_water * EXTRA_INGREDIENT_COSTS["water"] +
            extra_milk * EXTRA_INGREDIENT_COSTS["milk"] +
            extra_coffee * EXTRA_INGREDIENT_COSTS["coffee"]
        )

        self.cost += extra_cost
        return self

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                # print(f"Found drink: {item.name}, Ingredients: {item.ingredients}")
                return item
        print("Sorry that item is not available.")
