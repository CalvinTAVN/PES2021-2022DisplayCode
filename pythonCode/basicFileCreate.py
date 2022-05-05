import os
import can
from datetime import datetime

#Time Module
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y,%H_%M_%S")


#Can Message setup
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel='can0', bustype='socketcan')

#Initial Values for Files
value1 = 0;
value2 = 0;
value3 = 0;

# Creation of New File
print(dt_string)
newFile = open('dataInfo/' + dt_string, 'w')
newFile.write("NewText File\n")
newFile.write("Time   |  1700  |  1713   |   1714\n")
for x in range(10):
    currentTime = datetime.now();
    currentTimeString = currentTime.strftime("%M : %S")
    msg = can0.recv(3.0)
    dataArray = msg.data
    print(msg)
    if (msg.arbitration_id == 1700):
        value1 = dataArray[6]
    if (msg.arbitration_id == 1713):
        value2 = dataArray[4]
    if(msg.arbitration_id == 1714):
        value3 = dataArray[0]
    newFile.write(currentTimeString + "|   " + str(value1) + "    | " + str(value2) +  "    |    " + str(value3) + "\n")

newFile.close();


os.system("sudo ifconfig can0 down")
