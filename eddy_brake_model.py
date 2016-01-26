import time
import canvas
from random import randint

sender = 0
receiver = 0

id_filter = [ # receive: stop, get engine status, go # highest level commands
		'get_eddy_brake_angle',
		'get_eddy_brake_angle_rep',
		'get_eddy_brake_power',
		'get_eddy_brake_power_rep',
		'get_eddy_brake_temp',
		'get_eddy_brake_temp_rep',
		'set_eddy_brake_angle',
		'set_eddy_brake_power'
		]


# Eddy brakes - Getter functions
def get_eddy_brake_angle():
	return randint(0,89)

def get_eddy_brake_power():
	return randint(0,99)
	
def get_eddy_brake_temp():
	return randint(0,40)


# Eddy brakes - Setter functions
def set_eddy_brake_angle(ang):
	print "Eddy brake angle set to %d degrees.\n".format(ang)

def set_eddy_brake_power(pow):
	print "Eddy brake power set to %d percent.\n".format(pow)
	
	
# Main loop
def main():
	
	global receiver 
	receiver = canvas.init_receiver()

	global sender 
	sender = canvas.init_sender()
	
	canvas.add_id(receiver, id_filter)

	# Main loop, modelled after control node's loop
	while 1:
	
		# See if any messages have been sent
		msg_name, data = canvas.recv(receiver)
		if (msg_name == 'set_eddy_brake_angle'):
			set_eddy_brake_angle(data)
		elif (msg_name == 'set_eddy_brake_power'):
			set_eddy_brake_power(data)
		elif (msg_name == 'get_eddy_brake_angle'):
			canvas.send( sender, 'get_eddy_brake_angle_rep', get_eddy_brake_angle() )
		elif (msg_name == 'get_eddy_brake_power'):
			canvas.send( sender, 'get_eddy_brake_power_rep', get_eddy_brake_power() )
		elif (msg_name == 'get_eddy_brake_temp'):
			canvas.send( sender, 'get_eddy_brake_temp_rep', get_eddy_brake_temp() )
			
		time.sleep(1)

if __name__ == '__main__':
    main()
	
#EOF
