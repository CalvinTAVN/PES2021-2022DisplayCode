import os
import can
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d_%m_%Y,%H_%M_%S")
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")


can0 = can.interface.Bus(channel='can0', bustype='socketcan')

value1 = 0
value2 = 0
print(dt_string)
with open('dataInfo/' + dt_string, 'w') as f:
	f.write("NewText File\n")
	f.write("1700     | 1713\n")
	for  x in range(10):
		msg = can0.recv(3.0)
		dataArray = msg.data
		print(msg)
		if (msg.arbitration_id == 1700):
			value1 = dataArray[6]
		if (msg.arbitration_id == 1713):
			value2 = dataArray[4]
		f.write(str(value1) + " | " + str(value2) + "\n")

	
	
"""
for x in range(10):
	msg = can0.recv(3.0)
	dataArray = msg.data
	print(msg)
	print(msg.data)
	print("------------------")
	for x in dataArray:
		print(x)
	print("---------")
	print(dataArray[2])
	print(msg.arbitration_id)
"""
os.system("sudo ifconfig can0 down")
