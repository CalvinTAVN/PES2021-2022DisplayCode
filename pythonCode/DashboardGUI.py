from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class DashboardGUI:

    def __init__(self, args):
        self.values = {}
        self.app = QApplication(args)
        self.window = QMainWindow()
        self.frame = QFrame()
        self.layout = QGridLayout()
        self.speed_module = self.SpeedModule(self)
        self.controller_module = self.ControllerModule(self)
        self.motor_module = self.MotorModule(self)
        self.battery_module = self.BatteryModule(self, numCells = 5)
        self.current_module = self.CurrentModule(self)
        self.setup_gui()

    def setup_gui(self):
        self.window.setWindowTitle('Dashboard GUI')
        
        self.layout.setRowStretch(0, 8)
        self.layout.setRowStretch(1, 2)
        self.layout.setColumnStretch(0, 4)
        self.layout.setColumnStretch(1, 4)
        self.layout.setColumnStretch(2, 4)

        self.layout.addLayout(self.speed_module.get_module(), 0, 0, 1, 2)
        self.layout.addLayout(self.controller_module.get_module(), 1, 0)
        self.layout.addLayout(self.motor_module.get_module(), 1, 1)
        self.layout.addLayout(self.battery_module.get_module(), 0, 2)
        self.layout.addLayout(self.current_module.get_module(), 1, 2)

        self.frame.setLayout(self.layout)

        self.window.setCentralWidget(self.frame)

    def display(self):
        screen_size = QGuiApplication.primaryScreen().availableGeometry()
        self.window.resize(screen_size.width() // 2, screen_size.height() // 2)
        self.window.move(screen_size.center() - self.window.frameGeometry().center())
        self.window.show()

    def execute(self):
        self.app.exec()

    def edit_values(self, new_values):
        for key in new_values.keys():
            if self.values[key]:
                self.values[key].setText(str(new_values[key]))

    class SpeedModule:
        def __init__(self, gui):
            self.gui = gui
            self.speed_module = QGridLayout()
            self.gui.values['mph'] = QLabel()
            self.gui.values['rpm'] = QLabel()
            self.setup_module()
        
        def setup_module(self):
            mph_container = QFrame()

            mph_layout = QGridLayout(mph_container)

            mph_label = QLabel('MPH')
            mph_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            mph_layout.addWidget(mph_label, 0, 0)

            self.gui.values['mph'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            mph_layout.addWidget(self.gui.values['mph'], 1, 0)

            self.speed_module.addWidget(mph_container, 0, 0)

            rpm_container = QFrame()

            rpm_layout = QGridLayout(rpm_container)
            rpm_label = QLabel('RPM')
            rpm_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            rpm_layout.addWidget(rpm_label, 0, 0)

            self.gui.values['rpm'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            rpm_layout.addWidget(self.gui.values['rpm'], 1, 0)
            
            self.speed_module.addWidget(rpm_container, 0, 1)

        def get_module(self):
            return self.speed_module

    class ControllerModule:

        def __init__(self, gui):
            self.gui = gui
            self.controller_module = QGridLayout()
            self.temperature_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            temperature_container = QFrame()

            temperature_layout = QGridLayout(temperature_container)
            temperature_label = QLabel('Controller Temperature')
            temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temperature_layout.addWidget(temperature_label, 0, 0)

            temperature_layout.addWidget(self.temperature_value, 1, 0)

            self.controller_module.addWidget(temperature_container, 0, 0)

        def get_module(self):
            return self.controller_module

    class MotorModule:

        def __init__(self, gui):
            self.gui = gui
            self.motor_module = QGridLayout()
            self.temperature_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            temperature_container = QFrame()

            temperature_layout = QGridLayout(temperature_container)
            temperature_label = QLabel('Motor Temperature')
            temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temperature_layout.addWidget(temperature_label, 0, 0)

            temperature_layout.addWidget(self.temperature_value, 1, 0)

            self.motor_module.addWidget(temperature_container, 0, 0)

        def get_module(self):
            return self.motor_module        

    class BatteryModule:
        
        def __init__(self, gui, numCells):
            self.gui = gui
            self.numCells = numCells
            self.battery_module = QGridLayout()
            self.cell_modules = []
            self.low_voltage_value = QLabel()
            self.average_voltage_value = QLabel()
            self.high_voltage_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            for cell in range(self.numCells):
                self.cell_modules.append(self.CellModule(self.gui))
                self.battery_module.addLayout(self.cell_modules[cell].get_module(), cell, 0)

            cell_stats_module = QGridLayout()

            low_voltage_container = QFrame()

            low_voltage_layout = QGridLayout(low_voltage_container)

            low_voltage_label = QLabel('Low Voltage')
            low_voltage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            low_voltage_layout.addWidget(low_voltage_label, 0, 0)

            low_voltage_layout.addWidget(self.low_voltage_value, 1, 0)

            cell_stats_module.addWidget(low_voltage_container, 0, 0)

            average_voltage_container = QFrame()

            average_voltage_layout = QGridLayout(average_voltage_container)

            average_voltage_label = QLabel('Average Voltage')
            average_voltage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            average_voltage_layout.addWidget(average_voltage_label, 0, 0)

            average_voltage_layout.addWidget(self.average_voltage_value, 1, 0)

            cell_stats_module.addWidget(average_voltage_container, 0, 1)

            high_voltage_container = QFrame()

            high_voltage_layout = QGridLayout(high_voltage_container)

            high_voltage_label = QLabel('High Voltage')
            high_voltage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            high_voltage_layout.addWidget(high_voltage_label, 0, 0)

            high_voltage_layout.addWidget(self.high_voltage_value, 1, 0)

            cell_stats_module.addWidget(high_voltage_container, 0, 2)

            self.battery_module.addLayout(cell_stats_module, self.numCells, 0)
        
        def get_module(self):
            return self.battery_module

        class CellModule:
            
            def __init__(self, gui):
                self.gui = gui
                self.cell_module = QGridLayout()
                self.temperature_value = 0
                self.voltage_value = 0
                self.current_value = 0
                self.setup_module()

            def setup_module(self):
                cell_container = QFrame()

                cell_layout = QGridLayout(cell_container)

                cell_layout.setRowMinimumHeight(0, 5)

                temperature_container = QFrame()

                cell_layout.addWidget(temperature_container, 0, 0)

                voltage_container = QFrame()

                cell_layout.addWidget(voltage_container, 0, 1)

                current_container = QFrame()

                cell_layout.addWidget(current_container, 0, 2)

                self.cell_module.addWidget(cell_container)

            def get_module(self):
                return self.cell_module
        
    class CurrentModule:
        def __init__(self, gui):
            self.gui = gui
            self.current_module = QGridLayout()
            self.dc_value = QLabel()
            self.phase_value = QLabel()
            self.knots_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            dc_container = QFrame()

            dc_layout = QGridLayout(dc_container)

            dc_label = QLabel('DC')
            dc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            dc_layout.addWidget(dc_label, 0, 0)

            dc_layout.addWidget(self.dc_value, 1, 0)

            self.current_module.addWidget(dc_container, 0, 0)

            phase_container = QFrame()

            phase_layout = QGridLayout(phase_container)

            phase_label = QLabel('Phase Current')
            phase_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            phase_layout.addWidget(phase_label, 0, 0)

            phase_layout.addWidget(self.phase_value, 1, 0)
            
            self.current_module.addWidget(phase_container, 0, 1)

        def get_module(self):
            return self.current_module

def main():
    gui = DashboardGUI(sys.argv)
    gui.display()
    sys.exit(gui.execute())

if __name__ == '__main__':
    main()