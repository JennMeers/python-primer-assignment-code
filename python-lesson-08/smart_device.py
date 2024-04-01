class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=set()):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Demo App"):
        if app_name in self.app_list:
            print(f"{app_name} is already installed")
        else:
            print(f"Installing {app_name}...")
        self.app_list.add(app_name)
        return self.app_list
    
    def delete_app(self, app_name):
        print(f"{app_name} has been deleted.")
        self.app_list.remove(app_name)
        return self.app_list

device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

device_a.install_app("Test app")
device_a.install_app()
device_a.install_app()
device_a.install_app("coffee")
device_a.install_app("coffee")
print(f"Device A app list: {device_a.app_list}")

device_a.delete_app("Test app")
device_a.delete_app("coffee")
device_a.delete_app("Demo App")
print(f"Device A app list: {device_a.app_list}")

device_b = SmartDevice(12345, 'Miso', 3.5)
device_b.report()

device_b.install_app()
device_b.install_app("Ramen")
print(f"Device B app list: {device_b.app_list}")
