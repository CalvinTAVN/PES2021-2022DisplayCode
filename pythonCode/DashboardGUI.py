import PyQt6
import PyQt6.QtWidgets
import PyQt6.QtCore
import sys

'''
Battery box - bms, motor controller
battery temperature, motor, motor controller
battery current, motor controller current (phase current)
battery voltage (individual, total pack, lowest cell)
'''

class DashboardGUI:

    def __init__(self, values):
        self.window = PyQt6.QtWidgets.QMainWindow()
        self.frame = PyQt6.QtWidgets.QFrame()
        self.layout = PyQt6.QtWidgets.QGridLayout()
        self.values = values
        self.speed_module = self.SpeedModule(self.values).get_module()
        self.controller_module = self.ControllerModule(self.values).get_module()
        self.motor_module = self.MotorModule(self.values).get_module()
        self.battery_module = self.BatteryModule(self.values).get_module()
        self.setup_gui()

    def setup_gui(self):
        self.layout.addLayout(self.speed_module, 0, 0, 2, 1)

        self.layout.addLayout(self.controller_module, 0, 1)

        self.layout.addLayout(self.motor_module, 1, 1)

        self.layout.addLayout(self.battery_module, 0, 2, 2, 1)

        self.frame.setLayout(self.layout)
        self.window.setCentralWidget(self.frame) 

    def display(self):
        self.window.show()
    
    def edit_widget(self, key, label):
        self.values[key].setText(label)

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
            
            ## Cell 1 ##
            cell1_module = PyQt6.QtWidgets.QGridLayout()

            # Temperature #
            cell1_temperature_layout = PyQt6.QtWidgets.QGridLayout()
            cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 1 Temperature')
            cell1_temperature_layout.addWidget(cell_temperature_label, 0, 0)
            values['cell1_temperature'] = PyQt6.QtWidgets.QLabel()
            cell1_temperature_layout.addWidget(values['cell1_temperature'], 1, 0)

            cell1_module.addLayout(cell1_temperature_layout, 0, 0)

            # Voltage #
            cell1_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 1 Voltage')
            cell1_voltage_layout.addWidget(cell_voltage_label, 0, 0)
            values['cell1_voltage'] = PyQt6.QtWidgets.QLabel()
            cell1_voltage_layout.addWidget(values['cell1_voltage'], 1, 0)

            cell1_module.addLayout(cell1_voltage_layout, 0, 1)

            # Current #
            cell1_current_layout = PyQt6.QtWidgets.QGridLayout()
            cell_current_label = PyQt6.QtWidgets.QLabel('Cell 1 Current')
            cell1_current_layout.addWidget(cell_current_label, 0, 0)
            values['cell1_current'] = PyQt6.QtWidgets.QLabel()
            cell1_current_layout.addWidget(values['cell1_current'], 1, 0)

            cell1_module.addLayout(cell1_current_layout, 0, 2)

            self.battery_module.addLayout(cell1_module, 0, 0)

            ## Cell 2 ##
            cell2_module = PyQt6.QtWidgets.QGridLayout()

            # Temperature #
            cell2_temperature_layout = PyQt6.QtWidgets.QGridLayout()
            cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 2 Temperature')
            cell2_temperature_layout.addWidget(cell_temperature_label, 0, 0)
            values['cell2_temperature'] = PyQt6.QtWidgets.QLabel()
            cell2_temperature_layout.addWidget(values['cell2_temperature'], 1, 0)

            cell2_module.addLayout(cell2_temperature_layout, 0, 0)

            # Voltage #
            cell2_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 2 Voltage')
            cell2_voltage_layout.addWidget(cell_voltage_label, 0, 0)
            values['cell2_voltage'] = PyQt6.QtWidgets.QLabel()
            cell2_voltage_layout.addWidget(values['cell2_voltage'], 1, 0)

            cell2_module.addLayout(cell2_voltage_layout, 0, 1)

            # Current #
            cell2_current_layout = PyQt6.QtWidgets.QGridLayout()
            cell_current_label = PyQt6.QtWidgets.QLabel('Cell 2 Current')
            cell2_current_layout.addWidget(cell_current_label, 0, 0)
            values['cell2_current'] = PyQt6.QtWidgets.QLabel()
            cell2_current_layout.addWidget(values['cell2_current'], 1, 0)

            cell2_module.addLayout(cell2_current_layout, 0, 2)

            self.battery_module.addLayout(cell2_module, 1, 0)

            ## Cell 3 ##
            cell3_module = PyQt6.QtWidgets.QGridLayout()

            # Temperature #
            cell3_temperature_layout = PyQt6.QtWidgets.QGridLayout()
            cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 3 Temperature')
            cell3_temperature_layout.addWidget(cell_temperature_label, 0, 0)
            values['cell3_temperature'] = PyQt6.QtWidgets.QLabel()
            cell3_temperature_layout.addWidget(values['cell3_temperature'], 1, 0)

            cell3_module.addLayout(cell3_temperature_layout, 0, 0)

            # Voltage #
            cell3_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 3 Voltage')
            cell3_voltage_layout.addWidget(cell_voltage_label, 0, 0)
            values['cell3_voltage'] = PyQt6.QtWidgets.QLabel()
            cell3_voltage_layout.addWidget(values['cell3_voltage'], 1, 0)

            cell3_module.addLayout(cell3_voltage_layout, 0, 1)

            # Current #
            cell3_current_layout = PyQt6.QtWidgets.QGridLayout()
            cell_current_label = PyQt6.QtWidgets.QLabel('Cell 3 Current')
            cell3_current_layout.addWidget(cell_current_label, 0, 0)
            values['cell3_current'] = PyQt6.QtWidgets.QLabel()
            cell3_current_layout.addWidget(values['cell3_current'], 1, 0)

            cell3_module.addLayout(cell3_current_layout, 0, 2)

            self.battery_module.addLayout(cell3_module, 2, 0)

            ## Cell 4 ##
            cell4_module = PyQt6.QtWidgets.QGridLayout()

            # Temperature #
            cell4_temperature_layout = PyQt6.QtWidgets.QGridLayout()
            cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 4 Temperature')
            cell4_temperature_layout.addWidget(cell_temperature_label, 0, 0)
            values['cell4_temperature'] = PyQt6.QtWidgets.QLabel()
            cell4_temperature_layout.addWidget(values['cell4_temperature'], 1, 0)

            cell4_module.addLayout(cell4_temperature_layout, 0, 0)

            # Voltage #
            cell4_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 4 Voltage')
            cell4_voltage_layout.addWidget(cell_voltage_label, 0, 0)
            values['cell4_voltage'] = PyQt6.QtWidgets.QLabel()
            cell4_voltage_layout.addWidget(values['cell4_voltage'], 1, 0)

            cell4_module.addLayout(cell4_voltage_layout, 0, 1)

            # Current #
            cell4_current_layout = PyQt6.QtWidgets.QGridLayout()
            cell_current_label = PyQt6.QtWidgets.QLabel('Cell 4 Current')
            cell4_current_layout.addWidget(cell_current_label, 0, 0)
            values['cell4_current'] = PyQt6.QtWidgets.QLabel()
            cell4_current_layout.addWidget(values['cell4_current'], 1, 0)

            cell4_module.addLayout(cell4_current_layout, 0, 2)

            self.battery_module.addLayout(cell4_module, 3, 0)

            ## Cell 5 ##
            cell5_module = PyQt6.QtWidgets.QGridLayout()

            # Temperature #
            cell5_temperature_layout = PyQt6.QtWidgets.QGridLayout()
            cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 5 Temperature')
            cell5_temperature_layout.addWidget(cell_temperature_label, 0, 0)
            values['cell5_temperature'] = PyQt6.QtWidgets.QLabel()
            cell5_temperature_layout.addWidget(values['cell5_temperature'], 1, 0)

            cell5_module.addLayout(cell5_temperature_layout, 0, 0)

            # Voltage #
            cell5_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 5 Voltage')
            cell5_voltage_layout.addWidget(cell_voltage_label, 0, 0)
            values['cell5_voltage'] = PyQt6.QtWidgets.QLabel()
            cell5_voltage_layout.addWidget(values['cell5_voltage'], 1, 0)

            cell5_module.addLayout(cell5_voltage_layout, 0, 1)

            # Current #
            cell5_current_layout = PyQt6.QtWidgets.QGridLayout()
            cell_current_label = PyQt6.QtWidgets.QLabel('Cell 5 Current')
            cell5_current_layout.addWidget(cell_current_label, 0, 0)
            values['cell5_current'] = PyQt6.QtWidgets.QLabel()
            cell5_current_layout.addWidget(values['cell5_current'], 1, 0)

            cell5_module.addLayout(cell5_current_layout, 0, 2)

            self.battery_module.addLayout(cell5_module, 4, 0)

            ## Cell Stats ##
            cell_stats_module = PyQt6.QtWidgets.QGridLayout()

            # Lowest Voltage #
            lowest_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            lowest_voltage_label = PyQt6.QtWidgets.QLabel('Lowest Voltage')
            lowest_voltage_layout.addWidget(lowest_voltage_label, 0, 0)
            values['lowest_voltage'] = PyQt6.QtWidgets.QLabel()
            lowest_voltage_layout.addWidget(values['lowest_voltage'], 1, 0)

            cell_stats_module.addLayout(lowest_voltage_layout, 0, 0)

            # Average Voltage #
            average_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            average_voltage_label = PyQt6.QtWidgets.QLabel('Average Voltage')
            average_voltage_layout.addWidget(average_voltage_label, 0, 0)
            values['average_voltage'] = PyQt6.QtWidgets.QLabel()
            average_voltage_layout.addWidget(values['average_voltage'], 1, 0)

            cell_stats_module.addLayout(average_voltage_layout, 0, 1)

            # Highest Voltage #
            highest_voltage_layout = PyQt6.QtWidgets.QGridLayout()
            highest_voltage_label = PyQt6.QtWidgets.QLabel('Highest Voltage')
            highest_voltage_layout.addWidget(highest_voltage_label, 0, 0)
            values['highest_voltage'] = PyQt6.QtWidgets.QLabel()
            highest_voltage_layout.addWidget(values['highest_voltage'], 1, 0)

            cell_stats_module.addLayout(highest_voltage_layout, 0, 2)

            self.battery_module.addLayout(cell_stats_module, 5, 0)
        
        def get_module(self):
            return self.battery_module

