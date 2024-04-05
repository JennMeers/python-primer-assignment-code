class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)
    def cleaning_cycle(self, cycle_duration):
        print("Cleaning cycle started, please wait " + cycle_duration + " minutes")

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
    def update_menu(self, new_coffee):
        if new_coffee in self.coffee_menu:
            print(f"{new_coffee} has previously been added to the menu")
        else:
            self.coffee_menu.append(new_coffee)
            print(f"{new_coffee} added to menu")
    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"Making {coffee_type}")
        else:
            (print(f"{coffee_type} is not available on today's menu. Please choose from the following menu items: \n{self.coffee_menu}"))
    def cleaning_cycle(self):
        print("Please check water tank is full before cleaning cycle begins")

my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')
    
class SmartOven(KitchenAppliance):
    def __init__ (self, model_number, brand, temperature_range):
        KitchenAppliance.__init__(self, model_number, brand)
        self.temperature_range = temperature_range
    def preheat (self, select_temperature):
        if select_temperature in self.temperature_range:
            print(f"Heating to {select_temperature} degrees")
        else:
            print(f"{select_temperature} degrees is outside the programmed temperature range \nPlease select a temperature between {min(self.temperature_range)} and {max(self.temperature_range)} degrees")

my_smart_oven = SmartOven(12345, 'LG', range(50,251))
my_smart_oven.report()
my_smart_oven.preheat(100)
my_smart_oven.preheat(300)

my_smart_oven.cleaning_cycle('45')
my_coffee_machine.cleaning_cycle()