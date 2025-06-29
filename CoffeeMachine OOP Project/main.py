from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_register = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: \n").lower()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        my_register.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink):
            if my_register.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

