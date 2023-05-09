# The coffee machine

from data import MENU, resources


def check_resource(order_ingredients):
    """Return True if there is enough ingredients, or False if opposite"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there isn't enough {item}")
            return False
    return True


def process_coin():
    """Return the total of Coin inserted"""
    total = float(input("How many Quarters? ")) * 0.25
    total += float(input("How many Dimes? ")) * 0.1
    total += float(input("How many Nickels? ")) * 0.05
    total += float(input("How many Pennies? ")) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    """Return True if payment is sufficient, or False if opposite"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry you're ${drink_cost - money_received} short")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the resources after making drinks"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name.capitalize()}. Enjoy!")


profit = 0
is_on = True
while is_on:
    order = input("What would you like? (espresso, latte, cappuccino)\n").lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[order]
        if check_resource(drink['ingredients']):
            payment = process_coin()
            if is_payment_successful(payment, drink['cost']):
                make_coffee(order, drink["ingredients"])
