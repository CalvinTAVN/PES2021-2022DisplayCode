import PyQt6
import sys

'''
Battery box - bms, motor controller
battery temperature, motor, motor controller
battery current, motor controller current (phase current)
battery voltage (individual, total pack, lowest cell)
'''

class DashboardGUI:

    def __init__(self):
        self.window = PyQt6.QtWidgets.QMainWindow()
        self.frame = PyQt6.QtWidgets.QFrame()
        self.layout = PyQt6.QtWidgets.QGridLayout()
        self.speed_module = self.SpeedModule()
        self.controller_module = self.ControllerModule()
        self.motor_module = self.MotorModule()
        self.battery_module = self.BatteryModule()
        self.setup_gui()

    def setup_gui(self):
        self.layout.addLayout(self.get_layout(self.speed_module))
        self.layout.addLayout(self.get_layout(self.controller_module))
        self.layout.addLayout(self.get_layout(self.motor_module))
        self.layout.addLayout(self.get_layout(self.battery_module))        
        self.frame.setLayout(self.layout)
        self.window.setCentralWidget(self.frame)

    def display(self):
        self.window.show()
    
    def edit_widget(module, key, label):
            module.widgets[key].setText(label)

    def get_layout(module):
            layout = PyQt6.Widgets.QGridLayout()
            for widget in module.widgets.values():
                layout.addWidget(widget)
            return layout
        
    class SpeedModule:

        def __init__(self):
            self.widgets = {}
            self.widgets['rpm'] = PyQt6.QtWidgets.QLabel()
            self.widgets['speed'] = PyQt6.QtWidgets.QLabel()

    class ControllerModule:

        def __init__(self):
            self.widgets = {}
            self.widgets['controller_temp'] = PyQt6.QtWidgets.QLabel()
    
    class MotorModule:

        def __init__(self):
            self.widgets = {}
            self.widgets['motor_temp'] = PyQt6.QtWidgets.QLabel()

    class BatteryModule:

        def __init__(self, num_cells):
            self.widgets = {}
            for i in range(num_cells):
                self.widgets['battery_temp' + i] = PyQt6.QtWidgets.QLabel()
                self.widgets['battery_current' + i] = PyQt6.QtWidgets.QLabel()
                self.widgets['battery_voltage' + i] = PyQt6.QtWidgets.QLabel()
        
def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    gui = DashboardGUI()
    gui.display()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()