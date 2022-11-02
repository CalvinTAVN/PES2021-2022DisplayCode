from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class DashboardGUI:

    def __init__(self, numCells):
        self.window = QMainWindow()
        self.frame = QFrame()
        self.layout = QGridLayout()
        self.speed_module = self.SpeedModule(self)
        self.controller_module = self.ControllerModule()
        self.motor_module = self.MotorModule()
        self.battery_module = self.BatteryModule(numCells)
        self.setup_gui()

    def setup_gui(self):
        self.window.setWindowTitle('Dashboard GUI')

        self.layout.addLayout(self.speed_module.get_module(), 0, 0, 2, 1)
        self.layout.addLayout(self.controller_module.get_module(), 0, 1)
        self.layout.addLayout(self.motor_module.get_module(), 1, 1)
        self.layout.addLayout(self.battery_module.get_module(), 0, 2, 2, 1)

        self.frame.setLayout(self.layout)

        self.window.setCentralWidget(self.frame) 

    def display(self):
        self.window.show()
    
    def setColor(self, widget, colorRole, color):
        palette = widget.palette()
        palette.setColor(colorRole, color)
        widget.setPalette(palette)

    class SpeedModule:
        def __init__(self, gui):
            self.gui = gui
            self.speed_module = QGridLayout()
            self.mph_value = QLabel()
            self.rpm_value = QLabel()
            self.knots_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            mph_container = QWidget()
            mph_container.setAutoFillBackground(True)
            self.gui.setColor(mph_container, mph_container.backgroundRole(), QColor(0, 0, 0))

            mph_layout = QGridLayout(mph_container)

            mph_label = QLabel('MPH')
            mph_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gui.setColor(mph_label, mph_label.foregroundRole(), QColor(255, 255, 255))
            mph_layout.addWidget(mph_label, 0, 0)

            mph_layout.addWidget(self.mph_value, 1, 0)

            self.speed_module.addWidget(mph_container, 0, 0, 1, 2)

            rpm_container = QWidget()
            rpm_container.setAutoFillBackground(True)
            self.gui.setColor(rpm_container, rpm_container.backgroundRole(), QColor(0, 0, 0))

            rpm_layout = QGridLayout(rpm_container)
            rpm_label = QLabel('RPM')
            rpm_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gui.setColor(rpm_label, rpm_label.foregroundRole(), QColor(255, 255, 255))
            rpm_layout.addWidget(rpm_label, 0, 0)

            rpm_layout.addWidget(self.rpm_value, 1, 0)
            
            self.speed_module.addWidget(rpm_container, 1, 0)
            
            knots_container = QWidget()
            knots_container.setAutoFillBackground(True)
            self.gui.setColor(knots_container, knots_container.backgroundRole(), QColor(0, 0, 0))

            knots_layout = QGridLayout(knots_container)
            knots_label = QLabel('Knots')
            knots_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gui.setColor(knots_label, knots_label.foregroundRole(), QColor(255, 255, 255))
            knots_layout.addWidget(knots_label, 0, 0)

            knots_layout.addWidget(self.knots_value, 1, 0)

            self.speed_module.addWidget(knots_container, 1, 1)

        def get_module(self):
            return self.speed_module

    class ControllerModule:

        def __init__(self):
            ## Controller ##
            self.controller_module = QGridLayout()

            # Temperature #
            temperature_layout = QGridLayout()
            temperature_label = QLabel('Controller Temperature')
            temperature_layout.addWidget(temperature_label, 0, 0)
            self.temperature_value = QLabel()
            temperature_layout.addWidget(self.temperature_value, 1, 0)

            self.controller_module.addLayout(temperature_layout, 0, 0)
        
        def get_module(self):
            return self.controller_module

    class MotorModule:

        def __init__(self):
            ## Motor ##
            self.motor_module = QGridLayout()
            
            # Temperature #
            temperature_layout = QGridLayout()
            temperature_label = QLabel('Motor Temperature')
            temperature_layout.addWidget(temperature_label, 0, 0)
            self.temperature_value = QLabel()
            temperature_layout.addWidget(self.temperature_value, 1, 0)

            self.motor_module.addLayout(temperature_layout, 0, 0)

        def get_module(self):
            return self.motor_module        

    class BatteryModule:
        
        def __init__(self, numCells):
            ### Battery ###
            self.battery_module = QGridLayout()
            self.cell_modules = []
            for cell in range(numCells):
                self.cell_modules.append(self.CellModule())
            self.setup_module()
        
        def setup_module(self):
            for cell in range(len(self.cell_modules)):
                self.battery_module.addLayout(self.cell_modules[cell].get_module(), cell, 0)
        
        def get_module(self):
            return self.battery_module

        class CellModule:

            def __init__(self):
                ## Cell ##
                self.cell_module = QGridLayout()

                # Temperature #
                temperature_layout = QGridLayout()
                temperature_label = QLabel('Cell Temperature')
                temperature_layout.addWidget(temperature_label, 0, 0)
                self.temperature_value = QLabel()
                temperature_layout.addWidget(self.temperature_value, 1, 0)

                self.cell_module.addLayout(temperature_layout, 0, 0)

                # Voltage #
                voltage_layout = QGridLayout()
                voltage_label = QLabel('Cell Voltage')
                voltage_layout.addWidget(voltage_label, 0, 0)
                self.voltage_value = QLabel()
                voltage_layout.addWidget(self.voltage_value, 1, 0)

                self.cell_module.addLayout(voltage_layout, 0, 1)

                # Current #
                current_layout = QGridLayout()
                current_label = QLabel('Cell  Current')
                current_layout.addWidget(current_label, 0, 0)
                self.current_value = QLabel()
                current_layout.addWidget(self.current_value, 1, 0)

                self.cell_module.addLayout(current_layout, 0, 2)

            def get_module(self):
                return self.cell_module

def main():
    NUM_CELLS = 5
    app = QApplication(sys.argv)
    gui = DashboardGUI(NUM_CELLS)
    gui.display()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()