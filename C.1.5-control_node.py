import time
import canvas
import math
from random import randint
from IDs import MessageList as ml

sender = 0
receiver = 0

id_filter = [
		'stop',
		'start',
		'get_engine_status',
		'get_hover_height',
		'get_pod_status',
		'hover_height_data', 
		'pod_temp_data',
		'pod_attitude_data',
		'pod_position_data',
		'pod_pressure_data',
		'power_distribution_node_started',
		'status_node_started',
		'move'
		] 

def move_pod(data):
	canvas.print_out("tilt hover engine at angle calculated from target speed")		
	canvas.send(sender, ml.messages['tilt_l']['id'], math.asin(float(data)/20)*5) # title engine at calculated angle

	canvas.print_out("get hover engine L status")
	canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L	

def start_pod():
	canvas.print_out("start hover engine L")		
	canvas.send(sender, ml.messages['start_l']['id'], 0) # start engine

	canvas.print_out("get hover engine L status")
	canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L

def stop_pod():
	canvas.print_out("tilt hover engine to stop position")		
	canvas.send(sender, ml.messages['tilt_l']['id'], 0) # tilt engine back to stop position
	
	canvas.print_out("stop hover engine")		
	canvas.send(sender, ml.messages['stop_l']['id'], "") # stop engine L
	
	canvas.print_out("get hover engine l status")
	canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L	

def get_hover_height():
	return "%d.%d" % (randint(0,6),randint(0,99))

def get_pod_status():
	temp = 0
	pressure = 0
	attitude = ""
	position = 0

	i = 4

	canvas.send_batch(sender, ['pod_temp_req', 'pod_pressure_req', 'pod_position_req', 'pod_attitude_req'])

	#wait untill all 4 responses have arrived. order of responses arriving does not matter with this method
	#we also make sure we do not count the same data arriving twice.
	while i > 0:
		msg_name, data = canvas.recv(receiver)

		#if the "temp" variable is not 0 (its default value), that means we have received the temperature data already.
		if(msg_name == 'pod_temp_data' and temp == 0):
			temp = data
			i -= 1

		elif(msg_name == 'pod_pressure_data' and pressure == 0):
			pressure = data
			i -= 1

		elif(msg_name == 'pod_attitude_data' and attitude == ""):
			attitude = data
			i -= 1

		elif(msg_name == 'pod_position_data' and position == 0):
			position = data
			i -= 1

	return temp, pressure, attitude, position

def main():
	global receiver 
	receiver = canvas.init_receiver()

	global sender 
	sender = canvas.init_sender()

	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out("Control node started")
	canvas.wait(receiver, ['power_distribution_node_stared', 'status_node_started'])
	canvas.print_out("rPod running")

	while 1:
		canvas.send_cmd(sender, 'get_pod_status')
		msg_name, data = canvas.recv(receiver)
		# get status of all engines
		if (msg_name == 'get_engine_status'):
			canvas.print_out("COMMANDS:")
			canvas.print_out("get all engine statuses")
			
			# get the status for each individual engine node
			canvas.send_cmd(sender, 'get_engine_status_l')
			
		elif (msg_name == 'move'):
			canvas.print_out("COMMANDS:")
			canvas.print_out("move %s" % data)

			move_pod(data)
			
		elif (msg_name == 'start'):
			canvas.print_out("COMMANDS:")
			canvas.print_out("start pod")
			
			start_pod()
			
		elif (msg_name == 'stop'):
			canvas.print_out("COMMANDS:")
			canvas.print_out("stop")
			
			stop_pod()
		#collect data from all pod sensors
		elif (msg_name == 'get_pod_status'):
			canvas.print_out("COMMANDS:")
			canvas.print_out("get pod status")

			height = get_hover_height()
			temp, pressure, attitude, position = get_pod_status()

			canvas.print_out("Pod stauts: height - %smm, temp - %sC, pressure - %skPa, attitude - %s, position - %sm" % (height, temp, pressure, attitude, position) )

		time.sleep(1)
			

if __name__ == '__main__':
    main()
