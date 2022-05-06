import os
import can
from datetime import datetime
from tkinter import *
import RPi.GPIO as GPIO
import time

#ShutDown Button Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
    print("Shutting Down")
    runner = False;
    #os.system("sudo shutdown -h now")
#removed bouncetime=2000
GPIO.add_event_detect(4, GPIO.FALLING, callback=Shutdown)


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
    root.destroy()
    runner = False

#######################################################

#Initial Values for Files
#note, use the semicolon to separate parameters
value1 = 0; value2 = 0; value3 = 0

# Creation of New File #note screen size is 1024x600
print(dt_string)
newFile = open('dataInfo/' + dt_string, 'w')
newFile.write("NewText File\n")
newFile.write("Time   |  1700  |  1713   |   1714\n")

runner = True;
while runner:
    try:
        currentTime = datetime.now();
        currentTimeString = currentTime.strftime("%M : %S")
        msg = can0.recv(3.0)
        dataArray = msg.data
        print(msg)
        if (msg.arbitration_id == 1700):
            value1 = dataArray[6]
            avgV_lbl.config(text=str(value1))
        if (msg.arbitration_id == 1713):
            value2 = dataArray[4]
            avgV_lbl.config(text=str(value2))
        if(msg.arbitration_id == 1714):
            value3 = dataArray[0]
            avgV_lbl.config(text=str(value3))
        newFile.write(currentTimeString + "|   " + str(value1) + "    | " + str(value2) +  "    |    " + str(value3) + "\n")
        display.update()
        continue
    except TclError:
        newFile.write("End")
        break

#CAN ending protocol
newFile.close();
os.system("sudo ifconfig can0 down")

#Turning off Raspberry Pi
time.sleep(2)
os.system("sudo shutdown -h now")

#Display Tkinter Protocols
display.protocol("WM_DELETE_WINDOW", on_closing)
display.mainloop()
