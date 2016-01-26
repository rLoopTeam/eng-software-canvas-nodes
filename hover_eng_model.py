import time
import canvas
from random import randint

sender = 0
receiver = 0

id_filter = [ # receive: stop, get engine status, go # highest level commands
		'get_hover_eng_angle',
		'get_hover_eng_angle_rep',
		'get_hover_eng_power',
		'get_hover_eng_power_rep',
		'set_hover_eng_angle',
		'set_hover_eng_power'
		]

		
# Hover engine - getter functions
def get_hover_eng_angle():
	return randint(0,89)

def get_hover_eng_power():
	return randint(0,99)

	
# Hover engine - setter functions
def set_hover_eng_angle(ang):
	print "Hover engine angle set to %d degrees.\n".format(ang)

def set_hover_eng_power(pow):
	print "Hover engine power set to %d percent.\n".format(pow)
	

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
		if (msg_name == 'set_hover_eng_angle'):
			set_hover_eng_angle(data)
		elif (msg_name == 'set_hover_eng_power'):
			set_hover_eng_power(data)
		elif (msg_name == 'get_hover_eng_angle'):
			canvas.send( sender, 'get_hover_eng_angle_rep', get_hover_eng_angle() )
		elif (msg_name == 'get_hover_eng_power'):
			canvas.send( sender, 'get_hover_eng_power_rep', get_hover_eng_power() )
			
		time.sleep(1)

if __name__ == '__main__':
    main()
	
#EOF
