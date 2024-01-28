resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def coins_checker(money, order):
    """check if there is enough money for the user order or not"""
    if money == MENU[order]["cost"]:
        resources["money"] += MENU[order]["cost"]
    elif money > MENU[order]["cost"]:
        resources["money"] += MENU[order]["cost"]
        remain = round((money - MENU[order]["cost"]), 2)
        print(f"Here is ${remain}  in change")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 1


def coins(user_input):
    """give money from user and then check it based on the order cost"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    monetary_value = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01), 2)
    return coins_checker(monetary_value, user_input)


def ingredients_check(order):
    """check if there is enough ingredients for user order or not"""
    for i in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return 1
        elif MENU[order]["ingredients"][i] <= resources[i]:
            if coins(order) != 1:
                resources[i] = resources[i] - MENU[order]["ingredients"][i]
                return
            else:
                return 1


def machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        for x, y in resources.items():
            print(f"{x} = {y}")
        machine()
    elif user_input == "off":
        return
    else:
        if ingredients_check(user_input) != 1:
            print(f"Here is your {user_input} ☕️  Enjoy!")
        machine()


machine()