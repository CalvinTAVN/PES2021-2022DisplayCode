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
        self.controller_module = self.ControllerModule(self)
        self.motor_module = self.MotorModule(self)
        self.battery_module = self.BatteryModule(self, numCells)
        self.setup_gui()

    def setup_gui(self):
        self.window.setWindowTitle('Dashboard GUI')

        self.layout.addLayout(self.speed_module.get_module(), 0, 0)
        self.layout.addLayout(self.controller_module.get_module(), 1, 0)
        self.layout.addLayout(self.motor_module.get_module(), 1, 1)
        self.layout.addLayout(self.battery_module.get_module(), 0, 1)

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

        def __init__(self, gui):
            self.gui = gui
            self.controller_module = QGridLayout()
            self.temperature_value = QLabel()
            self.setup_module()
        
        def setup_module(self):
            temperature_container = QWidget()
            temperature_container.setAutoFillBackground(True)
            self.gui.setColor(temperature_container, temperature_container.backgroundRole(), QColor(0, 0, 0))

            temperature_layout = QGridLayout(temperature_container)
            temperature_label = QLabel('Controller Temperature')
            temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gui.setColor(temperature_label, temperature_label.foregroundRole(), QColor(255, 255, 255))
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
            temperature_container = QWidget()
            temperature_container.setAutoFillBackground(True)
            self.gui.setColor(temperature_container, temperature_container.backgroundRole(), QColor(0, 0, 0))

            temperature_layout = QGridLayout(temperature_container)
            temperature_label = QLabel('Motor Temperature')
            temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gui.setColor(temperature_label, temperature_label.foregroundRole(), QColor(255, 255, 255))
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
            self.setup_module()
        
        def setup_module(self):
            for cell in range(self.numCells):
                self.cell_modules.append(self.CellModule(self.gui))
                self.battery_module.addLayout(self.cell_modules[cell].get_module(), cell, 0)
        
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
                cell_container = QWidget()
                cell_container.setAutoFillBackground(True)
                self.gui.setColor(cell_container, cell_container.backgroundRole(), QColor(0, 0, 0))

                cell_layout = QGridLayout(cell_container)

                temperature_container = QWidget()
                temperature_container.setAutoFillBackground(True)
                self.gui.setColor(temperature_container, temperature_container.backgroundRole(), QColor(0, 255, 0))

                cell_layout.addWidget(temperature_container, 0, 0)

                voltage_container = QWidget()
                voltage_container.setAutoFillBackground(True)
                self.gui.setColor(voltage_container, voltage_container.backgroundRole(), QColor(0, 255, 0))

                cell_layout.addWidget(voltage_container, 0, 1)

                current_container = QWidget()
                current_container.setAutoFillBackground(True)
                self.gui.setColor(current_container, current_container.backgroundRole(), QColor(0, 255, 0))

                cell_layout.addWidget(current_container, 0, 2)

                self.cell_module.addWidget(cell_container)

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