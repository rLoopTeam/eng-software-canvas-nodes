import time
import canvas
from IDs import MessageList as ml

# Constants
pod_temp_max = 33
pod_temp_min = 21
pod_pres_max = 1100
pod_pres_min = 900
hover_height_max = 15 # No idea what actual tolerances are
hover_height_min = 3

sender = 0
receiver = 0

id_filter = [ # receive: stop, get engine status, go # highest level commands
		'get_engine_status',
		'get_hover_height',
		'get_pod_status',
		'hover_height_data', 
		'pod_temp_data',
		'pod_attitude_data',
		'pod_pressure_data',
		]
		
# Emergency node functions
def alert_ground_station(emer, loc):
	canvas.print_out("Sending message to ground station")		
	canvas.send(sender, ml.messages['emer_l']['id'], "Emergency code: {0} \nLocation: {1}".format(emer, loc))
	
def pod_shutdown():
	canvas.print_out("Shutting down pod")		
	canvas.send(sender, ml.messages['stop']['id'], 0)

# Main loop function
def main():
	
	global receiver 
	receiver = canvas.init_receiver()

	global sender 
	sender = canvas.init_sender()
	
	canvas.add_id(receiver, id_filter)

	# Main loop, modelled after control node's loop
	while 1:
	
		#Request several data points
		canvas.send_batch(sender, ['pod_temp_req', 'pod_pressure_req', 'pod_attitude_req'])
		msg_name, data = canvas.recv(receiver)
		
		# Check data, make sure none is abnormal
		if (msg_name == 'pod_temp_data'):
			if (data > pod_temp_max):
				alert_ground_station(1,location)
				pod_shutdown()
			elif (data < pod_temp_min):
				alert_ground_station(2,location)
				pod_shutdown()

		elif (msg_name == 'pod_pressure_data'):
			if (data > pod_pres_max):
				alert_ground_station(3,location)
				pod_shutdown()
			elif (data < pod_pres_min):
				alert_ground_station(4,location)
				pod_shutdown()
				

		elif (msg_name == 'pod_attitude_data'):
		
		elif (msg_name == 'hover_height_data'):
			if (data > hover_height_max):
				alert_ground_station(7,location)
				pod_shutdown()
			elif (data < hover_height_min):
				alert_ground_station(8,location)
				pod_shutdown()

		time.sleep(1)
		
if __name__ == '__main__':
    main()