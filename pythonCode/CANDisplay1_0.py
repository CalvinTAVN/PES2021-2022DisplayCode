#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import can
from datetime import datetime
from tkinter import *


#ShutDown Button Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Variable to activate the "turn off the raspberry pi
turnOffRaspberryPi = False;

def Shutdown(channel):
    print("Shutting Down")
    global runner;
    global turnOffRaspberryPi;
    runner = False;
    turnOffRaspberryPi = True;

GPIO.add_event_detect(4, GPIO.FALLING, callback=Shutdown, bouncetime=2000)


#Time Module
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y,%H_%M_%S")

#Can Message setup
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel='can0', bustype='socketcan')

########################################################
#GUI Setup
display = Tk()
display.title = ('PES Speedboat')
display.geometry('1024x600')
display.config(bg = 'gray')

lowTempLabel = Label(
    display,
    text = "lowTemp",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
lowTempLabel.grid(row = 0, column =0)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#lowTempLabel.pack()

lowTempMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
lowTempMeasure.grid(row = 1, column =0)
#lowTempMeasure.pack()

highTempLabel = Label(
    display,
    text = "highTemp",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
highTempLabel.grid(row = 0, column =1)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#highTempLabel.pack()

highTempMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
highTempMeasure.grid(row = 1, column =1)
#highTempMeasure.pack()

avgTempLabel = Label(
    display,
    text = "avgTemp",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
avgTempLabel.grid(row = 0, column =2)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#avgTempLabel.pack()

avgTempMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
avgTempMeasure.grid(row = 1, column =2)
#avgTempMeasure.pack()

packCurrentLabel = Label(
    display,
    text = "packCurrent",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
packCurrentLabel.grid(row = 0, column =3)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#packCurrentLabel.pack()

packCurrentMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
packCurrentMeasure.grid(row = 1, column =3)
#packCurrentMeasure.pack()

packVoltageLabel = Label(
    display,
    text = "packVoltage",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
packVoltageLabel.grid(row = 4, column =2)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#packVoltageLabel.pack()

packVoltageMeasure = Label(
    display,
    text = "0 for now",
    font = ('Verdana', 50),
    padx = 10,
    pady = 5,
    bg = 'white'

)
packVoltageMeasure.grid(row = 5, column =2)
#packVoltageMeasure.pack()


lowCellVoltageLabel = Label(
    display,
    text = "lowCellVoltage",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
lowCellVoltageLabel.grid(row = 0, column =5)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#lowCellVoltageLabel.pack()

lowCellVoltageMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
lowCellVoltageMeasure.grid(row = 1, column =5)
#lowCellVoltageMeasure.pack()

highCellVoltageLabel = Label(
    display,
    text = "highCellVoltage",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
highCellVoltageLabel.grid(row = 0, column =6)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#highCellVoltageLabel.pack()

highCellVoltageMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
highCellVoltageMeasure.grid(row = 1, column =6)
#highCellVoltageMeasure.pack()

avgCellVoltageLabel = Label(
    display,
    text = "avgCellVoltage",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
avgCellVoltageLabel.grid(row = 0, column =7)
#avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
#avgCellVoltageLabel.pack()

avgCellVoltageMeasure = Label(
    display,
    text = "0 for now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
avgCellVoltageMeasure.grid(row = 1, column =7)
#avgCellVoltageMeasure.pack()


display.update();



######################################################

def on_closing():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    runner = False
    display.destroy()

#######################################################

#Display Tkinter Protocols
display.protocol("WM_DELETE_WINDOW", on_closing)



##################################################

#Initial Values for Files
#note, use the semicolon to separate parameters
lowTemp = 0; highTemp = 0; avgTemp = 0
packCurrent = 0; packVoltage = 0; lowCellVoltage = 0; highCellVoltage = 0; avgCellVoltage = 0;

# Creation of New File #note screen size is 1024x600
print(dt_string)
newFile = open('/home/pes/dataInfo/' + dt_string, 'w')
newFile.write(dt_string + "\n")
newFile.write("Time   |lowTemp|highTemp|avgTemp|packCurrent|" +
              "packVoltage|lowCellVoltage|highCellVoltage|avgCellVoltage\n")
runner = True
while runner:
    try:
        currentTime = datetime.now();
        currentTimeString = currentTime.strftime("%M : %S")
        msg = can0.recv(3.0)
        if (msg != None):
            dataArray = msg.data
            #print(msg)
            #print(runner)
            if (msg.arbitration_id == 1701):
                avgTemp = dataArray[0]
                lowTemp = dataArray[1]
                highTemp = dataArray[2]
                avgTempMeasure.config(text=str(avgTemp))
                lowTempMeasure.config(text=str(lowTemp))
                highTempMeasure.config(text=str(highTemp))
                #avgV_lbl.config(text=str(value2)) Make Label for this
            if(msg.arbitration_id == 1702):
                packCurrent = dataArray[0]
                packVoltage = dataArray[1]
                lowCellVoltage = dataArray[3]
                highCellVoltage = dataArray[4]
                avgCellVoltage = dataArray[5]
                packCurrentMeasure.config(text = str(packCurrent))
                packVoltageMeasure.config(text = str(packVoltage))
                lowCellVoltageMeasure.config(text=str(lowCellVoltage))
                highCellVoltageMeasure.config(text=str(highCellVoltage))
                avgCellVoltageMeasure.config(text=str(avgCellVoltage))
                #avgV_lbl.config(text=str(value3)) Make Label for this as well
            newFile.write(currentTimeString + "|  " + str(lowTemp) + "   |   " + str(highTemp) +  "   |  " + str(avgTemp) +
                          "   |     " + str(packCurrent) + "     |      " + str(packVoltage) + "     |      " + str(lowCellVoltage) +
                          "      |      " + str(highCellVoltage) +       "         |      " + str(avgCellVoltage) + "\n")
        display.update()
        continue
    except TclError:
        newFile.write("End")
        break

#Tkinter off
if (turnOffRaspberryPi):
    display.destroy()

display.mainloop()
#CAN ending protocol
newFile.close();
os.system("sudo ifconfig can0 down")

#Turning off Raspberry Pi
time.sleep(3)
#print("Would of shutdown")
if (turnOffRaspberryPi):
    os.system("sudo shutdown -h now")

#Display Tkinter Protocols
#display.protocol("WM_DELETE_WINDOW", on_closing)
#display.mainloop()
