import time
import canvas
import math
from IDs import MessageList as ml

id_filter = [# receive: stop, get engine status, go # highest level commands
		ml.messages['stop']['id'],
		ml.messages['start']['id'],
		ml.messages['get_engine_status']['id'],
		ml.messages['get_hover_height']['id'],
		ml.messages['hover_height_data']['id'], 
		ml.messages['move']['id']
		] 

def main():
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)
	canvas.print_out("COntrol node started")
	while 1:
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
			
			canvas.print_out("tilt hover engine at angle calculated from target speed")		
			canvas.send(sender, ml.messages['tilt_l']['id'], math.asin(float(data)/20)*5) # title engine at calculated angle
			
			canvas.print_out("get hover engine L status")
			canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L	
		
		elif (msg_id == ml.messages['start']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("start pod")
			
			canvas.print_out("start hover engine L")		
			canvas.send(sender, ml.messages['start_l']['id'], 0) # start engine
			
			canvas.print_out("get hover engine L status")
			canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L
			
		elif (msg_id == ml.messages['stop']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("stop")
			
			canvas.print_out("tilt hover engine to stop position")		
			canvas.send(sender, ml.messages['tilt_l']['id'], 0) # tilt engine back to stop position
			
			canvas.print_out("stop hover engine")		
			canvas.send(sender, ml.messages['stop_l']['id'], "") # stop engine L
			
			canvas.print_out("get hover engine l status")
			canvas.send(sender, ml.messages['get_engine_status_l']['id'], "") # get engine status L	

		elif (msg_id == ml.messages['get_hover_height']['id']):
			canvas.print_out("COMMANDS:")
			canvas.print_out("get_hover_height")

			canvas.send(ml.messages['hover_height_req']['id'], "")
			#we DONT want to wait for a hover_height_data message here. if the reply is lost we deadlock the control node. BAD.

		elif (msg_id == ml.messages['hover_height_data']['id']):
			canvas.print_out("POD HOVER HEIGHT: %s" % data) #this should be sent back to ground station over wifi

		time.sleep(1)
			

if __name__ == '__main__':
    main()
