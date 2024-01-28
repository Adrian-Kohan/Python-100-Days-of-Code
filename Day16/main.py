from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def machine():
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        machine()
    elif order == "off":
        return
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        machine()


machine()

