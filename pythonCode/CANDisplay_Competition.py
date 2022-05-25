#!/usr/bin/python
# import RPi.GPIO as GPIO
import time
import os
import can
from datetime import datetime
from tkinter import *
from random import randint


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
        self.fg = 'black'
        self.bg = 'white'
        self.count = 1000

        # Configure Parent Frame
        self.parent.geometry("1024x600")
        self.parent.configure(bg=self.bg, padx=5)
        self.parent.rowconfigure(0, pad=15)
        self.parent.rowconfigure(1, pad=20)
        self.parent.rowconfigure(2, pad=20)
        self.parent.title('PES Speedboat')

        # Configure Top Frame
        self.topFrame = Frame(self.parent, bg=self.bg, highlightbackground=self.fg,
                              highlightthickness=2, width=900, height=225)
        self.topFrame.grid_propagate(False)
        self.topFrame.place(anchor='center', relx=0.5, rely=0.25)
        self.topFrame.rowconfigure(0, pad=20)
        self.topFrame.columnconfigure(0, pad=40)
        self.topFrame.columnconfigure(1, pad=40)

        # Configure Middle Frame
        self.middleFrame = Frame(self.parent, padx=5, pady=5, bg=self.bg, highlightbackground=self.fg,
                                 highlightthickness=2, width=700, height=125)
        # self.middleFrame.grid_propagate(False)
        self.middleFrame.place(anchor='center', relx=0.5, rely=0.58)
        self.middleFrame.rowconfigure(0, pad=10)
        self.middleFrame.rowconfigure(1, pad=10)
        self.middleFrame.columnconfigure(0, pad=10)
        self.middleFrame.columnconfigure(1, pad=10)
        self.middleFrame.columnconfigure(2, pad=10)

        # Configure Bottom Frame
        self.bottomFrame = Frame(self.parent, padx=5, pady=5, bg=self.bg, highlightbackground=self.fg,
                                 highlightthickness=2, width=700, height=125)
        self.bottomFrame.grid_propagate(False)
        self.bottomFrame.place(anchor='center', relx=0.5, rely=0.82)
        self.bottomFrame.rowconfigure(0, pad=10)
        self.bottomFrame.rowconfigure(1, pad=10)
        self.bottomFrame.columnconfigure(0, pad=10)
        self.bottomFrame.columnconfigure(1, pad=10)
        self.bottomFrame.columnconfigure(2, pad=10)

        # Top Frame Labels
        self.rpmLabel = Label(self.topFrame, text="RPM", font=('Verdana', 30), bg=self.bg, fg=self.fg)
        self.rpmLabel.place(anchor='center', relx=0.25, rely=0.2)

        self.rpmMeasure = Label(self.topFrame, text="0 for now", font=('Verdana', 70), bg=self.bg, fg=self.fg)
        self.rpmMeasure.place(anchor='center', relx=0.25, rely=0.65)

        self.speedLabel = Label(self.topFrame, text="Speed", font=('Verdana', 30), bg=self.bg, fg=self.fg)
        self.speedLabel.place(anchor='center', relx=0.75, rely=0.2)

        self.speedMeasure = Label(self.topFrame, text="100", font=('Verdana', 70), bg=self.bg, fg=self.fg)
        self.speedMeasure.place(anchor='center', relx=0.75, rely=0.65)

        # Middle Frame Labels
        self.batteryTempLabel = Label(self.middleFrame, text="Battery Temp", font=('Verdana', 18), bg=self.bg,
                                      fg=self.fg)
        self.batteryTempLabel.grid(row=0, column=0)

        self.batteryTempMeasure = Label(self.middleFrame, text="0 for now", font=('Verdana', 28), padx=25, bg=self.bg,
                                        fg=self.fg)
        self.batteryTempMeasure.grid(row=1, column=0)

        self.controllerTempLabel = Label(self.middleFrame, text="Controller Temp", font=('Verdana', 18), bg=self.bg,
                                         fg=self.fg)
        self.controllerTempLabel.grid(row=0, column=1)

        self.controllerTempMeasure = Label(self.middleFrame, text="0 for now", font=('Verdana', 28), padx=25,
                                           bg=self.bg, fg=self.fg)
        self.controllerTempMeasure.grid(row=1, column=1)

        self.motorTempLabel = Label(self.middleFrame, text="Motor Temp", font=('Verdana', 18), bg=self.bg, fg=self.fg)
        self.motorTempLabel.grid(row=0, column=2)

        self.motorTempMeasure = Label(self.middleFrame, text="1 for now", font=('Verdana', 28), padx=25, bg=self.bg,
                                      fg=self.fg)
        self.motorTempMeasure.grid(row=1, column=2)

        # Bottom Frame Labels
        self.packCurrentLabel = Label(self.bottomFrame, text="Pack Current", font=('Verdana', 18), bg=self.bg,
                                      fg=self.fg)
        self.packCurrentLabel.grid(row=0, column=0)

        self.packCurrentMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 28), padx=20, bg=self.bg,
                                        fg=self.fg)
        self.packCurrentMeasure.grid(row=1, column=0)

        self.packVoltageLabel = Label(self.bottomFrame, text="Avg Cell Voltage", font=('Verdana', 18), bg=self.bg,
                                      fg=self.fg)
        self.packVoltageLabel.grid(row=0, column=1)

        self.packMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 28), padx=20, bg=self.bg,
                                 fg=self.fg)
        self.packMeasure.grid(row=1, column=1)

        self.lowCellVoltageLabel = Label(self.bottomFrame, text="Low Cell Voltage", font=('Verdana', 18), bg=self.bg,
                                         fg=self.fg)
        self.lowCellVoltageLabel.grid(row=0, column=2)

        self.lowCellVoltageMeasure = Label(self.bottomFrame, text="0 for now", font=('Verdana', 28), padx=20,
                                           bg=self.bg, fg=self.fg)
        self.lowCellVoltageMeasure.grid(row=1, column=2)

    def update_labels(self):
        try:
            currentTime = datetime.now()
            currentTimeString = currentTime.strftime("%M : %S")
            rpm = self.count
            if rpm < 6000:
                rpm_color = self.fg
            elif rpm < 7200:
                rpm_color = 'yellow'
            else:
                rpm_color = 'red'
            self.rpmMeasure.config(text=str(self.count), fg=rpm_color)
            self.speedMeasure.config(text=str(self.count/10))
            self.count = (self.count + randint(0, 100)) % 10000
        except Exception as ex:
            print(ex)
        self.parent.after(50, self.update_labels)

    def on_closing(self):
        self.parent.destroy()

    def shutdown(self, channel):
        print("Shutting Down")
        global turnOffRaspberryPi
        turnOffRaspberryPi = True
        self.parent.destroy()


if __name__ == "__main__":
    # ShutDown Button Setup
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Variable to activate the "turn off the raspberry pi
    turnOffRaspberryPi = False

    root = Tk()
    display = Display(root)
    display.update_labels()
    root.protocol("WM_DELETE_WINDOW", display.on_closing)
    # GPIO.add_event_detect(4, GPIO.FALLING, callback=display.shutdown, bouncetime=2000)
    root.mainloop()

    # Turning off Raspberry Pi
    # time.sleep(3)
    if turnOffRaspberryPi:
        print("Would have shutdown")
        # os.system("sudo shutdown -h now")
