import time
import canvas
import math
from random import randint
from IDs import MessageList as ml

id_filter = [# receive: stop, get engine status, go # highest level commands
		ml.messages['pod_temp_req']['id'],
		ml.messages['pod_pressure_req']['id'],
		ml.messages['pod_attitude_req']['id'],
		ml.messages['pod_position_req']['id']
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

		msg_id, data = canvas.recv(receiver)

		if (msg_id == ml.messages['pod_temp_req']['id']):
			data = read_temp();
			canvas.send(sender, ml.messages['pod_temp_data']['id'], data)

		if (msg_id == ml.messages['pod_pressure_req']['id']):
			data = read_pressure();
			canvas.send(sender, ml.messages['pod_pressure_data']['id'], data)

		if (msg_id == ml.messages['pod_attitude_req']['id']):
			data = read_attitude();
			canvas.send(sender, ml.messages['pod_attitude_data']['id'], data)

		if (msg_id == ml.messages['pod_position_req']['id']):
			data = read_position();
			canvas.send(sender, ml.messages['pod_position_data']['id'], data)

if __name__ == '__main__':
    main()
