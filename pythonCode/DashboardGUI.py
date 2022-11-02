import PyQt6
import PyQt6.QtWidgets
import PyQt6.QtCore
import sys

NUM_CELLS = 5

class DashboardGUI:

    def __init__(self, values, numCells):
        self.window = PyQt6.QtWidgets.QMainWindow()
        self.frame = PyQt6.QtWidgets.QFrame()
        self.layout = PyQt6.QtWidgets.QGridLayout()
        self.update_values(values)
        self.speed_module = self.SpeedModule()
        self.controller_module = self.ControllerModule()
        self.motor_module = self.MotorModule()
        self.battery_module = self.BatteryModule(numCells)
        self.setup_gui()

    def setup_gui(self):
        self.layout.addLayout(self.speed_module.get_module(), 0, 0, 2, 1)
        self.layout.addLayout(self.controller_module.get_module(), 0, 1)
        self.layout.addLayout(self.motor_module.get_module(), 1, 1)
        self.layout.addLayout(self.battery_module.get_module(), 0, 2, 2, 1)
        self.frame.setLayout(self.layout)
        self.window.setCentralWidget(self.frame) 

    def display(self):
        self.window.show()
    
    def update_values(self, values):
        

    class SpeedModule:
        
        def __init__(self, values):
            ## Speed ##
            self.speed_module = PyQt6.QtWidgets.QGridLayout()

            # MPH #
            mph_layout = PyQt6.QtWidgets.QGridLayout()
            mph_label = PyQt6.QtWidgets.QLabel('MPH')
            mph_layout.addWidget(mph_label, 0, 0)
            values['mph'] = PyQt6.QtWidgets.QLabel()
            mph_layout.addWidget(values['mph'], 1, 0)

            self.speed_module.addLayout(mph_layout, 0, 0)

            # Rotations per minute #
            rpm_layout = PyQt6.QtWidgets.QGridLayout()
            rpm_label = PyQt6.QtWidgets.QLabel('RPM')
            rpm_layout.addWidget(rpm_label, 0, 0)
            values['rpm'] = PyQt6.QtWidgets.QLabel()
            rpm_layout.addWidget(values['rpm'], 1, 0)
            
            self.speed_module.addLayout(rpm_layout, 1, 0)

            # Knots #
            knots_layout = PyQt6.QtWidgets.QGridLayout()
            knots_label = PyQt6.QtWidgets.QLabel('Knots')
            knots_layout.addWidget(knots_label, 0, 0)
            values['knots'] = PyQt6.QtWidgets.QLabel()
            knots_layout.addWidget(values['knots'], 1, 0)

            self.speed_module.addLayout(knots_layout, 2, 0)
        
        def get_module(self):
            return self.speed_module

    class ControllerModule:

        def __init__(self, values):
            ## Controller ##
            self.controller_module = PyQt6.QtWidgets.QGridLayout()
            
            # Temperature #
            controller_layout = PyQt6.QtWidgets.QGridLayout()
            controller_label = PyQt6.QtWidgets.QLabel('Controller Temperature')
            controller_layout.addWidget(controller_label, 0, 0)
            values['controller_temperature'] = PyQt6.QtWidgets.QLabel()
            controller_layout.addWidget(values['controller_temperature'], 1, 0)

            self.controller_module.addLayout(controller_layout, 0, 0)
        
        def get_module(self):
            return self.controller_module

    class MotorModule:

        def __init__(self, values):
            ## Motor ##
            self.motor_module = PyQt6.QtWidgets.QGridLayout()
            
            # Temperature #
            motor_layout = PyQt6.QtWidgets.QGridLayout()
            motor_label = PyQt6.QtWidgets.QLabel('Motor Temperature')
            motor_layout.addWidget(motor_label, 0, 0)
            values['motor_temperature'] = PyQt6.QtWidgets.QLabel()
            motor_layout.addWidget(values['motor_temperature'], 1, 0)

            self.motor_module.addLayout(motor_layout, 0, 0)

        def get_module(self):
            return self.motor_module        

    class BatteryModule:
        
        def __init__(self, values):
            ### Battery ###
            self.battery_module = PyQt6.QtWidgets.QGridLayout()
            self.cell1_module = self.CellModule(values).get_module()
            self.cell2_module = self.CellModule(values).get_module()
            self.cell3_module = self.CellModule(values).get_module()
            self.cell4_module = self.CellModule(values).get_module()
            self.cell5_module = self.CellModule(values).get_module()
            self.cell_stats_module = self.CellModule(values).get_module()
            self.setup_module()
        
        def setup_module(self):
            self.battery_module.addLayout(self.cell1_module, 0, 0)
            self.battery_module.addLayout(self.cell2_module, 1, 0)
            self.battery_module.addLayout(self.cell3_module, 2, 0)
            self.battery_module.addLayout(self.cell4_module, 3, 0)
            self.battery_module.addLayout(self.cell5_module, 4, 0)
            self.battery_module.addLayout(self.cell_stats_module, 5, 0)
        
        def get_module(self):
            return self.battery_module

        class CellModule:

            def __init__(self, values):
                ## Cell ##
                self.cell_module = PyQt6.QtWidgets.QGridLayout()

                # Temperature #
                cell_temperature_layout = PyQt6.QtWidgets.QGridLayout()
                cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 1 Temperature')
                cell_temperature_layout.addWidget(cell_temperature_label, 0, 0)
                values['cell_temperature'] = PyQt6.QtWidgets.QLabel()
                cell_temperature_layout.addWidget(values['cell_temperature'], 1, 0)

                self.cell_module.addLayout(cell_temperature_layout, 0, 0)

                # Voltage #
                cell_voltage_layout = PyQt6.QtWidgets.QGridLayout()
                cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 1 Voltage')
                cell_voltage_layout.addWidget(cell_voltage_label, 0, 0)
                values['cell_voltage'] = PyQt6.QtWidgets.QLabel()
                cell_voltage_layout.addWidget(values['cell_voltage'], 1, 0)

                self.cell_module.addLayout(cell_voltage_layout, 0, 1)

                # Current #
                cell_current_layout = PyQt6.QtWidgets.QGridLayout()
                cell_current_label = PyQt6.QtWidgets.QLabel('Cell  Current')
                cell_current_layout.addWidget(cell_current_label, 0, 0)
                values['cell_current'] = PyQt6.QtWidgets.QLabel()
                cell_current_layout.addWidget(values['cell_current'], 1, 0)

                self.cell_module.addLayout(cell_current_layout, 0, 2)

            def get_module(self):
                return self.cell_module

def main():
    values = {}
    values['mph'] = 0
    values['rpm'] = 0
    values['knots'] = 0
    values['controller_temperature'] = 0
    values['motor_temperature'] = 0
    for i in range(NUM_CELLS):
        values['cell' + str(i)] = {}
        values['cell' + str(i)]['temperature'] = 0
        values['cell' + str(i)]['voltage'] = 0
        values['cell' + str(i)]['current'] = 0

    app = PyQt6.QtWidgets.QApplication(sys.argv)
    gui = DashboardGUI(values, NUM_CELLS)
    gui.display()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()