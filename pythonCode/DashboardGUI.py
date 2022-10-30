import PyQt6

'''
Battery box - bms, motor controller
battery temperature, motor, motor controller
battery current, motor controller current (phase current)
battery voltage (individual, total pack, lowest cell)
'''

class DashboardGUI:

    def __init__(self):
        # self.frame = 
        # self.widgets = 
        # self.layout =
        pass

    def display(self):
        layout = PyQt6.QtWidgets.QGridLayout()
        

    class SpeedWidget:

        def __init__(self, rpm, speed):
            self.rpm = rpm
            self.speed = speed

        def get_widgets(self):
            widgets = {}
            widgets['rpm'] = PyQt6.QtWidgets.QLabel(self.rpm)
            widgets['speed'] = PyQt6.QtWidgets.QLabel(self.speed)

        def get_module(self):
            speed_module = PyQt6.Widgets.QGridLayout()

    class TemperatureWidget:

        def __init__(self, motor_temp, controller_temp, battery_temps):
            self.motor_temp = motor_temp
            self.controller_temp = controller_temp
            self.battery_temps = battery_temps
    
    class ElectricalWidget:

        def __init__(self, battery_current, battery_voltages):
            self.battery_current = battery_current
            self.battery_voltages = battery_voltages
        
def main():
    pass

if __name__ == '__main__':
    main()