import time
import canvas
from random import randint

sender = 0
receiver = 0

id_filter = [ # receive: stop, get engine status, go # highest level commands
		'is_brake_engaged',
		'is_brake_engaged_rep',
		'get_brake_force',
		'get_brake_force_rep',
		'set_brake_force'
		]


# Mech brakes - "getter" functions
def get_brake_force():
	return randint(0,99)

def is_brake_engaged():
	if (get_brake_force > 0):
		return true
	else:
		return false


# Mech brakes - "setter" function
def set_brake_force(force):
	print "Mechanical brakes force set to %d percent.\n".format(force)
	

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
		if (msg_name == 'set_brake_force'):
			set_brake_force(data)
		elif ('get_brake_force'):
			canvas.send( sender, 'get_brake_force_rep', get_brake_force() )
		elif ('is_brake_engaged'):
			canvas.send( sender, 'is_brake_engaged_rep', is_brake_engaged() )
			
		time.sleep(1)

if __name__ == '__main__':
    main()
	
#EOF