def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    gui = DashboardGUI({})
    gui.display()

    def update_labels():
        gui.edit_widget('mph', str(0))
        gui.edit_widget('rpm', str(0))
        gui.edit_widget('knots', str(0))
        gui.edit_widget('controller_temperature', str(0))
        gui.edit_widget('motor_temperature', str(0))
        gui.edit_widget('cell1_temperature', str(0))
        gui.edit_widget('cell1_voltage', str(0))
        gui.edit_widget('cell1_current', str(0))
        gui.edit_widget('cell2_temperature', str(0))
        gui.edit_widget('cell2_voltage', str(0))
        gui.edit_widget('cell2_current', str(0))
        gui.edit_widget('cell3_temperature', str(0))
        gui.edit_widget('cell3_voltage', str(0))
        gui.edit_widget('cell3_current', str(0))
        gui.edit_widget('cell4_temperature', str(0))
        gui.edit_widget('cell4_voltage', str(0))
        gui.edit_widget('cell4_current', str(0))
        gui.edit_widget('cell5_temperature', str(0))
        gui.edit_widget('cell5_voltage', str(0))
        gui.edit_widget('cell5_current', str(0))
        gui.edit_widget('lowest_voltage', str(0))
        gui.edit_widget('average_voltage', str(0))
        gui.edit_widget('highest_voltage', str(0))

    timer = PyQt6.QtCore.QTimer()
    timer.timeout.connect(update_labels)
    timer.start(10)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()