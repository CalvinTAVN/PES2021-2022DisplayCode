import os
import can

os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")


can0 = can.interface.Bus(channel='can0', bustype='socketcan')
for x in range(10):
	msg = can0.recv(3.0)	
	print(msg)
	print(msg.data)
	print("------------------")
	for x in msg.data:
		print(x)
	print("---------")
	print(msg.arbitration_id)
#print(msg.data)
#print(msg.arbitration_id)
os.system("sudo ifconfig can0 down")
