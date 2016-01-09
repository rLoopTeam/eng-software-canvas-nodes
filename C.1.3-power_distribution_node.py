import time
import canvas
import math
from random import randint
from IDs import MessageList as ml

id_filter = [
		'uc_temp_req',
		'batt_temp_req',
		'batt_power_req',
		'so_temp_req'
		] 

def get_umbilical_temp():
	return randint(20, 40)

def get_standard_outlet_temp():
	return randint(20, 40)

def get_battery_temp():
	return randint(20, 40)

def get_batter_power():
	return randint(10, 20)

def main():
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out("Power distribution node started")
	canvas.send_cmd(sender, "power_distribution_node_started")

	while 1:

		canvas.send_cmd(sender, 'uc_temp_req')
		canvas.send_cmd(sender, 'batt_temp_req')
		canvas.send_cmd(sender, 'batt_power_req')
		canvas.send_cmd(sender, 'so_temp_req')

		msg_name, msg_data = canvas.recv(receiver)

		if (msg_name == 'uc_temp_req'):
			data = get_umbilical_temp()
			canvas.print_out("Umbilical temp: %s" % (data))

		elif (msg_name == 'batt_temp_req'):
			data = get_battery_temp()
			canvas.print_out("Battery temp: %s" % (data))

		elif (msg_name == 'batt_power_req'):
			data = get_batter_power()
			canvas.print_out("Battery power: %s" % (data))

		elif (msg_name == 'so_temp_req'):
			data = get_standard_outlet_temp()
			canvas.print_out("Standard outlet temp: %s" % (data))

		time.sleep(2)

if __name__ == '__main__':
    main()
