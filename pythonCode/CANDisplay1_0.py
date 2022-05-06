import RPi.GPIO as GPIO
import time
import os
import can
from datetime import datetime
from tkinter import *


#ShutDown Button Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
    print("Shutting Down")
    global runner
    runner = False;

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

avgV_lbl = Label(
    display,
    text = "0 for right now",
    font = (21),
    padx = 10,
    pady = 5,
    bg = 'white'

)
avgV_lbl.place(anchor = NW,bordermode=OUTSIDE, height=40, width=100, relx=0.5, rely=0.5)
display.update();

def on_closing():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    runner = False
    display.destroy()

#######################################################

#Initial Values for Files
#note, use the semicolon to separate parameters
lowTemp = 0; highTemp = 0; avgTemp = 0
packCurrent = 0; packVoltage = 0; lowCellVoltage = 0; highCellVoltage = 0; avgCellVoltage = 0;

# Creation of New File #note screen size is 1024x600
print(dt_string)
newFile = open('dataInfo/' + dt_string, 'w')
newFile.write("NewText File\n")
newFile.write("Time   |  lowTemp  | highTemp | avgTemp | packCurrent " +
              "packVoltage | lowCellVoltage | highCellVoltage | avgCellVoltage\n")
runner = True
while runner:
    try:
        currentTime = datetime.now();
        currentTimeString = currentTime.strftime("%M : %S")
        msg = can0.recv(3.0)
        dataArray = msg.data
        #print(msg)
        #print(runner)
        if (msg.arbitration_id == 1701):
            avgTemp = dataArray[0]
            lowTemp = dataArray[1]
            highTemp = dataArray[2]
            #avgV_lbl.config(text=str(value2)) Make Label for this
        if(msg.arbitration_id == 1702):
            packCurrent = dataArray[0]
            packVoltage = dataArray[1]
            lowCellVoltage = dataArray[3]
            highCellVoltage = dataArray[4]
            avgCellVoltage = dataArray[5]
            #avgV_lbl.config(text=str(value3)) Make Label for this as well
        newFile.write(currentTimeString + "| " + str(lowTemp) + " | " + str(highTemp) +  " | " + str(avgTemp) + 
                      " | " + str(packCurrent) + " | " + str(packVoltage) + " | " + str(lowCellVoltage) + 
                      " | " + str(highTemp) + " | " + str(avgCellVoltage) + "\n")

        display.update()
        continue
    except TclError:
        newFile.write("End")
        break

#Tkinter off
display.destroy()

#CAN ending protocol
newFile.close();
os.system("sudo ifconfig can0 down")

#Turning off Raspberry Pi
time.sleep(3)
#print("Would of shutdown")
os.system("sudo shutdown -h now")

#Display Tkinter Protocols
display.protocol("WM_DELETE_WINDOW", on_closing)
display.mainloop()
