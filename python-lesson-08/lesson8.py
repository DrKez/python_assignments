
class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Demo app"):
        print(f"Installing {app_name}...")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
        return self.app_list

    def delete_app(self, app_name):
        self.app_list.remove(app_name)
        return self.app_list


#testing that code works. Added each device to its own funtion so I could run and test together and seperately
def device_a(SmartDevice):
    device_a = SmartDevice(1233244, 'CLG', 5.7)
    device_a.report()
    print(f"The current apps installed are: {device_a.app_list}")
    device_a.install_app()
    device_a.install_app("Tetris")
    device_a.install_app("Tetris")
    device_a.install_app("Frogger")
    print(f"App list with no duplicates: {device_a.app_list}")
    device_a.delete_app("Tetris")
    print(f"App list with app removed: {device_a.app_list}")

def device_b(SmartDevice):
    device_b = SmartDevice(112991, 'KezPhone', 6)
    device_b.report()
    print(f"The current apps installed are: {device_b.app_list}")
    device_b.install_app("Lemmings")
    device_b.install_app("Sudoku")
    device_b.install_app("Demo app")
    print(f"App list with no duplicates: {device_b.app_list}")
    device_b.delete_app("Demo app")
    print(f"App list with app removed: {device_b.app_list}")

device_b(SmartDevice)
device_a(SmartDevice)