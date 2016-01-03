import time
import canvas
import math
from random import randint
from IDs import MessageList as ml

id_filter = [# receive: stop, get engine status, go # highest level commands
		'pod_temp_req',
		'pod_pressure_req',
		'pod_attitude_req',
		'pod_position_req'
		] 

def read_temp():
	return randint(18, 30) #read cabin internal temp (in Celsius)

def read_pressure():
	return randint(90, 110) #read cabin internal pressure (kPa)

def read_attitude():
	return "p:0.%d y:0.%d r:0.%d" % (randint(0, 100), randint(0, 100), randint(0, 100)) #read pod attitude (pitch, yaw, roll)

def read_position():
	return randint(0, 10000) #read pod position along the track

def main():
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out("Status node started")

	while 1:

		msg_name, data = canvas.recv(receiver)

		if (msg_name == 'pod_temp_req'):
			data = read_temp();
			canvas.send_data(sender, 'pod_temp_data', data)

		if (msg_name == 'pod_pressure_req'):
			data = read_pressure();
			canvas.send_data(sender, 'pod_pressure_data', data)

		if (msg_name == 'pod_attitude_req'):
			data = read_attitude();
			canvas.send_data(sender, 'pod_attitude_data', data)

		if (msg_name == 'pod_position_req'):
			data = read_position();
			canvas.send_data(sender, 'pod_position_data', data)

if __name__ == '__main__':
    main()
