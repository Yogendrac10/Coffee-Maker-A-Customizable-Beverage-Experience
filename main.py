from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    print(options)
    choice = input("Which drink do you want??  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  
        money_machine.report()   
    elif choice == options:
        menu.find_drink(choice)
        payment = money_machine.process_coins()
        money_machine.make_payment(menu.item[cost])