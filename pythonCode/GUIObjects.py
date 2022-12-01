from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class ValueContainer:
    
    def __init__(self, args):
        self.values = {}
        self.frame = QFrame()
        self.layout = QGridLayout()
        self.setup_gui()

def main():
    pass

if __name__ == '__main__':
    main()