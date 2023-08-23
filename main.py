from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_make = CoffeeMaker()
money_machine = MoneyMachine()

turn_off_machine = False

while not turn_off_machine:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if choice == 'off':
        turn_off_machine = True
    elif choice == 'report':
        coffee_make.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_make.make_coffee(chosen_drink)
