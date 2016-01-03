import time
import canvas
import math
from IDs import MessageList as ml

sender = 0
receiver = 0

id_filter = [# receive: stop, get engine status, go # highest level commands
		ml.messages['stop']['id'],
		ml.messages['start']['id'],
		ml.messages['get_engine_status']['id'],
		ml.messages['get_hover_height']['id'],
		ml.messages['get_pod_status']['id'],
		ml.messages['hover_height_data']['id'], 
		ml.messages['pod_temp_data']['id'],
		ml.messages['pod_attitude_data']['id'],
		ml.messages['pod_position_data']['id'],
		ml.messages['pod_pressure_data']['id'],
		ml.messages['move']['id']
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

def get_pod_status():
	temp = 0
	pressure = 0
	attitude = ""
	position = 0

	i = 4

	#send request messages for all the data we need
	canvas.send(sender, ml.messages['pod_temp_req']['id'], "")
	canvas.send(sender, ml.messages['pod_attitude_req']['id'], "")
	canvas.send(sender, ml.messages['pod_position_req']['id'], "")
	canvas.send(sender, ml.messages['pod_pressure_req']['id'], "")

	#wait untill all 4 responses have arrived. order of responses arriving does not matter with this method
	#we also make sure we do not count the same data arriving twice.
	while i > 0:
		msg_id, data = canvas.recv(receiver)

		#if the "temp" variable is not 0 (its default value), that means we have received the temperature data already.
		if(msg_id == ml.messages['pod_temp_data']['id'] and temp == 0):
			temp = data
			i -= 1

		elif(msg_id == ml.messages['pod_pressure_data']['id'] and pressure == 0):
			pressure = data
			i -= 1

		elif(msg_id == ml.messages['pod_attitude_data']['id'] and attitude == ""):
			attitude = data
			i -= 1

		elif(msg_id == ml.messages['pod_position_data']['id'] and position == 0):
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
	while 1:
		canvas.send(sender, ml.messages['get_pod_status']['id'], "")
		msg_id, data = canvas.recv(receiver)
		# get status of all engines
		if (msg_id == ml.messages['get_engine_status']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("get all engine statuses")
			
			# get the status for each individual engine node
			canvas.send(sender, ml.messages['get_engine_status_l']['id'], "")
			
		elif (msg_id == ml.messages['move']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("move %s" % data)

			move_pod(data)
			
		elif (msg_id == ml.messages['start']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("start pod")
			
			start_pod()
			
		elif (msg_id == ml.messages['stop']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("stop")
			
			stop_pod()

		elif (msg_id == ml.messages['get_pod_status']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("get pod status")

			temp, pressure, attitude, position = get_pod_status()

			canvas.print_out("Pod stauts: temp - %s, pressure - %s, attitude - %s, position - %s" % (temp, pressure, attitude, position) )

		time.sleep(1)
			

if __name__ == '__main__':
    main()
