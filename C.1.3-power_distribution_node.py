import time
import canvas
import math
from IDs import MessageList as ml

id_filter = [# receive: stop, get engine status, go # highest level commands
		ml.messages['uc_temp_data']['id'],
		ml.messages['batt_temp_data']['id'],
		ml.messages['batt_power_data']['id'],
		ml.messages['so_temp_data']['id']
		] 

def main():
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out("Power distribution node started")

	while 1:

		canvas.send(sender, ml.messages['uc_temp_req']['id'], '')
		canvas.send(sender, ml.messages['batt_temp_req']['id'], '')
		canvas.send(sender, ml.messages['batt_power_req']['id'], '')
		canvas.send(sender, ml.messages['so_temp_req']['id'], '')

		msg_id, data = canvas.recv(receiver)

		if (msg_id == ml.messages['uc_temp_data']['id']):
			canvas.print_out("Umbilical temp: %s" % (data))

		elif (msg_id == ml.messages['batt_temp_data']['id']):
			canvas.print_out("Battery temp: %s" % (data))

		elif (msg_id == ml.messages['batt_power_data']['id']):
			canvas.print_out("Battery power: %s" % (data))

		elif (msg_id == ml.messages['so_temp_data']['id']):
			canvas.print_out("Standard outlet temp: %s" % (data))

		time.sleep(2)

if __name__ == '__main__':
    main()
