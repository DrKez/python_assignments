class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand

    def report(self):
        print("This is model " + str(self.model_number) + " from " + self.brand)


class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        super().__init__(model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, new_coffee):
        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
        return self.coffee_menu

    def make_coffee(self):
        coffee_type = input("What type of coffee would you like? ")
        while coffee_type not in self.coffee_menu:
            print(f"Sorry, we cannot make a '{coffee_type}'.")
            print("Please choose from the following coffee types:")
            print("\U00002615 " + '\n\U00002615 '.join(self.coffee_menu))
            coffee_type = input("What type of coffee would you like? ")

        print(f"Making a {coffee_type}.")
        print("Enjoy your coffee \U0001f600")


my_coffee_machine = SmartCoffeeMachine(1.2, 'CaffeDelux')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee()
