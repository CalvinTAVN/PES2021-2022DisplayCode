#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import can
from datetime import datetime
from tkinter import *


class Display:
    def __init__(self, parent):
        self.parent = parent
        self.lowTemp = 0
        self.highTemp = 0
        self.avgTemp = 0
        self.packCurrent = 0
        self.packVoltage = 0
        self.lowCellVoltage = 0
        self.highCellVoltage = 0
        self.avgCellVoltage = 0
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d_%m_%Y,%H_%M_%S")
        self.can0 = can.interface.Bus(channel='can0', bustype='socketcan')
        self.count = 0

        # Configure Parent Frame
        self.parent.geometry("1024x600")
        self.parent.configure(bg='white', padx=5)
        self.parent.rowconfigure(0, pad=15)
        self.parent.rowconfigure(1, pad=20)
        self.parent.rowconfigure(2, pad=20)
        self.parent.title('PES Speedboat')

        # Configure Top Frame
        self.topFrame = Frame(self.parent, padx=14, pady=14, bg='white', highlightbackground="black",
                              highlightthickness=2)
        self.topFrame.place(anchor='center', relx=0.5, rely=0.25)
        self.topFrame.rowconfigure(0, pad=20)
        self.topFrame.columnconfigure(0, pad=40)
        self.topFrame.columnconfigure(1, pad=40)

        # Configure Middle Frame
        self.middleFrame = Frame(self.parent, padx=5, pady=5, bg='white', highlightbackground="black",
                                 highlightthickness=2)
        self.middleFrame.place(anchor='center', relx=0.5, rely=0.58)
        self.middleFrame.rowconfigure(0, pad=10)
        self.middleFrame.rowconfigure(1, pad=10)
        self.middleFrame.columnconfigure(0, pad=10)
        self.middleFrame.columnconfigure(1, pad=10)
        self.middleFrame.columnconfigure(2, pad=10)

        # Configure Bottom Frame
        self.bottomFrame = Frame(self.parent, padx=5, pady=5, bg='white', highlightbackground="black",
                                 highlightthickness=2)
        self.bottomFrame.place(anchor='center', relx=0.5, rely=0.82)
        self.bottomFrame.rowconfigure(0, pad=10)
        self.bottomFrame.rowconfigure(1, pad=10)
        self.bottomFrame.columnconfigure(0, pad=10)
        self.bottomFrame.columnconfigure(1, pad=10)
        self.bottomFrame.columnconfigure(2, pad=10)

        # Top Frame Labels
        self.highTempLabel = Label(self.topFrame, text="High Temp", font=('Verdana', 30), bg='white')
        self.highTempLabel.grid(row=0, column=0)

        self.highTempMeasure = Label(self.topFrame, text="0 for now", font=('Verdana', 70), bg='white')
        self.highTempMeasure.grid(row=1, column=0)

        self.packVoltageLabel = Label(self.topFrame, text="Pack Voltage", font=('Verdana', 30), bg='white')
        self.packVoltageLabel.grid(row=0, column=1)

        self.packVoltageMeasure = Label(self.topFrame, text="0 for now", font=('Verdana', 70), bg='white')
        self.packVoltageMeasure.grid(row=1, column=1)

        # Middle Frame Labels
        self.lowTempLabel = Label(self.middleFrame, text="Low Temp", font=('Verdana', 18), bg='white')
        self.lowTempLabel.grid(row=0, column=0)

        self.lowTempMeasure = Label(self.middleFrame, text="0 for now", font=('Verdana', 26), padx=25, bg='white')
        self.lowTempMeasure.grid(row=1, column=0)

        self.avgTempLabel = Label(self.middleFrame, text="Avg Temp", font=('Verdana', 16), bg='white')
        self.avgTempLabel.grid(row=0, column=1)

        self.avgTempMeasure = Label(self.middleFrame, text="0 for now", font=('Verdana', 26), padx=25, bg='white')
        self.avgTempMeasure.grid(row=1, column=1)

        self.packCurrentLabel = Label(self.middleFrame, text="Pack Current", font=('Verdana', 16), bg='white')
        self.packCurrentLabel.grid(row=0, column=2)

        self.packCurrentMeasure = Label(self.middleFrame, text="0 for now", font=('Verdana', 26), padx=25, bg='white')
        self.packCurrentMeasure.grid(row=1, column=2)

        # Bottom Frame Labels
        self.lowCellVoltageLabel = Label(self.bottomFrame, text="Low Cell Voltage", font=('Verdana', 16), bg='white')
        self.lowCellVoltageLabel.grid(row=0, column=0)

        self.lowCellVoltageMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 26), padx=20,
                                           bg='white')
        self.lowCellVoltageMeasure.grid(row=1, column=0)

        self.avgCellVoltageLabel = Label(self.bottomFrame, text="Avg Cell Voltage", font=('Verdana', 16), bg='white')
        self.avgCellVoltageLabel.grid(row=0, column=1)

        self.avgCellVoltageMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 26), padx=20,
                                           bg='white')
        self.avgCellVoltageMeasure.grid(row=1, column=1)

        self.highCellVoltageLabel = Label(self.bottomFrame, text="High Cell Voltage", font=('Verdana', 16), bg='white')
        self.highCellVoltageLabel.grid(row=0, column=2)

        self.highCellVoltageMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 26), padx=20,
                                            bg='white')
        self.highCellVoltageMeasure.grid(row=1, column=2)

        print(self.dt_string)
        self.new_file = open('/home/pes/dataInfo/' + self.dt_string, 'w')
        self.new_file.write(self.dt_string + "\n")
        self.new_file.write("Time   |lowTemp|highTemp|avgTemp|packCurrent|" +
                       "packVoltage|lowCellVoltage|highCellVoltage|avgCellVoltage\n")
        self.new_file.flush()

    def update_labels(self):
        try:
            currentTime = datetime.now()
            currentTimeString = currentTime.strftime("%M : %S")
            msg = self.can0.recv(3.0)
            if (msg != None):
                dataArray = msg.data
                if self.count % 1 == 5:
                    print('-----------------------------')
                    print('msg: ' + str(msg))
                    print('arb id: ' + str(msg.arbitration_id))
                    print('data: ' + str(msg.data))
                    print('-----------------------------')
                if (msg.arbitration_id == 1701):
                    self.avgTemp = dataArray[0]
                    self.lowTemp = dataArray[1]
                    self.highTemp = dataArray[2]
                    self.avgTempMeasure.config(text=str(self.avgTemp))
                    self.lowTempMeasure.config(text=str(self.lowTemp))
                    self.highTempMeasure.config(text=str(self.highTemp))
                    # avgV_lbl.config(text=str(value2)) Make Label for this
                if (msg.arbitration_id == 1702):
                    self.packCurrent = dataArray[0]
                    self.packVoltage = dataArray[1]
                    self.lowCellVoltage = dataArray[3]
                    self.highCellVoltage = dataArray[4]
                    self.avgCellVoltage = dataArray[5]
                    self.packCurrentMeasure.config(text=str(self.packCurrent))
                    self.packVoltageMeasure.config(text=str(self.packVoltage))
                    self.lowCellVoltageMeasure.config(text=str(self.lowCellVoltage))
                    self.highCellVoltageMeasure.config(text=str(self.highCellVoltage))
                    self.avgCellVoltageMeasure.config(text=str(self.avgCellVoltage))
                    # avgV_lbl.config(text=str(value3)) Make Label for this as well

                self.new_file.write(currentTimeString + "|  " + str(self.lowTemp) + "   |   " + str(self.highTemp) +
                                  "   |  " + str(self.avgTemp) + "   |     " + str(self.packCurrent) + "     |      " +
                                  str(self.packVoltage) + "     |      " + str(self.lowCellVoltage) + "      |      " +
                                  str(self.highCellVoltage) + "         |      " + str(self.avgCellVoltage) + "\n")
                self.new_file.flush()
                self.count += 1


        except TclError as ex:
            print(ex)
            self.new_file.write('End')
            self.new_file.flush()
        except Exception as ex:
            print(ex)

        self.parent.after(1000, self.update_labels)

    def on_closing(self):
        self.new_file.close()
        self.parent.destroy()

    def shutdown(self, channel):
        print("Shutting Down")
        global turnOffRaspberryPi
        turnOffRaspberryPi = True
        self.new_file.close()
        self.parent.destroy()


if __name__ == "__main__":
    # Can BUS Setup
    os.system("sudo ip link set can0 type can bitrate 500000")
    os.system("sudo ifconfig can0 up")

    # ShutDown Button Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Variable to activate the "turn off the raspberry pi
    turnOffRaspberryPi = False

    root = Tk()
    display = Display(root)
    display.update_labels()
    root.protocol("WM_DELETE_WINDOW", display.on_closing)
    GPIO.add_event_detect(4, GPIO.FALLING, callback=display.shutdown, bouncetime=2000)
    root.mainloop()

    # Turning off Raspberry Pi
    time.sleep(3)
    os.system("sudo ifconfig can0 down")
    if turnOffRaspberryPi:
        # print("Would of shutdown")
        os.system("sudo shutdown -h now")
