import os
import can

os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")


can0 = can.interface.Bus(channel='can0', bustype='socketcan')
for x in range(10):
	msg = can0.recv(3.0)
	if msg is None:
		print('msg: ' + str(msg))
		continue
	print('-----------------------------')
	print('msg: ' + str(msg))
	print('arb id: ' + str(msg.arbitration_id))
	print('data: ' + str(msg.data))
	for i in msg.data:
		print('values: ' + str(i))
	print('-----------------------------')
#print(msg.data)
#print(msg.arbitration_id)
os.system("sudo ifconfig can0 down")
