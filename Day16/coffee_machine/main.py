from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

option = my_menu.get_items()

is_on = True

while is_on:
    choice = input(f"What would you like? {option} ")
    drink = my_menu.find_drink(choice)
    if choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == 'off':
        is_on = False
        print("Bye Bye!")
    else:
        my_coffee_maker.is_resource_sufficient(drink)
        my_coffee_maker.make_coffee(drink)
        my_money_machine.make_payment(drink.cost)













