
import zmq
import sys
from IDs import MessageList as ml

class msg:
    def __init__(self, a, b):
        self.id = a
        self.data = b

#stdout print function that works well with supervisord
def print_out ( str ):
	sys.stdout.write( str )
	sys.stdout.write( "\n" )
	sys.stdout.flush()

#init a zmq "CAN" sender
def init_sender():
	context = zmq.Context()
	sender = context.socket(zmq.PUSH)
	sender.connect("tcp://127.0.0.1:9998")
	return sender

#init a zmq "CAN" receiver
def init_receiver():
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect("tcp://127.0.0.1:9999")
	return receiver

#send two strings as id, data on the CAN bus
def send(socket, msg_id, msg_data):
	socket.send("%s %s" % (msg_id, msg_data))

#send a cavas message on the CAN bus
def send_msg(socket, msg):
	socket.send("%s %s" % (msg.id, msg.data))

#send a command message from the CAN message list
def send_cmd(socket, msg_name):
	socket.send("%s %s" % (ml.messages[msg_name]['id'], ""))	

#send a batch of commands from the CAN message list
def send_batch(socket, msg_names):
	for name in msg_names:
		socket.send("%s %s" % (ml.messages[name]['id'], ""))

#send a data message with some data from the CAN message list
def send_data(socket, msg_name, msg_data):
	socket.send("%s %s" % (ml.messages[msg_name]['id'], msg_data))	

#blocking receive on the CAN bus. returns message name
def recv(socket):
	can_message = socket.recv()
	msg_id, data = can_message.split(' ', 1)
	return ml.ids[msg_id]['name'], data

#blocking receive on the CAN bus. returns message id
def recv_id(socket):
	can_message = socket.recv()
	msg_id, data = can_message.split(' ', 1)
	return msg_id, data

#non-blocking receive on the CAN bus. returns message name
def recv_noblock(socket):
	try:
		can_message = socket.recv(flags=zmq.NOBLOCK)
	except zmq.error.Again, e:
		return "no_id", "no_message"
	msg_id, data = can_message.split(' ', 1)
	return ml.ids[msg_id]['name'], data


#non-blocking receive on the CAN bus. returns message id
def recv_noblock_id(socket):
	try:
		can_message = socket.recv(flags=zmq.NOBLOCK)
	except zmq.error.Again, e:
		return "no_id", "no_message"
	msg_id, data = can_message.split(' ', 1)
	return msg_id, data

def wait(socket, msg_names):
	i = len(msg_names)
	received_msgs = []

	while i > 0:
		msg_name, data = recv(socket)

		if msg_name in msg_names: 
			if msg_name not in received_msgs:
				i -= 1
				received_msgs.append(msg_name)
				print_out("GOT ONE")

	return

#add message filters to a CAN receiver
def add_id(socket, filters):
	for f in filters:
		id_number = ml.messages[f]['id']
		socket.setsockopt(zmq.SUBSCRIBE, id_number)
	
#remove message filters from a CAN receiver
def rm_id(socket, filters):
	for f in filters:
		id_number = ml.messages[f]['id']
		socket.setsockopt(zmq.UNSUBSCRIBE, id_number)
	
