import os
import can

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

#msg = can0.recv(5.0)


msg = can.Message(arbitration_id=0x123, data = [0, 1, 2, 3])
can0.send(msg)
#print(msg)

os.system('sudo ifconfig can0 down')
