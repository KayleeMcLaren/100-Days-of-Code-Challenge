
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    menu_options = menu.get_items()
    order = input(f"\nWhat would you like? {menu_options}: ").lower()
    if order == 'report':
        money_machine.report()
        coffee_maker.report()
    elif order == "off":
        print("Turning machine off")
        machine_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
