from DashboardGUI import DashboardGUI as GUI
import sys

def main():
    gui = GUI(sys.argv)
    gui.display()
    sys.exit(gui.execute())

if __name__ == '__main__':
    main()