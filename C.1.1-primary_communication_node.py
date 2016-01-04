import time
#import canvas
import math

from flask import Flask, jsonify, make_response, request
from IDs import MessageList as ml

app = Flask(__name__)

commands = [
    {
        'id': 1,
        'name': u'stop',
        'arguments': [],
        'return_values': [],
        'description': 'This command brings the pod to a stop.'
    },
    {
        'id': 2,
        'name': u'start',
        'arguments': [],
        'return_values': [],
        'description': 'This command initialises the various systems and gets the pod ready to move.'
    },
    {
        'id': 3,
        'name': u'move',
        'arguments': ['speed'],
        'return_values': [],
        'description': 'This command makes the pod move at a specified speed.'
    },
    {
        'id': 4,
        'name': u'get_status',
        'arguments': [],
        'return_values': ['power_level',
                          'battery_temperature',
                          'internal_temperature',
                          'external_temperature',
                          'internal_pressure',
                          'external_pressure'],
        'description': 'This command returns the status of the modules in the pod.'
    },
    {
        'id': 5,
        'name': u'get_position',
        'arguments': [],
        'return_values': ['x','y','z'],
        'description': 'This command returns the x,y and z coordinates of the pod.'
    },
    {
        'id': 6,
        'name': u'get_speed',
        'arguments': [],
        'return_values': ['speed'],
        'description': 'This command returns the speed of the pod'
    }
]

@app.route('/stop', methods=['POST'])
def stop():
    return jsonify({'command': 'stop'}), 201

@app.route('/commands', methods=['GET'])
def get_commands():
        return jsonify({'commands':commands})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def main():
	#sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	#canvas.print_out("Primary communication node started")

	while 1:
                print("heart beat")

		time.sleep(2)

if __name__ == '__main__':
    app.run(debug=True)
