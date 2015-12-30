
import canvas
import time
from IDs import MessageList as ml
from random import randint

id_filter = [
			ml.messages['hover_height_req']['id']
			]

def main():
	
	#init canvas sender and receiver
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out('Hover height sensor started')

	while 1:

		msg_id, msg_data = canvas.recv(receiver)
		
		if (msg_id == ml.messages['hover_height_req']['id']):
			hover_height = randint(400,600)
			canvas.send(sender, ml.messages['hover_height_data']['id'], hover_height) #send random temp data

if __name__ == '__main__':
    main()
