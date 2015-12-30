
import canvas
import time
from IDs import MessageList as ml
from random import randint

id_filter = [
			ml.messages['batt_temp_req']['id'],
			ml.messages['batt_power_req']['id']
			]

def main():
	
	#init canvas sender and receiver
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out('Batteries started')

	while 1:

		msg_id, msg_data = canvas.recv(receiver)
		
		if (msg_id == ml.messages['batt_temp_req']['id']):
			temp_data = randint(20,30)
			canvas.send(sender, ml.messages['batt_temp_data']['id'], temp_data) #send random temp data

		if (msg_id == ml.messages['batt_power_req']['id']):
			power_data = randint(10,20)
			canvas.send(sender, ml.messages['batt_power_data']['id'], power_data) #send random temp data


if __name__ == '__main__':
    main()
