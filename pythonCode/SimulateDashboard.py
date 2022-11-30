from DashboardGUI import DashboardGUI as GUI
import sys

def main():
    gui = GUI(sys.argv)
    gui.display()

    new_values = {}
    new_values['mph'] = 0
    new_values['rpm'] = 1
    gui.edit_values(new_values)

    sys.exit(gui.execute())

if __name__ == '__main__':
    main()