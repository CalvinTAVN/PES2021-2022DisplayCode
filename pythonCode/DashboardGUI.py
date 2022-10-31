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

    def __init__(self):
        self.window = PyQt6.QtWidgets.QMainWindow()
        self.frame = PyQt6.QtWidgets.QFrame()
        self.layout = PyQt6.QtWidgets.QGridLayout()

        self.values = {}
        self.setup_gui()

    def setup_gui(self):
        ## Speed ##
        speed_module = PyQt6.QtWidgets.QGridLayout()

        # Speed #
        speed_layout = PyQt6.QtWidgets.QGridLayout()
        speed_label = PyQt6.QtWidgets.QLabel('Speed')
        speed_layout.addWidget(speed_label, 0, 0)
        self.values['speed'] = PyQt6.QtWidgets.QLabel()
        speed_layout.addWidget(self.values['speed'], 1, 0)

        speed_module.addLayout(speed_layout, 0, 0)

        # Rotations per minute #
        rpm_layout = PyQt6.QtWidgets.QGridLayout()
        rpm_label = PyQt6.QtWidgets.QLabel('RPM')
        rpm_layout.addWidget(rpm_label, 0, 0)
        self.values['rpm'] = PyQt6.QtWidgets.QLabel()
        rpm_layout.addWidget(self.values['rpm'], 1, 0)
        
        speed_module.addLayout(rpm_layout, 1, 0)

        self.layout.addLayout(speed_module, 0, 0, 2, 1)

        ## Controller ##
        controller_module = PyQt6.QtWidgets.QGridLayout()
        
        # Temperature #
        controller_layout = PyQt6.QtWidgets.QGridLayout()
        controller_label = PyQt6.QtWidgets.QLabel('Controller Temperature')
        controller_layout.addWidget(controller_label, 0, 0)
        self.values['controller_temperature'] = PyQt6.QtWidgets.QLabel()
        controller_layout.addWidget(self.values['controller_temperature'], 1, 0)

        controller_module.addLayout(controller_layout, 0, 0)

        self.layout.addLayout(controller_module, 0, 1)

        ## Motor ##
        motor_module = PyQt6.QtWidgets.QGridLayout()
        
        # Temperature #
        motor_layout = PyQt6.QtWidgets.QGridLayout()
        motor_label = PyQt6.QtWidgets.QLabel('Motor Temperature')
        motor_layout.addWidget(motor_label, 0, 0)
        self.values['motor_temperature'] = PyQt6.QtWidgets.QLabel()
        motor_layout.addWidget(self.values['motor_temperature'], 1, 0)

        motor_module.addLayout(motor_layout, 0, 0)

        self.layout.addLayout(motor_module, 1, 1)

        ### Battery ###
        battery_module = PyQt6.QtWidgets.QGridLayout()
        
        ## Cell 1 ##
        cell1_module = PyQt6.QtWidgets.QGridLayout()

        # Temperature #
        cell1_temperature_layout = PyQt6.QtWidgets.QGridLayout()
        cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 1 Temperature')
        cell1_temperature_layout.addWidget(cell_temperature_label, 0, 0)
        self.values['cell1_temperature'] = PyQt6.QtWidgets.QLabel()
        cell1_temperature_layout.addWidget(self.values['cell1_temperature'], 1, 0)

        cell1_module.addLayout(cell1_temperature_layout, 0, 0)

        # Voltage #
        cell1_voltage_layout = PyQt6.QtWidgets.QGridLayout()
        cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 1 Voltage')
        cell1_voltage_layout.addWidget(cell_voltage_label, 0, 0)
        self.values['cell1_voltage'] = PyQt6.QtWidgets.QLabel()
        cell1_voltage_layout.addWidget(self.values['cell1_voltage'], 1, 0)

        cell1_module.addLayout(cell1_voltage_layout, 0, 1)

        # Current #
        cell1_current_layout = PyQt6.QtWidgets.QGridLayout()
        cell_current_label = PyQt6.QtWidgets.QLabel('Cell 1 Current')
        cell1_current_layout.addWidget(cell_current_label, 0, 0)
        self.values['cell1_current'] = PyQt6.QtWidgets.QLabel()
        cell1_current_layout.addWidget(self.values['cell1_current'], 1, 0)

        cell1_module.addLayout(cell1_current_layout, 0, 2)

        battery_module.addLayout(cell1_module, 0, 0)

        ## Cell 2 ##
        cell2_module = PyQt6.QtWidgets.QGridLayout()

        # Temperature #
        cell2_temperature_layout = PyQt6.QtWidgets.QGridLayout()
        cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 2 Temperature')
        cell2_temperature_layout.addWidget(cell_temperature_label, 0, 0)
        self.values['cell2_temperature'] = PyQt6.QtWidgets.QLabel()
        cell2_temperature_layout.addWidget(self.values['cell2_temperature'], 1, 0)

        cell2_module.addLayout(cell2_temperature_layout, 0, 0)

        # Voltage #
        cell2_voltage_layout = PyQt6.QtWidgets.QGridLayout()
        cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 2 Voltage')
        cell2_voltage_layout.addWidget(cell_voltage_label, 0, 0)
        self.values['cell2_voltage'] = PyQt6.QtWidgets.QLabel()
        cell2_voltage_layout.addWidget(self.values['cell2_voltage'], 1, 0)

        cell2_module.addLayout(cell2_voltage_layout, 0, 1)

        # Current #
        cell2_current_layout = PyQt6.QtWidgets.QGridLayout()
        cell_current_label = PyQt6.QtWidgets.QLabel('Cell 2 Current')
        cell2_current_layout.addWidget(cell_current_label, 0, 0)
        self.values['cell2_current'] = PyQt6.QtWidgets.QLabel()
        cell2_current_layout.addWidget(self.values['cell2_current'], 1, 0)

        cell2_module.addLayout(cell2_current_layout, 0, 2)

        battery_module.addLayout(cell2_module, 1, 0)

        ## Cell 3 ##
        cell3_module = PyQt6.QtWidgets.QGridLayout()

        # Temperature #
        cell3_temperature_layout = PyQt6.QtWidgets.QGridLayout()
        cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 3 Temperature')
        cell3_temperature_layout.addWidget(cell_temperature_label, 0, 0)
        self.values['cell3_temperature'] = PyQt6.QtWidgets.QLabel()
        cell3_temperature_layout.addWidget(self.values['cell3_temperature'], 1, 0)

        cell3_module.addLayout(cell3_temperature_layout, 0, 0)

        # Voltage #
        cell3_voltage_layout = PyQt6.QtWidgets.QGridLayout()
        cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 3 Voltage')
        cell3_voltage_layout.addWidget(cell_voltage_label, 0, 0)
        self.values['cell3_voltage'] = PyQt6.QtWidgets.QLabel()
        cell3_voltage_layout.addWidget(self.values['cell3_voltage'], 1, 0)

        cell3_module.addLayout(cell3_voltage_layout, 0, 1)

        # Current #
        cell3_current_layout = PyQt6.QtWidgets.QGridLayout()
        cell_current_label = PyQt6.QtWidgets.QLabel('Cell 3 Current')
        cell3_current_layout.addWidget(cell_current_label, 0, 0)
        self.values['cell3_current'] = PyQt6.QtWidgets.QLabel()
        cell3_current_layout.addWidget(self.values['cell3_current'], 1, 0)

        cell3_module.addLayout(cell3_current_layout, 0, 2)

        battery_module.addLayout(cell3_module, 2, 0)

        ## Cell 4 ##
        cell4_module = PyQt6.QtWidgets.QGridLayout()

        # Temperature #
        cell4_temperature_layout = PyQt6.QtWidgets.QGridLayout()
        cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 4 Temperature')
        cell4_temperature_layout.addWidget(cell_temperature_label, 0, 0)
        self.values['cell4_temperature'] = PyQt6.QtWidgets.QLabel()
        cell4_temperature_layout.addWidget(self.values['cell4_temperature'], 1, 0)

        cell4_module.addLayout(cell4_temperature_layout, 0, 0)

        # Voltage #
        cell4_voltage_layout = PyQt6.QtWidgets.QGridLayout()
        cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 4 Voltage')
        cell4_voltage_layout.addWidget(cell_voltage_label, 0, 0)
        self.values['cell4_voltage'] = PyQt6.QtWidgets.QLabel()
        cell4_voltage_layout.addWidget(self.values['cell4_voltage'], 1, 0)

        cell4_module.addLayout(cell4_voltage_layout, 0, 1)

        # Current #
        cell4_current_layout = PyQt6.QtWidgets.QGridLayout()
        cell_current_label = PyQt6.QtWidgets.QLabel('Cell 4 Current')
        cell4_current_layout.addWidget(cell_current_label, 0, 0)
        self.values['cell4_current'] = PyQt6.QtWidgets.QLabel()
        cell4_current_layout.addWidget(self.values['cell4_current'], 1, 0)

        cell4_module.addLayout(cell4_current_layout, 0, 2)

        battery_module.addLayout(cell4_module, 3, 0)

        ## Cell 5 ##
        cell5_module = PyQt6.QtWidgets.QGridLayout()

        # Temperature #
        cell5_temperature_layout = PyQt6.QtWidgets.QGridLayout()
        cell_temperature_label = PyQt6.QtWidgets.QLabel('Cell 5 Temperature')
        cell5_temperature_layout.addWidget(cell_temperature_label, 0, 0)
        self.values['cell5_temperature'] = PyQt6.QtWidgets.QLabel()
        cell5_temperature_layout.addWidget(self.values['cell5_temperature'], 1, 0)

        cell5_module.addLayout(cell5_temperature_layout, 0, 0)

        # Voltage #
        cell5_voltage_layout = PyQt6.QtWidgets.QGridLayout()
        cell_voltage_label = PyQt6.QtWidgets.QLabel('Cell 5 Voltage')
        cell5_voltage_layout.addWidget(cell_voltage_label, 0, 0)
        self.values['cell5_voltage'] = PyQt6.QtWidgets.QLabel()
        cell5_voltage_layout.addWidget(self.values['cell5_voltage'], 1, 0)

        cell5_module.addLayout(cell5_voltage_layout, 0, 1)

        # Current #
        cell5_current_layout = PyQt6.QtWidgets.QGridLayout()
        cell_current_label = PyQt6.QtWidgets.QLabel('Cell 5 Current')
        cell5_current_layout.addWidget(cell_current_label, 0, 0)
        self.values['cell5_current'] = PyQt6.QtWidgets.QLabel()
        cell5_current_layout.addWidget(self.values['cell5_current'], 1, 0)

        cell5_module.addLayout(cell5_current_layout, 0, 2)

        battery_module.addLayout(cell5_module, 4, 0)

        self.layout.addLayout(battery_module, 0, 2, 2, 1)


        ### Global ###
        self.frame.setLayout(self.layout)
        self.window.setCentralWidget(self.frame) 

    def display(self):
        self.window.show()
    
    def edit_widget(self, key, label):
        self.values[key].setText(label)
        
def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    gui = DashboardGUI()
    gui.display()

    def update_labels():
        gui.edit_widget('speed', str(0))
        gui.edit_widget('rpm', str(0))
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

    timer = PyQt6.QtCore.QTimer()
    timer.timeout.connect(update_labels)
    timer.start(10)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()